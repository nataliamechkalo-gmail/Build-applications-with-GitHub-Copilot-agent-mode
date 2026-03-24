"""
Script to populate the octofit_db MongoDB database with test data using Django ORM.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

# Create test users
user1, _ = User.objects.get_or_create(username='alice', defaults={'password': 'testpass'})
user2, _ = User.objects.get_or_create(username='bob', defaults={'password': 'testpass'})

# Create test teams
team1, _ = Team.objects.get_or_create(name='Team Alpha')
team2, _ = Team.objects.get_or_create(name='Team Beta')
team1.members.add(user1)
team2.members.add(user2)

# Create test activities
Activity.objects.get_or_create(user=user1, activity_type='run', duration=30, calories_burned=250, date='2023-01-01')
Activity.objects.get_or_create(user=user2, activity_type='cycle', duration=45, calories_burned=400, date='2023-01-02')

# Create test workouts
workout1, _ = Workout.objects.get_or_create(name='Cardio', description='Cardio workout')
workout2, _ = Workout.objects.get_or_create(name='Strength', description='Strength workout')
workout1.suggested_for.add(user1)
workout2.suggested_for.add(user2)

# Create leaderboard entries
Leaderboard.objects.get_or_create(user=user1, points=100)
Leaderboard.objects.get_or_create(user=user2, points=80)

print('Test data populated successfully!')
