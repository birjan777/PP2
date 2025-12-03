import csv

filename = ('users.csv')
with open (filename, 'w')as csvfile:
    csv_writer = csv.writer(csvfile)
    print("CSV created")