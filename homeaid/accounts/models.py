from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, unique=True)


    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar.png', upload_to='profile')
    cover = models.ImageField(default='cover.png', upload_to='cover')
    status = models.TextField(default='Enjoying Moments..')
    created = models.DateTimeField(auto_now_add=True)
    dob = models.CharField(max_length=12,default='DD-MM-YYYY')
    fname = models.CharField(max_length=12,default='First Name')
    lname = models.CharField(max_length=12,default='Last Name')
    gender = models.CharField(max_length=12,default='Gender')
    profile_status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username + " - " + self.created.strftime('%d-%m-%y')

def create_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=Users)