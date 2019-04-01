from django.contrib import admin
from .models import Profile, Projects, Categories,Image

# Register your models here.

admin.site.register(categories)
admin.site.register(technologies)
admin.site.register(colors)
admin.site.register(countries)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Profile)
admin.site.register(Rating)
# Register your models here.
