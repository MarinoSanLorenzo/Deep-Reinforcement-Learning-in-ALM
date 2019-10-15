import numpy as np

def calc_mean_var_step(array):
    variation_array = np.array([])
    for i,j in enumerate(array):
	    if i == 0 :
			   continue # prevent from calculating the relative difference between first element
	    variation = ((array[i] - array[i-1])/array[i-1])*100
	    variation_array = np.append(variation_array, variation)
    mean_variation = np.mean(variation_array)
    return mean_variation


def calc_var_step(array, step):
	    # can't insert step = 0 
	    variation = (array[step] - array[step-1])
	    
	    return variation

