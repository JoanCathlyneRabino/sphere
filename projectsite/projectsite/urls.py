"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from studentorg.views import (
    HomePageView, 
    OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    OrgMemberList, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView,
    ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView,
    CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
    StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView
)
from fire.views import HomePageView, ChartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart',)
    
    # Organization URLs
    path('organization/', OrganizationList.as_view(), name='organization-list'),
    path('organization/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization/<pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization/<pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),

    # Organization Members URLs
    path('orgmember/', OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmember/add/', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember/<pk>/', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmember/<pk>/delete/', OrgMemberDeleteView.as_view(), name='orgmember-delete'),

    # Program URLs
    path('program/', ProgramList.as_view(), name='program-list'),
    path('program/add/', ProgramCreateView.as_view(), name='program-add'),
    path('program/<pk>/', ProgramUpdateView.as_view(), name='program-update'),
    path('program/<pk>/delete/', ProgramDeleteView.as_view(), name='program-delete'),

    # College URLs
    path('college/', CollegeList.as_view(), name='college-list'),
    path('college/add/', CollegeCreateView.as_view(), name='college-add'),
    path('college/<pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('college/<pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),

    # Student URLs
    path('student/', StudentList.as_view(), name='student-list'),
    path('student/add/', StudentCreateView.as_view(), name='student-add'),
    path('student/<pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

]