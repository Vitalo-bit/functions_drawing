numbers = input().split()
N = int(numbers[0])
K = int(numbers[1])
M = int(numbers[2])
cubes = []
words = []
count = 0
cubes_temp = cubes.copy()
for cub in range(N):
    cubes.append(input())
for wrd in range(M):
    words.append(input())
for m in range(M):
    for w in words[m]:
        for n in range(len(cubes_temp)):
            if w in cubes_temp[n]:
                try:
                    del cubes_temp[cubes_temp.index(w)]
                except ValueError:
                    break
            else:
                break
        count += 1
    cubes_temp = cubes.copy()
print(count)