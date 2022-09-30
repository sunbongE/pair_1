from turtle import title
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "crud/index.html", context)


def new(request):
    return render(request, "crud/new.html")


def create(request):
    content = request.GET.get("content")
    title = request.GET.get("title")

    Review.objects.create(
        content=content,
        title=title,
    )

    context = {
        "content": content,
        "title": title,
    }
    return redirect("crud:index")


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "crud/detail.html", context)


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()

    return redirect("crud:index")


def edit(request, pk):

    review = Review.objects.get(pk=pk)

    context = {
        "review": review,
    }

    return render(request, "crud/edit.html", context)


def update(request, pk):
    # update할 특정 데이터를 불러온다. -> todo_pk 를 사용해서
    review = Review.objects.get(pk=pk)

    content_ = request.GET.get("content")
    title_ = request.GET.get("title")

    review.content = content_
    review.title = title_

    review.save()

    return redirect("crud:index")
