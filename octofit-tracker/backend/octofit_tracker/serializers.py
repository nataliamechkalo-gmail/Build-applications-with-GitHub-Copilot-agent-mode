from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard
from bson import ObjectId

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
    def get_id(self, obj):
        return str(obj.id)

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'members', 'created_at']
    def get_id(self, obj):
        return str(obj.id)

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'calories_burned', 'date']
    def get_id(self, obj):
        return str(obj.id)

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    suggested_for = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for']
    def get_id(self, obj):
        return str(obj.id)

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'total_points', 'updated_at']
    def get_id(self, obj):
        return str(obj.id)
