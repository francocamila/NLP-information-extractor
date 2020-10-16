from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import UploadPdf
from .forms import UploadPdfForm


@csrf_exempt 

def upload_pdf(request):
    if request.method == 'POST':
        form = UploadPdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UploadPdfForm()
    return render(request, 'pdf_kw_extractor/upload_pdf.html', {
            'form':form,
        })
        #form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        #    handle_uploaded_file(request.FILES['file'])
        #    return HttpResponseRedirect('/success/url/')
    #else:
    #    form = UploadFileForm()
    #return render(request, 'upload.html', {'form': form})