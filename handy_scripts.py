##this is a little function for calculating the indices of all the relative extrema in the data. 
##data array is the name of the array of data in question, widthval should be integer value of the minimum distance
##between points (see distance parameter in the scipy.signal.find_peaks documentation)
##Reccomend that you set an array equal to the result of this, e.g. peaks = calculate_peaks(data_aray=,widthval=)
def calculate_peaks(data_array,widthval):
    #Imports
    from scipy.signal import find_peaks
    import numpy as np
    #Action
    fakepeaks, _ = find_peaks(data_array,width=widthval)
    realpeaks, _ = find_peaks((data_array*-1),width=widthval)
    outarray = np.concatenate((fakepeaks,realpeaks))
    return(outarray)
