from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm, ReservationForm
from .models import GalleryImage, MenuCategory, Post, TeamMember


def home(request):
    return render(request, 'cafe/home.html', {
        'categories': MenuCategory.objects.all(),
        'posts': Post.objects.all()[:3],
        'gallery': GalleryImage.objects.all()[:4],
    })


def menu(request):
    return render(request, 'cafe/menu.html', {
        'categories': MenuCategory.objects.prefetch_related('items'),
    })


def about(request):
    return render(request, 'cafe/about.html', {'team': TeamMember.objects.all()})


def gallery(request):
    return render(request, 'cafe/gallery.html', {'images': GalleryImage.objects.all()})


def news(request):
    return render(request, 'cafe/news.html', {'posts': Post.objects.all()})


def news_detail(request, pk):
    return render(request, 'cafe/news_detail.html', {'post': get_object_or_404(Post, pk=pk)})


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Ви благодариме! Вашата порака е примена.')
        return redirect('contact')
    return render(request, 'cafe/contact.html', {'form': form})


def reservation(request):
    form = ReservationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Вашата резервација е примена. Ќе ве контактираме за потврда.')
        return redirect('reservation')
    return render(request, 'cafe/reservation.html', {'form': form})


def privacy(request):
    return render(request, 'cafe/privacy.html')
