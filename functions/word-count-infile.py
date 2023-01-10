from os import strerror

source_file_name = input("Ingresa el nombre del archivo fuente: ")
try:
    source_file = open(source_file_name, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)	

content = source_file.read().lower()
dictionary = {}

for i in range(26):
    order = 97
    dictionary[chr(order + i)] = 0
    # dictionary['a' + chr(i)] = 0 # Alternative dictionary generation
    i += 1

counter = 0
result = {}
for i in content:
	if chr(i) in dictionary:
		dictionary[chr(i)] += 1
		counter += 1
for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True):
    if v > 0:
            result[k] = v

openme = open('openme.hist', 'wt')
for k, v in result.items():
	newline = '\n'
	line = k + " -> " + str(v) + newline
	openme.write(line)
	
openme.close() 
