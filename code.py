a = input('enter the name of a doctor or specialization: ')
b = a.lower()
import csv
with open ('dr.csv','r') as csvfile:
	reader = csv.DictReader(csvfile)
	for i in reader:
		if b in i.values():


			d = i.get('name')
			e = i.get('Eduction')
			f = i.get('Experience')
			h = i.get('specialist')
			g = i.get('fees')
			print('name --> '+ 'Dr.'+ d)
			print('Eduction --> ' + e)
			print('Experience --> ' + f)
			print('fees --> ' + g)
			print('specialization --> '+ h )
		


from datetime import datetime as dt
p = dt.now()
s = input('\nenter yes to book an appointment: ')
x = s.lower()
if x == 'yes':
	print('\nyour appointment has been confirmed\n')
	print('the details of the booking are:')
	print('name --> '+ 'Dr.'+ d)
	print('Eduction --> ' + e)
	print('Experience --> ' + f)
	print('fees --> ' + g)
	print('specialization --> '+ h)
	print('time of booking')
	print(p) 
else:
	print('No Booking Made')


print('\nTHANK YOU')