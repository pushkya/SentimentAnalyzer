# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:35:13 2020

@author: Pushkar
"""

import re
from step1 import X
import string
def remove_punct(text):
    text_nopunct = ''
    text_nopunct = re.sub(string.punctuation,'',text)
    return text_nopunct
X['Text_Clean'] = X[0,1].apply(lambda x: remove_punct(x))
    