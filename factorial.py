import math
from datetime import datetime

# Generate timestamp for the filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"factorial_results_{timestamp}.txt"

# Calculate factorials from 1 to 10
results = []
print("Calculating Factorials 1 to 10...")
for i in range(1, 11):
    fact = math.factorial(i)
    results.append(f"{i}! = {fact}")
    print(f"{i}! = {fact}")

# Write to a text file with a timestamp
with open(filename, "w") as f:
    f.write("Factorial Results (1 to 10)\n")
    f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("-" * 30 + "\n")
    for line in results:
        f.write(line + "\n")
        

print(f"\n✅ Results successfully saved to {filename}")