
#Defining the node of a doubly-linked list
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


#Class Object for the Cache, built on top of a hash map and a doubly linkedlist
class LRUCache:
    def __init__(self,size):
        self.size = size
        self.valdict = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addtoCache(self,node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def removeFromCache(self, node):
        self.tail.prev = node.prev
        node.prev.next = self.tail

    #Function for getting the value corresponding to a key
    def get(self,key):
        # Modify its position to top of the linkedlist
        if key in self.valdict:
            node = self.valdict[key]
            #Remove it from its current position
            self.removeFromCache(node)
            #Add it to the top of the linkedlist
            self.addtoCache(node)
            return node.val
        else:
            return -1

    #Function for putting a key and its value in the cache
    def put(self,key,value):
        #If key is already in cache, add and remove it
        if key in self.valdict:
            self.removeFromCache(self.valdict[key])
            self.addtoCache(self.valdict[key])

        else:
            #If cache full, remove LRU
            if len(self.valdict)>= self.size:
                #Remove LRU node
                self.removeFromCache(self.tail.prev)
                #Remove it from HashMap
                del self.valdict[self.tail.prev.key]

            # Add new value (MRU) to head.next
            self.addtoCache(Node(key, value))
            # Add new value to hashmap
            self.valdict[key] = Node(key, value)


    #Function for deleting a key and its value from the cache
    def delete(self, key):
        if key in self.valdict:
            node = self.valdict[key]
            self.removeFromCache(node)
            del self.valdict[key]

        else:
            print('Value is not in cache and cannot be delete')

    #Function for resetting the cache
    def reset(self):
        #Reset linkedlist
        self.head.next = self.tail
        self.tail.prev = self.head
        #Clear hashmap
        self.valdict.clear()

         