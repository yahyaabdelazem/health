from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Hospital, HospType, HospDept, Government, Surgery, SurgType, Report, Malfunction, Missing


class HospitalAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(HospitalAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(admin=request.user)


admin.site.register(Hospital, HospitalAdmin)


class HospTypeAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(HospTypeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(hosptype__admin=request.user)


admin.site.register(HospType, HospTypeAdmin)

admin.site.register(HospDept)

admin.site.register(Government)


class SurgeryAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(SurgeryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(hospital__admin=request.user)


admin.site.register(Surgery, SurgeryAdmin)

admin.site.register(SurgType)


class ReportAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(ReportAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(hospital__admin=request.user)


admin.site.register(Report, ReportAdmin)


class MalfunctionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(MalfunctionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(report__hospital__admin=request.user)


admin.site.register(Malfunction, MalfunctionAdmin)


class MissingAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(MissingAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(report__hospital__admin=request.user)


admin.site.register(Missing, MissingAdmin)

