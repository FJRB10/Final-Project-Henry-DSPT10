import requests
#API_KEY = ''
#place_name = 'City Textile'
#location = '34.018891,-118.21529'  # Reemplaza con la latitud y longitud del lugar

def get_place_id(API_KEY,place_name,location):
    url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place_name}&inputtype=textquery&fields=place_id&locationbias=circle:2000@{location}&key={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        place_id = response.json().get('candidates', [{}])[0].get('place_id')
        return place_id
    else:
        print(f'Error: {response.status_code} - {response.text}')