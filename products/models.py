from django.db import models

class Drink(models.Model):
    korean_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    allergy = models.ManyToManyField('Allergy')
    nutritions = models.ManyToManyField('Size', through='Nutrition')

    def __str__(self) -> str:
        return self.korean_name
    class Meta:
        db_table = 'drinks'


class Category(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'categories'


class Menu(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'menus'


class Image(models.Model):
    url = models.TextField()
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    class Meta:
        db_table = 'images'


class Allergy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'allergies'


class Nutrition(models.Model):
    one_serving_kcal = models.IntegerField(null=True)
    sodium_mg = models.IntegerField(null=True)
    saturated_fat_g = models.IntegerField(null=True)
    sugars_g = models.IntegerField(null=True)
    protein_g = models.IntegerField(null=True)
    caffeine_mg = models.IntegerField(null=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey('Size', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.one_serving_kcal

    class Meta:
        db_table = 'nutritions'


class Size(models.Model):
    name = models.CharField(max_length=50)
    size_ml = models.IntegerField(null=True)
    size_fluid_ounce = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'sizes'
