from django.contrib import admin
from foo.banana.models import Variety

# def foo():
#     return None

# class VarietyAdmin(admin):

#     def queryset(self, request):
#         # particular case, as we want to be able to edit superadmin
#         return super(VarietyAdmin, self).queryset(request).filter(Q(owner=foo())
#                                                                   | Q(owner__isnull=True))

# admin.site.register(Variety, VarietyAdmin)
