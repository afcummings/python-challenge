import csv

candidates = []
total_votes = []
num_votes = 0

with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    column = next(csvreader,None)

    for column in csvreader:

        num_votes = num_votes + 1
        candidate = column[2]

        if candidate in candidates:
            candidate_info = candidates.index(candidate)
            total_votes[candidate_info] = total_votes[candidate_info] + 1
        else:
            candidates.append(candidate)
            total_votes.append(1)

percents = []
maximum = 0
max_votes = total_votes[0]

for count in range(len(candidates)):
    new_percents = round(total_votes[count]/num_votes*100, 2)
    percents.append(new_percents)
    if total_votes[count] > max_votes:
        max_votes = total_votes[count]
        maximum = count
winner = candidates[maximum]

print("Election Results\n")
print(" \n")
print(f"Total Votes: {num_votes}\n")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percents[count]}% ({total_votes[count]})\n")
print(" \n")
print(f"The winner is: {winner}\n")

results = f"pypoll_results.txt"

with open(results, 'w') as results_write:

    results_write.write("Election Results\n")
    results_write.write(" \n")
    results_write.write(f"Total Votes: {num_votes}\n")
    for count in range(len(candidates)):
        results_write.write(f"{candidates[count]}: {percents[count]}% ({total_votes[count]})\n")
    results_write.write(" \n")
    results_write.write(f"The winner is: {winner}\n")
    results_write.write(" \n")


