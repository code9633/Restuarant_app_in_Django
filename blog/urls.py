from django.urls import path 
from . import views

# first step

urlpatterns = [
    path('', views.index, name='index'), # this path fucntion should include the the three paremeters
    # path('specific', views.specific, name= 'specific'),
    # path('article/<int:article_id>', views.article, name='article'),
    path('menu', views.menu, name='menu'),
    path('specials', views.specials, name='specials'),
    path('meals', views.meals, name='meals')
]
