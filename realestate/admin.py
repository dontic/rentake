from django.contrib import admin
from django import forms
from .models import *


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")
    search_fields = ("first_name", "last_name", "email", "phone")


@admin.register(RentalAsset)
class RentalAssetAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "catastral_reference",
        "is_rented",
    )
    search_fields = (
        "title",
        "catastral_reference",
        "parking_number",
        "number_of_bedrooms",
        "number_of_bathrooms",
        "address_line_1",
        "address_line_2",
        "postcode",
        "city",
        "province",
        "country",
        "is_rented",
    )
    list_filter = ("is_rented",)


class RentalAssetTitleFilter(admin.SimpleListFilter):
    title = "Rental Asset Title"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        rental_assets = set()
        for obj in model_admin.model.objects.all():
            for rental_asset in obj.rental_assets.all():
                rental_assets.add(rental_asset)
        return [(rental_asset.id, rental_asset.title) for rental_asset in rental_assets]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title=self.value())
        else:
            return queryset

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "list_tenants",
        "list_rental_assets",
        "start_date",
        "end_date",
        "price",
        "deposit",
    )
    search_fields = (
        "start_date",
        "end_date",
        "price",
        "deposit", 
    ) 
    list_filter = (RentalAssetTitleFilter, "start_date", "end_date",)

    def list_tenants(self, obj):
        return ", ".join([tenant.first_name for tenant in obj.tenants.all()])
    list_tenants.short_description = "Tenants"

    def list_rental_assets(self, obj):
        return ", ".join([rental_asset.title for rental_asset in obj.rental_assets.all()])
    list_rental_assets.short_description = "Rental Assets"

    def catrastral_reference(self, obj):
        return obj.rental_assets.catastral_reference
    catrastral_reference.short_description = "Catastral Reference"





@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "rental_asset",
        "price",
        "start_date",
        "end_date",
        "is_active",
    )
    search_fields = (
        "rental_asset",
        "price",
        "start_date",
        "end_date",
        "is_active",
    )
    list_filter = ("start_date", "end_date", "is_active")
