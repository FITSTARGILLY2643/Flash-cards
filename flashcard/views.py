from flashcard.models import Folder,Card,Profile
from django.shortcuts import render, redirect
from .forms import RegisterForm,AddFolderForm, AddCardForm
from .models import Folder, Card
from django.utils import timezone

# Create your views here.
def home(request):
    folders = Folder.objects.filter(user_id=request.user.id)
    return render(request, 'index.html', {"folders": folders})


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)

def folder(request, folder):
    current_folder = Folder.objects.get(id=folder)
    cards = Card.objects.filter(folder_id=folder)
    return render(request, 'folder.html', {"folder": current_folder, "cards": cards})

def add_folder(request):
    if request.method == 'POST':
        form = AddFolderForm(request.POST)
        if form.is_valid():
            folder = Folder(title=form.cleaned_data.get('title'),
                        user=request.user)
            folder.save()
            return redirect('home')
        else:
            return render(request, 'add-folder.html', {'form': form})
    else:
        form = AddFolderForm()
        return render(request, 'add-folder.html', {'form': form})

def add_card(request, folder):
    if request.method == 'POST':
        form = AddCardForm(request.POST)
        if form.is_valid():
            card = Card(title=form.cleaned_data.get('title'),
                        notes=form.cleaned_data.get('notes'),
                        folder=Folder.objects.get(id=folder))
            card.save()
            return redirect('folder', folder=int(folder))
        else:
            return render(request, 'add-card.html', {'form': form})
    else:
        form = AddCardForm()
        return render(request, 'add-card.html', {'form': form})



def delete_card(request, card):
    current_card=Card.objects.get(id=card)
    folder=current_card.folder
    current_card.delete()
    return redirect('folder', folder=folder.id)

def edit_card(request, card):
    page_title = "Edit Card"
    editting_card = Card.objects.get(id=card)

    if request.method == 'POST':
        form = AddCardForm(request.POST)
        if form.is_valid():
            card = Card.objects.get(id=card)
            card.title=form.cleaned_data.get('title')
            card.notes=form.cleaned_data.get('notes')
            card.date_updated = timezone.now()
            card.save()
            return redirect('folder', folder=card.folder.id)
        else:
            return render(request, 'add-card.html', {'form': form, "page_title": page_title})
    else:
        form = AddCardForm(initial={'title': editting_card.title, 'notes': editting_card.notes})
        return render(request, 'add-card.html', {'form': form, "page_title": page_title})
