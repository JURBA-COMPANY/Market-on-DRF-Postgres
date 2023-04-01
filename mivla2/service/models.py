from django.db import models


class Users(models.Model):
    class Meta:
        db_table = 'users'
        managed = False
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, max_length=50),
    second_name = models.CharField(null=False, max_length=50)
    phone = models.CharField(null=False, max_length=12)
    email = models.CharField(null=False, max_length=100)


class Colours(models.Model):
    class Meta:
        db_table = 'colours'
        managed = False
    colour_id = models.BigAutoField(primary_key=True)
    colour_name = models.CharField(null=False, max_length=30)


class Diler(models.Model):
    class Meta:
        db_table = 'diler'
    diler_id = models.AutoField(primary_key=True)
    diler_name = models.CharField(null=False, max_length=30)
    is_related = models.BooleanField(null=False)


class Shipment(models.Model):
    class Meta:
        db_table = 'shipment'
    ship_id = models.BigAutoField(primary_key=True)
    ship_date = models.DateField(null=False)
    weigth = models.FloatField(max_length=30)
    diler_id = models.ForeignKey(to='Diler', on_delete=models.CASCADE)


class Furniture(models.Model):
    class Meta:
        db_table = 'furniture'

    length = models.FloatField(max_length=20, null=False, blank=False)
    height = models.FloatField(max_length=20, null=False, blank=False)
    depth = models.FloatField(max_length=20, null=False, blank=False)
    ship_name = models.ForeignKey(to='Shipment', on_delete=models.CASCADE)
    colour_id = models.ForeignKey(to='Colours', on_delete=models.CASCADE)


class Sofa(models.Model):
    class Meta:
        db_table = 'sofa'

    self_id = models.AutoField(primary_key=True)
    fur_id = models.ForeignKey(to='Furniture', on_delete=models.PROTECT)
    num_seats = models.IntegerField(null=False, blank=False)
    expand = models.BooleanField(null=False)
    corner = models.BooleanField(null=False)


class Wardrobe(models.Model):
    class Meta:
        db_table = 'wardrobe'

    self_id = models.AutoField(primary_key=True)
    fur_id = models.ForeignKey(to='Furniture', on_delete=models.PROTECT)
    num_shelfs = models.IntegerField(null=False, blank=False)


class Stol(models.Model):
    class Meta:
        db_table = 'stol'

    self_id = models.AutoField(primary_key=True)
    fur_id = models.ForeignKey(to='Furniture', on_delete=models.PROTECT)
    expand = models.BooleanField(null=False)


class Orders(models.Model):
    class Meta:
        db_table = 'orders'

    user_id = models.ForeignKey(to='Users', on_delete=models.PROTECT)
    order_date = models.DateField(null=False)
    order_cost = models.FloatField(max_length=15, null=False)
