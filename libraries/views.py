# libraries/views.py #

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def library_list(request):
    libraries = [
        {'id': 1, 'name': '大阪市立図書館本館'},
        {'id': 2, 'name': '東大阪市立図書館西分館'},
    ]
    context = {
        'site_name': 'Personal Library',
        'libraries': libraries,
    }
    return render(request, 'libraries/library_list.html', context)

@login_required
def library_detail(request, library_id):
    libraries_data = {
        1: {'name': '大阪市立図書館本館', 'address': '大阪府大阪市西成区西野1-1-1', 'TEL': '00-000', 'reviews': [{'user': '田中　一郎', 'text': '蔵書数がすごい'}]},
        2: {'name': '東大阪市立図書館西分館', 'address': '大阪府東大阪市近藤1-1-1', 'TEL': '11-000', 'reviews': [{'user': '佐藤　愛子', 'text': '司書さんがていねいに教えてくれる。'}]},
    }


    library_info = libraries_data.get(library_id, {'title': '図書館が見つかりません', 'name': '', 'address': '', 'TEL': '', 'reviews': []})

    context = {
        'site_name': 'Personal Library',
        'library_info': library_info,
    }
    return render(request, 'libraries/library_detail.html', context)