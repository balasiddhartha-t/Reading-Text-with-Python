# Import the required module for text 
# to speech conversion
from gtts import gTTS

import os
# The text that you want to convert to audio
mytext = 'This is used to read this line of code'
 
# Language in which you want to convert
#List of languages that are available are
#* 'af' : 'Afrikaans'
#* 'sq' : 'Albanian'
#* 'ar' : 'Arabic'
#* 'hy' : 'Armenian'
#* 'bn' : 'Bengali'
#* 'ca' : 'Catalan'
#* 'zh' : 'Chinese'
#* 'zh-cn' : 'Chinese (Mandarin/China)'
#* 'zh-tw' : 'Chinese (Mandarin/Taiwan)'
#* 'zh-yue' : 'Chinese (Cantonese)'
#* 'hr' : 'Croatian'
#* 'cs' : 'Czech'
#* 'da' : 'Danish'
#* 'nl' : 'Dutch'
#* 'en' : 'English'
#* 'en-au' : 'English (Australia)'
#* 'en-uk' : 'English (United Kingdom)'
#* 'en-us' : 'English (United States)'
#* 'eo' : 'Esperanto'
#* 'fi' : 'Finnish'
#* 'fr' : 'French'
#* 'de' : 'German'
#* 'el' : 'Greek'
#* 'hi' : 'Hindi'
#* 'hu' : 'Hungarian'
#* 'is' : 'Icelandic'
#* 'id' : 'Indonesian'
#* 'it' : 'Italian'
#* 'ja' : 'Japanese'
#* 'km' : 'Khmer (Cambodian)'
#* 'ko' : 'Korean'
#* 'la' : 'Latin'
#* 'lv' : 'Latvian'
#* 'mk' : 'Macedonian'
#* 'no' : 'Norwegian'
#* 'pl' : 'Polish'
#* 'pt' : 'Portuguese'
#* 'ro' : 'Romanian'
#* 'ru' : 'Russian'
#* 'sr' : 'Serbian'
#* 'si' : 'Sinhala'
#* 'sk' : 'Slovak'
#* 'es' : 'Spanish'
#* 'es-es' : 'Spanish (Spain)'
#* 'es-us' : 'Spanish (United States)'
#* 'sw' : 'Swahili'
#* 'sv' : 'Swedish'
#* 'ta' : 'Tamil'
#* 'th' : 'Thai'
#* 'tr' : 'Turkish'
#* 'uk' : 'Ukrainian'
#* 'vi' : 'Vietnamese'
#* 'cy' : 'Welsh'
language = 'en'
 

myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("NewAudioFile.mp3")

os.system("mpg123 NewAudioFile.mp3")