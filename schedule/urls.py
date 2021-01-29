from django.urls import path
from .views import create, update, manage, delete

app_name = "schedule"

urlpatterns = [
    path('<int:id_reg_tour>/', manage, name='manage'),
    path('create/<int:id_reg_tour>/', create, name='create'),
    path('update/<int:id_reg_tour>/<int:id_schedule>/', update, name='update'),
    path('delete/<int:id_reg_tour>/<int:id_schedule>/', delete, name='delete')
]
