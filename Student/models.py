from django.db import models

# Create your models here.


class Student(models.Model):

    BRANCH_CHOICES = (
        ('CSE', 'Computer Science Enginnering'),
        ('IT', 'Information Technology'),
        ('MAE', 'Mechanical and Automation Engineering'),
        ('EEE', 'Electronics and Electrical Engineering'),
        ('ECE', 'Electronics and Communication Engineering')
    )

    name = models.CharField(max_length=50)
    enr_no = models.CharField(max_length=12,
                    verbose_name="Enrollment number")
    enr_year = models.PositiveSmallIntegerField(default=2015,
                    verbose_name="Enrollment year")
    dob = models.DateField(verbose_name="Date of birth")
    degree = models.CharField(max_length=20, default="B.Tech", editable=False)
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES)
    email = models.EmailField()
    has_graduated = models.BooleanField(verbose_name="Has the student graduated?")
    gpa = models.FloatField(verbose_name="GPA")
    achievements = models.TextField(blank=True, null=True)
    skills = models.TextField(verbose_name="Technical skills", blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to="resume", blank=True, null=True)

    def __str__(self):
        return self.name
