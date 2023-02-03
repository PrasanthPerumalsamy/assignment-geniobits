from django.db import models

# Create your models here.

class CsvFile(models.Model):
    # upload to MEDIA_ROOT/temp
    file = models.FileField(upload_to="csv", blank=False, null=False)

    def __str__(self):
        return self.file.name