from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import UploadPdf
from .forms import UploadPdfForm
from .utils import *
import textract
import re
import glob
import os


@csrf_exempt 

def upload_pdf(request):
    if request.method == 'POST':
        form = UploadPdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            list_of_files = glob.glob('/home/camila/Desktop/projetos/ibti/NLP-information-extractor/media/documents/*')
            lastest_file = max(list_of_files, key=os.path.getctime)
            text = textract.process(lastest_file, method='pdfminer').decode('utf-8')
            paragraphs = re.split('\n\n', text)
            clean_paragraphs = cleanner(text)
            occurrences_keywords(paragraphs)
            save_db(lastest_file)
            return redirect('/')
    else:
        form = UploadPdfForm()
    return render(request, 'pdf_kw_extractor/upload_pdf.html', {
            'form':form,
        })