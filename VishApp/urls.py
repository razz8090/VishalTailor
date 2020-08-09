from django.conf.urls import include
from django.urls import path

from . import views


urlpatterns = [
    path('',views.homePage, name='homePage'),
    path('log_in_form/',views.lo_in_form, name='log_in_form'),
    path('admin_log_in/',views.validate_admin, name='admin_log_in'),
    path('cust_form/',views.cust_form, name='cust_form'),
    path('submit_detils/',views.submit_detils, name='submit_detils'),
    path('edit_info/',views.edit_info,name='edit_info'),
    path('cust_update/',views.cust_update, name='cust_update'),
    path('get_status/',views.get_status, name='get_status'),
    path('customer_list/',views.Customer_list, name='customer_list'),
    path('show_update_list/',views.show_update_list, name='show_update_list'),
    path('status_ready/', views.status_ready, name='status_ready'),
    path('emp_form/', views.emp_form, name='emp_form'),
    path('emp_acc/',views.emp_acc, name='emp_acc'),
    path('emp_record/', views.emp_record, name='emp_record'),
]
