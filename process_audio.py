import sys
import os
import speech_recognition as sr
from pydub import AudioSegment

def process_audio(file_path):
    # Convert audio file to WAV format if it's not already
    if not file_path.endswith('.wav'):
        audio = AudioSegment.from_file(file_path)
        file_path = file_path.replace('.mp3', '.wav')
        audio.export(file_path, format='wav')

    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(file_path) as source:
            # Record audio
            audio_data = recognizer.record(source)
            
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print(f"Recognized Text: {text}")
            return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Google Speech Recognition request error; {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_audio.py <audio_file>")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    if not os.path.isfile(audio_file):
        print(f"File not found: {audio_file}")
        sys.exit(1)
    
    # Process the audio file and print the result
    result = process_audio(audio_file)
    print(result)
