# Click Clash

A basic example of a websockets app, which simply tracks the number of times
users click a button, and displays the live click counts to all visitors.

## Installation

#### Manual installation

Make a new virtualenv for the project, and run:

    pip install -r requirements.txt

Then, you'll need Redis running locally; the settings are configured to
point to `localhost`, port `6379`, but you can change this in the
`CHANNEL_LAYERS` setting in `settings.py`.

Finally, run:

    python manage.py migrate
    python manage.py runserver

#### Docker installation

Run the app:
  
    docker-compose up -d

The app will now be running on: {your-docker-ip}:8000

**Note:** You will need to prefix `python manage.py` commands with: `docker-compose run --rm web`. e.g.: `docker-compose run --rm web python manage.py createsuperuser`

Finally, run:

    docker-compose run --rm web python manage.py migrate


## Usage

Navigate to http://localhost:8000 and register for an account.  After
registering, go to the Play page (http://localhost:8000/play) and start
clicking the button.  You should see your counter increase for both
"Clientside" and "Websockets".

In incognito mode, register for a second account and you'll notice the
numbers update in real time for both users.  You'll also notice both
users appear in the Active Leaders pane.  Closing a session will
remove the user from the Active Leaders list.


## Further Reading

For more information about Django Channels: http://channels.readthedocs.org

This implementation was heavily influenced by the examples at https://github.com/andrewgodwin/channels-examples/
