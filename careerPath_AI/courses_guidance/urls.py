from django.urls import include,path
from rest_framework.routers import DefaultRouter

from courses_guidance.views import course_deatil, create_course, create_stream, get_course, get_stream, stream_detail

#from .views import CourseViewSet, StreamViewSet

# Create a router and register our viewsets with it.
#router = DefaultRouter()
# router.register(r'streams', StreamViewSet)
# router.register(r'courses', CourseViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('stream/',get_stream, name='get_stream'),
    path('stream/create/',create_stream, name='create_stream'),
    path('stream/<int:pk>/',stream_detail, name='stream_detail'),

    path('course/',get_course,name='get_course'),
    path('course/create/',create_course,name='create_course'),
    path('course/<int:pk>/',course_deatil,name='course_deatil'),


]
