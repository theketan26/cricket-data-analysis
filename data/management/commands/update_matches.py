from django.core.management.base import BaseCommand
from data.functions.update import updateMatches


class Command(BaseCommand):
    help = 'Update match data from README.txt file to Django SQLite database'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Starting to update match data from README.txt...')
        )

        try:
            updateMatches()
            self.stdout.write(
                self.style.SUCCESS('Successfully updated match data')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error during update: {str(e)}')
            )
            raise