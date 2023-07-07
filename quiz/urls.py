from django.urls import path
from quiz.views import (
    index_view,
    category_view,
    quiz_view,
)

urlpatterns = [
    path('', index_view, name='index'),
    path('<slug:category_slug>/', category_view, name='category'),
    path('<slug:category_slug>/<slug:quiz_slug>/', quiz_view, name='quiz'),
]