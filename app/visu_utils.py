import pandas as pd
import glob
import re
import random


def parse_time_slice(string):
    regexp = re.compile("c1_en|c2_en|c1_de|c2_de")
    idx_slice = re.findall(regexp, string)[0]
    if idx_slice == "c1_en":
        return '1810-1860'
    elif idx_slice == "c2_en":
        return '1960-2010'
    elif idx_slice == "c1_de":
        return '1800-1899'  
    elif idx_slice == "c2_de":
        return '1946-1990'  


def map_time_slice(time_range):
    """
    Get the time slice used to compute the score and return the mean year to choose the position of the cloud on the graph.
    """
    start, end = time_range.split("-")
    year = str(random.randint(int(start), int(end)))
    return year 


def normalize_scores(value):
    """
    idx = 0
    for i in df['Score'].values:
        df['Score'][idx] = float(i*100)
        idx+=1
    """
    value = float(float(value)*100)
    return value


def read_results_one_period(res_file):
    """
    :str: res_file : CSV output of measure_semantic_shift.py

    Read the CSV file from the measure_semantic_shift.py and wrap it into a nice formatted dataframe for the visualization.
    """

    fill_color = { "gold": "#efcf6d", "silver": "#cccccc", "bronze": "#c59e8a" }
    color_text = { "black": "#000000", "red": "#cc0000"}

    df = pd.read_csv(res_file, sep=",", encoding='utf-8')  
    df = df.drop_duplicates(ignore_index=True)
    nb_words = df['word'].size
    tg_word = df["word"][0]
    
    
    df['Year'] = None
    df['Color'] = fill_color['gold']
    df['Size'] = 10
    df['TextColor'] = color_text['black']
    
    df["Parent"] = None
    df["Synonyms"] = None
    df["Score"] = None

 
    all_neighbors = []
    all_distances = []
    all_years = []

    for i in range(nb_words):
        tg_word = df.word[i]
        time_slice = parse_time_slice(df.slice[i])
        neighbors = df.cluster[i]
        neighbors = neighbors.split(";")
        all_neighbors.append(neighbors)
        distances = df.distance[i]
        distances = distances.split(";")
        for d in range(len(distances)):
            distances[d] = normalize_scores(distances[d]) 
        all_distances.append(distances)

        for w in range(len(neighbors)):
            all_years.append(map_time_slice(time_slice))
        
        
    all_neighbors = sum(all_neighbors, [])
    all_distances = sum(all_distances, [])

    res = {"word":all_neighbors,
                    "Score":all_distances, "Year": all_years}
    
    df1 = pd.DataFrame(data=res)
    df1['Color'] = fill_color['gold']
    df1['Size'] = 10
    df1['TextColor'] = color_text['black']

    
    df1.loc[df1['word'].size] = [tg_word, 0.0, 1835, fill_color['silver'], 20, color_text['red']]
    df1.loc[df1['word'].size+1] = [tg_word, 0.0, 1985, fill_color['silver'], 20, color_text['red']]

    return df1 



def results_all_periods(folder_path, tg_word, lang):
    """
    :str: folder_path : folder with all the csv files dumped by measure_semantic_shift.py

    Collect all the dataframes from all time slices and create the final huge dataframe to feed to the visualization. 
    """
    print("Retrieving files from ", folder_path)
    list_files = glob.glob(folder_path + "*.csv")
    [print(f) for f in list_files]
    regexp = re.compile("([a-zA-Z]+)")
    if lang == "English":
        lang = "en"
    elif lang == "German":
        lang = "de"
    
    full_results = []
    for f in list_files: 
        f_trim = f.split("/")
        f_trim = f_trim[len(f_trim)-1]
        parsed_lang = re.findall(regexp, f_trim)[2]
        parsed_word = re.findall(regexp, f_trim)[0]
        if parsed_lang == lang and parsed_word.lower() == tg_word.lower():
            df = read_results_one_period(f)
            full_results.append(df)
    
    df_full = pd.concat(full_results)

    return df_full

