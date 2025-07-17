# dashboard/urls.py
from django.urls import path
from .views import (home,logout, calendar_view,get_planning_events,save_planning, delete_planning,export_planning_excel,
                    export_planning_pdf, get_planning_summary, quarter_view,get_planning_data,quarterview_excel, quarterview_pdf,
                    data_view)

from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', logout, name='logout'),
    path('calendar/', calendar_view, name='calendar'),
    path('api/get-events/', get_planning_events, name='get_planning_events'),
    path('api/get-planning-summary/', get_planning_summary, name='get_planning_summary'),
    path('save-planning/', save_planning, name='save_planning'),
    path('delete-planning/', delete_planning, name='delete_planning'),
    path('export-planning-excel/', export_planning_excel, name='export_planning_excel'),
    path("export-planning-pdf/", export_planning_pdf, name="export_planning_pdf"),

    path('quarterview/', quarter_view, name='quarterview'),
    path('api/get_planning_data/', get_planning_data, name='get_planning_data'),
    path('quarterview_excel/', quarterview_excel, name='quarterview_excel'),
    path('quarterview_pdf/', quarterview_pdf, name='quarterview_pdf'),

    # path('add_user/', add_user, name='add_user'),
    # path('add-employee/', add_employee, name='add_employee'),
    # path('get-employee-details/', get_employee_details, name='get_employee_details'),
    # path('employee-name-autocomplete/', employee_name_autocomplete, name='employee_name_autocomplete'),
    # path('delete-employee/', delete_employee, name='delete_employee'),

    path('data_view/', data_view, name='data_view'),

    path("save-employee/", views.save_employee, name="save_employee"),
    path("update-employee/", views.update_employee, name="update_employee"),
    path("delete-employee/", views.delete_employee, name="delete_employee"),

    path("save-client/", views.save_client, name="save_client"),
    path("update-client/", views.update_client, name="update_client"),
    path("delete-client/", views.delete_client, name="delete_client"),

    path("save-user/", views.save_user, name="save_user"),
    path("update-user/", views.update_user, name="update_user"),
    path("delete-user/", views.delete_user, name="delete_user"),

    path('change-password/', views.change_password, name='change_password'),
    path('holiday/', views.add_holiday, name='add_holiday'),

    path('allocated-resources/', views.allocated_resources_view, name='allocated_resources_view'),
    path('allocated_data/', views.allocated_data, name='allocated_data'),
    path('export-allocated-data/', views.export_allocated_data_excel, name='export_allocated_data_excel'),


    path('unallocated-resources/', views.unallocated_resources_view, name='unallocated_resources_view'),
    path('unallocated_data/', views.unallocated_data, name='unallocated_data'),
    path('export-unallocated-data/', views.export_unallocated_data_excel, name='export_unallocated_data_excel'),
    



]
