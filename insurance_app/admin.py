from django.contrib import admin
from .models import InsurancePlan, UserPolicy, Claim, User

admin.site.register(InsurancePlan)
admin.site.register(UserPolicy)
admin.site.register(Claim)
admin.site.register(User)

# Register your models here.
