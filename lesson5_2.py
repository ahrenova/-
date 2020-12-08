print(f"coutn lines: {len(list(open('lesson5_2.txt')))}")
for line in open('lesson5_2.txt').readlines():
    print(f"count words: {len(line.split())}")

