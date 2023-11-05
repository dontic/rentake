from django.db import models


class Tenant(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Property(models.Model):
    title = models.CharField(max_length=200)
    catastral_reference = models.CharField(max_length=200)
    storage_room_number = models.CharField(max_length=200, blank=True, null=True)
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    postcode = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    is_rented = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Parking(models.Model):
    number = models.CharField(max_length=200)
    floor = models.IntegerField()
    associated_property = models.ForeignKey(
        Property, on_delete=models.SET_NULL, blank=True, null=True
    )
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    postcode = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    is_rented = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.number}"


class Contract(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(
        Property, on_delete=models.SET_NULL, blank=True, null=True
    )
    parkings = models.ManyToManyField(Parking, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    file = models.FileField(upload_to="contracts", blank=True, null=True)

    def __str__(self):
        return f"{self.tenant} - {self.property}"
