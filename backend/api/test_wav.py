from vosk import Model, KaldiRecognizer, SetLogLevel, GpuInit, GpuThreadInit
import sys
import os
import wave
import json
RELATIVEMODELPATH = './backend/api/model/'


SetLogLevel(0)

if not os.path.exists(RELATIVEMODELPATH):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

GpuInit()
model = Model("model")

rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

resulting_dict = {}
i = 0
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        temp = rec.Result()
        print(temp)
        resulting_dict[i] = json.loads(temp)
        i += 1
    else:
        print(rec.PartialResult())
 
resulting_dict[i] = json.loads(rec.FinalResult())

with open(file=f"{sys.argv[2]}", mode="w", encoding="utf-8") as f:
    f.write(json.dumps(resulting_dict))
print(resulting_dict)

"""with open(file=f"{sys.argv[2]}", mode="w", encoding="utf-8") as f:
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            temp = rec.Result()
            print(temp)
            f.write(temp)
        else:
            print(rec.PartialResult())
            

    f.write(rec.FinalResult())
    
f.close()"""