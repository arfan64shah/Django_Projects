from django.shortcuts import render
from django.core.files.storage import FileSystemStorage 


def index(request):
    context = {'a': 1}
    return render(request, 'index.html', context)

def predictImage(request):
    print(request)
    print(request.POST.dict())
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    fs.save(fileObj.name, fileObj)
    context = {'a': 1}
    return render(request, 'index.html', context)