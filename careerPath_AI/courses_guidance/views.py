from courses_guidance.models import Course, Stream
from courses_guidance.serializers import CourseSerializers, StreamSerializers
#from courses_guidance.models import Course, Stream
#from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# class StreamViewSet(viewsets.ModelViewSet):
#   queryset = Stream.objects.all()
#   serializer_class = StreamSerializers

# class CourseViewSet(viewsets.ModelViewSet):
#   queryset = Course.objects.all()
#   serializer_class = CourseSerializers 

@api_view(['GET'])
def get_stream(request):
  stream = Stream.objects.all()
  serializer_stream = StreamSerializers(stream,many=True)
  return Response(serializer_stream.data)

@api_view(['POST'])
def create_stream(request):
  serializer_stream = StreamSerializers(data = request.data)
  if serializer_stream.is_valid():
    serializer_stream.save()
    return Response(serializer_stream.data,status = status.HTTP_201_CREATED)
  return Response(serializer_stream.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def stream_detail(request, pk):
  try:
    stream = Stream.objects.get(pk=pk)
  except Stream.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer_stream = StreamSerializers(stream)
    return Response(serializer_stream.data)
  
  elif request.method == 'PUT':
    serializer_stream = StreamSerializers(stream, data = request.data)
    if serializer_stream.is_valid:
      serializer_stream.save()
      return Response(serializer_stream.data)
    return Response(serializer_stream.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    stream.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_course(request):
  course = Course.objects.all()
  serializer_course = CourseSerializers(course,many = True)
  return Response(serializer_course.data)

@api_view(['POST'])
def create_course(request):
  serializer_couse = CourseSerializers(data=request.data)
  if serializer_couse.is_valid():
    serializer_couse.save()
    return Response(serializer_couse.data, status=status.HTTP_201_CREATED)
  return Response(serializer_couse.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def course_deatil(request,pk):
  try:
    course = Course.objects.get(pk=pk)
  except Course.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer_course = CourseSerializers(course)
    return Response(serializer_course.data)

  elif request.method == 'PUT':
    serializer_course = CourseSerializers(course,data = request.data)
    if serializer_course.is_valid:
      serializer_course.save()
      return Response(serializer_course.data)
    return Response(serializer_course.errors,status=status.HTTP_400_BAD_REQUEST)  
  
  elif request.method == 'DELETE':
    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


