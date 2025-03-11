from json import load, dump
from math import isnan

def isnan2(value) -> bool:
    if not isinstance(value, float): return value is None
    return isnan(value)

def keep_fields(data: list[dict], fields: list[str]) -> list[dict]:
    return [
        {
            key: val
            for key in fields
            if key in entry and not isnan2(val := entry[key]) # null check
        }
        for entry in data
    ]

if __name__ == "__main__":
    PATH_DIR = "C:/Users/ryana/Documents/VsCode/Python Projects/AI Proj/Json/"
    PATH_IN = f"{PATH_DIR}MOVIE_WITH_GENRES.json"
    PATH_OUT = f"{PATH_DIR}MOVIE_WITH_GENRES_min.json"
    FIELDS = ["ID", "FILMID", "TITLE", "ORIGINAL_LANGUAGE", "OVERVIEW", "POSTER_PATH", "RELEASE_DATE", "RUNTIME", "COLLECTIONID", "Genres"]

    with open(PATH_IN, "r") as f:
        original = load(f)

    with open(PATH_OUT, "w") as f:
        output = keep_fields(original, FIELDS)
        dump(output, f)
