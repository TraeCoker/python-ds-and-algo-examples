from logic import *

read_line("(?x c ?x)")

e = read_line("((a b) c (a b))")
f = read_line("(?x c ?x)")
env = Frame(None)
unify(e, f, env)
env.bindings
print(env.lookup('?x'))

e = read_line("(?x ?x)")
f = read_line(" ((a ?y c) (a b ?z))")
env = Frame(None)
unify(e, f, env)
env.bindings

def unify(e, f, env):
    """Destructively extend ENV so as to unify (make equal) e and f, returning
    True if this succeeds and False otherwise.  ENV may be modified in either
    case (its existing bindings are never changed)."""
    e = lookup(e, env)
    f = lookup(f, env)
    if e == f:
        return True
    elif isvar(e):
        env.define(e, f)
        return True
    elif isvar(f):
        env.define(f, e)
        return True
    elif scheme_atomp(e) or scheme_atomp(f):
        return False
    else:
        return unify(e.first, f.first, env) and unify(e.second, f.second, env)


def search(clauses, env, depth):
    """Search for an application of rules to establish all the CLAUSES,
    non-destructively extending the unifier ENV.  Limit the search to
    the nested application of DEPTH rules."""
    if clauses is nil:
        yield env
    elif DEPTH_LIMIT is None or depth <= DEPTH_LIMIT:
        if clauses.first.first in ('not', '~'):
            clause = ground(clauses.first.second, env)
            try:
                next(search(clause, glob, 0))
            except StopIteration:
                env_head = Frame(env)
                for result in search(clauses.second, env_head, depth+1):
                    yield result
        else:
            for fact in facts:
                fact = rename_variables(fact, get_unique_id())
                env_head = Frame(env)
                if unify(fact.first, clauses.first, env_head):
                    for env_rule in search(fact.second, env_head, depth+1):
                        for result in search(clauses.second, env_rule, depth+1):
                            yield result


def rename_variables(expr, n):
    """Rename all variables in EXPR with an identifier N."""
    if isvar(expr):
        return expr + '_' + str(n)
    elif scheme_pairp(expr):
        return Pair(rename_variables(expr.first, n),
                    rename_variables(expr.second, n))
    else:
        return expr