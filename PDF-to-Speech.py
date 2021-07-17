"""
API REFERENCE DOCUMENTATION LINK: https://googleapis.dev/python/texttospeech/latest/index.html
Google Cloud Text-To-Speech API Combined with PDF API
Usage: Run this in the console rather than from your IDE itself
"""

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="x"
# Replace the x in the string to the location to where the json file containing your key is
# e.g. "/home/user/Downloads/service-account-file.json"

from google.cloud import texttospeech

import PyPDF2
 
# creating a pdf file object
pdfFileObj = open('insert name of pdf.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

current_page = input("What page?")
# creating a page object
pageObj = pdfReader.getPage(current_page)
# extracting text from page
page = pageObj.extractText())



# Instantiates the text to speech client

client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text = page)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("female")
voice = texttospeech.VoiceSelectionParams(
language_code = 'en-US',
name = 'en-US-Wavenet-B',
ssml_gender = texttospeech.SsmlVoiceGender.FEMALE)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
audio_encoding = texttospeech.AudioEncoding.MP3,
speaking_rate = 2.0)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
input=synthesis_input, voice=voice, audio_config=audio_config
)

pdfFileObj.close()

with open('output.mp3', 'wb') as out:
# Write the response to the output file.
out.write(response.audio_content)
print('Audio content written to file "output.mp3"')
