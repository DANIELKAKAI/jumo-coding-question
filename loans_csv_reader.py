import csv

from shutil import copyfile


def csv_handler(input_filename,output_filename):
	loan_total = 0
	loan_count = 0

	#reads the loans csv
	with open(input_filename,newline='') as loans_csv:
		reader = csv.DictReader(loans_csv)
		for row in reader:
			loan_count += 1
			loan_total += float(row['Amount'])

	#copy the contents from loans csv to output csv
	copyfile(input_filename,output_filename)

	#append a line that has loan count and total to output csv
	with open(output_filename,'a',newline='') as output_csv:
		writer = csv.DictWriter(output_csv,fieldnames=['MSISDN','Network','Date','Product','Amount'])
		writer.writerow({'MSISDN':'','Network':'','Date':'','Product':loan_count,'Amount':loan_total})


if __name__=="__main__":
	csv_handler('Loans.csv','Output.csv')
		