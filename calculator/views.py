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

def _get_servings(request):
    """Вспомогательная функция: безопасно получить число порций."""
    servings_str = request.GET.get('servings')
    try:
        servings = int(servings_str)
        if servings <= 0:
            servings = 1
    except (TypeError, ValueError):
        servings = 1
    return servings


def omlet(request):
    servings = _get_servings(request)
    recipe_data = DATA.get('omlet', {})
    recipe = {ingredient: amount * servings for ingredient, amount in recipe_data.items()}

    context = {'recipe': recipe}
    return render(request, 'calculator/omlet.html', context)


def pasta(request):
    servings = _get_servings(request)
    recipe_data = DATA.get('pasta', {})
    recipe = {ingredient: amount * servings for ingredient, amount in recipe_data.items()}

    context = {'recipe': recipe}
    return render(request, 'calculator/pasta.html', context)


def buter(request):
    servings = _get_servings(request)
    recipe_data = DATA.get('buter', {})
    recipe = {ingredient: amount * servings for ingredient, amount in recipe_data.items()}

    context = {'recipe': recipe}
    return render(request, 'calculator/buter.html', context)