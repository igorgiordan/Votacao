from django.contrib import admin
from .models import *

admin.site.register(UUIDUser)
admin.site.register(Proposal)
admin.site.register(Comment)
admin.site.register(Vote)