from multiprocessing import context
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ClassForm, StudentForm
from .models import Class, Student
from other_apps.models import Upload_download_file


def Homepage(request):
    files = Upload_download_file.objects.all()
    return render(request, 'Homepage/index.html', {'files': files})


def index(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            form = ClassForm()

    else:
        form = ClassForm()

        authors = Class.objects.all()

        student_6 = Student.objects.filter(author_id="1").count()
        student_7 = Student.objects.filter(author_id="2").count()
        student_8 = Student.objects.filter(author_id="3").count()
        student_9 = Student.objects.filter(author_id="4").count()
        student_10 = Student.objects.filter(author_id="5").count()

        context = {

            'form': form,
            'authors': authors,
            'student_6': student_6,
            'student_7': student_7,
            'student_8': student_8,
            'student_9': student_9,
            'student_10': student_10,

        }

    return render(request, 'home.html', context)


def create_book(request, pk):
    author = Class.objects.get(id=pk)
    books = Student.objects.filter(author=author)
    form = StudentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("detail-book", pk=book.id)
        else:
            return render(request, "partials/book_form.html", context={
                "form": form
            })

    context = {
        "form": form,
        "author": author,
        "books": books
    }

    return render(request, "create_book.html", context)


def update_book(request, pk):
    book = Student.objects.get(id=pk)
    form = StudentForm(request.POST or None, instance=book)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("detail-book", pk=book.id)

    context = {
        "form": form,
        "book": book
    }

    return render(request, "partials/book_form.html", context)


def delete_book(request, pk):
    book = get_object_or_404(Student, id=pk)

    if request.method == "POST":
        book.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def detail_book(request, pk):
    book = get_object_or_404(Student, id=pk)
    context = {
        "book": book
    }
    return render(request, "partials/book_detail.html", context)


def create_book_form(request):
    form = StudentForm()
    context = {
        "form": form
    }
    return render(request, "partials/book_form.html", context)
