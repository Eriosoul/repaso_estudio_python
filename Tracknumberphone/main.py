import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Asegúrate de que el número incluya el código de país, por ejemplo, "+34123456789"
number = ""

# Obtener la ubicación general (país o región)
pepnumber = phonenumbers.parse(number, "ES")
location = geocoder.description_for_number(pepnumber, "es")
print(f"Ubicación general: {location}")

# Obtener el proveedor de servicios del número
service_pro = phonenumbers.parse(number)
provider = carrier.name_for_number(service_pro, 'es')
print(f"Proveedor de servicios: {provider}")

# Utilizar OpenCage para mejorar la precisión de la geolocalización
key = ""
geocoder = OpenCageGeocode(key)
query = str(location)

try:
    results = geocoder.geocode(query)
    if results and len(results) > 0:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        print(f"Coordenadas: {lat}, {lng}")

        # Crear un mapa con Folium
        myMap = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(myMap)

        # Guardar el mapa en un archivo HTML
        myMap.save("mylocation.html")
        print("Mapa guardado como 'mylocation.html'")
    else:
        print("No se encontraron resultados precisos para la ubicación.")
except Exception as e:
    print(f"Error al obtener la geolocalización: {e}")