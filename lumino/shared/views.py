from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return redirect('subjects:subject-list')
    return render(request, 'index.html')


def custom_404(request, exception):
    context = {}

    return render(request, '404.html', context, status=404)


def custom_403(request, exception):
    context = {}

    return render(request, '403.html', context, status=403)
