from django.db import models


class Tenant(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    NIF = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class RentalAsset(models.Model):
    HOUSE_TYPE = "house"
    PARKING_TYPE = "parking"

    ASSET_TYPES = [
        (HOUSE_TYPE, "House"),
        (PARKING_TYPE, "Parking"),
    ]

    type = models.CharField(max_length=10, choices=ASSET_TYPES, default=HOUSE_TYPE)
    title = models.CharField(max_length=200)
    catastral_reference = models.CharField(max_length=200)
    parking_number = models.CharField(max_length=200, blank=True, null=True)
    number_of_bedrooms = models.IntegerField(blank=True, null=True)
    number_of_bathrooms = models.IntegerField(blank=True, null=True)
    storage_room = models.IntegerField(blank=True, null=True)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    postcode = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    is_rented = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.catastral_reference}"


class Price(models.Model):
    rental_asset = models.ForeignKey(
        RentalAsset, on_delete=models.CASCADE, related_name="prices"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.rental_asset} - {self.price}"


class Contract(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    rental_assets = models.ManyToManyField(RentalAsset)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    file = models.FileField(upload_to="contracts", blank=True, null=True)

    def __str__(self):
        return f"{self.tenant} - {self.rental_assets}"
