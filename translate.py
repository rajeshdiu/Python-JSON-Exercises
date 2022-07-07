import googletrans
from googletrans import Translator


text1="Hello"
text2="How are you"

trans=Translator()

print(trans.detect(text1))