# Yield - return (retorna um generator)

def gerador():
    for i in range(5):
        yield i

g = gerador()
print(g) # no console apenas g

print(next(g)) # no console apenas next(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g)) # StopIteration

# -----------------------------------------

# def gerador():
#     yield 1
#     for i in range(2, 5):
#         yield i

# g = gerador()

# print(next(g)) # no console apenas next(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # StopIteration

