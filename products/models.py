from django.db import models

class Product(models.Model):
    korean_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    allergy = models.ManyToManyField('Allergy')
    sizes = models.ManyToManyField('Size', through="Nutrition")

    def __str__(self) -> str:
        return self.korean_name
    class Meta:
        db_table = 'products'


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
    url = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        db_table = 'images'


class Allergy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'allergies'


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey('Size', on_delete=models.CASCADE, null=True)
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
