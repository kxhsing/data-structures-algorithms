class HashTable(object):
    def __init__(self, size):
        """Initialize size, slots to hold keys and data to hold values"""

        self.size = size #Best to have size be primary number to ensure efficiency
        self.slots = [None] * self.size
        self.data = [None] * self.size 

    def hash_function(self, key):
        """Take key, hash and then use remainder as hash val"""

        return hash(key) % self.size

    def put(self, key, data):
        """Put new key data pair into our hash table"""

        hash_value  = self.hash_function(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data

        else:
            if self.slots[hash_value] == key: #if key there already, update data
                self.data[hash_value] = data
            else: #original slot taken, need to rehash
                next_slot = self.rehash(hash_value) 
                while self.slots[next_slot] and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data #key found at next slot, so just need to update

    def rehash(self, old_hash):
        """If first hash value taken, use this to rehash for new one"""

        return (old_hash +1) % self.size

    def get(self, key):
        """Get the value for the key in hash table"""

        start_slot = hash_function(key)

        data = None
        found = False
        stop = False
        position = start_slot

        while self.slots[position] != None and not found and not stop:
            if self[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == start_slot: #Back at initial slot which means we
                    stop = True #went through whole table and not there, so stop
        return data

    def __getitem__(self, key):
        """Gives us Python dictionary functionality of brackets [ ] """

        return self.get(key)

    def __setitem__(self, key, data):
        """Gives us Python dictionary functionality of brackets [ ] """

        return self.put(key, data)



H = HashTable(11)
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)







