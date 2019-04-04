from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import ProfileUploadForm,ProfileForm,ImageUploadForm,ImageForm
from django.http  import HttpResponse
from . models import Rating,Profile,Project
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializer import Project,Profile
# from .serializer import MerchSerializer

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
      title = 'Awards'
      image_posts = Project.objects.all()
      
      print(image_posts)
      return render(request, 'index.html', {"title":title,"image_posts":image_posts})


@login_required(login_url='/accounts/login/')
def rating(request,id):
	
	post = get_object_or_404(Image,id=id)	
	current_user = request.user
	print(post)

	if request.method == 'POST':
		form = RatingForm(request.POST)

		if form.is_valid():
			rating = form.save(commit=False)
			rating.user = current_user
			rating.image = post
			rating.save()
			return redirect('index')
	else:
		form = RatingForm()

	return render(request,'rating.html',{"form":form})  


@login_required(login_url='/accounts/login/')
def profile(request):
	 current_user = request.user
	 profile = Profile.objects.all()
	

	 return render(request, 'profile.html',{"current_user":current_user,"profile":profile})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_images = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                
                requested_profile.profile_pic = form.cleaned_data['profile_picture']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_picture = form.cleaned_data['profile_picture'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()


    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})

@login_required(login_url='/accounts/login/')
def upload_images(request):
    '''
    View function that displays a forms that allows users to upload images
    '''
    current_user = request.user

    if request.method == 'POST':

        form = ImageForm(request.POST ,request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.user_key = current_user
           
            image.save() 

           
    else:
        form = ImageForm() 
    return render(request, 'upload_images.html',{"form" : form}) 


# Create your views here.
