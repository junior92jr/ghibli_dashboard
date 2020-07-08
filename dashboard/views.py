from django.shortcuts import render

from .utils import DataManager


def index(request):
    """
    Index View that handles the data to be displayed.
    """

    manager = DataManager()

    films_list = manager.get_dashboard_data()

    context = {'error': None}

    if films_list:
        context.update({'films_list': films_list})
    else:
        context.update({'error': 'Data not available, Come back Later'})

    return render(request, "dashboard/index.html", context)
