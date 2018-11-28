#   Fernando Serrano, Instructor: Diego Aguirre, T.A.: Anindita Nath, 11/27/2018, CS 2302 DataStructures
#   Program written to create a Min-Heap array that stores the values given in a file, where each number is seperated
#   by a coma, ands orders the list. It can then extract the minimum value and still maintain the min_heap requirements
#   and allows the user to print the sorted list.
import os


class Heap:
    def __init__(self):
        self.heap_array = []

#   Inserts the number at the end of the list and then percolates up if the number is smaller than the father
    def insert(self, k):
        self.heap_array.append(k)
        i = len(self.heap_array) - 1
        #   moves the number up in the array by checking the position of the father at (i-1)//2, and if the number is
        #   smaller than the father switches the two numbers
        while (i-1)//2 >= 0:
            if self.heap_array[(i-1)//2] > self.heap_array[i]:
                temp = self.heap_array[(i-1)//2]
                self.heap_array[(i-1)//2] = self.heap_array[i]
                self.heap_array[i] = temp
            i = (i-1)//2

#   extracts the minimum number in the array/min_heap and places the last number in the array in its position
#   before percolating down the list until it is in proper order
    def extract_min(self):
        if self.is_empty():
            return None
        #   removes the min number of the heap and replaces it with the last number in the array
        min_elem = self.heap_array[0]
        temp = self.heap_array.pop()
        self.heap_array[0] = temp
        #   checks if the children are smaller than the number that was moved upwards and reorganizes the array
        #   arcordingly to left and right child sizes
        i = 0
        while ((i*2) + 2) < len(self.heap_array):
            #   if the second child(right node in tree) is less than the father and its sibling, it switches the right
            #   node with the father
            if self.heap_array[(i*2)+1] > self.heap_array[(i*2)+2] and self.heap_array[i] > self.heap_array[(i*2)+2]:
                temp = self.heap_array[(i * 2) + 2]
                self.heap_array[(i * 2) + 2] = self.heap_array[i]
                self.heap_array[i] = temp
                i = (i * 2) + 2
            #   if the first child(left node in the tree) is less than the father and its sibling, it switches the
            #   left node with the father
            elif self.heap_array[(i*2)+1] < self.heap_array[(i*2)+2] and self.heap_array[i] > self.heap_array[(i*2)+1]:
                temp = self.heap_array[(i*2) + 1]
                self.heap_array[(i*2)+1] = self.heap_array[i]
                self.heap_array[i] = temp
                i = (i*2) + 1

        return min_elem

#   Checks if the array/Min_Heap is empty
    def is_empty(self):
        return len(self.heap_array) == 0

#   Prints the array/Min-Heap in a readable format
    def printlist(self):
        for i in self.heap_array:
            if i == self.heap_array[len(self.heap_array) - 1]:
                print(i)
                break

            print(i, end= ", ")
        print()


def fileinsert(minheaparray, filename):
    if not os.path.isfile(filename):
        print("File not found")
        main()
    try:
        with open(filename) as ins:
            for line in ins:
                line = line.replace("\n", "")
                line = line.replace(" ", "")
                num = line.split(",")
                for i in num:
                    print(i)
                    #   Float is used in-case integer is not specified, this allows any number to be used
                    minheaparray.insert(float(i))
    except ValueError:
        print("Please only enter int/float in file")


def main():
    minheaparray = Heap()
    filename = input("Please input name of file")
    fileinsert(minheaparray, filename)

    #   prints the options and lists of the Min-Heap
    yesorno = input("Would you like to print the full min heap?"
                    "\nyes or no")
    if yesorno.lower() == "yes":
        print()
        print("printing min heap list:")
        minheaparray.printlist()
    yesorno = input("Would you like to print the mininum value in heap?"
                    "\nyes or no")
    if yesorno.lower() == "yes":
        print()
        print("extracting min")
        minheaparray.extract_min()
        minheaparray.printlist()


main()
