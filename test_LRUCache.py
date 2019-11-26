import unittest
#from mock import patch
from LRUCache import LRUCache, Node

class TestCache(unittest.TestCase):

    def setUp(self):
        self.cache1 = LRUCache(2)
        node1 = Node(1, 1)
        node2 = Node(2, 2)
        self.cache1.head.next = node1
        node1.prev = self.cache1.head
        node1.next = node2
        node2.prev = node1
        node2.next = self.cache1.tail
        self.cache1.tail.prev = node2
        self.cache1.valdict[1] = node1
        self.cache1.valdict[2] = node2

    def tearDown(self):
        #del self.cache1
        pass

    def test_get(self):
        print('Test_get')
        # Simple Get
        self.assertEqual(self.cache1.get(1),1)
        self.assertEqual(self.cache1.get(2),2)
        self.assertEqual(self.cache1.head.next.val,2)
        self.assertEqual(self.cache1.tail.prev.val,1)

        # Get value not in cache
        self.assertEqual(self.cache1.get(3),-1)


    def test_put(self):
        print('test_put')
        #Add with an overwrite
        self.cache1.put(1,1)
        self.assertEqual(self.cache1.head.next.val,1)

        #Add with a full cache
        self.cache1.put(3,3)
        self.assertEqual(self.cache1.head.next.val,3)
        self.assertEqual(self.cache1.head.next.next.val,1)


    def test_delete(self):
        print('Test Delete')
        #Delete of value in cache
        self.cache1.delete(1)
        self.assertEqual(self.cache1.head.next.val, 2)

        #Delete of value not in cache
        self.cache1.delete(3)
        self.assertEqual(self.cache1.head.next.val, 2)
        self.assertEqual(self.cache1.head.next.next.val, 0)

    def test_reset(self):
        print('Test Reset')
        self.cache1.reset()
        self.assertEqual(self.cache1.head.next.val, 0)

if __name__ == '__main__' :
    unittest.main()