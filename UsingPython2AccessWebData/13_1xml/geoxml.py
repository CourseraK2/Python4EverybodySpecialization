import urllib
import xml.etree.ElementTree as ET

fh = open("comments_182076.xml")
data = fh.read()
tree = ET.fromstring(data)

# putting .// actually searches anywhere
results = tree.findall('.//count')
#//commentinfo/comments/comment

sum = 0
for result in results:
    sum  = sum + int(result.text)

print(sum)

# fh =
# while True:
#     address = raw_input('Enter location: ')
#     if len(address) < 1 : break
#
#     url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#     print 'Retrieving', url
#     uh = urllib.urlopen(url)
#     data = uh.read()
#     print 'Retrieved',len(data),'characters'
#     print data
#     tree = ET.fromstring(data)
#
#
#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text
#
#     print 'lat',lat,'lng',lng
#     print location
