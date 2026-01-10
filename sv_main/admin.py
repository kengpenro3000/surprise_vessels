from django.contrib import admin
from .models import *
# from .models.results import Results
# from .models.results import Results


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Results)
admin.site.register(Question)
admin.site.register(Answer)
