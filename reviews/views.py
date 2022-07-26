from django.shortcuts import redirect
from django.shortcuts import render
from reviews.forms import ReviewForm
from reviews.models import Review
def main(request):
    if request.method == 'GET':
        form = ReviewForm()
        reviews = Review.objects.all()
        return render(request,'main.html',{'form':form, 'reviews':reviews})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')
            Review.objects.create( name=name,email=email,review=review,rating=rating)
            review_1 = Review.objects.get(id = 1)
            print(review_1.name)
            return redirect('main')
        reviews = Review.objects.all()
        form = ReviewForm()
        return render(request,'main.html',{'form':form, 'reviews':reviews})

    

# Create your views here.
