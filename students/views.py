
from django.core.mail import send_mail
from .models import Student
from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm
from django.db.models import Q
from students.tasks import generate_student_report_task
from pathlib import Path
from django.http import FileResponse, Http404


def student_list(request):
    query = request.GET.get("q")

    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) |
            Q(field__icontains=query)
        )
    else:
        students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    return render(
        request,
        "students/student_detail.html",
        {"student": student}
    )

def add_student(request):
    if request.method == "POST":
        print(request.POST)

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(
        request,
        "students/add_student.html",
        {"form": form}
    )

def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("student_detail", student_id=student.id)

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/update_student.html",
        {"form": form, "student": student}
    )

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(
        request,
        "students/delete_student.html",
        {"student": student}
    )

def test_email(request):
    send_mail(
        subject="Student Management System",
        message="This is a test email from my Django application.",
        from_email="admin@studentmanagement.com",
        recipient_list=["student@example.com"],
    )
    return render(request, "students/email_test.html")

def generate_report(request):
    task = generate_student_report_task.delay()

    return render(
        request,
        "students/report_started.html",
        {"task_id": task.id},
    )

def view_report(request):
    report_path = Path("student_report.txt")

    if not report_path.exists():
        raise Http404("Report has not been generated yet.")

    report_content = report_path.read_text(encoding="utf-8")

    return render(
        request,
        "students/view_report.html",
        {"report_content": report_content},
    )


def download_report(request):
    report_path = Path("student_report.txt")

    if not report_path.exists():
        raise Http404("Report has not been generated yet.")

    return FileResponse(
        open(report_path, "rb"),
        as_attachment=True,
        filename="student_report.txt",
    )