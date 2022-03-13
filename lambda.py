def compose1(f, g):
    return lambda x: f(g(x))

f = compose1(lambda x: x * x,
             lambda y: y + 1)
result = f(12)