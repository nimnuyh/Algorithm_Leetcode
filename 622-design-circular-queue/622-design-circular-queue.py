class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.Queue = [None for i in range(k)]
        self.Pointer = 0
        self.Full = False
        self.Length = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.Full == False :
            self.Queue[self.Pointer] = value
            self.Pointer += 1
            if self.Pointer == self.Length :
                self.Full = True
            return True
        else :
            return False
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.Queue[0] == None :
            return False
        else :
            self.Queue.pop(0)
            self.Queue.append('n')
            self.Pointer -= 1
            self.Queue[self.Pointer] = None
            if self.Full == True :
                self.Full = False
            return True

    def Front(self):
        """
        :rtype: int
        """
        if self.Pointer != 0 :
            return self.Queue[0]
        else :
            return -1

    def Rear(self):
        """
        :rtype: int
        """
        if self.Pointer != 0 :
            return self.Queue[self.Pointer - 1]
        else :
            return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.Pointer != 0 :
            return False
        else :
            return True

    def isFull(self):
        """
        :rtype: bool
        """
        return self.Full


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()