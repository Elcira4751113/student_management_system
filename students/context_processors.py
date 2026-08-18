from .models import Student


def student_count(request):
    count = Student.objects.count()

    return {
        "student_count": count
    }