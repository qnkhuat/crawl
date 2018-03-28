import json_lines as jl

with open('dic.jl') as f:
    data= jl.reader(f)
    for line in data:
        txt= open('dic.txt','a')
        txt.write(line['vin'] + '\n')

with open('dic2.jl') as f:
    data= jl.reader(f)
    for line in data:
        txt= open('dic.txt','a')
        txt.write(line['vin'] + '\n')
