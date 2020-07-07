from django.shortcuts import render

from .utils import DataManger


def index(request):
    """
    Index View that handles the data to be displayed.
    """
    
    manager = DataManger()

    films_list = manager.get_dashboard_data()

    return render(request, "dashboard/index.html", {'films_list': films_list})
