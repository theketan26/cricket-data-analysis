from django.core.management.base import BaseCommand
from data.functions.transform import transformformatplayers


class Command(BaseCommand):
    help = 'Transform player data for a specific cricket format (e.g., ODI, T20, Test)'

    def add_arguments(self, parser):
        parser.add_argument(
            'format',
            type=str,
            help='The cricket format to process (e.g., ODI, T20, Test)'
        )

    def handle(self, *args, **options):
        format_type = options['format']
        self.stdout.write(
            self.style.SUCCESS(f'Starting transformation for {format_type} format...')
        )

        try:
            transformformatplayers(format_type)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully completed transformation for {format_type} format')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error during transformation: {str(e)}')
            )
            raise