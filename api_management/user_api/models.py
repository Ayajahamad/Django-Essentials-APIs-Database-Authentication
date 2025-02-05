from django.db import models

# User Model
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Hair Model
class Hair(models.Model):
    user = models.OneToOneField(User, related_name='hair', on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.color} {self.type}"


# Address Model for User
class UserAddress(models.Model):
    user = models.ForeignKey(User, related_name='address', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    post_code = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"


# Bank Model
class Bank(models.Model):
    user = models.ForeignKey(User, related_name='bank', on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    card_type = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    iban = models.CharField(max_length=34)

    def __str__(self):
        return f"{self.card_type} - {self.card_number}"


# Company Model
class Company(models.Model):
    user = models.ForeignKey(User, related_name='company', on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.department}"


# Address Model for Company
class CompanyAddress(models.Model):
    company = models.ForeignKey(Company, related_name='address', on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"
