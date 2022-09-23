events= "Michael gets lost in the woods. Ulrich goes to find Michael. Both travel to the past but not in the same timeline. Ulrich gets put into the prison. Michael is Jonas's father. Michael committed suicide by hanging himself. Jonas travels back in time to save his father. He finds his dad and tells him about his death. His dad now understood what he had to do. Michael committed suicide by hanging himself. The entire family of Tannahaus was killed in a car accident. This drove him crazy. Tannahaus built a time machine. He also wrote a book on time travel. Claudia finds the book on time travel. Future Claudia gave the present Claudia and time machine. The present Claudia travels back in time and gave the time travelling book to Tannahaus. Tannahaus took ideas from the book he was supposed to write in future. Tannahaus built a time machine. A cult like faction keeps on abducting kids from Winden and experiments on them. None of the abducted kids are ever found again. Charlotte gave birth to Elizabeth. The apocalypse takes place and Charlotte dies. However, Elizabeth somehow survives and gets sent to the past. Elizabeth meets a guy and they have a daughter named Charlotte. After growing up Charlotte gets married. Charlotte gave birth to Elizabeth. Thus the cycle continues. After the apocalypse, only a handful of people survived. Elizabeth was one of them. She became the leader of a savage group. Jonas and Martha love each other. Martha is killed by Adam. Adam is from the future. Jonas travels through time to stop Adam, only to find out that he is the one who eventually becomes Adam. Adam is the only one capable of breaking the endless cycle. For Jonas to become Adam, it is necessary for Martha to die. Without her dying, Jonas would not become Adam and the cycle would never be broken. So, Adam goes back in time. Martha is killed by Adam. After Martha's death Jonas travels into another world"
events = events.split(". ")
d = {}

#Making a dict with the 1st line of the paradox and their index 
for i in range(len(events)):
  count = 0
  for j in range(len(events)):
    if events[i] == events[j]:
      count  += 1
  
  if count == 2 and events[i] not in d:
    d[events[i]] = i

#num of paradox 
print(f"{len(d)} Paradoxes \n")

#Printing the whole paradox
for i, j in d.items():
  #Took a temp list from +1 idx of the 1st line to exclude the 1st line while Iterrating or the loop would break immediately
  temp = events[j+1:]
  new = events[j] + ". "
  for k in range(len(temp)):
    #Adding lines to new untill the line doesn't match with 1s line of the paradox
    if temp[k] != events[j]:
      new += temp[k] + ". "
    #Breaking the loop after adding the line when the line mathes
    else:
      new += temp[k] + ". \n"
      break     
  print(new)