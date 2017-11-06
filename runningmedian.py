#MEHMET TUGRUL SAVRAN
import math
import bisect
import StringIO
import collections

###################################################################
#   Description:
#       Gradebook is a data structure that keeps track of every student
#       and their grade information. The cool thing about Gradebook is that
#       returning the k most average students takes only O(k) time, and 
#       updating a student's grade takes O(log(n) + k) time! 
#
###################################################################

###################################################################
# 
#   
#       Max_Heap is a general implementation of a max-heap modified to accept
#       (key, data) pairs. For instance, in the student GPA problem, the 
#       "key" would a student name and the "data" would be the student's GPA,
#       e.g. ("Bob Dylan", 1) 
#
#   Implementation/Initialization Details:
#       The keys (i.e. student names) are stored in a list called "self.keys"
#       The data (i.e. student GPAs) are stored in a list called "self.data"
#       Additionally, a dictionary called "self.key_to_index_mapping" keeps
#       track of the index of the key in the array. For instance, if we had 
#       the following list of (key, data) pairs, which already satisfies the 
#       max-heap property:
#
#           [("Ray Charles", 4), ("Bob Dylan", 1), ("Bob Marley", 3)]
#           
#       then,       self.keys = ["Ray Charles", "Bob Dylan", "Bob Marley"]
#                   self.data = [4, 1, 3]
#           self.key_to_index = {"Ray Charles": 0, 
#                                "Bob Dylan": 1,
#                                "Bob Marley": 2} 
#       where 0, 1, 2 corresponds to the index in "self.keys"
#
#   Provided Methods:
#       All the methods presented in lecture and recitation are provided, with
#       only slight changes to accomodate the (key, data) pair modification.
#       In addition, we provide the method show_tree(self) so that you may 
#       print out what your heap looks like.
#
#   
#       we may call:
#           
#           heap.max_heap_modify("Bob Marley", 5)
#
#       This should change Bob Marley's grade to 5, and then restore
#       the heap invariant so that the data structure looks like this:
#   
#               self.keys = ["Bob Marley", "Bob Dylan", "Ray Charles"]
#               self.data = [5, 1, 4]
#       self.key_to_index = {"Ray Charles": 2, 
#                           "Bob Dylan": 1,
#                           "Bob Marley: 0"} 
###################################################################
class Max_Heap:

    def __init__(self, keys, data):
        assert len(keys) == len(data)
        
        self.keys = collections.deque(keys)
        self.data = collections.deque(data)
        self.key_to_index = dict(zip(self.keys, range(len(self.keys)))) #!
        self.heapify()

    
    def max_heap_modify(self, key, data):
        index = self.key_to_index[key]
        olddata = self.data[index]
        self.data[index] = data
        #self.key_to_index[key] = data
        if self.data[index] >= olddata:
            self.increase_key(index,data)
        else:
            self.max_heapify(index)

    def maximum(self):
        return (self.keys[0], self.data[0])

    def size(self):
        return len(self.keys)

    def extract_max(self):
        if len(self.keys)<1:
            raise Exception("No elements in heap!")
        sm, gm = self.keys.popleft(), self.data.popleft()
        del self.key_to_index[sm]
        if len(self.keys) > 0:
            s, g = self.keys.pop(), self.data.pop()
            self.keys.appendleft(s)
            self.data.appendleft(g)
            self.key_to_index[s] = 0
            self.max_heapify(0)
        return (sm, gm)

    def insert_key(self, k, d):
        self.keys.append(k)
        self.data.append(-float("inf"))
        self.key_to_index[k] = len(self.keys)-1 #!
        self.increase_key(len(self.keys)-1, d)

    def max_heapify(self, i):
        heap_size = len(self.keys)
        l = i*2 + 1
        r = i*2 + 2
        largest = i
        if l < heap_size and self.data[l] > self.data[i]:
            largest = l
        if r < heap_size and self.data[r] > self.data[largest]:
            largest = r
        if largest != i:
            self.swap(largest, i)
            self.max_heapify(largest)

    def increase_key(self, i, key):
        if key < self.data[i]:
            raise Exception("New key is smaller than current key.")
        self.data[i] = key
        parent = (i-1)/2
        while i > 0 and self.data[i] > self.data[parent]:
            self.swap(i, parent)
            i = parent
            parent = (i-1)/2

    def heapify(self):
        for i in range(len(self.keys)/2)[::-1]:
            self.max_heapify(i)

    # Exchanges the students and GPAs at two indices
    def swap(self, i1, i2):
        self.key_to_index[self.keys[i1]] = i2 #!
        self.key_to_index[self.keys[i2]] = i1 #!
        self.data[i1], self.data[i2] = self.data[i2], self.data[i1]
        self.keys[i1], self.keys[i2] = self.keys[i2], self.keys[i1]

    # modified from https://pymotw.com/2/heapq/
    # Displays the heap as a tree
    def show_tree(self, total_width=60, fill=' '):
        """Pretty-print a tree."""
        output = StringIO.StringIO()
        last_row = -1
        for i, n in enumerate(self.keys):
            if i:
                row = int(math.floor(math.log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            towrite = str(n) + " (" + str(self.data[i]) + ")"
            output.write(str(towrite).center(col_width, fill))
            last_row = row
        print output.getvalue()
        print '-' * total_width
        print
        return ""



    ########################################################################
    # The following methods are methods used for testing and may be ignored.
    ########################################################################

    def check_heap_invariant(self):
        n = len(self.data)
        for i in range(n/2):
            parent = self.data[i]
            if parent < self.data[2*i+1]:
                return False
            if 2*i + 2 < n:
                if parent < self.data[2*i+2]:
                    return False
        return True

    def check_student_index(self):
        for s,i in self.key_to_index.iteritems():
            if i >= len(self.keys):
                return False
            if self.keys[i] != s:
                return False
        return True

# a = Max_Heap([],[])
# a.show_tree()


###################################################################
# Part (b)
#   The implementation of Min_Heap is the same as Max_Heap, but modified
#   to be a min-heap. Please refer to the description for Max_Heap.
###################################################################
class Min_Heap:
    '''
    keys: list of key values
    data: list of data that corresponds to the key values
    student_index: a dictionary that maps students names to their index in the
        list representation of the heap
    '''
    def __init__(self, keys, data):
        assert len(keys) == len(data)
        self.keys = collections.deque(keys)
        self.data = collections.deque(data)
        self.key_to_index = dict(zip(self.keys, range(len(self.keys)))) #!
        self.heapify()

    # TODO
    def min_heap_modify(self, key, data):
        index = self.key_to_index[key]
        olddata = self.data[index]
        self.data[index] = data
        #self.key_to_index[key] = data
        if self.data[index] <= olddata:
            self.decrease_key(index,data)
        else:
            self.min_heapify(index)

    def minimum(self):
        return (self.keys[0], self.data[0])

    def size(self):
        return len(self.keys)

    def extract_min(self):
        if len(self.keys)<1:
            raise Exception("No elements in heap!")
        sm, gm = self.keys.popleft(), self.data.popleft()
        del self.key_to_index[sm]
        if len(self.keys) > 0:
            s, g = self.keys.pop(), self.data.pop()
            self.keys.appendleft(s)
            self.data.appendleft(g)
            self.key_to_index[s] = 0
            self.min_heapify(0)
        return (sm, gm)

    def insert_key(self, k, d):
        self.keys.append(k)
        self.data.append(float("inf"))
        self.key_to_index[k] = len(self.keys)-1 #!
        self.decrease_key(len(self.keys)-1, d)

    def min_heapify(self, i):
        heap_size = len(self.keys)
        l = i*2 + 1
        r = i*2 + 2
        smallest = i
        if l < heap_size and self.data[l] < self.data[i]:
            smallest= l
        if r < heap_size and self.data[r] < self.data[smallest]:
            smallest = r
        if smallest != i:
            self.swap(smallest, i)
            self.min_heapify(smallest)

    def decrease_key(self, i, key):
        if key > self.data[i]:
            raise Exception("New key is larger than current key.")
        self.data[i] = key
        parent = (i-1)/2
        while i > 0 and self.data[i] < self.data[parent]:
            self.swap(i, parent)
            i = parent
            parent = (i-1)/2

    def heapify(self):
        for i in range(len(self.keys)/2)[::-1]:
            self.min_heapify(i)

    # Exchanges the students and GPAs at two indices
    def swap(self, i1, i2):
        self.key_to_index[self.keys[i1]] = i2 #!
        self.key_to_index[self.keys[i2]] = i1 #!
        self.data[i1], self.data[i2] = self.data[i2], self.data[i1]
        self.keys[i1], self.keys[i2] = self.keys[i2], self.keys[i1]

    # modified from https://pymotw.com/2/heapq/
    # Displays the heap as a tree
    def show_tree(self, total_width=60, fill=' '):
        """Pretty-print a tree."""
        output = StringIO.StringIO()
        last_row = -1
        for i, n in enumerate(self.keys):
            if i:
                row = int(math.floor(math.log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            towrite = str(n) + " (" + str(self.data[i]) + ")"
            output.write(str(towrite).center(col_width, fill))
            last_row = row
        print output.getvalue()
        print '-' * total_width
        print
        return ""

    ########################################################################
    # The following methods are methods used for testing and may be ignored.
    ########################################################################

    def check_heap_invariant(self):
        n = len(self.data)
        for i in range(n/2):
            parent = self.data[i]
            if parent > self.data[2*i+1]:
                return False
            if 2*i + 2 < n:
                if parent > self.data[2*i+2]:
                    return False
        return True

    def check_student_index(self):
        for s,i in self.key_to_index.iteritems():
            if i >= len(self.keys):
                return False
            if self.keys[i] != s:
                return False
        return True

class Gradebook:

    # TODO
    def __init__(self, student_names, k):

        self.k = k
        population = len(student_names)
        self.population = population #THIS IS WHAT WE CALL N
        middles = collections.deque()
        self.middles = middles
        diction = collections.defaultdict(list)  #A DEFAULT DICT(LIST) OF STUDENT'S RECORDS {"Jason":[total units, grades*units,GPA], "Tugrul":[etc, etc, GPA]}
        self.diction = diction
        for i in student_names:
            diction[i] = [0,0,0] #total units, product, gpa
        
        maxheap = Max_Heap([],[])
        self.maxheap = maxheap
        minheap = Min_Heap([],[])
        self.minheap = minheap

        maxlimit = math.floor((self.population-k)/2)
        self.maxlimit = maxlimit

        minlimit = math.ceil((self.population-k)/2)
        self.minlimit = minlimit


        for i in range(population):
            if i < maxlimit:
                self.maxheap.insert_key(student_names[i],diction[student_names[i]][2])
            elif maxlimit <= i < (maxlimit + k):
                self.middles.appendleft((student_names[i],diction[student_names[i]][2]))
            else:
                self.minheap.insert_key(student_names[i],diction[student_names[i]][2])
        # print self.maxheap.show_tree()
        # print self.middles
        # print minheap.show_tree()
    def update_grade(self, student, credit, grade):

        currentGPA = self.diction[student][2]
        product = credit*grade
        self.diction[student][0] += credit
        self.diction[student][1] += product
        self.diction[student][2] = float(self.diction[student][1])/self.diction[student][0]
        newGPA = self.diction[student][2]
        boolean = False
        for i in self.middles:
            if i[0] == student:
                boolean = True
                break 
        if not boolean:
            if student in self.maxheap.key_to_index:
                self.maxheap.max_heap_modify(student, newGPA)
                if self.maxheap.maximum()[1] <= self.middles[0][1]:
                    pass #student stays there 
                elif self.middles[0][1] < self.maxheap.maximum()[1] < self.minheap.minimum()[1]: #ENDS UP AT DEQUE aka middles

                    todq = self.maxheap.extract_max()
                    tomaxheap = self.middles.popleft()
                    self.maxheap.insert_key(tomaxheap[0], tomaxheap[1])
                    self.middles.appendleft(todq)
                    self.middles = sorted(self.middles, key=lambda (k,v): v)
                    self.middles = collections.deque(self.middles)
                else:
                    #print 'ammmm'
                    tominheap = self.maxheap.extract_max()

                    dqtomax = self.middles.popleft()
                    self.maxheap.insert_key(dqtomax[0],dqtomax[1])
                    minheaptodq = self.minheap.extract_min()
                    self.minheap.insert_key(tominheap[0],tominheap[1])
                    self.middles.append(minheaptodq)
                    self.middles = sorted(self.middles, key=lambda (k,v): v)
                    self.middles = collections.deque(self.middles)
            else:
                self.minheap.min_heap_modify(student,newGPA)
                if self.minheap.minimum()[1] >= self.middles[self.k-1][1]:
                    pass #STAYS IN MIN HEAP
                elif self.middles[0][1] <= self.middles[0][1] <= self.minheap.minimum()[1] < self.middles[self.k-1][1]:
                    dqtominheap = self.middles.pop()
                    minheaptodq = self.minheap.extract_min()
                    self.minheap.insert_key(dqtominheap[0],dqtominheap[1])
                    self.middles.append(minheaptodq)
                    self.middles = sorted(self.middles, key=lambda (k,v): v)
                    self.middles = collections.deque(self.middles)
                else:
                    tomaxheap = self.minheap.extract_min()
                    maxtodq = self.maxheap.extract_max()
                    dqtomin = self.middles.pop()
                    self.maxheap.insert_key(tomaxheap[0],tomaxheap[1])
                    self.middles.appendleft(maxtodq)
                    self.minheap.insert_key(dqtomin[0],dqtomin[1])
                    self.middles = sorted(self.middles, key=lambda (k,v): v)
                    self.middles = collections.deque(self.middles)

        elif boolean:

            for i in list(self.middles):
                if i[0] == student:
                    self.middles.remove(i)
                    i = (student,newGPA)
                    self.middles.append(i)
                    break
            self.middles = sorted(self.middles, key = lambda (k,v):v)
            self.middles = collections.deque(self.middles)
            if self.middles[self.k-1][1] > self.minheap.minimum()[1]:
                tomin = self.middles.pop()
                todq = self.minheap.extract_min()
                self.middles.append(todq)
                self.minheap.insert_key(tomin[0],tomin[1])
                self.middles = sorted(self.middles, key=lambda (k,v): v)
                self.middles = collections.deque(self.middles)
            elif self.middles[0][1] < self.maxheap.maximum()[1]:
                tomax = self.middles.popleft()
                todq = self.maxheap.extract_max()
                self.middles.append(todq)
                self.maxheap.insert_key(tomax[0],tomax[1])
                self.middles = sorted(self.middles, key=lambda (k,v): v)
                self.middles = collections.deque(self.middles)

        
        # print self.maxheap.show_tree()
        # print self.middles
        # print self.minheap.show_tree()
    def average(self, student):
        GPA = self.diction[student][2]
        # Return a single number representing the GPA for student
        return GPA
    # TODO
    def middle(self):
        # Return the k most average students and their GPAs as a 
        #   list of tuples, e.g. [(s1, g1),(s2,g2)]
        return self.middles






