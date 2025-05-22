from django.contrib import admin
from django.urls import path
from job import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Choose Page
    path('', views.start , name='index'),
    
    # Login Page
    path('EmpLogin', views.EmpLogin , name='EmpLogin '),
    path('ComLogin', views.ComLogin, name='ComLogin'),
    
    # Account Create
    path('EmpAccount', views.EmpAccount, name='EmpAccount'),
    path('ComAccount', views.ComAccount, name='ComAccount'),

    # Epm Home
    path('EmpHome', views.EmpHome, name='EmpHome'),
    path('SearchJob', views.SearchJob, name='SearchJob'),
    path('ApplicationStatus', views.ApplicationStatus, name='ApplicationStatus'),
   
    # Com Home
    path('ComHome', views.ComHome, name='ComHome'),
    path('CreateJobPost', views.CreateJobPost, name='CreateJobPost'),
    path('Emphiring', views.Emphiring, name='Emphiring'),
    path('EmpSelect/<int:id>', views.EmpSelect, name='EmpSelect'),

    # DataBase
    path('deletepost/<int:id>',views.deletepost, name='deletepost'),
    path('EmpApplyJob/<int:id>',views.EmpApplyJob, name='EmpApplyJob'),
    path('EmpReject/<int:id>', views.EmpReject, name='EmpReject'),
    path('EmpHire/<int:id>', views.EmpHire, name='EmpHire')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


