from restDataProvider.models import PointOfInterest, Comments
from rest_framework import viewsets
from serializers import PointOfInterestSerializer, CommentSerializer


class PointOfInterestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows POIS to be viewed or edited.
    """
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Comments to be viewed or edited.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
