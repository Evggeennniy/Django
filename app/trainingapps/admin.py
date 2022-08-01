from django.contrib import admin
from trainingapps.models import Rate, Source, ContactUs
# from rangefilter.filters import DateTimeRangeFilter

# Register your models here.


class RateAdmin(admin.ModelAdmin):  # Creating a model for admin
    list_display = (
        "id",
        "base_ccy",
        "ccy",
        "sell",
        "buy",
    )  # ^ Customizing the output of table information

    search_fields = (
        "id",
        "base_ccy",
        "ccy",
    )  # ^ Basic search, the more fields the slower

    readonly_fields = (
        "base_ccy",
        "ccy",
        "sell",
        "buy",
    )  # ^ Setting non-editable fields
    # or this, permission for all users
    # def has_change_permission(self, request, obj=None):
    #     return False

    # list_filter = (
    #     "id",
    #     "created"
    # )  # ^ Default additional django search
    # or this to advanced search
    # list_filter = (
    #    ("created", DateTimeRangeFilter),
    # )

    def has_delete_permission(self, request, obj=None):
        return False
    # ^ Restriction on deletion for all users


class SourceAdmin(admin.ModelAdmin):  # Creating a model for admin
    list_display = (
        "id",
        "source_url",
        "name",
    )

    search_fields = (
        "id",
        "name",
    )

    def has_delete_permission(self, request, obj=None):
        return False


class ContactUsAdmin(admin.ModelAdmin):  # Creating a model for admin
    list_display = (
        "id",
        "email_from",
        "email_to",
        "subject",
        "message",
    )

    search_fields = (
        "id",
        "email_from",
        "email_to",
        "subject",
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Rate, RateAdmin)  # Сonnection of the application model with the admin model
admin.site.register(Source, SourceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
