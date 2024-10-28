# Naari - Virtual Assistant

**Naari** is a Python-based voice-activated virtual assistant that performs various tasks, including opening applications, playing music on YouTube, providing date and time, cracking jokes, and sharing personal information as per user configuration. Naari can be personalized with the user’s details, projects, and internship information.

---

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [Commands](#commands)
6. [Customization](#customization)
7. [Error Handling](#error-handling)
8. [License](#license)

---

### Features
- **Voice Commands**: Listens and responds to voice commands for hands-free use.
- **Open Applications**: Launches applications like Chrome, Notepad, Calculator, and Word.
- **Date and Time**: Provides the current date and time.
- **Play Music**: Searches and plays music on YouTube.
- **Project & Internship Info**: Shares information about user projects and internships.
- **Entertainment**: Tells jokes using the pyjokes library.
- **Personalized Responses**: Responds with personalized information based on user data.

---

### Requirements
- Python 3.x
- `speech_recognition`
- `pyttsx3`
- `pywhatkit`
- `pyjokes`
- `datetime`
- `webbrowser`
- `subprocess`

---

### Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/naari-assistant.git
    cd naari-assistant
    ```

2. **Install Dependencies**: Install required Python packages:
    ```bash
    pip install speechrecognition pyttsx3 pywhatkit pyjokes
    ```

3. **Configure Personal Information**: Open the script and adjust the variables for `name`, `branch`, `college`, `year`, `projects`, and `internship` dictionaries with your personal information.

4. **Run the Script**:
    ```bash
    python naari_assistant.py
    ```

---

### Usage
Once the setup is complete, run the script and interact with Naari by saying "Naari" followed by your command. For example:
- "Naari, play Shape of You" - Plays the song on YouTube.
- "Naari, what is the time?" - Tells the current time.
- "Naari, open Chrome" - Opens the Google Chrome browser.
- "Naari, tell me a joke" - Naari will tell a joke.

---

### Commands

#### Media:
- `play [song name]` – Searches and plays the song on YouTube.

#### Information:
- `time` - Tells the current time.
- `date` - Tells today’s date.
- `my name`, `my branch`, `my college`, `my year` - Shares personal details.
- `my projects` - Lists projects.
- `what internship` - Provides internship information.

#### Applications:
- `open Chrome`, `open YouTube`, `open Notepad`, `open Calculator`, `open Word`.

#### Fun:
- `joke` - Tells a joke.

#### Exit:
- `stop` - Ends the program.

---

### Customization
- **Personal Details**: Update personal details, projects, and internship information in the script for a personalized experience.
- **Add New Commands**: To add more applications or commands, expand the `open_application()` function and the `run_assistant()` command processing section with new cases.

---

### Error Handling
- **Timeouts**: Adjust the timeout duration in the `take_command` function as needed.
- **Unknown Commands**: If the command isn’t recognized, Naari will ask you to repeat it.
- **Error Messages**: Common errors are handled, and Naari provides feedback if an issue occurs.

---

### License
This project is licensed under the MIT License.
