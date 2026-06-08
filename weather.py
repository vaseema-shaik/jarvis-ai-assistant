import requests

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"

        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        else:
            return "Unable to fetch weather"

    except Exception as e:
        return f"Error: {e}"