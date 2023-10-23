import pandas as pd

# This script will add/drop columns for each of the CSV files

def FCS():

	# This function will add years to the FCS data
	# 20101 denotes first round of 2010 (2nd wave)
	# 20102 denotes second round of 2010 (3rd wave)
	data = pd.read_csv('./data_files/stage_1/FCSrd1.csv')
	data['year']=2009
	data.to_csv('./data_files/stage_2/FCSrd1.csv')

	data = pd.read_csv('./data_files/stage_1/FCSrd2.csv')
	data['year']=20101
	data.to_csv('./data_files/stage_2/FCSrd3.csv')

	data = pd.read_csv('./data_files/stage_1/FCSrd3.csv')
	data['year']=20102
	data.to_csv('./data_files/stage_2/FCSrd2.csv')

def preFCS():
	# This function will select all columns we want in the final data from pre FCS data

	data = pd.read_csv('./data_files/stage_1/PreFCS.csv')

	columns=['a0', 'a2', 'a3', 'a4', 'a6', 'a7', 'a8', 'a9', 'a10',
	'a11', 'a12', 'a13', 'a14', 'q1', 'q8', 'q6', 'q72', 'q73', 'q74',
	'q75', 'p4', 'p5', 'p7', 'p8', 'p3', 'q29', 'q30', 'q31',
	'q13', 'q14', 'q2', 'q3','q26', 'q27', 'q28', 'q25', 'q33','p1', 'q22'
	'q23', 'q24', 'q76', 'q77', 'q82', 'q21', 'q41', 'q42', 'q43', 'q45',
	'q46', 'q57', 'q47', 'q48', 'q49', 'q50', 'q39', 'q40', 'q77', 'a8', 'q67',
	'q76', 'q77', 'q60', 'j30']

	matching_columns = match_columns(data.columns, columns)
	df = data[matching_columns]
	df.to_csv('./data_files/stage_2/PreFCS.csv')

def timeline():
	# this function will drop all columns we don't want in the final data from timeline data

	data = pd.read_csv('./data_files/stage_1/timeline.csv')

	columns=['c12', 'c13', 'c14', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd17', 'd30', 'w', 'i'
	'q3', 'j', 'b20', 'a18', 'a19', 'o9']

	matching_columns = match_columns(data.columns, columns)

	# we want to keep j30 in the final set so we will employ the following trick

	j_columns = [col for col in data.columns if 'j30' in col[:3]]

	matching_columns = set(matching_columns)

	for j in j_columns:
		matching_columns.remove(j)

	fin_data=data.drop(columns=matching_columns)

	# fin_data.to_csv('./data_files/stage_2/timeline_Test.csv')

	# for j30 in j_columns:
	# 	fin_data=data.assign(j30=data[j30])

	fin_data.to_csv('./data_files/stage_2/timeline.csv')


def match_columns(cols: list, to_match: list):
	matching_columns = []
	for col_name in to_match:
		matching_columns.extend([col for col in cols if col_name in col[:len(col_name)]])
	return matching_columns

if __name__ == '__main__':
	FCS()
	preFCS()
	timeline()
