from django.contrib import admin
from hood.models import Neighbourhood, Post, Profile, Business, Health, Police

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Health)
admin.site.register(Police)