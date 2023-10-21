from django.shortcuts import render, redirect
from app.form import MyForm


def my_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            age = form.cleaned_data["age"]
            # You can optionally save this data to a database here.
            return render(
                request, "success_page.html", {"name": name, "email": email, "age": age}
            )
    else:
        form = MyForm()
    return render(request, "form.html", {"form": form})


def success_page(request):
    return render(request, "success_page.html")
