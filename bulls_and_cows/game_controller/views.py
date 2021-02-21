from django.shortcuts import render


def game_view(request):
    if request.method == 'GET':
        return render(request, 'game_page.html')
    elif request.method == 'POST':
        return render(request, 'game_page.html')

