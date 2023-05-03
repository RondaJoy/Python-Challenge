import csv

print("Election Results")
print()
print("-------------------------")
print()

# read data from .csv file
with open('election_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header
    PollData = list(reader)

# tally the number of rows/votes
TotVotes = len(PollData)
print("Total Votes: " +str(TotVotes))
print()
print("-------------------------")
print()

# create a list to store tally for each candidate
vcount = {}
# begin for loop to count occurrences of candidate name in Column C/2
for col in PollData:
    CAN = col[2]
    if CAN in vcount:
        vcount[CAN] += 1
    else:
        vcount[CAN] = 1

# generate output for candidate name, % of total vote, and actual # of votes
for CAN, count in vcount.items():
    PCNT = (count / TotVotes) *100
    format_PCNT = round(PCNT, 3)
    print(f"{CAN}: {format_PCNT}% ({count})")
    print()
    TCount.append(count)
    CCount.append(CAN)
print("-------------------------")
print()

WinCount = max(TCount)
result = []
index = []
for x, item in enumerate(TCount):
    if item == WinCount:
        result.append(item)
        index.append(x)
x = index[0] +1
print(f"Winner: {CCount[x]}")
