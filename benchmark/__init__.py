import timeit

def timefunc(function, n, *args):
    def wrap():
        function(*args)
    return timeit.Timer(wrap).timeit(n)
