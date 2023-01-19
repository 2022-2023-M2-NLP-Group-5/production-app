import pandas as pd
import glob
import re
import random

def map_time_slice(time_range):
    """
    Get the time slice used to compute the score and return the mean year to choose the position of the cloud on the graph.
    """
    start, end = time_range.split("-")
    #mean_year = str(round((int(start)+int(end))/2))
    year = str(random.randint(int(start), int(end)))
    return year #mean_year
    

def read_results_one_period(res_file, tg_word):
    """
    :str: res_file : CSV output of measure_semantic_shift.py

    Read the CSV file from the measure_semantic_shift.py and wrap it into a nice formatted dataframe for the visualization.
    """

    fill_color = { "gold": "#efcf6d", "silver": "#cccccc", "bronze": "#c59e8a" }
    color_text = { "black": "#000000", "red": "#cc0000"}

    df = pd.read_csv(res_file)
    nb_words = df['word'].size
    
    # Find the time slice and change it into a single year that match our predefined axis
    time_slice = re.findall("\d+-\d+",df.columns[1])[0]  #'1910-1950'
    #year = map_time_slice(time_slice)
    
    # Rename the column name of the metric we want to display on the graph for easier use
    # TODO dump the columns that are useless 
    df.rename(columns={f'MEANING GAIN/LOSS {time_slice}':'Score'}, inplace=True)
    df['Year'] = None
    df['Color'] = fill_color['gold']
    df['Size'] = 10
    df['TextColor'] = color_text['black']
    # TODO change the None after the tests 
    df["Parent"] = None

    # Special treatment for the target word
    start, end = time_slice.split("-")
    mean_year = str(round((int(start)+int(end))/2))
    # TODO correct with the new column 
    df.loc[nb_words] = [tg_word, None, None, None, None, None, None, None, None, None, None, None, None, None, 0, None, None, mean_year, fill_color['silver'], 20, color_text['red']]
    

    for i in range(nb_words):
        # We need to have a nice cloud, so we need to modulate a bit the year, I choose it randomly within the time range
        year = map_time_slice(time_slice)
        df['Year'][i] = year

    return df 

def results_all_periods(folder_path, tg_word):
    """
    :str: folder_path : folder with all the csv files dumped by measure_semantic_shift.py

    Collect all the dataframes from all time slices and create the final huge dataframe to feed to the visualization. 
    """
    print("Retrieving files from ", folder_path)
    list_files = glob.glob(folder_path + "*.csv")
    [print(f) for f in list_files]
    full_results = []
    for f in list_files: 
        df = read_results_one_period(f, tg_word)
        full_results.append(df)
    
    df_full = pd.concat(full_results)

    return df_full




# TODO reder_table only accept elements with __table__ attribute
"""
def fetch_coha_words():
    list_words = []
    data_en = pd.read_csv("./words_data/coha_sample.csv")
    for elem in data_en.word.values:
        print(elem)
        word = dict()
        word['word'] = elem
        list_words.append(word)
    #words['words'] = data_en.word.values.tolist()

    return list_words
"""
