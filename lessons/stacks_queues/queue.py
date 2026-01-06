""" Using a queue simulate a simple ticket counter system """

# 5 people join the queue one after the other
# The system serves each one of them in order, printing who's been served each time

from collections import deque

queue = deque()

for i in range(5):
    queue.append(input("Visitor: ")) # Adding person to the queue

    print(f"{queue[-1]} has joined the line")

print("All 5 visitors have been added to the line")

if "Favour" in queue:
    queue.remove("Favour")

    print("Favour has been served (VIP)")

while not len(queue) == 0:
    current = queue.popleft()

    print(f"{current} has been served")