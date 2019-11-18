def supervisor():
	signal = Signal()
	spinner = threading.Thread(target=spin,args=('thinking!',signal))
	print('spinner object:',spinner)
	spinner.start()
	result = slow_function()
	signal.go = False
	spinner.join()
	return result

@asyncio.coroutine
def supervisor():
	spinner = asyncio.async(spin('thinking!'))
	print('spinner object:',spinner)
	result = yield from slow_function()
	spinner.cancel()
	return result