from django.db import models

class Student(models.Model):
    EXAM_CHOICES = [
        ('10th', '10th'),
        ('12th', '12th'),
    ]
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    city = models.CharField(max_length=100)
    exam_type = models.CharField(max_length=4, choices=EXAM_CHOICES)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name
