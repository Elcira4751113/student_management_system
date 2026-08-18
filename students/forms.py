from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ["name", "age", "field", "gender", "email"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Enter student's name",
                }
            ),

            "age": forms.NumberInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Enter student's age",
                }
            ),

            "field": forms.TextInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Enter student's field",
                }
            ),

            "gender": forms.Select(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Enter student's email",
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]

        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError(
                "Name should contain only letters and spaces."
            )

        return name

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 1:
            raise forms.ValidationError(
                "Age must be greater than 0."
            )

        if age > 120:
            raise forms.ValidationError(
                "Please enter a valid age."
            )

        return age