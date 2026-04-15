class LRUCache:
    class Node:
        def __init__(self, key=-1, val=-1, next_node = None, prev_node = None):
            self.key = key
            self.val = val
            self.next_node = next_node
            self.prev_node = prev_node

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__hm = {}
        self.__dll = self.Node(-1, -1)
        ## add tail
        self.__dll.next_node = self.Node(-1, -1)
        self.__dll.next_node.prev_node = self.__dll
        self.__dll_tail = self.__dll.next_node

    def _remove_node(self, curr_node):
        # remove curr_node
        curr_node.prev_node.next_node = curr_node.next_node
        curr_node.next_node.prev_node = curr_node.prev_node

    def _add_node_to_tail(self, curr_node):
        ## add curr_node to tail (most recently used)
        curr_node.next_node = self.__dll_tail
        self.__dll_tail.prev_node.next_node = curr_node
        curr_node.prev_node = self.__dll_tail.prev_node
        self.__dll_tail.prev_node = curr_node


    def get(self, key: int) -> int:
        if key in self.__hm.keys():
            # remove curr_node
            self._remove_node(self.__hm[key])
            ## add curr_node to tail (most recently used)
            self._add_node_to_tail(self.__hm[key])
            return self.__hm[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.__hm.keys():
            self.__hm[key].val = value
            ## remove node
            self._remove_node(self.__hm[key])
            ## add node at tail
            self._add_node_to_tail(self.__hm[key])
        else: 
            self.__hm[key] = self.Node(key, value)
            if len(self.__hm) > self.__capacity:
                ## remove node from head and hm
                node_to_remove = self.__dll.next_node
                self._remove_node(node_to_remove)
                del self.__hm[node_to_remove.key]

            ## add new node to tail
            self._add_node_to_tail(self.__hm[key])
           

        
