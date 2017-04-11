import urllib2
import BeautifulSoup
import unicodedata

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def norm(s):
    return unicodedata.normalize('NFKD', s).encode('ascii','ignore')

radios = []

soup = BeautifulSoup.BeautifulSoup(urllib2.urlopen('http://www.listenlive.eu/france.html').read())
table = soup.find('tbody')
rows = table.findAll('tr')
for tr in rows[1:]:
    cols = tr.findAll('td')
    name = norm(unicode(cols[0].findAll('b')[0].string))
    url = cols[3].findAll('a')[0].get('href')
    category = norm(unicode(cols[4].string))
    radios += [ (name, url, category) ]

print '<?xml version="1.0" standalone="yes"?>'
print '<rhythmdb version="1.9">'

for radio in radios:
    print '<entry type="iradio">'
    print '<title>{}</title>'.format(radio[0])
    print '<genre>{}</genre>'.format(radio[2])
    print '<artist></artist>'
    print '<album></album>'
    print '<location>{}</location>'.format(radio[1])
    print '<play-count>0</play-count>'
    # <last-played></last-played>
    # <bitrate>96</bitrate>
    print '<date>0</date>'
    print '<media-type>application/octet-stream</media-type>'
    print '</entry>'

print '</rhythmdb>'
