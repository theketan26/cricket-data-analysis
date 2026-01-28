from django.core.management.base import BaseCommand
from data.functions.transform import extract_teams


class Command(BaseCommand):
    help = 'Extract team and player information from match data and save to JSON file'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Starting to extract team and player data...')
        )

        try:
            result = extract_teams()
            self.stdout.write(
                self.style.SUCCESS('Successfully extracted team and player data')
            )
            # Optionally show some info about what was extracted
            if isinstance(result, dict):
                team_count = len(result)
                total_players = sum(len(players) for players in result.values())
                self.stdout.write(
                    self.style.SUCCESS(f'Extracted {team_count} teams with {total_players} total players')
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error during extraction: {str(e)}')
            )
            raise