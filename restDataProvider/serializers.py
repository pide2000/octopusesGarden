from restDataProvider import models
from rest_framework import serializers


class PointOfInterestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PointOfInterest
        fields = ('title', 'lon', 'lat', 'description', 'rating', 'deleted')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Comments
        fields = ('poi', 'text')