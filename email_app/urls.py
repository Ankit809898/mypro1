from django.urls import path
from . import views

urlpatterns = [
    path('email/', views.EmailAttachmentView.as_view(), name='email_url'),
]