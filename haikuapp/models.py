from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


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
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    # foreign keys
    haiku = models.ForeignKey(Haiku, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Entry_Status(models.Model):
    ENTRY_STATUS_CHOICES = (
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    )

    entry_status = models.CharField(choices=ENTRY_STATUS_CHOICES, max_length=45)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.entry_status

    class Meta:
        verbose_name_plural = "Entry Status"


class Entry(models.Model):
    full_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=254)
    haiku_title = models.CharField(max_length=100)
    haiku_entry = models.CharField(max_length=500)
    author_alias = models.CharField(max_length=100)
    haiku_theme = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    # foreign keys
    entry_status = models.ForeignKey(Entry_Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.haiku_entry

    class Meta:
        verbose_name_plural = "Entries"








