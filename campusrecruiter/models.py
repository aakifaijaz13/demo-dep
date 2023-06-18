from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ContactPerson = models.CharField(max_length=255, null=True)
    CompanyUrl = models.CharField(max_length=255, null=True)
    CompanyAddress = models.CharField(max_length=255, null=True)
    MobileNumber = models.CharField(max_length=15, null=True)
    CompanyLogo = models.FileField(max_length=200, null=True, blank=True)
    CompanyRegdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SecondaryBoard = models.CharField(max_length=255, null=True)
    SecondaryBoardyop = models.CharField(max_length=100, null=True)
    SecondaryBoardper = models.CharField(max_length=255, null=True)
    SecondaryBoardcgpa = models.CharField(max_length=255, null=True)
    SSecondaryBoard = models.CharField(max_length=255, null=True)
    SSecondaryBoardyop = models.CharField(max_length=255, null=True)
    SSecondaryBoardper = models.CharField(max_length=255, null=True)
    SSecondaryBoardcgpa = models.CharField(max_length=255, null=True)
    GraUni = models.CharField(max_length=255, null=True)
    GraUniyop = models.CharField(max_length=255, null=True)
    GraUnidper = models.CharField(max_length=255, null=True)
    GraUnicgpa = models.CharField(max_length=255, null=True)
    PGUni = models.CharField(max_length=255, null=True)
    PGUniyop = models.CharField(max_length=255, null=True)
    PGUniper = models.CharField(max_length=255, null=True)
    PGUnicgpa = models.CharField(max_length=255, null=True)
    ExtraCurriculars = models.CharField(max_length=255, null=True)
    OtherAchivement = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.first_name


class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    MobileNumber = models.CharField(max_length=15, null=True)
    StudentID = models.IntegerField(null=True)
    Gender = models.CharField(max_length=15, null=True)
    Address = models.CharField(max_length=300, null=True)
    Age = models.CharField(max_length=15, null=True)
    DOB = models.DateField(null=True)
    Image = models.FileField(max_length=200, null=True, blank=True)
    ResponseDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name


class WorkExperience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    experience = models.CharField(max_length=100, null=True)
    skills = models.CharField(max_length=100, null=True)
    preferences = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.candidate.user.first_name


class Vacancy(models.Model):
    companies = models.ForeignKey(Company, on_delete=models.CASCADE)
    JobTitle = models.CharField(max_length=250, null=True)
    MonthlySalary = models.CharField(max_length=250, null=True)
    JobDescriptions = models.CharField(max_length=250, null=True)
    Category = models.CharField(max_length=100, null=True, default="Entry Level")
    NoofOpenings = models.CharField(max_length=150, null=True)
    JobLocation = models.CharField(max_length=250, null=True)
    ApplyDate = models.DateField(null=True)
    LastDate = models.DateField(null=True)
    JobpostingDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.JobTitle


class Applyjob(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    Resume = models.FileField(max_length=200, null=True)
    ApplyDate = models.DateField(null=True)
    Message = models.CharField(max_length=255, null=True)
    Remark = models.CharField(max_length=255, null=True)
    Status = models.CharField(max_length=255, null=True)
    ResponseDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.candidate.user.first_name


class Message(models.Model):
    appjob = models.ForeignKey(Applyjob, on_delete=models.CASCADE)
    Messages = models.CharField(max_length=100, null=True)
    Status = models.CharField(max_length=255, null=True)
    ResponseDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Status


