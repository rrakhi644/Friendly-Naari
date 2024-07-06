import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import pyjokes
import os
import subprocess  # for launching applications

# Initialize speech recognition and text-to-speech engines
listener = sr.Recognizer()
engine = pyttsx3.init()

# Adjust voice settings if needed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Personal Information
name = "Rakesh"
branch = "ECE"
college = "GPCET"
year = "4th year"

# Project Information
projects = {
    "Project 1": "Developing a voice-based virtual assistant"
}

# Internship Information
internship = {
    "Name": "Angstromers Internship",
    "Details": "I am currently doing an internship in Angstromers focusing on observational data analysis."
}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = listener.listen(source, timeout=5)  # Listen for up to 5 seconds
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'naari' in command:
                command = command.replace('naari', '')
                print(command)
    except sr.WaitTimeoutError:
        print("Timeout error. Please try again.")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
    except sr.RequestError:
        print("Sorry, my speech service is down.")
    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting...")
        exit()
    except Exception as e:
        print(f"Error: {e}")
    return command

def open_application(application_name):
    try:
        if 'chrome' in application_name.lower():
            talk('Opening Google Chrome')
            subprocess.Popen(['C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'])
        elif 'notepad' in application_name.lower():
            talk('Opening Notepad')
            subprocess.Popen(['notepad.exe'])
        elif 'calculator' in application_name.lower():
            talk('Opening Calculator')
            subprocess.Popen(['calc.exe'])
        elif 'word' in application_name.lower():
            talk('Opening Microsoft Word')
            subprocess.Popen(['C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'])
        # Add more applications as needed
        else:
            talk(f"Sorry, I don't know how to open {application_name}.")
    except Exception as e:
        talk(f"An error occurred while opening {application_name}: {str(e)}")

def run_assistant():
    while True:
        command = take_command()
        print("Command:", command)

        if command:
            if 'play' in command:
                song = command.replace('play', '')
                talk('Playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
            elif 'date' in command:
                date = datetime.datetime.now().strftime('%B %d, %Y')
                talk('Today is ' + date)
            elif 'open chrome' in command:
                open_application('Google Chrome')
            elif 'open youtube' in command:
                talk('Opening YouTube')
                webbrowser.open_new_tab("http://www.youtube.com")
            elif 'open notepad' in command:
                open_application('Notepad')
            elif 'open calculator' in command:
                open_application('Calculator')
            elif 'open word' in command:
                open_application('Microsoft Word')
            elif 'my name' in command:
                talk(f'Your name is {name}')
            elif 'my branch' in command:
                talk(f'You are studying {branch}')
            elif 'my college' in command:
                talk(f'Your college is {college}')
            elif 'my year' in command:
                talk(f'You are currently in {year}')
            elif 'my projects' in command:
                talk('Here is your project:')
                for project, description in projects.items():
                    talk(f'{project}: {description}')
            elif 'what internship' in command:
                talk(f'Your internship details are: {internship["Details"]}')
            elif 'are you single' in command:
                talk('I am in a relationship with WiFi.')
            elif 'joke' in command:
                talk(pyjokes.get_joke())
            elif 'stop' in command:
                talk('Goodbye!')
                break  # Exit the loop and stop the program
            else:
                talk('Please say the command again.')

if __name__ == "__main__":
    talk(f"Hello {name}! I'm Naari, your virtual assistant. How can I help you today?")
    run_assistant()
