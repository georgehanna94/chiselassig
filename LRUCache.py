
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

        #Check size input
        if size <= 0:
            raise ValueError("Cache Size must be > 0")

        self.size = size
        self.valdict = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    #Private Method, Used for adding new recently used item
    def __addtoCache(self,node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    #Private Method, Used for removing least recently used item
    def __removeFromCache(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    #Public Methods
    #Function for getting the value corresponding to a key
    def get(self,key):
        """
        :type key: int
        :rtype: int
        """

        # Modify its position to top of the linkedlist
        if key in self.valdict:
            node = self.valdict[key]
            #Remove it from its current position
            self.__removeFromCache(node)
            #Add it to the top of the linkedlist
            self.__addtoCache(node)
            return node.val
        else:
            return -1

    #Function for putting a key and its value in the cache
    def put(self,key,value):
        """
        :type key: int
        :type value: int
        :rtype nothing
        """

        #Create new node
        node = Node(key, value)

        #If key is already in cache, remove it first
        if key in self.valdict:
            self.__removeFromCache(self.valdict[key])
            del self.valdict[key]

        else:
            #If cache full, remove LRU
            if len(self.valdict)>= self.size:
                # Remove it from HashMap
                del self.valdict[self.tail.prev.key]
                #Remove LRU node
                self.__removeFromCache(self.tail.prev)

        # Add new value (MRU) to head.next
        self.__addtoCache(node)
        # Add new value to hashmap
        self.valdict[key] = node

    #Function for deleting a key and its value from the cache
    def delete(self, key):
        '''
        :type key: int
        :rtype nothing
        '''

        if key in self.valdict:
            node = self.valdict[key]
            self.__removeFromCache(node)
            del self.valdict[key]
        else:
            print('Value is not in cache and cannot be deleted')

    #Function for resetting the cache
    def reset(self):
        '''
        :rtype nothing
        '''

        #Reset linkedlist
        self.head.next = self.tail
        self.tail.prev = self.head
        #Clear hashmap
        self.valdict.clear()

    #Debugging function for printing values for linkedlist
    def printcache(self):
        '''
        :rtype nothing
        '''

        node = self.head.next
        while node.next:
            print(node.val, end =">")
            node = node.next
        print()

def main():

    '''Sample Calls'''
    lrucache = LRUCache(2)
    lrucache.put(1,1)
    lrucache.put(2,2);
    print(lrucache.get(1))
    lrucache.put(2,2)
    print(lrucache.get(1))
    print()
    lrucache.printcache()
    lrucache.reset()


if __name__ == '__main__':
    main()