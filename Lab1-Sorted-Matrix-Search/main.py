from time import perf_counter_ns
from searches import *
from mymatrix import MyMatrix

N = 2 ** 13
M_EXPONENT_RANGE = range(1, 14)
FILLING_TYPES = ['1', '2']
WORST_CASES = [2 * N + 1, 16 * N + 1]
SEARCH_TECHNIQUES = {'binary': MyMatrix.binary_search,
                     'ladder': MyMatrix.ladder_search,
                     'ladder+exp': MyMatrix.exp_search}


def get_data():
    res = [{2 ** x: {} for x in M_EXPONENT_RANGE} for _ in FILLING_TYPES]
    for x in M_EXPONENT_RANGE:
        m = 2 ** x
        matrix = MyMatrix(m, N)
        for type_, target in enumerate(WORST_CASES):
            matrix.fill(type_)
            print(f"Size: 2^{x}x2^13, filling type: {type_ + 1}")
            for tech in SEARCH_TECHNIQUES:
                s_time = perf_counter_ns()
                search_res = SEARCH_TECHNIQUES[tech](matrix, target)
                res[type_][m][tech] = perf_counter_ns() - s_time
                print(f"- {tech} search: {search_res}, time: {res[type_][m][tech]} ns")
    return res


def export_data(arr):
    for type_, data in enumerate(arr):
        with open(f'results_{type_ + 1}.csv', 'w') as f:
            for m in data:
                s = str(m) + ',' + ','.join(map(str, data[m].values())) + '\n'
                f.write(s)


def test_searches():
    print('Testing binary and exp search for 1-dimensional array...')
    a = [-100, -69, -3, 0, 1, 6, 9, 100, 1000, 1999, 2000, 3000, 11000, 111111]
    for x in a:
        print(f'Element {x}, binary : {binary_search(a, x)} , exp : {exp_search(a, x)}')
    x = 8888
    print(f'Element {x}, binary : {binary_search(a, x)} , exp : {exp_search(a, x)}')
    print('Finished')


def test_techniques():
    mat = MyMatrix(2 ** 4, N)
    mat.fill(0)
    print(mat.exp_search(8888))


def main():
    export_data(get_data())


main()
