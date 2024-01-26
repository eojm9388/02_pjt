import requests
from pprint import pprint


def bestseller_book():
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    book_list = []
    book_sale_title = []
    params = {
        'ttbkey': '알라딘api',
        'Query': '파울로 코엘료',
        'QueryType': 'Author',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    response = requests.get(URL, params=params).json()

    for book in response.get('item'):
        book_sale = []

        book_sale.append(book.get('salesPoint'))
        book_sale.append(book.get('title'))
        book_list.append(book_sale)

    book_list.sort(reverse=True)

    for book in book_list[:5]:
        book_sale_title.append(book[1])
    return book_sale_title


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(bestseller_book())