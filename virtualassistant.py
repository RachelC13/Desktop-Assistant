import pyttsx3 #python library allows text to be convertes to speech
import speech_recognition as sr #python library that recognizes spoken words
#from an audio input
import webbrowser #can be used to open a web page in a browser window
import datetime #it is a module that can be used to manipulate date and time
import wikipedia #this API allows to search the wikepdia content
import pyaudio # python library that allows to record and play back audio in Python
import requests

#takes the commands and recognizes them
def takeCommand():

    r = sr.Recognizer() #this allows to recognize the spoken words

    #microphone method to listen to the command
    with sr.Microphone() as source:
        print("Listening")

        #after this many seconds the phrase will be considered as complete
        r.pause_threshold = 0.5
        audio = r.listen(source)

        #see if the sound is recognized
        try:
            print("Recognizing")

            #listening a command in Indian
            Query = r.recognize_google(audio, language = "en-in")
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again Rachel")
            return "None"
        return Query


def speak(audio): #function speak that takes audio as a parameter
    engine = pyttsx3.init()
    #intitializes pyttsx3 engine
    #it gets the current value of the engine property
    voices = engine.getProperty('voices')

    #setting method .[0] is male voice and [1] female voice in this property
    engine.setProperty('voice', voices[0].id)
    #set it to a female voice that is availabel in the engine's system

    #using the engine's say method to speak the audio parameter
    engine.say(audio)

    #engine's runAndWait method which is called to wait for the speech to finish
    engine.runAndWait()

def tellDay(): #function called tellDay which tells the current day of the week
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Rachel today is " + day_of_the_week)

#tell time method
def tellTime():
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is Rachel" + hour + "Hours and" + min + "Minutes")

def tellWeather(city_name):
    api_key = "337aa65ee89b26044042190c15ba051c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"


    
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # Get the response from OpenWeatherMap
    response = requests.get(complete_url)
    
    # Convert response to JSON
    x = response.json()
    
    # Check if the city is found or not
    if x.get("cod") != "404":
        # Extract data from JSON
        main = x.get("main", {})
        weather = x.get("weather", [{}])[0]

        # Temperature in Celsius
        temperature = main.get("temp", 0) - 273.15
        pressure = main.get("pressure", 0)
        humidity = main.get("humidity", 0)
        weather_description = weather.get("description", "No description available")
        
        # Create the response string
        weather_response = (f"The temperature in {city_name} is {round(temperature, 2)} degrees Celsius "
                            f"with {weather_description}. The humidity is {humidity}% "
                            f"and the atmospheric pressure is {pressure} hPa.")
        
        # Print and speak the weather
        print(weather_response)
        speak(weather_response)
    else:
        speak("Sorry, I couldn't find the weather for the location.")



def Hello():
    speak("Hello Rachel this is Jarvis. I am your desktop assistant. What can I help you with today")
    

def Take_query():

    Hello() #making it interactive by callin the Hello function

    #while loop that will run until we say bye or exit the program
    while(True):

        query = takeCommand().lower()
        
        if "open youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        
        elif "open canvas" in query:
            speak("Opening Canvas ")
            webbrowser.open("https://canvas.rutgers.edu/")
            continue

        elif "open pearson" in query:
            speak("Opening Pearson")
            webbrowser.open("https://login.pearson.com/v1/piapi/piui/signin?client_id=dN4bOBG0sGO9c9HADrifwQeqma5vjREy&okurl=https:%2F%2Fmycourses.pearson.com%2Fcourse-home&siteid=8313")
            continue

        elif "what day is it" in query:
            tellDay()
            continue

        elif "what is the time" in query:
            tellTime()
            continue

        elif "what is the weather in" in query:
            
            # Extract city name by removing the trigger phrase from the query
            city_name = query.replace("what is the weather in", "").strip()
            tellWeather(city_name)
            continue

        # this will stop the program
        elif "bye" in query:
            speak("Bye Rachel. Take Care")
            exit()

        elif "from wikipedia" in query:

            #gets the information from wikepedia
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            #this will summarize the results from wikipedia
            result = wikipedia.summary(query, sentences = 4)
            speak("According to wikipedia")
            speak(result)

        elif "tell me your name" in query:
            speak("Hello my name is Jarvis. Your desktop Assistant")





if __name__ == '__main__':
    Take_query()
        
