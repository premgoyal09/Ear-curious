from django.shortcuts import render, HttpResponse, redirect
from myapp1.models import Contact
from django.contrib import messages

from .forms import SignupForm, LoginForm

# Create your views here.

def home(request):
    return render(request, 'nav/home.html')
    # return HttpResponse("I am EAt -m MAIN")

def about(request):
    return render(request, 'nav/about.html')
    # return HttpResponse("I am EAt -m about")

def products(request):
    return render(request, 'nav/products.html')
    # return HttpResponse("I am EAt -m products")

def recipes(request):
    return render(request, 'nav/recipes.html')
    # return HttpResponse("I am EAt -m recipes")

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "please fill the form attentively ")
        else:
            contact = Contact(name=name, email=email, phone=phone)
            contact.save()      
            messages.success(request, "thanks you , your messages was sent sucessfully")
  
    return render(request, 'nav/contact.html')
    # return HttpResponse("I am EAt -m contact")
    

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']
            user.save()
            return redirect('contact')
    else:
        form = SignupForm()
    return render(request, 'nav/contact.html', {'form':form})
    # return HttpResponse("Hey whts up guys this is signup")
    
            #homes=login
def homes(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            try:
                user = Contact.objects.get(name=name, password=password)
                request.session['user_id'] = user.id
                messages.success(request, 'Logged in this successfully')
                return redirect('contact') 
            except Contact.DoesNotExist:
                messages.error(request, 'Invalid Crediantails!')
    else:
        form = LoginForm()
    return render(request, 'form/login.html')


def main(request):
    # if 'user_id' in request.session:
        # user = Contact.objects.get(id=request.session['user_id'])
        # return render(request, 'form/main.html', {'user': user})
    # return redirect('use')
    return render(request, 'form/main.html')
    # return HttpResponse('I am main ........')


def users(request):
    if 'user_id' in request.session:
        users = Contact.objects.all()
        return render(request, 'form/users.html', {'users': users})
    # return redirect('main')
    
    
def logout_view(request):
    try:
        del request.session["user_id"]
    except KeyError:
        print("error")
    return redirect('signup')