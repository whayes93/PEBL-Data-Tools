'''opens PEBL Stroop data in csv format and calculates mean 
congruent, incongruent, and neutral latencies filtering out 
incorrect responses'''

#User enters file path for program to retrieve dataset 
#***MUST BE IN .CSV FORMAT***
path = input('Enter file path:')

#Creates file object and creates a list of lists 
data = open(path) 
lines = []
for line in data:
    separated = line.split(',')
    lines.append(separated)

#Gets rid of labels in top row of dataset 
lines.pop(0)

neut = []
inc = []
cong = []

#Classifies trials according to trial type (excludes practice trials)
for line in lines:
    if line[6] == 'N' and int(line[3]) != 0:
        neut.append(line)
    elif line[6] == 'I' and int(line[3]) != 0:
        inc.append(line)
    elif line[6] == 'C' and int(line[3]) != 0:
        cong.append(line)

#Excludes incorrect responses and missing responses         
Ncorrect = [line for line in neut if int(line[9]) == 1 and int(line[7]) ==1]
Icorrect = [line for line in inc if int(line[9]) == 1 and int(line[7]) ==1]
Ccorrect = [line for line in cong if int(line[9]) == 1 and int(line[7]) ==1]

#Extracts RTs
NRT = round(sum([int(line[11]) for line in Ncorrect])/len(Ncorrect), 3)
IRT = round(sum([int(line[11]) for line in Icorrect])/len(Icorrect), 3)
CRT = round(sum([int(line[11]) for line in Ccorrect])/len(Ccorrect), 3)

#***SAVE IN .TXT FORMAT***
outpath = input('Enter path of file-to-be-saved:')

summary = open(outpath, 'a')

summary.write('''Adjusted summary data for %r:\n
Ncorrect: %r\nIcorrect: %r\nCcorrect: %r\n
NRaw: %r\nIRaw: %r\nCRaw: %r\n
Congruent RT: %r\nIncongruent RT: %r\nNeutral RT: %r\n
NErrors: %r\nIErrors: %r\nCErrors: %r\n''' %(path, len(Ncorrect), len(Icorrect), len(Ccorrect), 
len(neut), len(inc), len(cong), CRT, IRT, NRT,(len(neut)-len(Ncorrect)), (len(inc)-len(Icorrect)), (len(cong)-len(Ccorrect))))


print('Congruent RT: %r\nIncongruent RT: %r\nNeutral RT: %r\n' %(CRT, IRT, NRT))
print('Ncorrect: %r\nIcorrect: %r\nCcorrect: %r\n' %(len(Ncorrect), len(Icorrect), len(Ccorrect)))
print('NRaw: %r\nIRaw: %r\nCRaw: %r\n' %(len(neut), len(inc), len(cong)))
print('NErrors: %r\nIErrors: %r\nCErrors: %r\n' %((len(neut)-len(Ncorrect)), (len(inc)-len(Icorrect)), (len(cong)-len(Ccorrect))))

data.close(); summary.close() 

