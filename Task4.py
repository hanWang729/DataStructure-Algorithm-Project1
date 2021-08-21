"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outList = []
inList = []

for i in range(len(calls)):
    outList.append(calls[i][0])
    inList.append(calls[i][1])
for j in range(len(texts)):
    inList.append(texts[i][0])
    inList.append(texts[i][1])
outSet = set(outList)
inSet = set(inList)
removeSet = set()

# for i in outSet:
#     if i in inSet:
#         removeSet.add(i)
#
# for i in removeSet:
#     outSet.remove(i)
# suggest by advisor: can do it use:
outSet = outSet - inSet


print("These numbers could be telemarketers: ")
print(*sorted(outSet), sep="\n")


