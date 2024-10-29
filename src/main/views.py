from django.shortcuts import render


def main_view(request):
    return render(request, "main/template/views/main.html", {"name": "ShowBlitz"})
