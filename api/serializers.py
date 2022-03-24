from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = []


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = []


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = []


class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(Profile)
    tags = TagSerializer(Tag, many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        exclude = []

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        return ReviewSerializer(reviews, many=True).data
