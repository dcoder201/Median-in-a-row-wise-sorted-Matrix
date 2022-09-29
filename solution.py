#User function Template for python3
import numpy as np
class Solution:
    def median(self, matrix, r, c):
    	#code here
    	flat_arr=np.array(matrix).flatten()
    	return(int(np.median(sorted(flat_arr))))
