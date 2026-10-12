
requests = [0, 30, 41, 62, 14]
head = 20

total_seek = 0
remaining = requests.copy()

current = head
while remaining :

    nearest = min(remaining,key=lambda r: abs(current - r))

    total_seek += abs(current - nearest)
    current = nearest
    remaining.remove(nearest)

print("Total Seek Time =", total_seek)
