import pandas as pd
import pyreadstat as read_stat
import os

# This last and final script will combine all csv files into one .dta file and one .csv file

def main():
	file_path='./data_files/stage_2/'
	file_list=os.listdir(file_path)
	final_data=pd.concat([pd.read_csv('./data_files/stage_2/'+f) for f in file_list], ignore_index=True)
	# print('unnamed column is: '+final_data.columns[0])
	final_data.to_csv('./data_files/final_data/final_data.csv')
	# read_stat.write_dta(final_data, './data_files/final_data/final_data.dta')

if __name__ == '__main__':
	main()