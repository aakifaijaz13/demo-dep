"""CampusRecruiterManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from campusrecruiter.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings # new
from  django.conf.urls.static import static #new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('jobDetails/<int:pid>', jobDetails, name='jobDetails'),


    #===================== Candidate URL Here ======================

    path('candidate', candidate, name='candidate'),
    path('canDashboard', canDashboard, name='canDashboard'),
    path('studentProfile', studentProfile, name='studentProfile'),
    path('addFormDetail', addFormDetail, name='addFormDetail'),
    path('manageFormDetail', manageFormDetail, name='manageFormDetail'),
    path('viewVacancy', viewVacancy, name='viewVacancy'),
    path('viewVacancyDetails/<int:pid>', viewVacancyDetails, name='viewVacancyDetails'),
    path('historyofAppliedJob', historyofAppliedJob, name='historyofAppliedJob'),
    path('viewHistoryAppliedjob/<int:pid>', viewHistoryAppliedjob, name='viewHistoryAppliedjob'),
    path('candbetweenDateReport', candbetweenDateReport, name='candbetweenDateReport'),
    path('candidateSearchCategory', candidateSearchCategory, name='candidateSearchCategory'),
    path('viewAppliedApplication/<int:pid>', viewAppliedApplication, name='viewAppliedApplication'),
    path('viewstudentEduDtls/<int:pid>', viewstudentEduDtls, name='viewstudentEduDtls'),
    path('candidateChangePwd', candidateChangePwd, name='candidateChangePwd'),
    path('manageWorkDetails', manageWorkDetails, name="manageWorkDetails"),
    path('addWorkDetails/<int:student_id>', workDetails, name="addWorkDetails"),
    #=================== Employee URL Here ===============================

    path('employees', employees, name='employees'),
    path('empDashboard', empDashboard, name='empDashboard'),
    path('comProfile', comProfile, name='comProfile'),
    path('addVacancy', addVacancy, name='addVacancy'),
    path('manageVacancy', manageVacancy, name='manageVacancy'),
    path('editVacancy/<int:pid>', editVacancy, name='editVacancy'),
    path('newApplication', newApplication, name='newApplication'),
    path('sortListedApplication', sortListedApplication, name='sortListedApplication'),
    path('rejectApplication', rejectApplication, name='rejectApplication'),
    path('allApplication', allApplication, name='allApplication'),
    path('vacancyReport', vacancyReport, name='vacancyReport'),
    path('applicationCountReport', applicationCountReport, name='applicationCountReport'),
    path('employerChangePwd', employerChangePwd, name='employerChangePwd'),

    # ============================ Admin Here ====================================

    path('admin_login', admin_login, name='admin_login'),
    path('dashboard', dashboard, name='dashboard'),
    path('totalRegCompany', totalRegCompany, name='totalRegCompany'),
    path('viewCompanyDtls/<int:pid>', viewCompanyDtls, name='viewCompanyDtls'),
    path('totalRegStudent', totalRegStudent, name='totalRegStudent'),
    path('viewStudentDtls/<int:pid>', viewStudentDtls, name='viewStudentDtls'),
    path('totalVacancy', totalVacancy, name='totalVacancy'),
    path('viewVacancyDtls/<int:pid>', viewVacancyDtls, name='viewVacancyDtls'),
    path('bwdateComReg', bwdateComReg, name='bwdateComReg'),
    path('admvacancyReport', admvacancyReport, name='admvacancyReport'),
    path('adminChangePwd', adminChangePwd, name='adminChangePwd'),
    path('logout', Logout, name='logout'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)