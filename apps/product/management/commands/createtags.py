from apps.product.models import Tag
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="Creates @all tag"

    def handle(self, *args, **kwargs):
        pr = Tag.objects.create(name='all')
        pr = Tag.objects.create(name='farming')
        pr = Tag.objects.create(name='metallurgy')
        pr.save()
