# Meeting Goals
1. CMD Diagrams with linear fits (opting for three fits here, ols on all data, RANSAC, and OLS on RANSAC-identified inliers). Labels: line labels, and r^2 values for both OLS regressions. 
2. Histogram of CMD slopes (take these slopes from the OLS on RANSAC identified inliers) where fits are signfificant...maybe four subplot histograms, each with its own r^2 cuttoff, e.g. ```axs[0,0]``` only has slopes with r^2 > 0.95, ```axs[0,1]``` has slopes with r^2 > 0.9, ```axs[1,0]``` has slopes with r^2 > 0.8, and ```axs[1,1]``` has slopes with r^2 > 0.68. 
3. Two plots, each with four subplots. First plot plots slope values vs nu values (subplots with same r^2 criteria as above), and second plot plots slope values vs std values (same as the slopes vs nu). 

Save results to csv files? 

# Meeting notes
### RANSAC
  - #### Resources
    - sklearn example: https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html
    - Medium article: https://medium.com/@iamhatesz/random-sample-consensus-bd2bb7b1be75
    - sklearn documentation: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor.predict
    
    
    
### Calculate standard deviation
  - I reccomend using ```np.std(x,ddof=1)``` (x = array of mags, ddof = delta degrees of freedom, makes divisor N - ddof; hence ```ddof=1``` returns the sample standard deviation.
### Sokolovsky Nu Metric 
  - Definition from Sokolovsky et al. 2017:
  
    <img src="https://github.com/thissop/YSOs/blob/main/Variability%20Investigation%20Notes/Screen%20Shot%202021-01-07%20at%2012.13.12%20PM.png" width="500" height="600">
  - I wrote up a code about this a bit ago (you may remember me getting slightly roasted for messing it up lol). I fixed the code recently so it works perfectly. 
    - Here's the code (x = array of mags, xerr = array of magerrs that correspond to mags in x): 
    ```
    def sokolovskyNu(x,xerr):
      #Import(s)
      import numpy as np

      #Action
      # [ (m-e)max - (m+e)min ] / [ (m-e)max + (m+e)min ]

      x = np.array(x)
      xerr = np.array(xerr)

      x_minus_xerr = x-xerr
      x_plus_xerr = x+xerr

      min_val = np.amin(x_plus_xerr)
      max_val = np.amax(x_minus_xerr)

      nu = (max_val-min_val)/(max_val+min_val)
      return nu
    ```
    
### For the CMD plots
- I'd include three lines: OLS line on all data, best fit RANSAC line, and OLS line on the RANSAC identified set of inliers. Plz label the plot with the value of each OLS line's r^2 value. 
- We need to include error measurements on every CMD point. yerr array should be symmetric array of magerrs for every green point. We will estimate xerr from this equation: ```\sqrt{nge^2 + re^2}```, where nge is the magerr on the green data point that is closest to the interpolated point (in terms of time in MJD), and re is the magerr on the red point you used. Use plt.errorbar for these. 

### MISC. 
- Currently working on getting data files for everyone to use. First folder will have all the usual data files, second directory will have .csv files with CMD information (each line will probably be formatted like this: ```g-r,g,g-r_err,g_err```).
