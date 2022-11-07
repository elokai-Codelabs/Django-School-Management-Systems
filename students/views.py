from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student
from .forms import StudentForm



# Create your views here.
def index(request):
    students = Student.objects.all();
    context = {'students': students}
    return render(request, 'students/index.html', context)

def view_student(request,id):
    student = Student.objects.get(pk =id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']

            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa,
            )

            new_student.save();
            context = {'form': StudentForm() ,'success' :True}
            return render(request, 'students/add.html', context)

        else :
            form = StudentForm()
            context = {'form': StudentForm()}
        return render(request, 'students/add.html', context)

def edit(request, id):
    if request.method =='POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            context = {'form': form, 'success':True}
            return render(request, 'students/edit.html')
        else:
            student = Student.objects.get(pk =id)
            form = StudentForm(instance=student)
        return render(request, 'students/edit.html')

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))  
