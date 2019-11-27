# chiselassig

## Overview
This repository describes the implementation of an (Least Recently Used) LRU Cache.
The implementation makes use of a dictionary and a doubly linked list to manage the fetching and ordering of the data.


### Initialization
To initialize the cache, specify the intended size and make the following call:
lruCache = LRUCache(<int size>)

### Inserting Items in Cache
lruCache.put(key, value)
e.g. lruCache.put(1,2)

Note:
A new value will be placed at the front of the linked list governing the cache's ordering.
If the value inserted already exists in the cache, it will be overwritten and place at the front of the cache.
When the cache is the full, the LRU item (tail element in the linked list) will be evicted.


### Getting Items from Cache
lruCache.get(key)
e.g. lruCache.get(2)

Note:
Retrieving an item from the cache will update its position to the top of the linked list
Retrieving an item that does not exist in the cache will result in a -1

### Deleting Items from Cache
lruCache.del(key)
e.g. lruCache.del(key)

Note:
Deleting an item that does not exist will result in a console message warning


### Reset Cache
lruCache.reset()


## TESTING

###Printing Cache ordering
lruCache.printCache()

Note:
Function prints values between Head and Tail of the linked list (in that order)

###Unit Testing

>> python test_LRUCache.py 

Note:
Unit testing will assess the different functions described above on a capacity 2 Cache. 



