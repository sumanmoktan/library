from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrower)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Reviews)
