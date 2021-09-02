# from linked_list.linked_list import LinkedList
class Node:
    def __init__(self, key=None,value=None):
        self.value = value
        self.key=key
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    # def includes(self, value):
    #     is_last = False
    #     current = self.head
    #     print(current)
    #     while not is_last:
    #         if str(current) == str(value):
    #             return True

    #         if current.next == None:
    #             is_last = True
    #         current = current.next
    #     return False

    def insert(self,key ,value):
        node = Node(key,value)

        if self.head:
            node.next = self.head
        self.head = node

class Hashmap():
    def __init__(self,size=1024) -> None:
        self.size=size
        self._buckets=[None]*size

    def _hash(self,key):
        """
            hash Arguments: key Returns: Index in the collection for that key.
        """
        sum=0
        for ch in key:
            sum+=ord(ch)

        return sum%self.size

    def add(self,key,value):
        """
            add: Arguments: key, value Returns: nothing
            This method hash the key, and add the key and value pair to the table, handling collisions as needed.
        """
        idx=self._hash(key)
        if not self._buckets[idx]:
            self._buckets[idx]=LinkedList()
        self._buckets[idx].insert(key,value)

    def get(self,key):
        """
            get: Arguments: key, Returns: Value associated with that key in the table
        """
        idx=self._hash(key)
        if not self._buckets[idx]:
            return None
        ll=self._buckets[idx].head
        while ll:
            if ll.key==key:
                return ll.value
            ll=ll.next
        return None


    def contains(self,key):
        """
            contains: Arguments: key Returns: Boolean, indicating if the key exists in the table already.
        """
        idx=self._hash(key)
        if not self._buckets[idx]:
            return False
        ll=self._buckets[idx].head
        while ll:
            if ll.key==key:
                return True
            ll=ll.next
        return False


if __name__=="__main__":
    hash_map=Hashmap(15)
    hash_map.add("Ali","0796873213")
    hash_map.add("Sara","0255444566")
    print(hash_map.get("Ali"))
    print(hash_map.get("ali"))
