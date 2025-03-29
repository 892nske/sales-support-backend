from django.contrib import admin
from .models import Investor, Proposal, ChatMessage

admin.site.register(Investor)
admin.site.register(Proposal)
admin.site.register(ChatMessage)
