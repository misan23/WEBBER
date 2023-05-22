import phonenumbers
from phonenumbers import geocoder
from myphone import number
import folium


key = 'c76ef1059f144cf696a0320504c166a4'

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("mylocation.html") 