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
        return self.title

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

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains = search_term)
        return project



# class Meta:
#         ordering = ['-pub_date']
class Profile(models.Model):
    username = models.CharField(default='User',max_length=30)
    profile_picture = models.ImageField(upload_to = "profile/",null=True)
    bio = models.TextField(default='',blank = True)
    project = models.ForeignKey(Project,null=True)
    contact = models.TextField(default='',null = True)
        # project = models.IntegerField(default=0)

    def __str__(self):
            return self.username

    def delete_profile(self):
        self.delete()

    def save_profile(self):
        self.save()

	

    # class Meta:
    #     ordering = ['-pub_date']
		

class Rating(models.Model):
    user = models.ForeignKey(User, null= True)
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project, null= True,related_name='rating')
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    # project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.content


    def delete_content(self):
        self.delete()

    def save_content(self):
        self.save()

# class MoringaMerch(models.Model):
#     name = models.CharField(max_length=40)
#     description = models.TextField()
#     price = models.DecimalField(decimal_places=2, max_digits=20)
# # Create your models here.