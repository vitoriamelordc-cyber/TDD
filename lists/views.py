from django.shortcuts import render
from .models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])

    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })