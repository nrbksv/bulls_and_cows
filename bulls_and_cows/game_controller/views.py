from django.shortcuts import render


def game_view(request):
    if request.method == 'GET':
        return render(request, 'game_page.html')
    elif request.method == 'POST':
        context = input_validation(request)
        return render(request, 'game_page.html', context)


def input_validation(request):
    warnings = {}
    try:
        guess = list(map(int, request.POST.get('guess').strip().split(' ')))
        counter = 0
        for i in guess:
            if 0 < i < 11:
                counter += 1
        if len(guess) != 4:
            warnings['warning'] = 'Enter 4 numbers'
        elif len(set(guess)) != 4:
            warnings['warning'] = 'Numbers should not be repeated'
        elif counter != 4:
            warnings['warning'] = 'Numbers should be in range 1-10'
        else:
            warnings['numbers'] = guess
    except ValueError:
        warnings['warning'] = 'Enter only numbers'
    return warnings
