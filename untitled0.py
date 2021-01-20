# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:57:45 2020

@author: Pushkar
"""

from flask import request, Flask
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "welcome All"






if __name__ == '__main__':
    app.run()