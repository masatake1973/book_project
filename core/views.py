# core/views.py

from django.shortcuts import render

def index(request):
    # トップページの表示ロジック
    # ★ ここでは仮のデータを渡して表示します
    context = {
        'site_name': 'Personal Library',
        'message': 'ようこそ！あなたの読書記録を共有しましょう。',
    }
    return render(request, 'core/index.html', context)