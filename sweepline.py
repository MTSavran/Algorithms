from bst import insert, search, delete
#MEHMET TUGRUL SAVRAN
#6.006 PSET2 

def get_smallest_at_least(node, bound):

  if node == None:
    return None 
  
  if node.key == bound:
    return node

  if bound < node.key:
    if node.left == None:
      return node
    elif node.left  is not None:
      y = get_smallest_at_least(node.left, bound) 
      if y == None:
        return node
      return y

  elif bound > node.key:
    if node.right == None:
        return None
    return get_smallest_at_least(node.right, bound)

def find_intersection(segments):
  points=[]

  for i in range(len(segments)):
    if segments[i][0][0] == segments[i][1][0]:
      points.append((segments[i][0], 'v', segments[i])) #i ID'li VERTICAL line'a ait nokta

    elif segments[i][0][1] == segments[i][1][1]:
      points.append((segments[i][0], 'h')) #i ID'li HORIZONTAL line'a ait nokta 
      points.append((segments[i][1], 'h')) 

  points = sorted(points, key=lambda x: x[0][0])
  #points.sort() #sorting points with respect to the x-coordinate values 

  # set root to be an empty tree
  root = None

  if len(points) == 1: 
    return None

  for i in range(len(points)):
    #print points
    #if point belongs to horizontal segments
    
    if points[i][1] == 'h':
      if search(root,points[i][0][1]) == None:
        #if not there then add it
        root = insert(root, points[i][0][1])

      else:
        #if there then delete it
        root = delete(root, points[i][0][1])

    #if vertical line
    else:

      #seg is the vertical line this point belongs to
      seg = points[i][2]

      y1 = seg[0][1]
      y2 = seg[1][1]

      ymin = min(y1,y2)
      ymax = max(y1,y2)

      least = get_smallest_at_least(root, ymin)

      if least == None: 
        continue
      elif least.key <= ymax:
        return (seg[0][0], least.key)

  return None

# asegment = [((1,4),(1,7)), ((1,5),(3,5))]


# print find_intersection(asegment)