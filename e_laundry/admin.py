from django.contrib import admin
from .models import demo
from .models import Holder
from .models import item
from .models import orders

# Register your models here.

admin.site.register(demo)
admin.site.register(Holder)
admin.site.register(item)
admin.site.register(orders)