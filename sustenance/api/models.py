from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Benefit(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='benefits/',
                                      default='benefits/default_benefit.png')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'benefits'
        ordering = ('name', 'image',)


class Nutrient(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='nutrients/',
                                       default='nutrients/default_nutrient.png')
    nutrient_benefits = models.ManyToManyField(Benefit, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'nutrients'
        ordering = ('name', 'image',)


class Origin(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'origins'
        ordering = ('name',)


class Item(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to='items/',
        default='items/default_item.png'
    )
    item_categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_benefits = models.ManyToManyField(Benefit)
    item_nutrients = models.ManyToManyField(Nutrient)
    item_origins = models.ManyToManyField(Origin)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'items'
        ordering = (
            'name',
            'image',
            'item_categories'
        )

