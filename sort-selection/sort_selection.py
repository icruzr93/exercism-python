def sort_selection(array):
  for in1 in range(len(array)):
    minIn = in1

    for in2 in range(in1+1, len(array)):
      if array[in2] < array[minIn]:
        minIn = in2
    
    temp = array[in1]
    array[in1] = array[minIn]
    array[minIn] = temp

  return array