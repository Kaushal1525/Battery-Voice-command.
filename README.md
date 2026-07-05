
# Python Voice Assistant

## Overview

Python Voice Assistant is a desktop-based virtual assistant developed using Python. The application uses speech recognition to capture voice commands, processes user requests, and responds through text-to-speech synthesis. It can search Google, play YouTube videos, retrieve information from Wikipedia, and open commonly used websites.

The project demonstrates the integration of speech recognition, natural language processing, web automation, and voice synthesis to create an interactive voice-controlled assistant.

---

## Features

- Voice command recognition
- Text-to-speech responses
- Google search
- YouTube playback
- Wikipedia information retrieval
- Website launching
- Continuous listening mode
- Voice-based application control
- Graceful error handling
- Stop command to terminate the assistant

---

## Technologies Used

- Python 3
- SpeechRecognition
- PyAudio
- pyttsx3
- Wikipedia API
- PyWhatKit
- Webbrowser Module

---

## Project Structure

```text
Python-Voice-Assistant/
│
├── voice_assistant.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Kaushal1525/Python-Voice-Assistant.git
```

### Navigate to the project directory

```bash
cd Python-Voice-Assistant
```

### Install the required packages

```bash
pip install -r requirements.txt
```

or install manually:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install wikipedia
pip install pywhatkit
pip install PyAudio
```

---

## Running the Project

Execute the following command:

```bash
python voice_assistant.py
```

The assistant will begin listening through your system microphone.

Speak a supported command to interact with the assistant.

To terminate the program, simply say:

```text
stop
```

or press:

```text
Ctrl + C
```

---

## Supported Voice Commands

### Google Search

```text
Search for Artificial Intelligence
```

### Play a YouTube Video

```text
Play Believer song
```

### Open Websites

```text
Open Google
```

```text
Open YouTube
```

```text
Open Instagram
```

```text
Open GPT
```

### Search on Google

```text
Open Machine Learning on Google
```

### Wikipedia Queries

```text
Who is Alan Turing
```

```text
What is Artificial Intelligence
```

### Exit the Assistant

```text
Stop
```

---

## Working Principle

1. Capture audio using the system microphone.
2. Convert speech into text using Google Speech Recognition.
3. Identify the requested command.
4. Execute the corresponding task.
5. Respond to the user through text-to-speech.
6. Continue listening until the stop command is received.

---

## Modules Used

### SpeechRecognition

Captures audio input and converts spoken language into text.

### pyttsx3

Provides offline text-to-speech functionality for voice responses.

### Wikipedia

Retrieves concise summaries from Wikipedia.

### PyWhatKit

Performs Google searches and plays YouTube videos.

### Webbrowser

Launches supported websites in the default web browser.

---

## Error Handling

The application handles several common situations including:

- Unrecognized speech
- Microphone timeout
- Internet connectivity issues
- Wikipedia page not found
- Ambiguous Wikipedia results
- Unsupported commands

---

## Future Enhancements

- Wake word detection
- Integration with ChatGPT
- Local large language model support
- Weather information
- News updates
- Email automation
- Calendar management
- Smart home device control
- Voice authentication
- Multi-language support
- Desktop application interface
- Offline speech recognition
- AI-powered conversational capabilities

---

## Applications

- Personal desktop assistant
- Educational assistant
- Voice-controlled computing
- Accessibility support
- Productivity automation
- Smart workstation assistant
- AI learning projects
- Human-computer interaction research

---

## Requirements

- Python 3.8 or later
- Microphone
- Internet connection (for speech recognition and web services)

---

## Dependencies

- SpeechRecognition
- PyAudio
- pyttsx3
- wikipedia
- pywhatkit

---

## Author

Kaushal Reddy

AI & Autonomous Systems Engineer

GitHub: https://github.com/Kaushal1525
````
