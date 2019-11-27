# chiselassig

## Overview
This repository describes the implementation of an (Least Recently Used) LRU Cache.
The implementation makes use of a dictionary and a doubly linked list to manage the fetching and ordering of the data.


### Initialization
To initialize the cache, specify the intended size and make the following call:
```python
lruCache = LRUCache(<int size>)
e.g. lruCache = LRUCache(5) # Cache size of 5 ints
```

### Inserting Items in Cache
```python
lruCache.put(key, value)
e.g. lruCache.put(1,2) #insert an element with key 1 and value 2
```

Note:
A new value will be placed at the front of the linked list governing the cache's ordering.
If the value inserted already exists in the cache, it will be overwritten and place at the front of the cache.
When the cache is the full, the LRU item (tail element in the linked list) will be evicted.


### Getting Items from Cache
The 'get' method allows for retrieval of items from the cache by means of the 'key'.

```python
lruCache.get(key)
e.g. lruCache.get(2) #Fetch the cache entry with key 2
```

Note:
Retrieving an item from the cache will update its position to the top of the linked list
Retrieving an item that does not exist in the cache will result in a -1

### Deleting Items from Cache
The 'del' method allows for the deletion of specific items from the cache by means of the 'key'

```python
lruCache.del(key)
e.g. lruCache.del(5) #Delete the cache entry with key 5
```

Note:
Deleting an item that does not exist will result in a console message warning


### Reset Cache
The reset method will remove all items from the cache and reset the linkedlist. The size chosen from earlier calls will remain the same however.

```python
lruCache.reset()
```

## TESTING
The following set of methods are intended for debugging and testing of the cache.

### Printing Cache ordering
Function prints values between Head and Tail of the linked list (in that order)

```python
lruCache.printCache()
```
Note:
Printing an empty cache will result in an empty line.

### Unit Testing
To conduct unit testing on the class, from the console, run the following command:
```python
>> python test_LRUCache.py 
```
Note:
Unit testing will assess the different functions described above on a capacity 2 Cache. 



