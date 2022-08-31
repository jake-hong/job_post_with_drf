from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.db import transaction

from rest_framework import viewsets, mixins, status, filters

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import JobPost
from .serializers import JobPostSerializer


class JobPostViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        print(queryset)
        return queryset

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = JobPostSerializer(data=request.data, context={'request' : request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            serializered_job_post = serializer.data

        return Response(serializered_job_post, status=status.HTTP_201_CREATED)

    @action(methods=['DELETE'], detail=False)
    def delete(self, request):
        queryset = super().get_queryset()
        pk = self.request.query_params.get('id')
        job_post = queryset.filter(company=pk)
        print(job_post)
        job_post.delete()

        return Response('delete success', status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         self.perform_destroy(instance)
    #     except Http404:
    #         pass
    #     return Response('delete success', status=status.HTTP_204_NO_CONTENT)
    #
    # def perform_destroy(self, instance):
    #     instance.delete()