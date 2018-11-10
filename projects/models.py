from django.db import models

# Create your models here.


class Projects(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    title = models.CharField(max_length=100, default='')
    githubLink = models.CharField(max_length=200, default=' ')
    myLink = "https://github.com/adar2378/"

    def getLink(self):
        return self.myLink+self.githubLink

    def __str__(self):
        return self.title
