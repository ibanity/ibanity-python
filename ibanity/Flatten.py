def flatten_json(to_flatten): 
    out = {} 
  
    def flatten(flat, name =''): 
        if type(flat) is dict:  
            for a in flat: 
                flatten(flat[a], a) 
        elif type(flat) is list:  
            i = 0
            for a in flat:                 
                flatten(a, name) 
                i += 1
        else:
            if name in out:
                None
            else: 
                out[name] = flat
    flatten(to_flatten) 
    return out 

def flatten_json_ponto(to_flatten): 
    out = {} 
  
    def flatten_ponto(flat, name =''): 
        if type(flat) is dict:     
            for a in flat: 
                flatten_ponto(flat[a], a) 
        elif type(flat) is list: 
            i = 0
            for a in flat:                 
                flatten_ponto(a, name) 
                i += 1
        else:
                out[name] = flat 
    flatten_ponto(to_flatten) 
    return out 