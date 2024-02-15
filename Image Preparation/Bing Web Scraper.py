import numpy as np 
import pandas as pd
import matplotlib as mp
import random as rd
import math as mth
#These libraries were just to test if importing them with anaconda works
import bing_image_downloader as bid
#Importing the bid library
from bing_image_downloader import downloader
dir= r'C:\Users\gabri\images'
#Specifically Importing the downloader to not have to type out everything
downloader.download ("people beige", limit=300, output_dir= dir, adult_filter_off= False, force_replace=False)
#Actual line of code that does the Web-Scraping