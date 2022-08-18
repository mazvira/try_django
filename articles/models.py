from django.db.models.signals import pre_save, post_save
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

import random

class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish=models.DateField(
        auto_now_add=False, auto_now=False, default=timezone.now, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        '''
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        '''
        
def slugify_instance_title(instance, save=False, new_slug=None):

    if new_slug is not None:
        slug = new_slug
    else:    
        slug = slugify(instance.title)
    qs = Article.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.rand_int(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance 

def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify_instance_title(instance)
    print('pre_save')
    print(sender, instance)

pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    print(sender, instance)

    if created:
        instance.slug = 'this is my slug'
        instance.save()

post_save.connect(article_post_save, sender=Article)