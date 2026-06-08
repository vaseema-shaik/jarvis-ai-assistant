from speech import listen, speak
from automation import *
from screenshot import take_screenshot
from weather import get_weather
from face_detection import detect_faces
from file_search import search_file

speak("Jarvis started")

while True:

    command = listen()

    if not command:
        continue

    command = command.lower()

    print("You:", command)

    if "open camera" in command:

        speak("Opening camera")
        open_camera()

    elif "take screenshot" in command:

        speak("Taking screenshot")
        take_screenshot()

    elif "weather" in command or "whether" in command:

        city = command.replace("weather", "")
        city = city.replace("whether", "")
        city = city.strip()

        if city:

            weather_info = get_weather(city)

            print(weather_info)
            speak(weather_info)

        else:

            speak("Please tell the city name")

    elif "face detection" in command:

        speak("Starting face detection")
        detect_faces()

    elif "search file" in command:

        filename = command.replace("search file", "").strip()

        result = search_file(filename)

        if result:

            print(result)
            speak("File found")

        else:

            speak("File not found")

    elif "open google" in command:

        speak("Opening Google")
        open_google()

    elif "open youtube" in command:

        speak("Opening YouTube")
        open_youtube()

    elif "open github" in command:

        speak("Opening GitHub")
        open_github()

    elif "open calculator" in command:

        speak("Opening Calculator")
        open_calculator()

    elif "open notepad" in command:

        speak("Opening Notepad")
        open_notepad()

    elif "open cmd" in command:

        speak("Opening Command Prompt")
        open_cmd()

    elif "open paint" in command:

        speak("Opening Paint")
        open_paint()

    

    elif "exit" in command or "stop" in command:

        speak("Goodbye")
        break

    else:

        speak("Command not recognized")