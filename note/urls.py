from django.urls import path
from .views import *

urlpatterns = [
    path('' , review_entry , name='review_entry'),
]