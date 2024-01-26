import requests
from pprint import pprint


def ebook_list(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    book_list = []
    params = {
        'ttbkey': '알라딘api',
        'Query': title,
        'QueryType': 'title',
        'MaxResults': 1,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    response = requests.get(URL, params=params).json()
    if response.get('item') == []:
        return None


    params['MaxResults'] = 1
    params['SearchTarget'] = 'eBook'
    
    response_ebook = requests.get(URL, params=params).json()

    
    return response_ebook.get('item')[0].get('priceSales')


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(ebook_list('베니스의 상인'))

    pprint(ebook_list('*'))
