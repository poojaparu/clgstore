
from django.urls import path

from . import views
app_name='store'

urlpatterns = [

    path('',views.department,name='department'),
    path('<slug:c_slug>', views.department, name='department_by_course'),
    path('<slug:c_slug>/<slug:dept_slug>/', views.deptdetail, name='deptcourcedetail')

]
