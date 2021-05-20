# -*- coding: utf-8 -*-
import json

with open("labels_to_name.json", "r") as read:
    
    data=json.load(read)

divisor = 100
total = len(data)
average = round(total/divisor)
incrimentor = 0

new_file ={}
for i in range(0,average):
    new_file[f"{incrimentor+1} - {divisor*(i+1)}"] = data[f"{incrimentor}"]
    incrimentor +=divisor 
    
with open('new_file.json', 'w') as outfile:
   json.dump(new_file, outfile)
