from courses_guidance.models import Course, Stream
from rest_framework import serializers
class StreamSerializers(serializers.ModelSerializer):
  class Meta:
    model = Stream
    fields = '__all__'

class CourseSerializers(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'    