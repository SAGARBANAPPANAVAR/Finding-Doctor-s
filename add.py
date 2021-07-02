import csv
fields = {'name','specialist','Eduction','Experience','Available','fees'}
rows = ({'name':'sagar','specialist':'dentist','Eduction':'MDS','Experience':'3 Years','Available':'yes','fees':'200rs'},
		{'name':'vishal','specialist':'general surgoen','Eduction':'MBBS','Experience':'2 Years','Available':'only on monday and wednesday','fees':'350rs'},
		{'name':'prajwal','specialist':'ent specialist','Eduction':'MBBS','Experience':'5 Years','Available':'on 21st may','fees':'300rs'},
		{'name':'prajwal','specialist':'dentist','Eduction':'BDS','Experience':'7 Years','Available':'currently not Available','fees':'300rs'})



with open ('dr.csv','w',newline='') as csvfile:
	writer = csv.DictWriter(csvfile,fieldnames=fields)
	writer.writeheader()
	for row in rows:
		writer.writerow(row)