from django.http import HttpResponse

def homepage(request):
    homepage_file='Front-End/home.html'
    return HttpResponse(homepage_file)