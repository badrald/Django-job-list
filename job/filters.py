import django_filters 
from .models import Job,Category

class JobFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Job
        fields = "__all__"
        exclude= ['photo','category','slug','owner']
