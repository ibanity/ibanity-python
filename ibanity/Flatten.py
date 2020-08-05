def flatten_json(y): 
    out = {} 
  
    def flatten(x, name =''): 
          
        # If the Nested key-value  
        # pair is of dict type 
        if type(x) is dict: 
              
            for a in x: 
                flatten(x[a], a) 
                  
        # If the Nested key-value 
        # pair is of list type 
        elif type(x) is list: 
              
            i = 0
              
            for a in x:                 
                flatten(a, name) 
                i += 1
        else: 
            out[name] = x 
  
    flatten(y) 
    return out 