from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification
from rest_framework import viewsets
from rest_framework.decorators import action



# Create your views here.

def index(request):
    return render(request, "authentication/login.html")

def admin_dashboard(request):
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()
    return render(request, "home/index.html")

def student_dashboard(request):
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()

    context = {
        "unread_notifications": unread_notification,
        "unread_count": unread_notification_count,
    }
    return render(request, "students/student-dashboard.html", context)

def teacher_dashboard(request):
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()
    return render(request, "students/teacher-dashboard.html")

def create_notification(user, message):
    Notification.objects.create(user=user, message=message)

def mark_notification_as_read(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

def clear_all_notification(request):
    if request.method == "POST":
        notification = Notification.objects.filter(user=request.user)
        notification.delete()
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden


def holiday_page(request):
    return render(request, 'html-template/holiday.html')

class AccountsView:
    @staticmethod
    def fee_collection(request):
        return render(request, 'html-template/fees-collections.html')

    @staticmethod
    def expenses(request):
        return render(request, 'html-template/expenses.html')

    @staticmethod
    def salary(request):
        return render(request, 'html-template/salary.html')

    @staticmethod
    def add_fees(request):
        return render(request, 'add-fees.html')

    @staticmethod
    def add_expenses(request):
        return render(request, 'add-expenses.html')

    @staticmethod
    def add_salary(request):
        return render(request, 'add-salary.html')

def fees(request):
    return render(request, 'fees.html')

class DepartmentView:
    def dep_add(request):
        if request.method == 'POST':
            # Logic to add department
            pass
        return render(request, 'add-department.html')

    def dep_view(request):
        # Logic to view departments
        return render(request, 'department.html')
    
    def dep_edit(request, id):
        if request.method == 'POST':
            # Logic to edit department
            pass
        return render(request, 'edit-department.html')
    
def events(request):
    # Logic to handle events
    return render(request, 'event.html')

def exam_list(request):
    # Logic to handle exam list
    return render(request, 'exam.html')

def library(request):
    # Logic to handle library
    return render(request, 'library.html')