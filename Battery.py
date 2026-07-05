import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import webbrowser

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
player = pyttsx3.init()
rate = player.getProperty('rate')
player.setProperty('rate', rate - 50)  # Adjust speaking rate

def listen():
    """Capture voice input and convert it to text."""
    with sr.Microphone() as input_device:
        print("Listening...")
        try:
            voice_content = listener.listen(input_device, timeout=10, phrase_time_limit=5)
            text_command = listener.recognize_google(voice_content).lower()
            print(f"User said: {text_command}")
            return text_command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition; {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

def talk(text):
    """Convert text to speech and speak it out."""
    player.say(text)
    player.runAndWait()

def get_summary(command):
    """Fetch a short Wikipedia summary while handling errors."""
    try:
        info = wikipedia.summary(command, sentences=2, auto_suggest=True)
        return info
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your search is ambiguous. Options: {', '.join(e.options[:5])}."
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find anything related to your request."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def open_website(url):
    """Open a given website in the default web browser."""
    webbrowser.open(url)

def run_voice_bot():
    """Main function to process voice commands."""
    while True:
        command = listen()

        if command:
            if "stop" in command:
                talk("You requested quitting, I'm exiting now.")
                print("You requested quitting, I'm exiting now.")
                break

            if "search for" in command:
                query = command.replace("search for", "").strip()
                talk(f"Searching Google for {query}")
                pywhatkit.search(query)

            elif "play" in command:
                song = command.replace("play", "").strip()
                talk(f"Playing {song} on YouTube")
                pywhatkit.playonyt(song)

            elif "open" in command:
                website = command.replace("open", "").strip()
                if "youtube" in website:
                    open_website("https://www.youtube.com")
                elif "google" in website:
                    open_website("https://www.google.com")
                elif "instagram" in website:
                    open_website("https://www.instagram.com")
                elif "gpt" in website:
                    open_website("https://chatgpt.com/")
                elif "on google" in website:
                    search_query = website.replace("on google", "").strip()
                    talk(f"Opening {search_query} on Google")
                    pywhatkit.search(search_query)
                else:
                    talk("Sorry, I am not sure about that website.")

            elif "what is" in command or "who is" in command:
                topic = command.replace("what is", "").replace("who is", "").strip()
                info = get_summary(topic)
                talk(info)

            else:
                talk("I am unable to process your request.")

# Run the voice assistant
try:
    run_voice_bot()
except KeyboardInterrupt:
    talk("You requested quitting, I'm exiting now.")
    print("You requested quitting, I'm exiting now.")
