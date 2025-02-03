from collections import deque
from math import pi

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print('List functions')
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4)) # Find next banana starting at position 4
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())

print('')
print('Stacks')
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

print('')
print('Queues')
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)


print('')
print('Comprehensions')
squares = []
for x in range(10):
    squares.append(x)

print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

other = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(other)

vec = [-4, -2, 0, 2, 4]
print(vec)
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print(freshfruit)
print([weapon.strip() for weapon in freshfruit])

print([(x, x**2) for x in range(6)])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print(vec)
print([num for elem in vec for num in elem])

print([str(round(pi, i)) for i in range(1, 6)])

