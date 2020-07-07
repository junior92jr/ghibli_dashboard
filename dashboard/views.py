from django.shortcuts import render

from .utils import DataManger


def index(request):
    """
    Index View that handles the data to be displayed.
    """

    manager = DataManger()

    films_list = manager.get_dashboard_data()

    context = {'error': None}

    if films_list:
        context.update({'films_list': films_list})
    else:
        context.update({'error': 'Data not available, Come back Later'})

    return render(request, "dashboard/index.html", context)
