from django.db import models

# Create your models here.
class PDFFILE(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to = "pdfs/")
    uploaded_at = models.DateTimeField(auto_now_add = True)