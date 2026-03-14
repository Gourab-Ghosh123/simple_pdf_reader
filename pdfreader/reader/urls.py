from django.urls import path
from . import views

urlpatterns = [
    path("/" , views.upload_pdf , name = "upload_pdf"),
    path("read/<int : pdf_id>/<int : page_number>/" , views.read_pdf , name = "read_pdf"),
]