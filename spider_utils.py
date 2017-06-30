# -*- coding: utf-8 -*-
import codecs
import re
import os

def remove_hml_tags(file_name):
    f = codecs.open(file_name, "r", "utf-8")
    data = f.read()
    
    f = codecs.open(file_name, "w", "utf-8")
    replaced = re.sub("<[^>]*>", "", data)
    
    replaced = remove_empry_lines(replaced)
    
    f.write(replaced)
    f.close()

    
def remove_empry_lines(text):
    return os.linesep.join([s for s in text.splitlines() if s])
        
        
def substitude_parameters_with_opinion(origin_url):
    return re.sub("\?(.*)", "opinion/", origin_url)