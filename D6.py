with open("input.txt") as f:
  inp = f.read().split("\n")

from collections import Counter

def part1(inp):
  f = [int(i) for i in inp[0].split(",")]
  for _ in range(80):
    i=0
    l = len(f)
    while i<l:
      if f[i]==0:
        f[i]=6
        f.append(8)
      else:
        f[i]-=1
      i+=1
  print(len(f))
    

def part2(inp):
  pool = [0]*9
  for k,v in Counter(int(i) for i in inp[0].split(",")).items():
    pool[k] = v
  for _ in range(256):
    pool.append(pool.pop(0))
    pool[6]+=pool[8]
  print(sum(pool))

part1(inp)
part2(inp)

