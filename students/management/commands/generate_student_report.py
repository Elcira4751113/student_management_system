from pathlib import Path

from django.core.management.base import BaseCommand
from students.models import Student


class Command(BaseCommand):
    help = "Generate a student report"

    def handle(self, *args, **options):
        students = Student.objects.all()

        report = []
        report.append("STUDENT REPORT")
        report.append("================")
        report.append(f"Total students: {students.count()}")
        report.append("")

        for student in students:
            report.append(
                f"Name: {student.name} | "
                f"Age: {student.age} | "
                f"Field: {student.field}"
            )

        report.append("")
        report.append("Report generated successfully.")

        report_path = Path("student_report.txt")
        report_path.write_text("\n".join(report))

        self.stdout.write(
            self.style.SUCCESS(
                f"Report created successfully: {report_path}"
            )
        )