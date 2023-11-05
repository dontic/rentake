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


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "tenant",
        "start_date",
        "end_date",
        "price",
        "deposit",
    )
    search_fields = (
        "tenant",
        "start_date",
        "end_date",
        "price",
        "deposit",
    )
    list_filter = ("start_date", "end_date")


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
