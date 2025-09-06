from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Verify ORM data population for all models.'

    def handle(self, *args, **kwargs):
        print(f'Users: {User.objects.count()}')
        print(f'Teams: {Team.objects.count()}')
        print(f'Activities: {Activity.objects.count()}')
        print(f'Leaderboard: {Leaderboard.objects.count()}')
        print(f'Workouts: {Workout.objects.count()}')
