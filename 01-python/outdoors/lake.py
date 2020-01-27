def draw_lake(width = 1, length = 5):
    for i in range(length):
    	print('-', end = '')
    print()
    for i in range(width):
    	for j in range(length):
    		print('|', end = '')
    	print()
    for i in range(length):
    	print('-', end = '')
    print()
    return
