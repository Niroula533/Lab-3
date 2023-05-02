


class BinarySearchTree:
    def __init__(self,size=35):
        self.bstArray = [None] * size
        self.maxIndex = size - 1

    #find size of bst
    def size(self):
        list = [e for e in self.bstArray if e is not None]
        return len(list)

    #insert element
    def add(self, value , key = 0):
        if key > self.maxIndex:
            return "Index out of range"
        elif self.bstArray[key] is None:
            self.bstArray[key] = value
        elif (value < self.bstArray[key]):
            self.add(value, 2 * key + 1)
        else:
            self.add(value, 2 * key + 2)

    #search element
    def search(self,searchKey):
        index = 0
        while (index <= self.maxIndex) and (self.bstArray[index] != searchKey):
            if self.bstArray[index] is None:
                return False
            if self.bstArray[index] > searchKey:
                index = 2*index + 1
            else:
                index = 2*index + 2
        if index <= self.maxIndex:
            return index
       

    #return smallest element
    def smallest(self, index = 0):
        try:
            while (self.bstArray[2 * index + 1] is not None):
                index = 2 * index + 1
            return self.bstArray[index]
        except:
            return self.bstArray[index]

    #return largest element
    def largest(self, index = 0):
        try:
            while (self.bstArray[2 * index + 2] is not None):
                index = 2 * index + 2
            return self.bstArray[index]
        except:
            return self.bstArray[index]

    def successor(self, startIndex):
        while ((2 * startIndex + 1) <= self.maxIndex) and (self.bstArray[startIndex * 2 + 1] != None):
            startIndex = startIndex * 2 + 1
        return startIndex
        

    #remove an element
    def remove(self, key, index = 0):
        keyIndex = index if index != 0  else self.search(key)
        if keyIndex is False:
            return False
        lchild = 2*keyIndex + 1
        rchild = 2*keyIndex + 2
        # has no children
        if (lchild > self.maxIndex) or ((self.bstArray[lchild] is None) and self.bstArray[rchild] is None):
            self.bstArray[keyIndex] = None
        #has one child
        elif(self.bstArray[lchild] is None):
            self.bstArray[keyIndex] = self.bstArray[rchild]
            self.remove(self.bstArray[rchild], rchild)
        elif (self.bstArray[rchild] is None):
            self.bstArray[keyIndex] = self.bstArray[lchild]
            self.remove(self.bstArray[lchild], lchild)
        #has two children
        else:
            successorI = self.successor(rchild)
            self.bstArray[keyIndex] = self.bstArray[successorI]
            self.remove(self.bstArray[successorI], successorI)

    #print tree
    def printTree(self):
        for e in self.bstArray:
            print(e)

    #inorder traversal
    def inorder_walk(self, index = 0):
        inorder_arr = []
        if (index <= self.maxIndex) and (self.bstArray[index] is not None):
            #left subtree
            inorder_arr.extend(self.inorder_walk(2*index+1))
            #root
            inorder_arr.append(self.bstArray[index])
            #right subtree
            inorder_arr.extend(self.inorder_walk(2*index+2))
        return inorder_arr
    
    #postorder traversal
    def postorder_walk(self, index = 0):
        postorder_arr = []
        if (index <= self.maxIndex) and (self.bstArray[index] is not None):
            #left subtree
            postorder_arr.extend(self.postorder_walk(2*index+1))
            #right subtree
            postorder_arr.extend(self.postorder_walk(2*index+2))
            #root
            postorder_arr.append(self.bstArray[index])
        return postorder_arr

    #preorder traversal
    def preorder_walk(self, index = 0):
        preorder_arr = []
        if (index <= self.maxIndex) and (self.bstArray[index] is not None):
            #root
            preorder_arr.append(self.bstArray[index])
            #left subtree
            preorder_arr.extend(self.preorder_walk(2*index+1))
            #right subtree
            preorder_arr.extend(self.preorder_walk(2*index+2)) 
        return preorder_arr


if __name__ == "__main__":    
    bst = BinarySearchTree(20)
    bst.add(12)
    bst.add(14)
    bst.add(11)
    bst.add(15)
    bst.add(13)
    bst.add(2)
    bst.add(11.5)

    #bst.remove(12)
    bst.printTree()
    print(bst.preorder_walk())
    print("the size is", bst.size())
    #print(bst.successor(12))
    print("The largest is: ",bst.largest())
    print("The smallest is: ",bst.smallest())

