# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 20:12:10 2018

@author: yuhao
"""

import numpy as np
import jieba
import jieba.analyse


def class2tokens(class2data, mode=1):
	"""
    args: class2data - A dict. {key class id : value = A list of data}

    returns: res - A dict. {key class id : value = A list of tokenized data}
    """
	res = {}
	for key in class2data:
		temp = cut_sentences(class2data[key], mode)
		res[key] = temp
	return res

        
def cut_sentences(slist, mode=1):
	"""
    Helper function for class2tokens. Split all sentences according to the mode.
    args: slist - A list of sentences to be cut.
    	  mode - 1 for cutting sentence; 2 for key word extraction.

    returns: res - A list of lists of tokens. 
    """
	res = []
	
	if mode == 1:
		for s in slist:
			temp = [i for i in jieba.cut(s)]
			res.append(temp)

	if mode == 2:
		for s in slist:
			res.append(jieba.analyse.extract_tags(s))

	return res


def num_to_one_hot(Y, num_classes):
    """
    args: Y - numerical labels
          num_classes - #classes

    returns: output - np.array. One hot labels. (None, num_calss)
    """
    width = num_classes
    height = len(Y)
    
    output = np.zeros((height, width))
    
    for i in range(height):
        output[i, Y[i]] = 1
        
    return output


def remove_duplication(words):
    """
    Remove duplications.
    e.g. remove_duplicated(['信用', '卡', '信用卡']) -> ['信用卡']

    args: words - List of words.

    returns: Refined list of words.
    """
    res = []
    l = len(words)
    for i in range(l):
        if i < l-2:
            if words[i] in words[i+1]:
                continue
            elif words[i] in words[i+2] and words[i+1] in words[i+2]:
                continue
        elif i == l-2:
            if words[i] in words[i+1]:
                continue
        res.append(words[i])
    return res