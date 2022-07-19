from django.shortcuts import redirect
from django.shortcuts import render
from reviews.forms import ReviewForm
def main(request):
    if request.method == 'GET':
        form = ReviewForm()
        return render(request,'main.html',{'form':form})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            with open('data.csv','a') as file:
                file.write(f'{name}|{email}|{review}\n')
            return redirect('main')
    else:
        form = ReviewForm()
        return render(request,'main.html',{'form':form})

    

# Create your views here.
