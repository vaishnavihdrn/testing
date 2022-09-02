from django.contrib import admin
import site
from datetime import date
from .models import Employee, Role
from django.contrib.admin import SimpleListFilter

# Register your models here.
class AgeFilter(SimpleListFilter):
   title = "Age"
   parameter_name = "pages"

   def lookups(self, request, model_admin):
       return [
           ("<=30s", "less or equal 30"),
           (">30", "greater than 30")
       ]

   def queryset(self, request, queryset):
       today = date.today()
       past_30_yr = today.replace(year=today.year - 30)
       if self.value() == "<=30":
           return queryset.filter(dob__gte=past_30_yr)
       elif self.value() == ">30":
           return queryset.filter(dob__lt=past_30_yr)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'dob','role','doj','experience','active')
    list_filter = ('role', AgeFilter)

    def age(self, obj):
        return obj.age()

    def experience(self, obj):
        return obj.experience()

admin.site.register(Role)