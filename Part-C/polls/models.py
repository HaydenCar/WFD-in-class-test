from django.db import models

# Create your models here.
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=255, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=10)
    year = models.IntegerField()
    car_for_sale = models.BooleanField()

class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)

class Sales_Person(models.Model):
    sales_person_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=30)
    address = models.TextField()
    city = models.CharField(max_length=20)
    state_slash_province = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=7)

class Parts(models.Model):
    parts_id = models.AutoField(primary_key=True)
    part_number = models.IntegerField()
    description = models.TextField()
    purchase_price = models.FloatField()
    retail_price = models.FloatField()

class Sales_Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=45, unique=True)
    date = models.DateField()
    car_id = models.ForeignKey(Car)
    customer_id = models.ForeignKey(Customer)
    salesperson_id = models.ForeignKey(Sales_Person)

class Service_Ticket(models.Model):
    service_ticket_id = models.AutoField(primary_key=True)
    service_ticket_number = models.CharField(max_length=45, unique=True)
    car_id = models.ForeignKey(Car)
    customer_id = models.ForeignKey(Customer)
    date_received = models.DateField()
    comments = models.TextField()
    date_returned_to_customer = models.DateField()

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=30)
    hourly_rate = models.IntegerField()

class Service_Mechanic(models.Model):
    service_ticket_id = models.ForeignKey(Service_Ticket)
    service_id = models.ForeignKey(Service)
    mechanic_id = models.ForeignKey(Mechanic)

class Parts_Used(models.Model):
    parts_used_id = models.ForeignKey(Service_Ticket)
    service_id = models.ForeignKey(Service)
    mechanic_id = models.ForeignKey(Mechanic)
