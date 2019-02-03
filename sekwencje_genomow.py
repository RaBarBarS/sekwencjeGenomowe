import sys

def complement (seq):
    outputseq=[]
    dictio1={
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
    }
    for letter in seq:
        outputseq.append(dictio1[letter])
    return(outputseq)

def reverseComplement (seq):
    dna = complement (seq)
    dna = list(dna)
    dna.reverse()

    dnarev = ''

    for i in dna:
        dnarev = dnarev + i

    dna = ''
    return dnarev

print(sys.argv)
filename = sys.argv[1]
file1 = open(filename, 'r').read()
lines = file1.split('\n')
dictio={}

for line in lines:
    if line.startswith('>'):
        helpline = line.split()[0].lstrip('>')
        dictio[helpline]=''
    else:
        line.strip('\n')
        dictio[helpline] += line

#file1.close()
filename = sys.argv[2]
file1 = open(filename, 'r').read()
lines = file1.split('\n')

slowo = sys.argv[3]

file2 = open('plik3.txt', 'w')

for line in lines:
    if line.startswith('contig'):
        line = line.split()
        if slowo == line[2]:
            file2.write('>' + line[0] + '|' + line[2] + '|')
            line[9] = line[9].lstrip('"').rstrip(';').rstrip('"')
            file2.write(line[9] + '|' + line[3] + ':' + line[4] + '|' + '-\n')
            helpline = reverseComplement(dictio[line[0]][int(line[3]):int(line[4])])
            while len(helpline) > 60:
                file2.write(helpline[0:60] + '\n')
                helpline = helpline[60:len(helpline)]
            file2.write(helpline[0:60] + '\n')