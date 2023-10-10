from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    
    path('usignup/',views.usignup, name='usignup'),
    path('udata/',views.udata, name='udata'),
    path('udatabase/',views.udatabase, name='udatabase'),
    
    path('asignup/',views.asignup, name='asignup'),
    path('adata/',views.adata, name='adata'),
    path('adatabase/',views.adatabase, name='adatabase'),
        
    path('ulogin/',views.ulogin, name='ulogin'),
    path('alogin/',views.alogin, name='alogin'),
    
    path('enquiry/',views.enquiryView,name='enquiry'),
    path('enquiryinsert/',views.insertEnquiryDataBase,name='enquiryinsert'),
    #========================================================================
    path('showpage/',views.showPage,name='showpage'),
    path('editpage/<int:pk>/',views.EditPage,name='editpage'),
    path('update/<int:pk>/',views.UpdateData,name='update'),
    path('delete/<int:pk>/',views.DeleteData,name='delete'),
      
]