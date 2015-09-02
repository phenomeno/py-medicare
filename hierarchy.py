def input_file(input_csv_name, list_name):
	import csv
	
	with open(input_csv_name, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			list_name.append(row)
		
def output_dict(output_csv_name, dictionary_name):
	import csv
	
	with open(output_csv_name, 'wb') as g:
		writer = csv.writer(g)
		for row in dictionary_name:
			writer.writerow([row] + dictionary_name[row])


def hcc(member_cc_list, output_hcc_dictionary):
	#import csv
	
	#member_dict = [];
	
	#with open(input_filename, 'rb') as f:
	#reader = csv.reader(f)
	#for row in reader:
	#	member_dict.append(row)
		
	
	def hier(row, hcc, *drop):
		if hcc in row:
			b = []
			if row[0] not in dictionary:
				dictionary[row[0]] = list()
			#for i in [i for i,z in enumerate(cc) if z==hcc]:
			#	pos = i
			dictionary[row[0]].append(hcc)
			#dictionary[row[0]].append(row[pos+1])
			#b.append(row[0]+"_"+hcc+row[pos])
			for x in drop:
				if x in row:
					b.append(x)
			for y in b:
				dictionary[row[0]].append(y)
				#pos2='2ndplaceholder'
				#for i in [i for i,z in enumerate(row) if z==y]:
				#	pos2 = i
				#dictionary[row[0]].append(row[pos2+1])

				#a.append(row[0]+'_'+hcc+row[pos+1]+ '__'+ row[0]+'_'+y+row[pos2+1])

	#a = []
	dictionary ={}
	
	for row in member_cc_list:
		# for 2014 hcc hierarchy, found in 2014 cms announcement pg 73
		hier(row, '3', '4')
		hier(row, '8', '9', '10', '11', '12', '13')
		hier(row, '9', '10', '11', '12', '13')
		hier(row, '10', '11', '12', '13')
		hier(row, '11', '12', '13')
		hier(row, '12', '13')
		hier(row, '18', '19', '20', '21', '46', '47')
		hier(row, '19', '20', '21')
		hier(row, '20', '21')
		hier(row, '34', '35', '36', '37', '38')
		hier(row, '35', '36', '37', '38')
		hier(row, '36', '37')
		hier(row, '41', '45', '48')
		hier(row, '42', '45')
		hier(row, '46', '47')
		hier(row, '54', '55')
		hier(row, '56', '57')
		hier(row, '66', '75')
		hier(row, '67', '75')
		hier(row, '68', '69', '74', '75')
		hier(row, '70', '71')
		hier(row, '73', '74')
		hier(row, '81', '82')
		hier(row, '87', '88', '89', '90', '102', '103')
		hier(row, '88', '89', '90', '102', '103')
		hier(row, '89', '90', '102', '103')
		hier(row, '96', '97')
		hier(row, '102', '90', '103')
		hier(row, '103', '90')
		hier(row, '106', '107', '108', '109', '110', '150', '151')
		hier(row, '107', '109', '110', '150', '151')
		hier(row, '108', '109', '110', '151')
		hier(row, '109', '110', '151')
		hier(row, '112', '113')
		hier(row, '125', '126', '127')
		hier(row, '126', '127')
		hier(row, '128', '129', '130')
		hier(row, '129', '130')
		hier(row, '131', '132')
		hier(row, '137', '138', '139')
		hier(row, '138', '139')
		hier(row, '145', '146', '149')
		hier(row, '150', '151')
		hier(row, '153', '217', '254')
		hier(row, '158', '159', '160', '161', '162')
		hier(row, '159', '160', '161')
		hier(row, '160', '161')
		hier(row, '162', '161')
		hier(row, '183', '184', '187', '188')
		hier(row, '184', '187', '188')
		hier(row, '187', '188')
		hier(row, '203', '204', '205')
		hier(row, '204', '205')
		hier(row, '207', '203', '204', '205', '208', '209')
		hier(row, '208', '209')
		hier(row, '226', '227')
		hier(row, '242', '243', '244', '245', '246', '247', '248', '249')
		hier(row, '243', '244', '245', '246', '247', '248', '249')
		hier(row, '244', '245', '246', '247', '248', '249')
		hier(row, '245', '246', '247', '248', '249')
		hier(row, '246', '247', '248', '249')
		hier(row, '247', '248', '249')
		hier(row, '248', '249')



