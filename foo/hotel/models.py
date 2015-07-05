from django.db import models


class HotelCompany(models.Model):
    """Simple model
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)
    foo = models.IntegerField(default=0)
    bar = models.FloatField(default=0)
    alpha = models.TextField(max_length=300)


class HotelColor(models.Model):
    """Simple model
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)
    foo = models.IntegerField(default=0)
    bar = models.FloatField(default=0)
    alpha = models.TextField(max_length=300)


class HotelDoor(models.Model):
    """Simple model
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)
    foo = models.IntegerField(default=0)
    bar = models.FloatField(default=0)
    alpha = models.TextField(max_length=300)


class HotelColor(models.Model):
    """Simple model
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)
    foo = models.IntegerField(default=0)
    bar = models.FloatField(default=0)
    alpha = models.TextField(max_length=300)


class HotelSkin(models.Model):
    """Test non indexes foreign key
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)
    foo = models.IntegerField(default=0)
    alpha = models.TextField(max_length=300)
    bar = models.FloatField(default=0)
    

class Client(models.Model):
    """Simple model
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)


class Hotel(models.Model):
    """Simple model
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)
    objtxt = models.TextField()
    color = models.ForeignKey(HotelColor)
    skin = models.ForeignKey(HotelSkin)
    door = models.ForeignKey(HotelDoor)
    company = models.ForeignKey(HotelCompany)

    def __unicode__(self):
        return self.name

    def uppername(self):
        return self.name.upper()

class Night(models.Model):
    """Simple model
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)
    client = models.ManyToManyField(Client)
    hotel = models.ManyToManyField(Hotel)


