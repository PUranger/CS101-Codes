def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None


def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key, value])


def make_hashtable(nbuckets):
    tab = []
    for unused in range(0, nbuckets):
        tab.append([])
    return tab


def hash_string(keyword, buckets):       # hash_string returns the bucket corresponding to the keyword
    h = 0
    for e in keyword:
        h = (h+ord(e)) % buckets
    return h


def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]    # return htable[n] which returns the n+1 th entry of htable 


def hashtable_add(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    bucket.append([key, value])

table = make_hashtable(3)
hashtable_update(table, 'udacity', 23)
hashtable_update(table, 'audacity', 17)
hashtable_update(table, 'boacity', 19)
hashtable_update(table, 'wodacity', 28)
hashtable_update(table, 'udacity', 27)
print hashtable_lookup(table, 'udacity')
print table
