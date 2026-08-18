
from django.urls import path
from . import views

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
]