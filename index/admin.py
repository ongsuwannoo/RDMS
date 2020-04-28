from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)
    group.short_description = 'Groups'

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'group')

admin.site.register(user, AuthorAdmin)
admin.site.register(Personal)
admin.site.register(Permission)

admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
