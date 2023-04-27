from django.urls import path

from . import views

app_name='accounts'

urlpatterns = [
    path("SignUp/",views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit',views.profile_edit,name='profile_edit'),
    path('candidates/',views.candidates,name='candidates'),
    path('candidates/<int:id>',views.candidate,name='candidate'),
    path('companies/',views.companies,name='companies'),
    path('companies/create/<int:profile_id>',views.create_company,name='create_company'),
    path('companies/<int:id>',views.company,name='company')
]
