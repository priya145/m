from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


# Register your models here.
admin.site.register(Movie, ImportExportModelAdmin)

admin.site.register(BiharCandidate, ImportExportModelAdmin)

admin.site.register(BiharWinners, ImportExportModelAdmin)

admin.site.register(BiharRunners, ImportExportModelAdmin)

admin.site.register(DubbakaCandidate, ImportExportModelAdmin)

admin.site.register(DubbakaWinners, ImportExportModelAdmin)

admin.site.register(DubbakaRunners, ImportExportModelAdmin)

