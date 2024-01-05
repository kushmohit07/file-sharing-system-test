from pyexpat import model
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_file_extension(value):
    allowed_extensions = ['pptx', 'docx', 'xlsx']
    file_extension = str(value.name).lower().split('.')[-1]
    print(file_extension)
    if file_extension not in allowed_extensions:
        raise ValidationError('Invalid file type. Please upload only pptx, docx, or xlsx files.')


class Upload_File(models.Model):
    upload=models.FileField(upload_to='file',validators=[validate_file_extension])
    def __str__(self):
        return self.upload.name

class Registation_details(models.Model):
    Name=models.CharField(max_length=20)
    email=models.EmailField(max_length=254,unique=True)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.Name