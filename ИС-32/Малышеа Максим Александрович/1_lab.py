mixed_list = [542,542,653,.432452,"4324",[4.4312,54],None,-342]

filtered_list = [x for x in mixed_list if x!=None]

tuple_list = (3,1,542,"5425",'rgrerdtfg',.542425,None)

dict_list = {"int": 131, 'float': -1.431, 'str': "gfdgsf", 'complex': (5+1/3j), 'ept': None}

filt_dict = {key: value for key, value in dict_list.items() if len(key)>3 or value != None}



print(filt_dict)
print(filtered_list)
