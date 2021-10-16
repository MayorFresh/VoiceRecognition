import speech_recognition as sr
import random
import pyttsx3

class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.speaker = pyttsx3.init()

    def __speaker_config(self):
        self.speaker.setProperty('rate', 160)
        self.speaker.setProperty('volume', 1)
        for voice in self.speaker.getProperty('voices'):
            if voice.name == 'Alex': # Change this to Samantha for a female voice
                self.speaker.setProperty('voice', voice.id)
                break

    def configure(self):
        print("List of microphones connected to your system:")
        mic_list = sr.Microphone.list_microphone_names()
        for index, name in enumerate(mic_list):
            print(f"{index} - {name}")
        choice = int(input("\nEnter the number of the microphone you want to use: "))
        fail_count = 0
        while choice not in range(len(mic_list)):
            if fail_count == 5:
                print("Program exiting...")
                return
            print("Please enter a valid number.")
            choice = int(input("\nEnter the number of the microphone you want to use: "))
            fail_count += 1
            self.microphone = sr.Microphone(device_index=choice)
        # Configure the speech recognition engine
        self.__speaker_config()
        self.speak(random.choice(["Say something", "Say something now", "Hello, what can I do for you?"]))

    def __get_words(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn't get that."
        except sr.RequestError as e:
            return "Sorry, my speech service is down."
    
    def speak(self, text):
        self.speaker.say(text)
        self.speaker.runAndWait()

    def listen(self):
        user_input = self.__get_words().lower()
        response = self.evaluate(user_input)
        self.speak(response)
        if response.lower() in ["goodbye", "bye", "see you later", "see you later!"]:
            self.close()
            return
        self.listen()

    def evaluate(self, user_input):
        # Add more commands
        if user_input in ["hello", "hi", "hey", "what's up", "what's up?"]:
            return random.choice(["Hello", "Hi", "Hey", "What's up", "What's up?"])
        elif user_input in ["goodbye", "bye", "see you later", "see you later!"]:
            return random.choice(["Goodbye", "Bye", "See you later", "See you later!"])
        elif user_input in ["what is your name", "what is your name?"]:
            return random.choice(["My name is Jarvis", "My name is Jarvis and I am your personal assistant"])
        elif user_input in ["what is your purpose", "what is your purpose?"]:
            return random.choice(["My purpose is to assist you in your daily life", "My purpose is to keep you updated on your daily life"])
        elif user_input in ["what is your favorite color", "what is your favorite color?"]:
            return random.choice(["My favorite color is blue", "My favorite color is red", "My favorite color is green"])
        elif user_input in ["what is your favorite food", "what is your favorite food?"]:
            return random.choice(["My favorite food is pizza", "My favorite food is pizza"])
        elif user_input in ["what is your favorite movie", "what is your favorite movie?"]:
            return random.choice(["My favorite movie is The Matrix", "My favorite movie is The Matrix"])
        elif user_input in ["what is your favorite song", "what is your favorite song?"]:
            return random.choice(["My favorite song is The Sign", "My favorite song is The Sign"])
        elif user_input in ["what is your favorite sport", "what is your favorite sport?"]:
            return random.choice(["My favorite sport is soccer", "My favorite sport is basketball"])
        else:
            return random.choice(["I didn't get that", "I don't know what that means", "Can you repeat that please?", "Say that again please"])

    def close(self):
        exit()
        
        
if __name__ == "__main__":
    speech = SpeechRecognition()
    speech.configure()
    speech.listen()