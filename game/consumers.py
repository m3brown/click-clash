import json
from channels import Group
from channels.auth import channel_session_user_from_http, channel_session_user
from .models import Counter

def dump_to_ws_format(obj):
    return {'text': json.dumps(obj)}

def get_socket_mode(message):
    return message.content['path'].strip('/').split('/')[1]

def get_alltime_list():
    toplist = Counter.objects.all().order_by('-count')[:10]
    toplist_json = []
    for item in toplist:
        toplist_json.append({'user': item.user.username, 'count': item.count})
    return {'action': 'alltime', 'toplist': toplist_json}

### WebSocket handling ###


# This decorator copies the user from the HTTP session (only available in
# websocket.connect or http.request messages) to the channel session (available
# in all consumers with the same reply_channel, so all three here)
@channel_session_user_from_http
def ws_connect(message):
    # All sessions receive updates for "active" users.  Add this session to the group
    # and update all existing members of the group with the new user
    Group('active').add(message.reply_channel)
    Group('active').send(dump_to_ws_format({'action': 'update',
                                            'user': message.user.username,
                                            'count': message.user.counter.count}))

    # The "scoreboard" page also has an all-time top 10 list
    mode = get_socket_mode(message)
    if mode == 'scoreboard':
        # print all-time top10
        Group('scoreboard').add(message.reply_channel)
        toplist = get_alltime_list()
        if message.user in  [item['user'] for item in toplist['toplist']]:
            Group('scoreboard').send(dump_to_ws_format(toplist))
        else:
            message.reply_channel.send(dump_to_ws_format(toplist))



@channel_session_user
def ws_receive(message):
    payload = json.loads(message['text'])
    if payload.get('increment', False):
        message.user.counter.count += 1
        message.user.counter.save()
    message.reply_channel.send(dump_to_ws_format({'action': 'update_self', 'count': message.user.counter.count}))
    Group('active').send(dump_to_ws_format({'action': 'update', 'user': message.user.username, 'count': message.user.counter.count}))


@channel_session_user
def ws_disconnect(message):
    Group('active').discard(message.reply_channel)
    Group('active').send(dump_to_ws_format({'action': 'discard', 'user': message.user.username}))


