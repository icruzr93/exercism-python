def sort_bubble(array):
  for ind1 in range(len(array)):
    for ind2 in range(len(array) - 1 - ind1):
      if(array[ind2] > array[ind2+1]):
        tempNum = array[ind2]
        array[ind2] = array[ind2+1]
        array[ind2+1] = tempNum

  return array