from django.shortcuts import render_to_response
from mainpage.models import List

# Create your views here.
def report(request):
    todo_listing = []
    for todo_list in List.objects.all():
        todo_dict = {}
        todo_dict['list_object'] = todo_list
        todo_dict['item_count'] = todo_list.item_set.count()
        todo_dict['items_complete'] = todo_list.item_set.filter(completed=True)
        todo_listing.append(todo_dict)
    return render_to_response('status_report.html', {'todo_listing' : todo_listing})

# def add(request):
# def status(request):
#     todo_listing = []
#     for todo_list in List.objects.all():
#         todo_dict = {}
#         todo_dict['items_not_complete'] = todo_list.item_set.filter(completed=False)
#     return render_to_response('login/templates/home.html', {'todo_listing' : todo_listing})