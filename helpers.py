import json
import ast

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
    #TODO modif par diego psq il y a des cas bizarres
    """
    Safely parses a genre string and extracts genre names.

    Args:
    - genre_string (str): A string representation of a dictionary containing genre information.

    Returns:
    - list or None: A list of genre names if parsing is successful, or None if the genre string is empty.
    """
    # Check if the genre string is empty
    if genre_string == '{}':
        genre_string = '{"no_genre": "No genre"}'
        
    # Safely evaluate the string as a dictionary and extract the values (which are the genres)
    return list(ast.literal_eval(genre_string).values())