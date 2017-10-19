from rest_framework_mongoengine import serializers
from models import boardgamedeals

class DealsHandlerSerializer(serializers.DocumentSerializer):
	class Meta:
		model = boardgamedeals
		fields = '__all__'