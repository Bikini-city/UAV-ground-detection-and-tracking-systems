import time
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

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'uploads/{0}/{1}'.format(instance.id, filename)
class Detections(models.Model):

    # User inputs
    image_to_detect = models.ImageField(upload_to=f'uploads/{time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())}/',
                                        default='')
    confidence = models.FloatField(default=0.25)

    # Control field
    processed = models.BooleanField(default=False)

    # Expected results: TODO
    # code_generated = models.FileField(upload_to='codes/', null=True)
    # json_file = models.FileField(upload_to='jsonfile/', null=True)
    # detected_image_path = models.ImageField(upload_to='detectedimage/', null=True)


    def __str__(self):
        return f'{self.processed}'