from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Project(models.Model):
    title = models.CharField(max_length = 60,null = True)
    image = models.ImageField(upload_to = "images/",null = True)
    user = models.ForeignKey(User,null=True)
    link = models.CharField(max_length = 70,null = True)
    description = models.TextField(null = True)
    


    def __str__(self):
        return self.image

    def delete_image(self):
        self.delete()

    def save_image(self):
        self.save()

    def update_description(self,new_description):
        self.image_description = new_description
        self.save()


    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image



 class Meta:
        ordering = ['-pub_date']
class Profile(models.Model):
	username = models.CharField(default='User',max_length=30)
	profile_picture = models.ImageField(upload_to = "profile/",null=True)
	bio = models.TextField(default='',blank = True)
	project = models.ForeignKey(Project,null=True)
    contact = models.TextField(null = True)
    project = models.IntegerField(default=0)

	def __str__(self):
		return self.username

	def delete_profile(self):
		self.delete()

	def save_profile(self):
		self.save()

	# @classmethod
	# def search_profile(cls,search_term):
	# 	got_profiles = cls.objects.filter(first_name__icontains = search_term)
	# 	return got_profiles

     class Meta:
        ordering = ['-pub_date']
		
class Image(models.Model):
    image = models.ImageField(upload_to = "images/",null = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)
    image_name = models.CharField(max_length = 40,null = True)
    likes = models.IntegerField(default=0)
    image_caption = models.TextField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    comments = models.CharField(max_length = 40,null = True)

    def __str__(self):
    	return self.image_name

    def delete_image(self):
    	self.delete()

    def save_image(self):
    	self.save()

    def update_caption(self,new_caption):
    	self.image_caption = new_caption
    	self.save()


class Rating(models.Model):
    user = models.ForeignKey(User, null= True)
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project, null= True,related_name='rating')
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

def __str__(self):
        return self.content


    def delete_content(self):
        self.delete()

    def save_content(self):
        self.save()
# Create your models here.