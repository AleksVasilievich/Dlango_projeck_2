import logging
from django.shortcuts import render
from .forms import ImageForm, UserForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render



logger = logging.getLogger(__name__)


def form_app4(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'form_app4.html', {'form': form})


# def form2_app4(request):
#     if request.method == 'POST':
#         form = ManyFieldsForm(request.POST)
#         if form.is_valid():
#             # Делаем что-то с данными
#             logger.info(f'Получили {form.cleaned_data=}.')
#     else:
#         form = ManyFieldsForm()
#     return render(request, 'form2_app4.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form':form})

