# -*- coding: utf-8 -*-
import codecs
import re

def remove_hml_tags(file_name):
    f = codecs.open(file_name, "r", "utf-8")
    data = f.read()
    
    f = codecs.open(file_name, "w", "utf-8")
    replaced = re.sub("<[^>]*>", "", data)
    f.write(replaced)
    f.close()
