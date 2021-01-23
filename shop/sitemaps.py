from django.contrib.sitemaps import Sitemap
from .models import Product
from django.urls import reverse

class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority=0.9
    i18n=True

    def items(self):
        return Product.objects.filter(available=True)

    # def location(self, item):
    #     return reverse(item)

    def lastmod(self, obj):
        return obj.updated


    # def save(self, force_insert=False, force_update=False):
    #     super().save(force_insert, force_update)
    #     try:
    #         ping_google()
    #     except Exception:
    #         # Bare 'except' because we could get a variety
    #         # of HTTP-related exceptions.
    #         pass
