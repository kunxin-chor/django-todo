from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
def show_todos(request):
    # return HttpResponse("Hello World")
    results = Item.objects.all()
    return render(request, 'todo.html', {
        'items': results
    })
    
def create_item(request):
  if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(show_todos)
    
  else:
    form = ItemForm()
    return render(request, "item_form.html", {'form': form})
    
def edit_item(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(show_todos)
    else:
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {'form': form})