from django.db import models

class Drink(models.Model):
    korean_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    allergy = models.ManyToManyField('Allergy')
    nutrition = models.ManyToManyField('Size', through='Nutrition')

    def __str__(self) -> str:
        return self.korean_name
    class Meta:
        db_table = 'drink'


class Category(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'category'


class Menu(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'menu'


class Image(models.Model):
    url = models.TextField()
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    class Meta:
        db_table = 'image'


class Allergy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'allergy'


class Nutrition(models.Model):
    one_serving_kcal = models.IntegerField()
    sodium_mg = models.IntegerField()
    saturated_fat_g = models.IntegerField()
    sugars_g = models.IntegerField()
    protein_g = models.IntegerField()
    caffeine_mg = models.IntegerField()
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.one_serving_kcal
    class Meta:
        db_table = 'nutrition'


class Size(models.Model):
    name = models.CharField(max_length=50)
    size_ml = models.IntegerField()
    size_fluid_ounce = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'size'
