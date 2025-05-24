from django.shortcuts import render
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'students/success.html')
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form})
