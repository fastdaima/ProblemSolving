class HashTable:
    def __init__(self,size):
        self.size = size
        self.hash_table = self.create_buckets(self.size)

    def create_buckets(self,size):
        return [[] for _ in range(self.size)]

    def set_val(self,key,val):
        hash_key = hash(key)%self.size
        bucket   = self.hash_table[hash_key]

        found_key = False
        for index,record in enumerate(bucket):
            record_key,record_val = record

            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key,val)
        else:
            bucket.append((key,val))

    def get_val(self,key):
        hash_key = hash(key)%self.size
        bucket = self.hash_table[hash_key]

        found_key = False
        for index,record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        return record_val if found_key else "value not in hashtable"

    def delete_val(self,key):
        hash_key = hash(key)%self.size
        bucket = self.hash_table[hash_key]

        found_key = False
        for index,record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        return bucket.pop(index) if found_key else "value not in hashtable"


h = HashTable(10)

h.set_val(1,'b')
h.set_val(2,'c')
h.set_val(3,'df')

print (h.hash_table)

h.delete_val(3)
print (h.hash_table)

h.set_val("df",'ad')
print (h.hash_table)

print (h.get_val(1))

