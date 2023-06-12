from django.db import models

# Create your models here.
class Actions(models.Model):
    action_order = models.IntegerField(default=1, unique=True)
    action = models.CharField(max_length=100)
    description = models.TextField(default='No description provided yet!')
    times_performed = models.IntegerField(default=0)
    cover_image = models.FileField(upload_to='media/action_cover_images/', blank=True, null=True)
    cover_image_url = models.CharField(max_length=100, blank=True, null=True)
    video = models.FileField(upload_to='media/action_video/', blank=True, null=True)
    video_url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Action'
        verbose_name_plural = 'Actions'
    
    def __str__(self):
        return self.action
    
class ActionSteps(models.Model):
    action = models.ForeignKey(Actions, on_delete=models.CASCADE)
    step1 = models.TextField(default="Step 1")
    step2 = models.TextField(default="Step 2")
    step3 = models.TextField(default="Step 3")
    step4 = models.TextField(default="Step 4")
    step5 = models.TextField(default="Step 5")

    class Meta:
        verbose_name = 'Action Step'
        verbose_name_plural = 'Action Steps'

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return str(self.name) + ' ' + str(self.email)