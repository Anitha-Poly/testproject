from django.contrib import admin
from guestreviews.models import admini,guest,public,library,Book
# Register your models here.
admin.site.register(admini)
admin.site.register(guest)
admin.site.register(public)
admin.site.register(Book)
