requests = [0, 30, 41, 62, 14]
head = 20

total_seek = 0

current = head
for r in requests:
    total_seek += abs(current - r)

    current = r


print("Total Seek Time =", total_seek)