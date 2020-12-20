# Text-to-Speech
# This script generates a voice for given text input 
from gtts import gTTS

text_en = 'A voice demo for source speaker'
text_tr = 'Kaynak konuşmacı için ses denemesi'

tts_en = gTTS(text_en, lang='en')
tts_tr = gTTS(text_tr, lang='tr')

tts_en.save('source/source_female_google_en.mp3')
tts_tr.save('source/source_female_google_tr.mp3')
