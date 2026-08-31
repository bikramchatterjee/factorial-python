import math
import os
from datetime import datetime

def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    return math.factorial(n)

if __name__ == "__main__":
    number = 15  # you can change this value
    # will change the number 
    result = factorial(number)

    # Define the output directory and create it if needed
    output_dir = r"C:\Users\Jaya\Documents\Bikram Chatterjee\Jenkins\temp"
    os.makedirs(output_dir, exist_ok=True)

    # Get current timestamp for the filename (safe for Windows: no spaces or colons)
    now = datetime.now()
    timestamp_str = now.strftime("%Y%m%d_%H%M%S")   # e.g., 20260831_143522

    # Create the filename with timestamp
    output_file = os.path.join(output_dir, f"factorial_output_{timestamp_str}.txt")

    # Write the result and timestamp inside the file
    with open(output_file, "w") as f:
        f.write(f"Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"The factorial of {number} is {result}\n")

    # Also print to console (Jenkins log)
    print(f"Result written to {output_file}")
    print(f"Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"The factorial of {number} is {result}")