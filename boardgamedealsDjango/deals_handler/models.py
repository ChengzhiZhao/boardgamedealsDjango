# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import *

connect('boardgamedealscrapy')

# Create your models here.

class boardgamedeals(Document):
	name = StringField(max_length=200, required=True)
	original_price = StringField(max_length=200, required=True)
	price = StringField(max_length=200, required=True)
	url = StringField(max_length=200, required=True)
	img_url = StringField(max_length=200, required=True)