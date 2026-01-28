from django.core.management.base import BaseCommand
from data.functions.clean import cleanUnwantedMatches


class Command(BaseCommand):
    help = 'Clean unwanted match data by removing matches of specific types from the database'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Starting to clean unwanted match data...')
        )

        try:
            result = cleanUnwantedMatches()
            self.stdout.write(
                self.style.SUCCESS(f'Successfully cleaned match data: {result}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error during cleaning: {str(e)}')
            )
            raise