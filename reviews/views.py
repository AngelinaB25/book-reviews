from django.shortcuts import render
from reviews.forms import ReviewForm
def main(request):
    form = ReviewForm()
    name = request.GET.get('name')
    email = request.GET.get('email')
    review = request.GET.get('review')
    return render(request, 'main.html',{'name':name, 'email':email,'review':review,'form':form})

# Create your views here.
