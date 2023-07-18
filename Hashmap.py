#creates Hashmap class
class Hashmap:
    def __init__(self, initial_size = 40):
       self.list = []
       for i in range(initial_size):
           self.list.append([])


#adds an item to the Hash map
    def update(self, key, val):
        bucket = hash(key) % 40
        grouping_list = self.list[bucket]

        for i in grouping_list:
            if i[0] == key:
                i[1] = val
                return True

        kv = [key, val]
        grouping_list.append(kv)
        return True

#search for items using key in Hash map
    def search(self, key):
        grouping = hash(key) % 40
        grouping_list = self.list[grouping]
        for i in grouping_list:
            if key == i[0]:
                return i[1]
        return None

# delete item from hash map using key
    def delete(self,key):
        grouping = hash(key) % 40
        location = self.list[grouping]

        if key in location:
            location.remove(key)