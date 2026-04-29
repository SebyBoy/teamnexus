from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Department)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Repository)
admin.site.register(ContactChannel)
admin.site.register(Dependency)
admin.site.register(Message)
admin.site.register(Meeting)