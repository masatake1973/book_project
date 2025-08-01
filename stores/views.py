from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def store_list(request):
    # 仮の書籍情報
    stores = [
        {'id': 1, 'name': 'ヤマキ書店'},
        {'id': 2, 'name': 'ABCブックストア'},
    ]
    context = {
        'site_name': 'Personal Library',
        'stores': stores,
    }
    return render(request, 'stores/store_list.html', context)

@login_required
def store_detail(request, store_id):
    store_data = {
        1: {'name': 'ヤマキ書店', 'address': '大阪府大阪市西成区西野1-1-1', 'TEL': '00-000', 'reviews': [{'user': '田中　一郎', 'text': '町の本屋さんです。'}]},
        2: {'name': 'ABCブックストア', 'address': '大阪府東大阪市近藤1-1-1', 'TEL': '11-000', 'reviews': [{'user': '佐藤　愛子', 'text': '広くてきれい。'}]},
    }




    store_info = stores_data.get(store_id, {'title': '書店が見つかりません', 'name': '', 'address': '', 'TEL': '', 'reviews': []})

    context = {
            'site_name': 'Personal Library',
            'store_info': store_info,
        }
    return render(request, 'stores/store_detail.html', context)
