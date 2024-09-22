from django.db import models

# Create your models here.
class Stream(models.Model):
  stream_name = models.CharField(max_length=100)

  def __str__(self):
    return self.stream_name

class Course(models.Model):
  course_name = models.CharField(max_length=200)
  course_duration = models.CharField(max_length=100)
  course_type = models.CharField(max_length=100)
  stream = models.ForeignKey(Stream,on_delete=models.CASCADE)

  def __str__(self):
    return self.course_name