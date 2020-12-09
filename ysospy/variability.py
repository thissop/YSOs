def calculateFluxAsymmetry(x):
    #Description: Returns the flux asymmetry metric M from Bredall et al. 2019
    
    #Import(s)
    import numpy as np
    from scipy import stats

    #Action
    x = list(x)
    
    bottom10 = [] #bottom 10% of magnitude measurements
    top10 = [] #top 10% of magnitude measurements

    for item in x:
        if stats.percentileofscore(x,item) <= 10:
            bottom10.append(item)
        elif stats.percentileofscore(x,item) >= 90:
            top10.append(item)
    
    topandbottom10 = np.array(bottom10+top10)
    m10 = np.mean(topandbottom10)
    x_median = np.median(x) 
    sd = np.std(x)
    M = (m10-x_median)/(sd) #Flux Asymmetry metric, M
    
    return M

def sergisonDistribution(x,percentiles):
    #Import(s)
    import numpy as np
    
    #Action
    mag_list = list(x)
    mean_mag = np.mean(np.array(mag_list))
    lower_percentile,upper_percentile = np.percentile(np.array(mag_list),[percentiles[0], percentiles[1]])
    amp_metric = lower_percentile-upper_percentile
    

    normalized_mags = []

    for item in mag_list:
        normalized_mag = (item-mean_mag)/amp_metric
        normalized_mags.append(normalized_mag)

    return amp_metric, np.array(normalized_mags) # Return results
