from django.db import models
from django.urls import reverse


# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    img=models.ImageField(upload_to='course',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='course'
        verbose_name_plural='course'
    def get_url(self):
        return reverse('store:department_by_course',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)
class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='department', blank=True)
    desc = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    fees = models.IntegerField()

    def get_url(self):
        return reverse('store:deptcourcedetail',args=[self.course.slug,self.slug])


    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def __str__(self):
        return '{}'.format(self.name)





