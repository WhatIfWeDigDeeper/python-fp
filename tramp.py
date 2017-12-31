import types


def tramp(gen, *args, **kwargs):
    """
        Copyright, 2012, Alex Beal
    """
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)
    return g
