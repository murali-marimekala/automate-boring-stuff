import bs4, requests
def getCourseTaken(websiteurl):
    res = requests.get(websiteurl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #Pass CSS Selector
    elems = soup.select('#modal-1-content > ul > li:nth-child(2) > a > span')
    return elems[0].text.strip()


course = getCourseTaken('https://www.muralimarimekala.com')
print('Course taken is '+ course)