def calculatePeakLocs(x,w_val):
    #Import(s)
    from scipy.signal import find_peaks
    import numpy as np
    
    #Action
    fakepeaks, _ = find_peaks(x,width=w_val)
    realpeaks, _ = find_peaks((x*-1),width=w_val)
    outarray = np.concatenate((fakepeaks,realpeaks))
    return(outarray)

def returnDistances(x):
    #Import(s)
    import numpy as np
    
    #Action
    input_array = np.array(x)
    out_array = np.diff(input_array)
    return out_array
    

def sortData(x,y):
    #Import(s)
    import numpy as np
    
    #Action
    unsorted_dates = list(x)
    unsorted_mags = list(y)
    
    sorted_dates = list(np.sort(unsorteddates))
    sorted_mags = []
    for elem in sorted_dates:
        newIndex = sorted_dates.index(elem)
        oldIndex = unsorted_dates.index(elem)
        sorted_mags.append(unsorted_mags[oldIndex])
    
    sorted_dates = np.array(sorted_dates)
    sorted_mags = np.array(sorted_mags)
    
    return sorted_dates, sorted_mags
