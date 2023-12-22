import json
import ast
import numpy as np

### This file contains all helpers functions used in the notebooks ###


def sort_words(documents):
    """
    Sorts and returns a list of unique words from a collection of documents.

    Args:
    - documents (list): A list of documents, where each document is represented as a list of words.

    Returns:
    - list: A sorted list containing unique words from all the input documents.
    """

    # Initialize an empty list to store unique words from each document
    words_list = []
    
    # Iterate through each document in the input list
    for document in documents:
        # Remove repetitions within each document by converting to a set
        words_selected = list(set(document)) 
        # Append the list of unique words to the words_list
        words_list.append(words_selected)
    
    # Flatten the 2D list into a 1D list and sort the words alphabetically
    sorted_words = sorted([item for sublist in words_list for item in sublist])
    
    # Return the sorted list of words
    return sorted_words


def complete_date(date):
    """
    Completes a date by adding a month and a day for dates that have only the year.

    Args:
    - x: A date represented as an integer or string in the format 'YYYY' or 'YYYY-MM'.

    Returns:
    - str: Completed date in the format 'YYYY-MM' or 'YYYY-MM-DD'.
    """

    # Check if the input date has only the year (length of 4) and add month and day
    if len(str(date)) == 7:
        return str(date) + '-01'
    # Check if the input date has only the year and month (length of 7) and add day
    elif len(str(date)) == 4:
        return str(date) + '-01-01'
    # If the input date has more than 4 characters, return it as is
    else:
        return date


def create_words_database(list_of_words):
    """
    Creates a word database by counting the repetitions of each word.

    Args:
    - l (list): A list of words.

    Returns:
    - dict: A dictionary where keys are unique words and values are the counts of each word.
    """

    # Initialize an empty dictionary to store word counts
    database = {}

    # Iterate through the list of words
    for word in list_of_words:
        # Update the count for each word in the database
        if word in database:
            database[word] += 1
        else:
            database[word] = 1
    
    # Return the word database
    return database


def at_least_2_movies(pair):
    """
    Filters an actor dictionary to include only those with at least 2 movies.

    Args:
    - pair (tuple): A key-value pair representing an actor and the number of movies they have played in.

    Returns:
    - bool: True if the actor has played in at least 2 movies, False otherwise.
    """

    # Unpack the key-value pair
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

    
def extract_genre_names(row):
    """
    Extracts genre names from a JSON-encoded string.

    Args:
    - row (str): A JSON-encoded string representing genre information.

    Returns:
    - list or None: A list of genre names if decoding is successful, or None if there is a JSON decoding error.
    """

    try:
        # Decode the JSON string to a dictionary
        genres_dict = json.loads(row)
        
        # Extract genre names from the dictionary
        genre_names = list(genres_dict.values())
        
        # Return the list of genre names
        return genre_names
    except json.JSONDecodeError:
        # Return None if there is a JSON decoding error
        return None

    
def parse_genres(genre_string):
    """
    Safely parses a genre string and extracts genre names.

    Args:
    - genre_string (str): A string representation of a dictionary containing genre information.

    Returns:
    - list: A list of genre names
    """
    # Check if the genre string is empty
    if genre_string == '{}':
        genre_string = '{"no_genre": "No genre"}'
        
    # Safely evaluate the string as a dictionary and extract the values (which are the genres)
    return list(ast.literal_eval(genre_string).values())

def center_on_first_hit(df, row):
    """
    Computes the position of the movie from the passed row with respect to the first big-hit of the passed

    Args:
    - df (Dataframe): Dataframe subset containing the movies (ordered in chronological order) played by a specific actor
     - row (Series): One row of the passed df

    Returns:
    - float: the number representing the position of the row with respect to the passed df
    """
    # Function that return the position of the movie with respect to the fir big-hit (in chronological order)
    
    # Get the relative index of the row that is passed to the function with respect to the df
    n_actual = df[(df.releaseDate == row.releaseDate) & (df.success == row.success) & (df.name_movie == row.name_movie)].index.values[0]-df.index.values[0]
    # Get the number of movies before the first big-hit
    n_big_hit = row.movie_count_before_hit

    return n_actual - n_big_hit

def dotproduct_similarity_genre(c1, c2):
    """
    The dot product between two bags of words (i.e. counts the number of words that are the same)

    Args:
    - c1 (Counter): first bag of words
    - c2 (Counter): second bag of words

    Returns:
    - float: The dot product between the two passed bags of words
    """ 
    all_genres = set(c1).union(c2)
    dotproduct = sum(c1.get(g, 0) * c2.get(g, 0) for g in all_genres)
    
    return dotproduct
    
    
def similarity_two_prev_movie(df, row):
    """
    Computes the mean similarity between the movie genres from the passed row and the movie genres from the two rows above (looking at the passed df).

    Args:
    - df (Dataframe): Dataframe subset containing the movies (ordered in chronological order) played by a specific actor
    - row (Series): One row of the passed df

    Returns:
    - float or None: The mean similarity (using dotproduct_similarity function) between the movie of the passed row and the two previous movies in chronological order
    """    
    # Get the relative row index
    row_index = df[(df.movieID == row.movieID)].index[0]-df.index[0]

    # If it is the first movie of the considered actor then we cannot compute the wanted similarity
    if row_index == 0:
        return None

    # Get the genres of the movie from the given row
    current = row.genres
    # Get the genres of the movie that comes before the one of the given row
    prev_1 = df.iloc[row_index-1].genres

    # If it is the second movie of the considered actor, then we perform the similarity using only the movie that comes before
    if row_index == 1:
        # Return the smimilarity using the previously defined similarity function
        return dotproduct_similarity_genre(prev_1, current)

    # Get the genres of the second movie that comes before the one of the given row
    prev_2 = df.iloc[row_index-2].genres

    # Return the mean similarity unsing the previously defined similarity function
    return 0.5*(dotproduct_similarity_genre(prev_1, current)+dotproduct_similarity_genre(prev_2, current))

def similarity_two_prev_comp(df,row):
    """
    Computes the mean similarity between the compound from the passed row and the compound from the two rows above (looking at the passed df).

    Args:
    - df (Dataframe): Dataframe subset containing the movies (ordered in chronological order) played by a specific actor
    - row (Series): One row of the passed df

    Returns:
    - float or None: The mean similarity (using dotproduct_similarity function) between the coumpound of the passed row and the two previous movies in chronological order
    """    
    row_index = df[(df.movieID == row.movieID)].index[0]-df.index[0]

    if row_index == 0:
        return None
    
    current = row.comp

    prev_1 = df.iloc[row_index-1].comp

    # If it is the second movie of the considered actor, then we perform the similarity using only the movie that comes before
    if row_index == 1:
        # Return the smimilarity using the previously defined similarity function
        return dotproduct_similarity_comp(prev_1, current)
    
    prev_2 = df.iloc[row_index-2].comp

    # Return the mean similarity unsing the previously defined similarity function
    return 0.5*(dotproduct_similarity_comp(prev_1, current)+ dotproduct_similarity_comp(prev_2, current))


def dotproduct_similarity_comp(c1, c2):
    """
    The dot product between two vectors
    Args:
    - c1 (Numpy): first vector comp
    - c2 (Numpy): second vector comp

    Returns:
    - float: The dot product between the two vectors
    """ 
    # Calculate dot product
    dot_product = np.dot(c1, c2)

    # Calculate the magnitude (length) of the vectors
    magnitude_a = np.linalg.norm(c1)
    magnitude_b = np.linalg.norm(c2)
    if magnitude_a * magnitude_b == 0:
        return 0 
    else:
        cosine_similarity = dot_product / (magnitude_a * magnitude_b)

    
    return cosine_similarity
