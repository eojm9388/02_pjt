import requests
from pprint import pprint


def author_other_works(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    book_list = []
    params = {
        'ttbkey': '알라딘api',
        'Query': title,
        'QueryType': 'title',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    response = requests.get(URL, params=params).json()
    if response.get('item') == []:
        return None
    else:
        author = response.get('item')[0].get('author')
        author_index = author.find('(지은이)')


    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params['Query'] = author[:author_index]
    params['QueryType'] = 'Author'
    params['MaxResults'] = 5
    
    response_author = requests.get(URL, params=params).json()

    for book in response_author.get('item'):
        book_list.append(book.get('title'))
    
    return book_list





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
