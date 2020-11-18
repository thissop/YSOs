##this is a little function for calculating the indices of all the relative extrema in the data. 
##data array is the name of the array of data in question, widthval should be integer value of the minimum distance
##between points (see distance parameter in the scipy.signal.find_peaks documentation)
##Reccomend that you set an array equal to the result of this, e.g. peaks = calculate_peaks(...)
def calculate_peaks(data_array,widthval):
    #Imports
    from scipy.signal import find_peaks
    import numpy as np
    #Action
    fakepeaks, _ = find_peaks(data_array,width=widthval)
    realpeaks, _ = find_peaks((data_array*-1),width=widthval)
    outarray = np.concatenate((fakepeaks,realpeaks))
    return(outarray)

##This is a handy script for sorting both an array of mags and its array of dates
##it first sorts the dates array, and then sorts the magnitudes based on this array
##unsorted dates and unsorted mags must be pre-assigned variables that can be numpy arrays or 
##lists from the data files; the function returns two numpy arrays, the first is an array of sorted dates,
##the second is an array of sorted mags. To assign the array of sorted mags to a variable, set the variable equal
##to the 0th index of the function, e.g. sorted_dates = sort_data(...)[0]. Conversely, to set a variable equal to the
##sorted mags, assign the variable to the 1st index of the function, e.g. sorted_mags = sort_data(...)[1]
##This function exists because a lot of functions aren't working on the data arrays when they aren't sorted 
##(e.g. searching for local extrema in the data) 
##example: srd = sort_data(unsorteddates=red_dates,unsortedmags=red_mags)[0]
def sort_data(unsorteddates,unsortedmags):
    #Import
    import numpy as np
    #Action
    unsorteddates= list(unsorteddates)
    unsortedmags=list(unsortedmags)
    
    sorteddates=list(np.sort(unsorteddates))
    sortedmags = []
    for elem in sorteddates:
        newIndex = sorteddates.index(elem)
        oldIndex = unsorteddates.index(elem)
        sortedmags.append(unsortedmags[oldIndex])
    
    sorteddates = np.array(sorteddates)
    sortedmags = np.array(sortedmags)
    
    return sorteddates, sortedmags


##This function returns an array of differences between values in another array. Example: green_differences = find_differences(x=sgd)
def find_differences(x):
    #Imports
    import numpy as np
    #Action
    inputlist = list(x)
    outlist = []
    for elem in inputlist:
        followindex = inputlist.index(elem)+1
        if followindex+1 <= len(inputlist):
            difference = inputlist[followindex]-elem
            outlist.append(difference)
    outarray = np.array(outlist)
    return(outarray)
