from django.db import models
from django.contrib.auth.models import User
from .encryption_util import encrypt


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    def encrypt_category(self):
        return encrypt(self.id)


class Haiku(models.Model):

    COMMENT_STATUS_CHOICES = (
        ('hide', 'hide'),
        ('show', 'show'),
        ('featured', 'featured'),
    )

    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    haiku_status = models.CharField(max_length=45)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    # foreign keys
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        if self.title != "":
            return self.title
        else:
            return self.author

    class Meta:
        verbose_name_plural = "Haiku"

    def encrypt_haiku(self):
        return encrypt(self.id)


class Comment(models.Model):
    COMMENT_STATUS_CHOICES = (
        ('hide', 'hide'),
        ('show', 'show'),
    )

    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, blank=True, null=True)
    comment = models.CharField(max_length=500)
    rating = models.FloatField()
    comment_status = models.CharField(choices=COMMENT_STATUS_CHOICES, max_length=45)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    # foreign keys
    haiku = models.ForeignKey(Haiku, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Entry_Status(models.Model):
    entry_status = models.CharField(max_length=45, unique=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.entry_status

    class Meta:
        verbose_name_plural = "Entry Status"


class Entry(models.Model):

    THEMES = {
        ('', '---------'),
        ('human nature', 'human nature'),
        ('nature and seasons', 'nature and seasons'),
        ('others', 'others'),
    }

    full_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=254)
    haiku_title = models.CharField(max_length=100, blank=True, null=True)
    haiku_entry = models.CharField(max_length=500)
    author_alias = models.CharField(max_length=100)
    haiku_theme = models.CharField(choices=sorted(THEMES), max_length=100)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    # foreign keys
    entry_status = models.ForeignKey(Entry_Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.haiku_entry

    class Meta:
        verbose_name_plural = "Entries"

    def encrypt_entry(self):
        return encrypt(self.id)









