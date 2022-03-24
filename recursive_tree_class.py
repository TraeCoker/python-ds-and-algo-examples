class Tree:
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches
    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))
    def is_leaf(self):
        return not self.branches


def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.label + right.label, (left, right))

fib_tree(5)


def sum_labels(t):
    """Sum the labels of a Tree instance, which may be None."""
    return t.label + sum([sum_labels(b) for b in t.branches])


sum_labels(fib_tree(5))

sum_labels(fib_tree(5))

#memoization can save substantial computation time and memory
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized


fib_tree = memo(fib_tree)
big_fib_tree = fib_tree(35)
big_fib_tree.label
big_fib_tree.branches[0] is big_fib_tree.branches[1].branches[1]
sum_labels = memo(sum_labels)
sum_labels(big_fib_tree)

