from .views import book_list_view, book_detail_view
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

urlpatterns = [
    path('', book_list_view, name='book_list'),
    path('<int:pk>', book_detail_view, name='book_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
