def calculatePeaks(x,w_val):
    #Import(s)
    from scipy.signal import find_peaks
    import numpy as np
    
    #Action
    fakepeaks, _ = find_peaks(x,width=w_val)
    realpeaks, _ = find_peaks((x*-1),width=w_val)
    outarray = np.concatenate((fakepeaks,realpeaks))
    return(outarray)
