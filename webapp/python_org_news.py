import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        result = requests.get(url)
        result. raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    
def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        resul_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            resul_news.append({
                "title": title,
                "utl": url,
                "published": published
            })
        return resul_news
    return False
      
    # print(all_news)

# if __name__==('__main__'):
#     html = get_html("https://www.python.org/blogs/")
#     if html:
#         news = get_python_news(html)
#         print(news)
#         # print('Все ок')
#         # with open('python.org.html', 'w', encoding = 'utf-8') as f:
#         #     f.write(html)