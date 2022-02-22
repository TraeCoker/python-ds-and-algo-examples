MAX_HASH_TABLE_SIZE = 4096

class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size
        
    def get_valid_index(self, key):
        idx = hash(key) % len(self.data_list)
        
        while True:
            kv = self.data_list[idx]
            
            if kv is None:
                return idx
            
            k, v = kv
            if k == key:
                return idx
            
            idx += 1
            
            if idx == len(self.data_list):
                idx = 0
        
    def __getitem__(self, key):
        idx = self.get_valid_index(key)
        
        kv = self.data_list[idx]
        
        return None if kv is None else kv[1]
    
    def __setitem__(self, key, value):
        idx = self.get_valid_index(key)
        
        self.data_list[idx] = (key, value)
    
    def __iter__(self):
        return (x for x in self.data_list if x is not None)
    
    def __len__(self):
        return len([x for x in self])
    
    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"
    
    def __str__(self):
        return repr(self)