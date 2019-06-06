from django.shortcuts import render

from .forms import CareerForm

def home(request):
	return render(request, 'index.html', {})

def create(request):
	title = 'Create new career'
	form = CareerForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context_data = {
		'title': title,
		'form': form
	}
	return render(request, 'create.html', context_data)