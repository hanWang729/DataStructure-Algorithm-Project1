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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
"Suggestion from reviewer to use format()"
# print("First record of text, " + texts[0][0] + " texts " + texts[0][1] + " at time " + texts[0][2])
# print("Last record of calls, " + calls[-1][0] + " calls " + calls[-1][1] + " at time " + calls[-1][2])
print("First record of text, {} calls {} at time {}".format(texts[0][0],texts[0][1],texts[0][2]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[-1][0],calls[-1][1],calls[-1][2],calls[-1][3]))