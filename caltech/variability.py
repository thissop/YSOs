def sergisonDistribution(x,percentiles):
    #Import(s)
    import numpy as np
    
    #Actions
    mag_list = list(x)
    mean_mag = np.mean(np.array(mag_list))
    lower_percentile,upper_percentile = np.percentile(np.array(mag_list),[percentiles[0], percentiles[1]])
    amp_metric = lower_percentile-upper_percentile
    

    normalized_mags = []

    for item in mag_list:
        normalized_mag = (item-mean_mag)/amp_metric
        normalized_mags.append(normalized_mag)

    return amp_metric, np.array(normalized_mags) # Return results
