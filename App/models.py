from django.db import models

# Create your models here.
class Actions(models.Model):
    action = models.CharField(max_length=100)
    action_order = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    performed = models.IntegerField(default=0)
    cover_image = models.FileField(upload_to='action_cover_images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Action'
        verbose_name_plural = 'Actions'
    
    def __str__(self):
        return self.action 
    
class ActionMedia(models.Model):
    action = models.ForeignKey(Actions, on_delete=models.CASCADE)
    media = models.FileField(upload_to='action_media/', blank=True, null=True)

    def __str__(self):
        return str(self.action)
    
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return str(self.name) + str(self.email)
    
class PerformLogs(models.Model):
    action = models.ForeignKey(Actions, on_delete=models.CASCADE)
    input_file = models.FileField(upload_to='action_input_file/', blank=True, null=True)
    output_file = models.FileField(upload_to='action_output_file/', blank=True, null=True)

    class Meta:
        verbose_name = "Perform Logs"
        verbose_name_plural = "Perform Logs"

    def __str__(self):
        return str(self.action)