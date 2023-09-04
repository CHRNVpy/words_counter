import mimetypes

from django.shortcuts import render
from .forms import FileUploadForm
from .logic import count_words_in_pdf, count_words_in_docx


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            if uploaded_file:
                mime_type, encoding = mimetypes.guess_type(uploaded_file.name)
                if mime_type == 'application/pdf':
                    result = count_words_in_pdf(uploaded_file)
                    return render(request, 'counter/upload.html',
                                  {'form': form, 'additional_info': result, 'filename': uploaded_file.name})
                elif mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                    result = count_words_in_docx(uploaded_file)
                    return render(request, 'counter/upload.html',
                                  {'form': form, 'additional_info': result, 'filename': uploaded_file.name})
                else:
                    result = '‼️ Incorrect file type, file type must be PDF or docx'
                    return render(request, 'counter/upload.html',
                                  {'form': form, 'wrong_filetype': result, 'filename': uploaded_file.name})
    else:
        form = FileUploadForm()
    return render(request, 'counter/upload.html', {'form': form})
