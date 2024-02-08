import random
from collections import defaultdict
import matplotlib.pyplot as plt

counts = defaultdict(int)
num = 1_000_000

def dice_roll():
    return random.randint(1, 6)

for i in range(num):
    sum = dice_roll() + dice_roll()
    counts[sum] += 1
sorted_counts = dict(sorted(counts.items()))
x = []
y = []
print(f"|{'sum':^15}|{'count':^20}|{'probabilities':^20}")
print(f"|{'-'*15}|{'-'*20}|{'-'*20}")
for sum, count in sorted_counts.items():
    print(f"|{sum:^15}|{count:^20}|      {count/num:.2%}")
    x.append(sum)
    y.append(round(count/num * 100))

plt.bar(x, y)
plt.xlabel("Sum of two dice rolls")
plt.ylabel("Probability (%)")
plt.show()