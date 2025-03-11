

import pandas as pd
import json
ROOT = "C:/Users/ryana/Documents/VsCode/Python Projects/AI Proj/"

# # Load the three Excel files uploaded by the user
# movie_genre_file = '/mnt/dataMOVIE_GENRE.xlsx'
# genre_file = '/mnt/data/GENRE.xlsx'
# movie_file = '/mnt/data/MOVIE.xlsx'

# # Function to convert Excel files to JSON
# def excel_to_json(file_path):
#     # Read the Excel file (assuming single sheet per file)
#     excel_data = pd.read_excel(file_path)
#     # Convert the dataframe to a dictionary (normalized)
#     json_data = excel_data.to_dict(orient="records")
#     return json_data

# # Convert all three files to JSON format
# movie_genre_json = excel_to_json(movie_genre_file)
# genre_json = excel_to_json(genre_file)
# movie_json = excel_to_json(movie_file)

# # Save the JSON outputs to files
# with open('/mnt/data/MOVIE_GENRE.json', 'w') as f:
#     json.dump(movie_genre_json, f, indent=4)

# with open('/mnt/data/GENRE.json', 'w') as f:
#     json.dump(genre_json, f, indent=4)

# with open('/mnt/data/MOVIE.json', 'w') as f:
#     json.dump(movie_json, f, indent=4)

# # Returning the paths to the generated JSON files
# output_files = {
#     'MOVIE_GENRE.json': '/mnt/data/MOVIE_GENRE.json',
#     'GENRE.json': '/mnt/data/GENRE.json',
#     'MOVIE.json': '/mnt/data/MOVIE.json'
# }

# output_files











## converting excel to json

movie_genre_file = f'{ROOT}archive/MOVIE_GENRE.xlsx'
genre_file = f'{ROOT}archive/GENRE.xlsx'
movie_file = f'{ROOT}archive/MOVIE.xlsx'

def excel_to_json(file_path):
    excel_data = pd.read_excel(file_path)
    json_data = excel_data.to_dict(orient="records")
    return json_data

movie_genre_json = excel_to_json(movie_genre_file)
genre_json = excel_to_json(genre_file)
movie_json = excel_to_json(movie_file)

with open(f'{ROOT}Json/MOVIE_GENRE.json', 'w') as f:
    json.dump(movie_genre_json, f, indent=2)

with open(f'{ROOT}Json/GENRE.json', 'w') as f:
    json.dump(genre_json, f, indent=2)

with open(f'{ROOT}Json/MOVIE.json', 'w') as f:
    json.dump(movie_json, f, indent=2)

output_files = {
    'MOVIE_GENRE.json': f'{ROOT}Json/MOVIE_GENRE.json',
    'GENRE.json': f'{ROOT}Json/GENRE.json',
    'MOVIE.json': f'{ROOT}Json/MOVIE.json'
}












# Load the previously generated JSON data
with open(f'{ROOT}Json/MOVIE_GENRE.json', 'r') as f:
    movie_genre_data = json.load(f)

with open(f'{ROOT}Json/GENRE.json', 'r') as f:
    genre_data = json.load(f)

with open(f'{ROOT}Json/MOVIE.json', 'r') as f:
    movie_data = json.load(f)

# mapping of genre IDs to genre names from genre_data
genre_id_to_name = {genre['GENREID']: genre['GENRE'] for genre in genre_data}

# mapping of movie IDs to genre IDs from movie_genre_data
movie_id_to_genre_ids = {}
for movie_genre in movie_genre_data:
    movie_id = movie_genre['FILMID']
    genre_id = movie_genre['GENREID']
    if movie_id not in movie_id_to_genre_ids:
        movie_id_to_genre_ids[movie_id] = []
    movie_id_to_genre_ids[movie_id].append(genre_id)

# Add the list of genre names to each movie in movie_data using 'FILMID' as the key
for movie in movie_data:
    movie_id = movie['FILMID']
    genre_ids = movie_id_to_genre_ids.get(movie_id, [])
    # Get the genre names corresponding to the genre IDs
    genre_names = [genre_id_to_name.get(genre_id, "Unknown Genre") for genre_id in genre_ids]
    # Add a new attribute 'Genres' to the movie
    movie['Genres'] = genre_names

output_movie_file = f'{ROOT}Json/MOVIE_WITH_GENRES.json'
with open(output_movie_file, 'w') as f:
    json.dump(movie_data, f)

