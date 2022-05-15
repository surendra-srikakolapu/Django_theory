from django.db import models

# Create your models here.


class Upload_download_file(models.Model):

    file_name = models.CharField(max_length=50)
    file_upload = models.FileField(upload_to='upload_download_files')

    def __str__(self):
        return self.file_name
