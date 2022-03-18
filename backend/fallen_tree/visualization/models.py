from django.db import models
from datetime import date
from django.core.validators import FileExtensionValidator

#For Test
class FileUpload(models.Model):
    title = models.TextField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class DataSet(models.Model):
    id = models.AutoField(help_text="primary key", primary_key=True, null=False)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lng = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    src = models.FileField(null=True, upload_to="", blank=True,validators=[FileExtensionValidator(allowed_extensions=['mp4','jpeg','jpg','png'])])
    date = models.DateField(("Date"), default=date.today)

    class Meta:
        db_table = "dataset"

class Result(models.Model):
    id = models.AutoField(help_text="primary key", primary_key=True, null=False)
    dataSet_id = models.ForeignKey("DataSet", related_name="dataset", on_delete=models.CASCADE, db_column="dataset_id")
    broken = models.IntegerField()
    down = models.IntegerField()

    class Meta:
        db_table = "result"