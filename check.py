from bs4 import BeautifulSoup
from lxml import etree
from get_xpath import xpath_soup


def get_features(doc):
    file = open(doc, 'r')
    soup = BeautifulSoup(file.read(), features='html.parser', multi_valued_attributes=None)
    elem = soup.find(id='make-everything-ok-button')
    return elem.attrs


f = 'sample-0-origin.html'
feats = get_features(f)

print(feats)
for i in feats.items():
    print(i)