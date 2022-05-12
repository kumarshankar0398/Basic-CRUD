from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('AddRec', views.AddRec),
    path('AddRec1', views.AddRec1),
    path('ShowRec', views.ShowRec),
    path('EditRec/<int:id>', views.EditRec),
    path('UpdateRec/<int:id>', views.UpdateRec),
    path('DeleteRec/<int:pk>/', views.DeleteRec),
    path('ShowRec1', views.ShowRec1),
    path('SearchRec/', views.SearchRec, name='SearchRec'),
    path('SortRecByEmpName/', views.SortRecByEmpName),
    path('SortRecByEmpId/', views.SortRecByEmpId),
    path('SortRecByEmpContact', views.SortRecByEmpContact),
    path('SortRecByEmpSal', views.SortRecByEmpSal),
    path('SortRecByEmpEmail', views.SortRecByEmpEmail),
    path('SortRecByEmpAddress', views.SortRecByEmpAddress),
    path('signup/', views.signup),
    path('', views.login_user),
    path('logout/', views.logout_user, name='logout'),
]
