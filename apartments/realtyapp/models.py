from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class Apartment(models.Model):
    CATEGORY_CHOICES = (
        ('New Buildings', _('New Buildings')),
        ('Houses', _('Houses')),
        ('Garages', _('Garages')),
    )
    name = models.CharField(verbose_name=_("Название"), max_length=256)
    price = models.IntegerField(_("Цена"))
    description = models.TextField(_("Описание"))
    type = models.CharField(_("Тип"), max_length=128)
    area = models.FloatField(_("Площадь"))
    floor = models.CharField(_("Этаж"), max_length=16)
    location = models.CharField(_("Локация"), max_length=512)
    year = models.IntegerField(_("Год постройки"))
    station = models.CharField(_("Метро"), max_length=256, default='Первомайская', null=True, blank=True)
    category = models.CharField(_("Категория"), max_length=128, choices=CATEGORY_CHOICES, default='New Buildings')

    def __str__(self):
        return self.name
    
class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(_(""), upload_to='apartment_images/')
    
    
class Favorites(models.Model):
    apartment_id = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    def __str__(self):
        return f"Apartment: {self.apartment_id.name} - User: {self.user.username}"
    
    
class Purchases(models.Model):
    apartment_id = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    def __str__(self):
        return f"Apartment: {self.apartment_id.name} - User: {self.user.username}"