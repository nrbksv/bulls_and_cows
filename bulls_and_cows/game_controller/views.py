from django.shortcuts import render
from random import randint

history = [{'step': 0, 'res': ''}]


def game_view(request):
    if request.method == 'GET':
        return render(request, 'game_page.html')
    elif request.method == 'POST':
        context = input_validation(request)
        if context.get('numbers'):
            check(context.get('numbers'))
            context['result'] = history[-1].get('res')
        return render(request, 'game_page.html', context)


def history_view(request):
    context = {'history': history}
    return render(request, 'game_history.html', context)


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


def check(numbers):
    bulls = 0
    cows = 0
    secret_nums = [1, 2, 3, 5]

    for i in range(len(numbers)):
        if numbers[i] == secret_nums[i]:
            bulls += 1
        elif numbers[i] in secret_nums:
            cows += 1

    step = history[-1]['step']
    if bulls == 4:
        history.append({'step': step+1, 'res': 'You got it right!'})
        return
    history.append({'step': step+1, 'res': f'You got {bulls} bulls, {cows} cows'})



