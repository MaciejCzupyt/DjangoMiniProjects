from django.db import models


class UrlData(models.Model):
    url = models.CharField(max_length=200)  # Full URL
    slug = models.CharField(max_length=15)  # Shortened URL

    def __str__(self):
        return f"url:{self.url}\nslug:{self.slug}"
