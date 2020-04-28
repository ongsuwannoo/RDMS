from django.contrib import admin

from index.models import user

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(user, AuthorAdmin)
