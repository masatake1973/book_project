# books/views.py

from django.shortcuts import render, get_object_or_404
# 将来的にはBookモデルから書籍情報を取得しますが、今は仮のデータを使います

def book_detail(request, book_id):
    # 書籍詳細ページの表示ロジック
    # ★ ここでは仮の書籍情報とデータを表示します
    # 実際にはデータベースから書籍を検索します

    # 仮の書籍情報
    books_data = {
        1: {'title': 'レ・ミゼラブル', 'author': 'ヴィクトル・ユーゴー', 'description': 'フランスの貧困と革命を描いた大作。', 'reviews': [{'user': '田中　一郎', 'text': '感動しました！'}]},
        2: {'title': '罪と罰', 'author': 'フョードル・ドストエフスキー', 'description': 'ロシア文学の金字塔。', 'reviews': [{'user': '佐藤　愛子', 'text': '深く考えさせられました。'}]},
        3: {'title': '存在と時間', 'author': 'マルティン・ハイデガー', 'description': '20世紀の哲学の根幹をなす著作。', 'reviews': [{'user': '佐藤　愛子', 'text': '難解でしたが、読む価値あり。'}]},
    }

    book_info = books_data.get(book_id, {'title': '本が見つかりません', 'author': '', 'description': '', 'reviews': []})

    context = {
        'site_name': 'Personal Library',
        'book_info': book_info,
    }
    return render(request, 'books/book_detail.html', context)