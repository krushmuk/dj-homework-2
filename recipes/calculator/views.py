from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_maker(request, recipe):
    servings = int(request.GET.get('servings', 1))
    context = {'recipe': {}}
    for ingredient in DATA[recipe].keys():
        context['recipe'][ingredient] = round(DATA[recipe][ingredient]*servings, 3)

    return render(request, 'calculator/index.html', context)
