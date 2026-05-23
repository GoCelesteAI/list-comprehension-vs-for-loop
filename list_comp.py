"""list_comp.py — 5 list comprehension patterns + when to use a for loop instead.

Run:
  python list_comp.py
"""
import time

nums = list(range(10))

# 1. Map — transform every element
squares = [x * x for x in nums]
print("=== 1. map ===")
print(f"squares: {squares}")
print()

# 2. Filter — keep elements matching a condition
evens = [x for x in nums if x % 2 == 0]
print("=== 2. filter ===")
print(f"evens: {evens}")
print()

# 3. Map + filter together
pos_squares = [x * x for x in nums if x > 3]
print("=== 3. map + filter ===")
print(f"pos_squares: {pos_squares}")
print()

# 4. Flatten — nested for clauses (read left-to-right like nested loops)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for row in matrix for item in row]
print("=== 4. flatten nested list ===")
print(f"flat: {flat}")
print()

# 5. Dict + set comprehensions — same syntax, different brackets
words = ["python", "lambda", "comprehension"]
lengths = {w: len(w) for w in words}
unique_mods = {x % 3 for x in range(100)}
print("=== 5. dict + set comprehensions ===")
print(f"lengths: {lengths}")
print(f"unique_mods: {unique_mods}")
print()

# Speed — comprehensions are ~30% faster than for + append on the same job
N = 100_000

t0 = time.perf_counter()
out = []
for i in range(N):
  out.append(i * 2)
loop_ms = (time.perf_counter() - t0) * 1000

t0 = time.perf_counter()
out = [i * 2 for i in range(N)]
comp_ms = (time.perf_counter() - t0) * 1000

print("=== speed comparison (100k items) ===")
print(f"for+append:  {loop_ms:>7.1f} ms")
print(f"comprehend:  {comp_ms:>7.1f} ms   ({loop_ms/comp_ms:.1f}x faster)")
print()

# When NOT to use a comprehension — multi-step, side effects, debugging
def process_with_logging(items):
  out = []
  for item in items:
    cleaned = item.strip().lower()
    if not cleaned:
      continue  # break / continue read more naturally in a regular loop
    print(f"  processing: {cleaned}")
    out.append(cleaned)
  return out

print("=== when to use a for loop instead ===")
result = process_with_logging(["  PYTHON  ", "", " lambda "])
print(f"  result: {result}")
