import re
import sys
from collections import Counter

pattern = re.compile(r"^(\S+ \S+) (INFO|WARNING|ERROR) (.*)$")
levels, errors = Counter(), Counter()
first_error = last_error = None

for line in sys.stdin:
    m = pattern.match(line.strip())
    if not m:
        continue
    ts, level, msg = m.groups()
    levels[level] += 1
    if level == "ERROR":
        errors[msg] += 1
        first_error = first_error or ts
        last_error = ts

print("# Log Summary")
print(f"Levels: {dict(levels)}")
if errors:
    print(f"First error: {first_error} | Last error: {last_error}")
    print("Top errors:")
    for msg, count in errors.most_common(3):
        print(f"  {count}x  {msg}")
else:
    print("No errors found.")