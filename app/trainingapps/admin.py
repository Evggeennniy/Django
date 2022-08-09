from django.contrib import admin
from trainingapps.models import Rate, Source, ContactUs
from import_export import resources
from import_export.admin import ExportMixin
# from import_export.fields import Field
# from rangefilter.filters import DateTimeRangeFilter

# Register your models here.

"""
RESOURCES
"""


class RateResource(resources.ModelResource):
    """Field represent mapping between object field and representation of this field.

    Parameters:
attribute – A string of either an instance attribute or callable off the object.
column_name – Lets you provide a name for the column that represents this field in the export.
widget – Defines a widget that will be used to represent this field’s data in the export.
readonly – A Boolean which defines if this field will be ignored during import.
default – This value will be returned by clean() if this field’s widget did not return an adequate value.
saves_null_values – Controls whether null values are saved on the object
clean(data, **kwargs)
Translates the value stored in the imported datasource to an appropriate Python object and returns it.
    export(obj)
        Returns value from the provided object converted to export representation.
    get_value(obj)
        Returns the value of the object’s attribute.
    save(obj, data, is_m2m=False, **kwargs)
If this field is not declared readonly, the object’s attribute will be set to the value returned by clean()."""

    # add_column = Field(column_name='export_date')
    # ^ Declaring fields. Available field types and options.

    # def dehydrate_full_title(self, book):
    #     book_name = getattr(book, "name", "unknown")
    #     author_name = getattr(book.author, "name", "unknown")
    #     return '%s by %s' % (book_name, author_name)
    # ^ Advanced data manipulation on export.

    class Meta:
        """
        In Django, we use Django models to design our database tables and their fields.
        If we need to add data about the model itself, we use the Meta class.
        """

        model = Rate
        # ^ Selection of the appropriate model.

        skip_unchanged = True
        # ^ By default all records will be imported, even if no changes are detected.
        # This can be changed setting the skip_unchanged option.

        report_skipped = False
        # ^ Also, the report_skipped option controls whether skipped records appear in the import Result object,
        # and if using the admin whether skipped records will show in the import preview page.

        # import_id_fields = (
        #     "id"
        # )  # ^  The default field for object identification is id,
        # you can optionally set which fields are used as the id when importing.

        fields = (
            "id",
            "ccy",
            "base_ccy",
            "buy",
            "sell",
        )  # ^ To affect which model fields will be included in an import-export resource,
        # use the fields option to whitelist fields.

        # exclude = (
        #     'imported',
        # )  # ^ Or the exclude option to blacklist fields.

        export_order = (
            "base_ccy",
            "ccy",
            "sell",
            "buy",
            "id",
        )  # ^ An explicit order for exporting fields can be set using the export_order option.
# ^ Configuring Import Export for Models.


"""
Admins
"""


class RateAdmin(ExportMixin, admin.ModelAdmin):  # Creating a model for admin
    # ^ Note that ExportActionMixin is declared first in the example above!

    resource_class = RateResource
    # ^ Select resource class

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
    )  # ^ Setting non-editable fields.

    # Or this, permission for all users.
    # def has_(change, add, edit, delete)_permission(self, request, obj=None):
    #     return False

    list_filter = (
        "base_ccy",
        "ccy",
    )  # ^ Default additional django filter.

    # Or this to advanced filter.
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


admin.site.register(Rate, RateAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
# ^ Сonnection of the application model with the admin model
