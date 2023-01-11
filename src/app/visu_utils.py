import pandas as pd
import glob
import re

def map_time_slice(time_range):
    """
    Get the time slice used to compute the score and return the mean year to choose the position of the cloud on the graph.
    """
    start, end = time_range.split("-")
    mean_year = str(round((int(start)+int(end))/2))
    return mean_year
    

def read_results_one_period(res_file):
    """
    :str: res_file : CSV output of measure_semantic_shift.py

    Read the CSV file from the measure_semantic_shift.py and wrap it into a nice formatted dataframe for the visualization.
    """

    fill_color = { "gold": "#efcf6d", "silver": "#cccccc", "bronze": "#c59e8a" }

    df = pd.read_csv(res_file)
    nb_words = df['word'].size
    
    # Find the time slice and change it into a single year that match our predefined axis
    time_slice = re.findall("\d+-\d+",df.columns[1])[0]  #'1910-1950'
    year = map_time_slice(time_slice)  # TODO parse this info in the file name, in measure_semantic_shift
    
    # Rename the column name of the metric we want to display on the graph for easier use
    df.rename(columns={f'MEANING GAIN/LOSS {time_slice}':'Score'}, inplace=True)
    
    for i in range(nb_words):
        # TODO need to have a nice cloud, so we need to modulate a bit the year
        df['Year'] = year
        # TODO rm 
        df['Color'] = fill_color['gold']

    return df 

def results_all_periods(folder_path):
    """
    :str: folder_path : folder with all the csv files dumped by measure_semantic_shift.py

    Collect all the dataframes from all time slices and create the final huge dataframe to feed to the visualization. 
    """

    list_files = glob.glob(folder_path + "*.csv")
    #df1 = pd.read_csv('/home/mathilde/Documents/S9 Project/sandbox/src/ex_res_shift.csv') # TODO rm, juste pour les examples
    #df2 = pd.read_csv('/home/mathilde/Documents/S9 Project/sandbox/src/ex_res_shift.csv') # TODO rm, juste pour les examples
    full_results = []  #[df1, df2]  # TODO rm
    for f in list_files: 
        df = read_results_one_period(f)
        full_results.append(df)
    
    df_full = pd.concat(full_results)

    return df_full
