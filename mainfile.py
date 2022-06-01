from extract_tweets import extraction
from preprocessing import processing
from naive import naiveclassify

def calling():
    extraction()
    processing()
    naiveclassify()
    print("======================================================")
    

if __name__ == "__main__":
    num = 3
    for counter in range(num):
        calling()