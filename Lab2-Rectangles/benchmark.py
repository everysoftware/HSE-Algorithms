from time import perf_counter, perf_counter_ns

from rectangles_naive import *
from rectangles_map import *
from rectangles_tree import *


X_PRIME = 113
Y_PRIME = 131
POINTS_COUNT = 10 ** 4
ALGORITHMS = [BruteForceAlgorithm, AlgorithmOnMap, AlgorithmOnTree]
RAW_DIR = 'raw'


def generate_rectangles(n):
    return tuple((10 * i, 10 * i, 10 * (2 * n - i), 10 * (2 * n - i)) for i in range(n))


def generate_points(n):
    return tuple((pow(X_PRIME * i, 31, 20 * n), pow(Y_PRIME * i, 31, 20 * n)) for i in range(n))


def get_raw_data():
    result = {}
    print('Launching tests')
    launch_start = perf_counter()
    print(f'M = {POINTS_COUNT}')
    for i in range(1, 6):
        print(f'N = 10^{i}')
        rectangles = generate_rectangles(10 ** i)
        time = []
        for j, algo in enumerate(ALGORITHMS):
            res = {'preparation': 0, 'query': 0, 'sum': 0}
            if i >= 4 and j == 1:
                print(f'Skipping algorithm #{j + 1}...')
                time.append(res)
                continue
            print(f'Testing algorithm #{j + 1}...')
            points = generate_points(POINTS_COUNT)
            start = perf_counter_ns()
            al = algo(rectangles)
            res['preparation'] = perf_counter_ns() - start
            start = perf_counter_ns()
            al.execute(points)
            res['query'] = perf_counter_ns() - start
            res['sum'] = res['preparation'] + res['query']
            time.append(res)
            del al  # фикс замера 1 алгоритма
            print(f'result: {res}')
        result[f'10^{i}'] = time
    print()
    print(f'Testing done in {perf_counter() - launch_start} s.')
    return result


def write_raw_data(raw_data):
    s = [
        {'key': 'preparation', 'file': f'{RAW_DIR}/preparation.tsv', 'content': ''},
        {'key': 'query', 'file': f'{RAW_DIR}/query.tsv', 'content': ''},
        {'key': 'sum', 'file': f'{RAW_DIR}/sum.tsv', 'content': ''}
    ]
    print('Writing raw data...')
    for x in s:
        for power in raw_data:
            x['content'] += '\t'.join([power] + [str(result[x['key']]) for result in raw_data[power]]) + '\n'
        with open(x['file'], 'w') as f:
            f.write(x['content'])
    print(f'Writing done. Check "{RAW_DIR}" directory')


def benchmark():
    raw = get_raw_data()
    write_raw_data(raw)
