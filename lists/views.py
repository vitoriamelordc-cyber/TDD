from django.shortcuts import render, redirect
from .models import Item


def home_page(request):
    if request.method == 'POST':
        item_text = request.POST['item_text']

        if item_text:
            Item.objects.create(text=item_text)

        return redirect('/')

    return render(request, 'home.html', {
        'new_item_text': '',
    })