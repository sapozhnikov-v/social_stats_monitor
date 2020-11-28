from django.views.generic import ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.core.paginator import Paginator
from django.shortcuts import render


from .models import Source, Stat
from .serializers import SourceSerializer, StatSerializer


class SourceViewSet(ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type_social', ]
    search_fields = ['name']
    ordering_fields = ['id', 'name']


class StatViewSet(ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['source', ]
    search_fields = ['date', 'source']
    ordering_fields = ['id', 'updated_at', 'source']


class SourceDetailView(DetailView):

    model = Source


class SourcesListView(ListView):

    model = Source
    context_object_name = 'sources'
    paginate_by = 8


def listing(request):
    sources_list = Source.objects.all()
    paginator = Paginator(sources_list, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'monitor/source_list.html', {'page_obj': page_obj})


class SourceCreateView(CreateView):

    model = Source
    fields = '__all__'

    def get_success_url(self):
        return '/monitor/sources/'
