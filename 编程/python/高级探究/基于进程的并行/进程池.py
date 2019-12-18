from multiprocessing import Pool
import time
def f(x):
	return x*x
if __name__ == '__main__':
	with Pool(processes=4) as pool:
		result = pool.apply_async(f,(10,))
		print(result.get(timeout=1))

		print(pool.map(f,range(10)))

		it = pool.imap(f,[x for x in range(1,10)])
		a = next(it)
		print(type(a))
'''		
		print(next(it))

		print(next(it))
		print(next(it))
		print(it.next(timeout=1))
'''

