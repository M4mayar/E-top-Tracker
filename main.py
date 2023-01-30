import folium
import phonenumbers
from numpy import key
from opencage.geocoder import opencage
from phonenumbers import carrier

from myNumber import number

Key = '80a51872409b44c9a83471a68ec1b888'
sanNumber = phonenumbers.parse(number)
geocoder = opencage(key)

yourLocation = geocoder.description_for_number(sanNumber, "en")
print(yourLocation)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

geocoder = opencage(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)
 
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)
# save map in html file
myMap.save("MyLocation.html")
