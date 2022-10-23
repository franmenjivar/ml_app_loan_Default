from rest_framework import serializers
from .models import CustomerAnalytics

'''
ScoreSerializer class extending the rest_framework class.
the model CustomerAnalytics is being declared to be serialized with all the defined parameters.
@Author Erick.
'''

class ScoreSerializer(serializers.ModelSerializer):
    class Meta():
        model = CustomerAnalytics
        fields = ('id','client','default_probability','updated_at')
