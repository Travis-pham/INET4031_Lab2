#!/usr/bin/env python3
f = open('fileprocessor.input', 'r')
lines = f.readlines()
print("Printing out User Data:\n")
for line in lines:
    if line.startswith('#'):
        skipped_data = []
        skipped_data.append(line.strip().split(':'))
        print(f"{skipped_data[0][0]} is skipped because it starts with a hashtag (commented out)")
        continue
    data = line.strip().split(':')
    print(f"The user {data[0]} has a password of {data[1]} and has a userid {data[2]} and groupid {data[3]}")
print("\n")
print("End of User Data")
