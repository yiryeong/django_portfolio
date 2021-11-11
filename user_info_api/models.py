from django.db import models


class userInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    phoneNo = models.CharField(max_length=45)
    age = models.IntegerField()
    address = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'django_project'
