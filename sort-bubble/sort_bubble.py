def sort_bubble(array):
  for ind1 in range(len(array)):
    for ind2 in range(len(array)):
      if(array[ind2] > array[ind1]):
        tempNum = array[ind2]
        array[ind2] = array[ind1]
        array[ind1] = tempNum

  return array