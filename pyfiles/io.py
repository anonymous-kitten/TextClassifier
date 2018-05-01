# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 20:12:10 2018

@author: yuhao
"""

import codecs
import numpy as np
import re


def load_data(path):
    """
    Read and process all training data.
    
    Params:
        path - Path of training data.
        
    Returns:
        class2data - A dict {key = class id : value = a list of data}
        distribution - A dict {key = class id ： value = num of data in this class}
    """
    class2data = {}
    distribution = {}
    class2data = {}
    num_class = 0
    num_data = 0
    
    with codecs.open(path, encoding='utf8') as f:
        for sentence in f:
            if sentence == '\r\n':
                num_class += 1
                continue
            else:
                num_data += 1
                s = process_sentence(sentence)  # simply process the sentence

                if num_class in distribution:  # update distribution
                    distribution[num_class] += 1
                else:
                    distribution[num_class] = 1

                if num_class in class2data:  # update class2data
                    class2data[num_class].append(s)
                else:
                    class2data[num_class] = [s]
                
    print('{} data with {} classes loaded.'.format(num_data, num_class+1)) 
    return class2data, distribution


def process_sentence(s):
    """
    Helper function for load_data(). Process a given sentence. e.g. remove '\n', '\s'......
    
    Params:
        s - A string. The given sentence.
    
    Returns:
        res - Processed sentence.
    """
    res = s.replace('\r\n', '')
    res = res.strip()
    pattern = re.compile(u"[\u4e00-\u9fa5]") # keep all chinese characters
    chars = pattern.findall(res)
    res = ''
    for c in chars:
    	res += c
    return res

