
from django.urls import path
from . import views
from .views import generate_report
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api-students-v2", views.StudentViewSet)

urlpatterns = [
   
    path("", views.student_list, name="student_list"),

    path(
        "<int:student_id>/",
        views.student_detail,
        name="student_detail",
    ),

    path(
        "add/",
        views.add_student,
        name="add_student",
    ),

    path(
        "<int:student_id>/update/",
        views.update_student,
        name="update_student",
    ),

    path(
    "<int:student_id>/delete/",
    views.delete_student,
    name="delete_student",
    ),

    path("test-email/", 
         views.test_email, 
         name="test_email"
    ),

    path(
        "generate-report/",
        views.generate_report,
        name="generate_report",
    ),

    path(
        "report/",
        views.view_report,
        name="view_report",
    ),

    path(
        "report/download/",
        views.download_report,
        name="download_report",
    ),


    path("api-students/", 
         views.api_students, 
         name="api_students"
    ),
]

urlpatterns += router.urls
