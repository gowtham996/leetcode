from collections import Counter

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
taskscount = Counter(tasks)
maxfeq = max(taskscount.values())
maxfeqtasks = sum(1 for count in taskscount.values() if count == maxfeq)
intervelneeded = (maxfeq - 1) * (n + 1) + maxfeqtasks
print(max(intervelneeded, len(tasks)))
