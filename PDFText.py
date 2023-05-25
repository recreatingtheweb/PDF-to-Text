# importing the modules
from pypdf import PdfReader
import pyttsx3

# path of the PDF file
path = open('Resume.pdf', 'rb')

# creating a PdfFileReader object
reader = PdfReader(path)

# select the first page
page = reader.pages[0]

print(page.extract_text())

# extract the text from the PDF
text = page.extract_text()

# reading the text
engine = pyttsx3.init()

# getting details of current speaking rate
rate = engine.getProperty('rate')   

 # setting up new voice rate out of 200
engine.setProperty('rate', 150) 

#getting details of current voice
voices = engine.getProperty('voices')       

#Setting voice to female
engine.setProperty('voice', voices[1].id)

#Save speach to text file
engine.save_to_file(text, 'test.mp3')

#Start speach audio
engine.say(text)
engine.runAndWait()
