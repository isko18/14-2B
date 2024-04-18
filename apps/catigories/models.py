from django.db import models

# Create your models here.
class Category(models.Model):
    title =models.CharField(
        max_length=255,
        verbose_name="Заголовок"        
    )
    parent = models.ForeignKey(
        'self', on_delete= models.CASCADE,
        related_name='subcategoty',
        verbose_name='Родетель',
        blank=True, null=True       
    )
    slug = models.SlugField(
        verbose_name='Человекопонятный URL'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категрия"
        verbose_name_plural = "Категории"