from django.db import models
from gst_field.modelfields import GSTField, PANField
LEAD_SOURCE =(
    ("1", "Team Referal"),
    ("2", "tele"),
    ("3", "Inbound call"),
    ("4", "Mailchimp"),
    ("5", "Inbound Email"),
    ("6", "Outbound call"),
    ("7", "Website"),
    ("8", "IndiaMart")
)
city = (
    ("1","delhi"),
    ("2","Patna"),
    ("3","pune")
)
owner = (
    ("1","Ajit"),
    ("2","pratik"),
    ("3","abhishek")
    )

class company(models.Model):
    Company_Name  = models.CharField(max_length=100)
    Company_Email = models.EmailField(max_length=100)
    Alternative_Email = models.EmailField(max_length=200)
    Mobile_no = models.CharField(max_length=100)
    Alternative_Mobile_no = models.CharField(max_length=100)
    GSTN = GSTField()
    PAN_No = PANField()
    Lead_source = models.CharField(
        max_length = 20,
        choices =LEAD_SOURCE,
        default = '1')
    Adress = models.CharField(max_length=200)
    Area = models.CharField(max_length=100)
    City = models.CharField(
        max_length=50,
        choices = city,default='1')
    PINCODE =models.CharField(max_length=100)
    WEBSITE = models.URLField(max_length=500)
    OWNER = models.CharField(max_length=50,choices = owner,default='1')

    def __str__(self):
        return self.Company_Name
class contact(models.Model):
    First_Name  = models.CharField(max_length=100)
    Last_Name  = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Alternative_Email = models.EmailField(max_length=200)
    Mobile_no = models.CharField(max_length=100)
    Alternative_Mobile_no = models.CharField(max_length=100)

    def __str__(self):
        return self.First_Name
