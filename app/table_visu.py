import pandas as pd
import re
import glob
#from .visu_utils import normalize_scores

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



def table_visu(tg_word):

    list_files = glob.glob("./model_outputs/" + "*.csv")
    regexp = re.compile("([a-zA-Z]+)")

    headings = ("Word", "Time slice", "Distance from the target word", "Target word")

    for f in list_files:
        f_trim = f.split("/")
        f_trim = f_trim[len(f_trim)-1]
        parsed_word = re.findall(regexp, f_trim)[0]
        if parsed_word.lower() == tg_word.lower():

            df = pd.read_csv(f)
            df = df.drop_duplicates(ignore_index=True)

            data = tuple()
            
            for i in range(df['word'].size):
                #tg_word = df.word[i]
                time_slice = parse_time_slice(df.slice[i])
                neighbors = df.cluster[i]
                neighbors = neighbors.split(";")
                distances = df.distance[i]
                distances = distances.split(";")
                for x in zip(neighbors, distances):
                    word, dist = x
                    data = data + ((word, time_slice, dist, tg_word),)
            
    
    return headings, data


def table_display():

    list_files = ["./words_data/generated_words_en.csv", "./words_data/generated_words_de.csv"]

    headings = ("Word", "Language")

    data = tuple()

    for f in list_files:
        df = pd.read_csv(f)
        df = df.drop_duplicates(ignore_index=True)
        lg = None
        if f == list_files[0]:
            lg = "English"
        else:
            lg = "German"
        
        for i in range(df['word'].size):
            word = df.word[i]
            data = data + ((word, lg),)
    
    return headings, data

