<<<<<<< HEAD
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
=======
def draw_lake(width = 5, length = 20):
    """ 
    Draw a rectangular lake. 
  
    Parameters: 
        width (int): The width of the lake. 
        length (int): The length of the lake.    
    """
    
    if width < 0 or length < 0:
        raise ValueError("width and length must be greater than 0")
    elif width == 0 or length == 0:
        return
        
    for i in range(width):
        draw_vertical(False)
        
        if i == 0 or i == width - 1:
            for _ in range(length):
                draw_horizontal()
        else:    
            for _ in range(length):
                draw_wave()
        
        draw_vertical(True)
>>>>>>> 0e9345cda92eb5709818714a905c011dfd8d30ce
    return


def draw_horizontal():
    """Draw a horizontal fence."""
    print("=", end = '')
    
def draw_vertical(newline = False):
    """
    Draw a vertical fence.
    
    Parameter:
        newline (boolean): add a new line after drawing vertical component.
    """
    if newline == False:
        print("||", end = '')
    else:
        print("||")
    
def draw_wave():
    """Draw waves representing water."""
    print("~", end = '')
    