import json
import ast

# The goal of the file is to put all helpers that we use in the main notebook
def sort_words(documents):
    words_list = []
    
    for document in documents:
        # Remove repetition by line
        words_selected = list(set(document)) 
        # Glue everything into a 2D matrix
        words_list.append(words_selected)
    
    # Glue everything into 1D matrix and sort by alphabet and return result
    return sorted([item for sublist in words_list for item in sublist])

# Define a function that adds a month and a day for dates that have only the year
def complete_date(x):
    if len(str(x)) == 7:
        return str(x) + '-01'
    elif len(str(x)) == 4:
        return str(x) + '-01-01'
    else:
        return x
    

def create_words_database(l):
    # Sum all the repetitions and output a database like idf but without log and divided
    database = {}
    for words in l:
        if words in database:
            database[words] += 1
        else:
            database[words] = 1
    return database

# Define a function to filter the actor dictionary
def at_least_2_movies(pair):
    key, value = pair
    
    # Set the minimal number of movies played
    n = 2
    # Test condition
    if value >= n:
        # Keep pair in the filtered dictionary
        return True
    else:
        # Filter pair out of the dictionary
        return False  
    

# Define a function to extract genre names
def extract_genre_names(row):
    try:
        genres_dict = json.loads(row)
        genre_names = list(genres_dict.values())
        return genre_names
    except json.JSONDecodeError:
        return None
    

# Define a function to safely parse the genre string
def parse_genres(genre_string):
    #TODO modif par diego psq il y a des cas bizarres
    if genre_string == '{}':
        return None 
    # Safely evaluate the string as a dictionary and extract the values (which are the genres)
    return list(ast.literal_eval(genre_string).values())