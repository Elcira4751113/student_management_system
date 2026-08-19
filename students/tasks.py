from pathlib import Path
from datetime import datetime

from celery import shared_task
from django.db.models import Avg, Count

from students.models import Student


@shared_task
def generate_student_report_task():

    students = Student.objects.all()

    total_students = students.count()

    average_age = students.aggregate(
        average=Avg("age")
    )["average"]

    students_by_field = students.values("field").annotate(
        total=Count("id")
    )

    report = []

    report.append("STUDENT MANAGEMENT REPORT")
    report.append("=========================")
    report.append("")

    report.append(
        f"Report generated: {datetime.now().strftime('%d %B %Y, %H:%M')}"
    )
    report.append("")

    report.append("SUMMARY")
    report.append("-------")
    report.append(f"Total students: {total_students}")

    if average_age is not None:
        report.append(f"Average age: {average_age:.1f}")
    else:
        report.append("Average age: No data")

    report.append("")

    report.append("STUDENTS BY FIELD")
    report.append("------------------")

    for item in students_by_field:
        report.append(
            f"{item['field']}: {item['total']}"
        )

    report.append("")

    report.append("STUDENT DETAILS")
    report.append("----------------")

    for student in students:
        report.append(
            f"Name: {student.name} | "
            f"Age: {student.age} | "
            f"Field: {student.field} | "
            f"Gender: {student.gender} | "
            f"Email: {student.email}"
        )

    report.append("")
    report.append("Report generated successfully.")

    report_path = Path("student_report.txt")

    report_path.write_text(
        "\n".join(report),
        encoding="utf-8"
    )

    return f"Report created successfully: {report_path}"