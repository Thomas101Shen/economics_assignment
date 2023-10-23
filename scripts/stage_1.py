import pandas as pd

# This script will turn all .dta files into .csv files

def preFCS():
	# This function will convert the 05-08 pre fcs data into a csv file
	data = pd.io.stata.read_stata('./data_files/raw_data/Turkey2005_2008_panel.dta')
	data.to_csv('./data_files/stage_1/PreFCS.csv')

def FCS():
	# This function will convert the 09-10 fcs data into a csv file
	data = pd.io.stata.read_stata('./data_files/raw_data/Turkey-2010-FCS-full data-.dta')
	data.to_csv('./data_files/stage_1/FCSrd3.csv')

	data = pd.io.stata.read_stata('./data_files/raw_data/Turkey-2010-FCS w3-full data-.dta')
	data.to_csv('./data_files/stage_1/FCSrd2.csv')

	data = pd.io.stata.read_stata('./data_files/raw_data/Turkey-2009-FCS-full-data-.dta')
	data.to_csv('./data_files/stage_1/FCSrd1.csv')

def timeline():
	# This function will convert the 08-13-19 data into a csv file
	data = pd.io.stata.read_stata('./data_files/raw_data/Turkey_2008_2013_2019.dta', convert_categoricals=False)
	data.to_csv('./data_files/stage_1/timeline.csv')

if __name__=='__main__':
	# preFCS()
	# FCS()
	timeline()
	print("Complete")