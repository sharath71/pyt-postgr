import requests
import json
import pandas as pd

def fetch_user_data():
    """Fetch user data from API"""
    
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    data = response.json()

    users = []
    for user in data:
        users.append({ 
            'id': user['id'],
            'name': user['name'],
            'city': user['address']['city'].strip(),
            'lat': str(user['address']['geo']['lat']).strip(),
            'lng': str(user['address']['geo']['lng']).strip()
        })
        
    user_df = pd.DataFrame(users)
    
    return user_df

def fetch_weather_func(location, api_key='5b6c8ec3280127b16da26dfb1a707490'):
    """
    Fetch weather data from OpenWeatherMap API based on location.

    Args:
        location (str): Location string in the format "city,lat,lng".
        api_key (str): API key for accessing the OpenWeatherMap API.

    Returns:
        dict: Weather data.
    """
    try:
        # Check if location is not None
        if location is None:
            return None
        
        # Split the location string into city, lat, and lon
        lat, lon = location.split(',')
        lat = lat.strip()
        lon = lon.strip()

        # Make API call to fetch weather data using the provided API key
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        # Check if response is successful (status code 200)
        response.raise_for_status()
        
        # Parse JSON response
        weather_data = response.json()
        
        # Check if the API response contains valid weather data
        if 'cod' in weather_data and weather_data['cod'] != 200:
            print(f"Error fetching weather data: {weather_data['message']}")
            return None
        
        # Extract relevant weather information
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        weather_conditions = weather_data['weather'][0]['main']
        
        return {'temp': temperature, 'desc': description,'weather_conditions':weather_conditions}
    
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    
    except json.JSONDecodeError as e:
        print(f"Error parsing weather data response: {e}")
        return None
