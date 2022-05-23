from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')

def new_list(request):
    my_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=my_list)
    return redirect('/lists/the-only-list-in-the-world/')
