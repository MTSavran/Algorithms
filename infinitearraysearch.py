'''
find_amulet: returns the chest index of the Amulet of Rivest
ARGS: magic_map(a,b): magic_map(a,b) returns true if the Amulet
is the chest index i where a <= i < b.
RETURN: index of chest containing amulet

HINT: magic_map(a,a+1) returns true iff the Amulet is in chest a
magic_map(1,float('inf')) will always return true
'''
def find_amulet(magic_map):
        
        #Basically, the problem is about doing a binary search on an infinitely long array. 
        #As we only have a function that returns true if the item is inside a specific range, 
        #we don't have specific lower/upperbounds. Starting from 0, we increase the index by a factor 
        #of 2 to find the upperbound in lg(n) time (index = 1 first, then 2, then 4, then 8, then 16 etc.)
        #Finally, we do binary search between this upperbound and lowerbound, which is upperbound/2 (or can very well be 0 as it will matter trivially)


        #PART 1: FINDING THE UPPERBOUND

        mini = 0 
        # print magic_map(1599,1600)
        i = 1 
        # i is kind of "upperbound" here

        if magic_map(mini, i):
        	return 0 #if chest is at index 0 
        

        else: 
        	while not magic_map(mini, i):
        		i = 2*i #increase index by factor of 2
                        print i
                        
                #PART 2: BINARY SEARCH 

        	upperbound = i #upperbound of binary search
        	lowerbound = i/2 #lowerbound of binary search 

                while lowerbound<upperbound-1: 
                       
                	midpoint = (upperbound + lowerbound)//2 
                	
        		if magic_map(lowerbound, midpoint):
        			upperbound=midpoint
        		else: 
        			lowerbound = midpoint

                return lowerbound #the index of the chest!
