from django.contrib import admin
from .models import User, TokenBlackList

admin.site.register(User)
admin.site.register(TokenBlackList)

