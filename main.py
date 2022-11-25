from bs4 import BeautifulSoup

with open('alice.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    hyperlink_tags = soup.find_all('a')
    for hyperlink in hyperlink_tags:
        print(hyperlink.text)