from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from hood.forms import SignupForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('home')

    else:
        form = SignupForm()

    context = {
        'form':form,
    }

    return render(request, 'auth/signup.html', context)

@login_required
def home(request):
    '''
    renders our homepage
    '''
    current_user = get_object_or_404(Profile,user = request.user)
    current_user = Profile.objects.get(user=request.user)
    business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
    police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
    hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
    user = request.user
    business = Business.objects.filter(neighbourhood=current_user.neighbourhood)
    locations = Neighbourhood.objects.all()
    posts = Post.objects.filter(neighbourhood = current_user.neighbourhood)
    context = {
        'business':business,
        'police':police,
        'hospitals':hospitals,
        'user':user,
        'current_user':current_user,
        'locations':locations,
        'posts':posts,
        
    }
    return render(request,'all/home.html',context)
        
@login_required
def add_bussiness(request):
    '''
    this view function either renders our add bussiness form our saves a new bussiness
    '''
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        hood = request.POST.get('Location')
        if form.is_valid():
            bussiness = form.save(commit=False)
            bussiness.neighbourhood = hood
            bussiness.posted_by = request.user
            bussiness.save()
            return redirect('home')
        else:
            messages.info(request,"all fields are required")
            return redirect('add-bussiness')
    else:
        current_user = get_object_or_404(Profile,user = request.user)
        current_user = Profile.objects.get(user=request.user)
        business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
        police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
        hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
        user = request.user
        business = Business.objects.filter(neighbourhood=current_user.neighbourhood)
        locations = Neighbourhood.objects.all()
        form = BusinessForm()
        context = {
            'business':business,
            'police':police,
            'hospitals':hospitals,
            'user':user,
            'current_user':current_user,
            'locations':locations,
            'form':form,
            
        }
        return render(request,'all/add_bs.html',context)

@login_required
def new_post(request):
    '''
    this is a view function that renders our new post form aswell as save our new post in the db
    '''
    profile = Profile.objects.get(user = request.user)
    hoods = ['Nairobi','Ngong','Ruiru'
             ,'Thika','Rwaka','Juja','Kenol','Westlands']
    if profile.neighbourhood not in hoods:
        messages.info(request,'Provide your neighbourhood information first before adding a post!')
        return redirect('update-profile')
    else:
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit = False)
                post.posted_by = request.user
                post.neighbourhood = profile.neighbourhood
                post.save()
                return redirect('home')
            else:
                messages.info(request,'All fields are required')
                return redirect('new-post')
        else:
            
            form = PostForm()
            current_user = get_object_or_404(Profile,user = request.user)
            current_user = Profile.objects.get(user=request.user)
            business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
            police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
            hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
            user = request.user
            business = Business.objects.filter(neighbourhood=current_user.neighbourhood)
            locations = Neighbourhood.objects.all()
            context = {
                'business':business,
                'police':police,
                'hospitals':hospitals,
                'user':user,
                'current_user':current_user,
                'locations':locations,
                'form':form,
                
            }
            return render(request,'all/new_post.html',context)
            
@login_required
def update_profile(request):
    '''
    this is a view function that handles the update funtionality of our profile
    '''
    
    if request.method == 'POST':
        hood = request.POST.get('Location')
        profileform = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        userform = UserUpdateform(request.POST,instance=request.user)
        
        if profileform.is_valid() and userform.is_valid():
            profile = profileform.save(commit=False)
            profile.neighbourhood = hood
            profile.user = request.user
            profile.save()
            userform.save()
            return redirect('profile')
        else:
            messages.info(request,'All fields are required!')
            return redirect('update-profile')
    
    else:
        profileform = UpdateProfileForm(instance=request.user.profile)
        userform = UserUpdateform(instance=request.user)
        
        current_user = get_object_or_404(Profile,user = request.user)
        current_user = Profile.objects.get(user=request.user)
        business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
        police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
        hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
        user = request.user
        business = Business.objects.filter(neighbourhood=current_user.neighbourhood)
        locations = Neighbourhood.objects.all()
        form = BusinessForm()
        context = {
            'business':business,
            'police':police,
            'hospitals':hospitals,
            'user':user,
            'current_user':current_user,
            'locations':locations,
            'profileform':profileform,
            "userform":userform,
            
        }
        return render(request,'all/update_prof.html',context)
    
@login_required
def profile(request):
    profile = Profile.objects.filter(user= request.user)
    posts = Post.objects.filter(posted_by = request.user)
    
    current_user = get_object_or_404(Profile,user = request.user)
    current_user = Profile.objects.get(user=request.user)
    business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
    police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
    hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
    user = request.user
    business = Business.objects.filter(neighbourhood=current_user.neighbourhood)
    locations = Neighbourhood.objects.all()
    context = {
        'business':business,
        'police':police,
        'hospitals':hospitals,
        'user':user,
        'current_user':current_user,
        'locations':locations,
        'profile':profile,
        'posts':posts,
        
    }
    
    return render(request,'all/profile.html',context)
    

    
@login_required()
def location_view(request,id):
    
    current_user = Profile.objects.get(user=request.user)
    business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
    police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
    hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
    user = request.user
    locations = Neighbourhood.objects.all()  
    location = get_object_or_404(Neighbourhood,id=id)
    occupants = Profile.objects.filter(neighbourhood = location.name)
    hospital_list= Health.objects.filter(neighbourhood = location.name)
    police_list = Police.objects.filter(neighbourhood = location.name)
    business_list = Business.objects.filter(neighbourhood = location.name)
    
    context = {
        'business':business,
        'police':police,
        'hospitals':hospitals,
        'user':user,
        'current_user':current_user,
        'locations':locations,
        'location':location,
        'occupants':occupants,
        'hospital_list':hospital_list,
        'police_list':police_list,
        'business_list':business_list
        
    }
    return render(request,'all/single_hood.html',context)


@login_required()
def business_view(request,id):
    bs = get_object_or_404(Business,id=id)
    current_user = Profile.objects.get(user=request.user)
    business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
    police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
    hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
    user = request.user
    locations = Neighbourhood.objects.all()
    context = {
        'business':business,
        'police':police,
        'hospitals':hospitals,
        'user':user,
        'current_user':current_user,
        'locations':locations,
        'bs':bs,
    }
    return render(request,'all/business.html',context)


