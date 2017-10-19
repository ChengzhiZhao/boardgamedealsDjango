# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from rest_framework_mongoengine import viewsets
from .deals_handler_serializers import DealsHandlerSerializer
from .models import boardgamedeals

class DealsViewSet(viewsets.ModelViewSet):
	lookup_field = 'id'
	serializer_class = DealsHandlerSerializer
	
	def get_queryset(self):
		return boardgamedeals.objects.all()