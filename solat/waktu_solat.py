from urllib.request import urlopen
import xmltodict

def solat(district):

    base_url = 'http://www2.e-solat.gov.my/xml/today/?zon='
    final_url = base_url + district

    jakim_xml = xmltodict.parse(urlopen(final_url).read())

    solat.districts = jakim_xml['rss']['channel']['description']
    solat.curr_time = jakim_xml['rss']['channel']['dc:date']

    solat.prayers = []
    solat.pray_time = []

    counter = 0
    while(counter < 7):
        solat.prayers.append(
                        jakim_xml['rss']['channel']['item'][counter]['title']
                        )
        solat.pray_time.append(
                            jakim_xml['rss']['channel']['item'][counter]['description']
                            )
        counter += 1

    solat.prayers_compact = zip(solat.prayers, solat.pray_time)

solat('KDH01')
print(solat.districts)
print(solat.curr_time)

for x, y in solat.prayers_compact:
    print('%s \t %s' % (x, y))
