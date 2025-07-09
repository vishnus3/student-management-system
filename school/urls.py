from django.contrib import admin
from django.urls import path, include
from .views import index, admin_dashboard, student_dashboard, teacher_dashboard, holiday_page, mark_notification_as_read, clear_all_notification, AccountsView, fees , \
DepartmentView, events, library, exam_list
from rest_framework.routers import DefaultRouter





urlpatterns = [

   path('',index, name="index"),
   path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
   path('student_dashboard/', student_dashboard, name='student_dashboard'),
   path('teacher_dashboard/', teacher_dashboard, name='teacher_dashboard'),
   path('holiday/', holiday_page, name='holiday'), 
   path('notification/mark-as-read/', mark_notification_as_read, name='mark_notification_as_read' ),
   path('notification/clear-all', clear_all_notification, name= "clear_all_notification"),
   path('accounts/fees-collections/', AccountsView().fee_collection, name='accounts-fees-collections'),
   path('accounts/expenses/', AccountsView().expenses, name='accounts-expenses'),
   path('accounts/salary/', AccountsView().salary, name='accounts-salary'),
   path('accounts/add-fees/', AccountsView().add_fees, name='accounts-add-fees'),
   path('accounts/add-expenses/', AccountsView().add_expenses, name='accounts-add-expenses'),
   path('accounts/add-salary/', AccountsView().add_salary, name='accounts-add-salary'),
   path('accounts/view-fees/', fees, name='view-fees'),
   path('departments/', DepartmentView.dep_view, name='departments-list'),
   path('departments/add/', DepartmentView.dep_add, name='departments-add'),
   path('departments/edit/<int:id>/', DepartmentView.dep_edit, name='departments-edit'),
   path('events/', events, name='events'),
   path('exam/', exam_list, name='exam-list'),
   path('library/', library, name='library'),

]


