from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    ROLE_CHOICES = [
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='job_seeker')

    def __str__(self):
        return f"{self.user.username} ({self.role})"


class JobPosting(models.Model):
    EMPLOYMENT_TYPES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]

    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    employment_type = models.CharField(max_length=32, choices=EMPLOYMENT_TYPES, default='full_time')
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_postings')

    def __str__(self):
        return f"{self.title} @ {self.company_name}"


class Resume(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume {self.id} ({self.owner.username})"


class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('reviewing', 'Reviewing'),
        ('interview', 'Interview'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    ]

    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='applied')
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'candidate')

    def __str__(self):
        return f"{self.candidate.username} -> {self.job.title} ({self.status})"
