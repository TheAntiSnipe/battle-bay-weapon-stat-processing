import pandas as pd

def write_dataframe_to_file(dataframe_to_write, filename,index_flag):
    data = open(filename, 'w')
    data.write(dataframe_to_write.to_csv(
        index=index_flag, line_terminator='\n'))
    data.close()
    #! Writes to file without indices and empty spaces.

def main():
    original_dataframe=pd.read_csv('skills-r-1159.csv')
    original_dataframe.dropna(subset=['FlightTime'], inplace=True)
    # Drop the data of all weapons whose flight time is not applicable.

    flighttime_data=original_dataframe[['ID','FlightTime']]
    final_sorted_dataframe = flighttime_data.sort_values(by=['FlightTime'])
    #Select weapon name and sort it by the column 'FlightTime'
    
    write_dataframe_to_file(final_sorted_dataframe,'flighttime-data.csv',False)

if(__name__=='__main__'):
    main()