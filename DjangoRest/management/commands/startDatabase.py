from Products.models import Estado
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create initial database"
    
    def handle(self, *args, **kwargs):
        estados = ['Activo', 'Inactivo']

        for estado in estados:
            nuevo_estado, created = Estado.objects.get_or_create(nombre=estado)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Estado "{estado}" creado exitosamente.'))
            else:
                self.stdout.write(self.style.WARNING(f'Estado "{estado}" ya existe.'))