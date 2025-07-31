# users/views.py

from django.shortcuts import render, get_object_or_404
# 将来的にはUserモデルからユーザー情報を取得しますが、今は仮のデータを使います
from django.contrib.auth import get_user_model

User = get_user_model() # DjangoのUserモデルを取得

def user_detail(request, username):
    # ユーザー詳細ページの表示ロジック
    # ★ ここでは仮のユーザー情報とデータを表示します
    # 実際にはデータベースからユーザーを検索します
    # user = get_object_or_404(User, username=username)

    # 仮のユーザー情報
    users_data = {
        '田中　一郎': {'bio': 'SF小説と歴史小説が好きです。', 'read_books': ['レ・ミゼラブル']},
        '佐藤　愛子': {'bio': '哲学と文学に興味があります。', 'read_books': ['罪と罰', '存在と時間']},
        '鈴木　たかし': {'bio': 'ミステリーとビジネス書を読みます。', 'read_books': []},
    }

    user_info = users_data.get(username, {'bio': 'ユーザーが見つかりません', 'read_books': []})

    context = {
        'site_name': 'Personal Library',
        'username': username,
        'user_info': user_info,
    }
    return render(request, 'users/user_detail.html', context)