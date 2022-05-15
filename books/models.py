from django.db import models


class Class(models.Model):
    CLASS_CHOICES = (
        ('6ᵗʰ', '6ᵗʰ'),
        ('7ᵗʰ', '7ᵗʰ'),
        ('8ᵗʰ', '8ᵗʰ'),
        ('9ᵗʰ', '9ᵗʰ'),
        ('10ᵗʰ', '10ᵗʰ'),

    )

    name = models.CharField(max_length=50, choices=CLASS_CHOICES)

    def __str__(self):
        return self.name


class Student(models.Model):
    author = models.ForeignKey(Class, on_delete=models.CASCADE)
    stu_name = models.CharField(max_length=100)
    stu_age = models.PositiveIntegerField()
    stu_fathername = models.CharField(max_length=50)
    stu_address = models.CharField(max_length=150)

    def __str__(self):
        return self.stu_name
