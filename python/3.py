instr="<<<한<글<< <<<Python>>> 프로>>>>그래밍>>>>"
outstr=""

for i in range(0,len(instr)):
    if instr[i]!="<" and instr[i]!=">":
        outstr+=instr[i]
print("원래 문자열 -->"+'['+instr+']')
print("공백 문자열 -->"+'['+outstr+']')