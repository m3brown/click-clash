from django.contrib import admin
from .models import Counter


admin.site.register(
    Counter,
    list_display=["id", "user", "count"],
    list_display_links=["id"],
)
