with open('stdout.txt', 'r') as stdout:
  for line in stdout:
    splitedLine = line.split()
    #print (line)
    if splitedLine[1] == "Running":
      percentage = line.split()[2]
    elif splitedLine[1] == "Requested":
      percentage = "0%"
    elif splitedLine[1] == "Done":
      percentage = "100%"
    print (percentage)

print ("Job Finished")