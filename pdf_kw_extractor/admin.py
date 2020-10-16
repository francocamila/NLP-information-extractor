from django.contrib import admin


from django.contrib import admin
from .models import Jugdments
from .models import UploadPdf

# Register your models here.
admin.site.register(Jugdments)
admin.site.register(UploadPdf)