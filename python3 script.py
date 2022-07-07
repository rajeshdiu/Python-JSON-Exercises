import json
import googletrans
from googletrans import Translator

myjsonFile= open('json.json', 'r')
data=myjsonFile.read()
obj = json.loads(data)
print(type(obj))
print(obj)
print(obj.keys())
print(obj.values())
print(str(obj["text"]))
obj["languages"][0]

print(obj["languages"][1:4])

list=obj["languages"]
print(list)
print(len(list))
s = list
for i in range(len(s)):
    s[i] = s[i].lower()
print(s)

translator = Translator()

print(googletrans.LANGUAGES)
lan_key=googletrans.LANGUAGES.keys()
print(lan_key)

lan_val=googletrans.LANGUAGES.values()
print(lan_val)

print(translator.detect(obj["text"]))

out=translator.translate(obj["text"],dest="bn")
print(out.text)
out=translator.translate(obj["text"],dest="zh-cn")
print(out.text)
out=translator.translate(obj["text"],dest="ja")
print(out.text)
out=translator.translate(obj["text"],dest="hi")
print(out.text)

book=json.dumps(out, sort_keys=True, indent=4)
