import json

with open('mahasiswa.json') as mhs:
	data = json.load(mhs)

print(data)	