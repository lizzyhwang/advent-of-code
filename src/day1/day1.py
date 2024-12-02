
# navigate to src/day1
# run with `python3 day1.py`
def main():
  input = open("input.txt", "r")

  # create our lists
  list1 = []
  list2 = []
  for line in input:
    tokens = line.split()
    list1.append(tokens[0])
    list2.append(tokens[1])

  # sort lists  
  list1.sort()
  list2.sort()
  
  # find differences per line
  counter = 0
  for i in range(0,len(list1)): # the lists are the same size
    counter += abs(int(list1[i]) - int(list2[i]))
  
  print(counter)

main()