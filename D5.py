with open("input.txt") as f:
  inp = f.read().split("\n")

from collections import defaultdict

def part1(inp):
  cache = defaultdict(int)
  for line in inp:
    s,e = line.split("->")
    x1,y1 = map(int,s.split(","))
    x2,y2 = map(int,e.split(","))
    if x1==x2:
      if y1>y2:
        y2,y1=y1,y2
      for y in range(y1,y2+1):
        cache[(x1,y)]+=1
    elif y1==y2:
      if x1>x2:
        x2,x1=x1,x2
      for x in range(x1,x2+1):
        cache[(x,y1)]+=1
     
  count=0
  for v in cache.values():
    if v>1:
      count+=1
      
  print(count)

def part2(inp):
  cache = defaultdict(int)
  for line in inp:
    s,e = line.split("->")
    x1,y1 = map(int,s.split(","))
    x2,y2 = map(int,e.split(","))
    if x1==x2:
      if y1>y2:
        y2,y1=y1,y2
      for y in range(y1,y2+1):
        cache[(x1,y)]+=1
    elif y1==y2:
      if x1>x2:
        x2,x1=x1,x2
      for x in range(x1,x2+1):
        cache[(x,y1)]+=1
    else:
      if x1>x2 and y1>y2:
        while x1>=x2:
          cache[(x1,y1)]+=1
          x1-=1
          y1-=1
      elif x1>x2 and y1<y2:
        while x1>=x2:
          cache[(x1,y1)]+=1
          x1-=1
          y1+=1
      elif x1<x2 and y1>y2:
        while x1<=x2:
          cache[(x1,y1)]+=1
          x1+=1
          y1-=1
      elif x1<x2 and y1<y2:
        while x1<=x2:
          cache[(x1,y1)]+=1
          x1+=1
          y1+=1
          
  count=0
  for v in cache.values():
    if v>1:
      count+=1
  #util_print(cache)
  print(count)

def util_print(cache):
  arr = [[0 for i in range(10)] for j in range(10)]
  print(cache)
  for x,y in cache.items():
    arr[x[1]][x[0]] = y

  for i in arr:
    print(*i)

part1(inp)
part2(inp)


  
