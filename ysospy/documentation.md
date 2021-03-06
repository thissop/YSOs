# ysospy 
This is the documentation for all the files and functions in our ysospy package. **Note: this documentation is out of date and missing multiple functions right now**

## Guidelines
#### Naming and Style Conventions 
- Module (file) names should be in snake_case, and functions in camelCase. 
- Example: 
```
from ysospy.plotting_funcs import plotLightCurve
```
#### General notes
- All functions automatically import the modules they require.  
## handy_scripts.py
- **Overview:** this file contains miscellaneous helpful routines. 
### calculatePeakLocs()
- **Summary:** this function uses the ```scipy.find_peaks``` function to return the indices of all relative extrema in an array of magnitudes. 
- **Parameters:**
  - x: the array of magnitudes (which has been previously sorted to a corresponding array of dates)
  - w_val: the required minimal horizontal distance between neighbouring peaks (scipy). This function is different than the ```scipy.find_peaks()``` it's based on because it finds relative minimums as well as relative maximums (it does this by find peaks in the array multiplied by negative one). 
#### Example: 
```
from ysospy.handy_scipts import calculatePeakLocs
peak_indices = calculatePeakLocks(x=example_array_of_mags,w_val=3)
```
### queryCoordSimbad()
- **Summary:** this function returns the string identifier from Simbad for a given input coordinate (it takes the closest result from the Simbad result table).
- **Parameters:**
  - raw_coord: the coordinate for the object in question should be in this form: ```raw_coord='20:50:32.32+44:26:17.4'```.
  - search_radius: the search radius (in arcseconds), should be an integer value. ```search_radius=5``` is the recommended default.
##### Example: 
```
from ysospy.handy_scipts import queryCoordSimbad
obsid = queryCoordSimbad(raw_coord='20:54:24.41+44:48:17.3',search_radius=5)
```
### removeIntervals()
- **Summary:** this function removes parameter defined intervals of data from a sorted array of dates and its corresponding array of mags. 
- **Parameters:**
  - x: the sorted date array. 
  - y: the array of mags, sorted to the date array. 
  - intervals: this should be a list in which the elements are formatted like this: ```'lower_date_bound:upper_date_bound'```. All data in the provided open intervals (lower_date_bound,upper_date_bound) will be removed. So if one wanted to remove all observations between HJD 2456202 and HJD 2456205 in a data set, you should set intervals to ```['2456202:2456205']```.
#### NOTE: This function is a work in progress and is not in handy_scripts.py yet!
### returnDistances()
- **Summary:** this function returns an array of all the distances between date values in an array. It can really be replaced by the one line np.diff(a) function that it's based off (it used to be a more extensive function, but then we realized we can just simplify it to np.diff). 
- **Parameters:** 
  - x: the array of dates in which you wish to find the differences between consecutive elements. 
#### Example:
```
from ysospy.handy_scripts import returnDistances
differences=returnDistances(example_date_array)
```
### sortData()
- **Summary:** this function sorts an array of dates and then sorts its corresponding, provided array of mags to the same order (so corresponding dates and mags are matched). The function returns the sorted dates array first and then returns the sorted mags array (as usual call these individually by indexing the function's output). 
- **Parameters:**
  - x: the date array. 
  - y: the corresponding array of magnitudes. 
#### Example: 
```
from ysospy.handy_scripts import sortData
sorted_dates=sortData(example_dates_array,example_mags_array)[0]
sorted_mags=sortDate(example_dates_array,example_mags_array)[1]
```
## interpolation.py
- **Overview:** this file contains routines that may be a great help when interpolating data.
### returnGoodIntervals()
- **Summary:** this function returns sub-interval arrays that meet certain criteria (maximum distance between elemental points, minimum cardinality of sub-interval) from an input array of dates. This function was originally written to improve interpolation quality by getting rid of regions where the data are sparsely sampled. There are three outputs of the function, which can be called by index. The first is the number of good sub-intervals returned, the second is a list of the good sub-interval arrays of dates, and the third is a list of the good sub-interval mags. 
- **Parameters:**
  - x: the sorted array of dates that you wish to split into good sub-intervals. 
  - y: the sorted array of magnitudes that correspond to the dates in x (as this function goes ahead and modifies the mag array while it's modifying the date array).
  - max_sep: the maximum separation in days allowed between elements in a good sub-interval.  
  - min_card: the minimum cardinality for good intervals. Intervals of data with lesser cardinality will be removed. 
#### Example: 
```
#Import(s)
import matplotlib.pyplot as plt
from ysospy.interpolation import returnGoodIntervals

#Action
num_arrays = returnGoodRegions(x=sgd,y=sgm,max_sep=20,min_card=3)[0] 
x_arrays = returnGoodRegions(x=sgd,y=sgm,max_sep=20,min_card=3)[1]
y_arrays = returnGoodRegions(x=sgd,y=sgm,max_sep=20,min_card=3)[2]
i = 0
colors = ['red','blue','green','yellow','purple','black','brown','pink','orange']
for elem in x_arrays:
    plt.scatter(elem,y_arrays[i],s=4,c=colors[i])
    i += 1
plt.gca().invert_yaxis()
plt.xlabel('HJD')
plt.ylabel('Mag')
plt.show()
```
<img src="https://github.com/thissop/YSOs/blob/main/ysospy/images/mincardinaction.png" width="350" height="230">
*Note that in this example, sgd was a predefined array of dates, and that sgm was a predefined array of mags. Also note that isolated data present in the graph below have been removed in the plot of the returnGoodIntervals output above.
<img src="https://github.com/thissop/YSOs/blob/main/ysospy/images/betterplotofprev.png" width="350" height="230">

## plotting_funcs.py
- **Overview:** this file contains general plotting routines. 
### plotLightCurve()
- **Summary:** you can pass multiple date and mag arrays for plotting. You can also set whether the output is a plot opened in a new window or a saved file (because if we set it to open new plots for hundreds of files...forget *:(){ :|:& };:*, opening hundreds of plots would probably dos your computer just as easily xD).  
- **Parameters:** 
  - x: should be a list of all the names of the date arrays you want to plot. 
  - y: should be a list of all the names of the magnitude arrays you want to plot, with each array in the same indice position as its corresponding date array in x. 
  - colors: a list of colors for each of the lines you want to plot, e.g. colors=['green','red'] will set the first line green and the second red. 
  - x_label: the string label for the x-axis. 
  - y_label: the string label for the y-axis. 
  - plot_title: the string label for the plot title.
  - line_labels: this should be a list of string labels for each of the lines being plotted. They should be in the same list order as the items in x in y. 
  - plot_type: there are four plot_type options:
    1. 'scatter': simple scatter plot
    2. 'plot': simple line plot
    3. 'Scatter_error': scatter plot with error bars 
    4. 'plot_error': line plot with error bars
  - out_type: should either be 'show', which results in plt.show(), or a string filepath (which will save the plot as the given path).
  - error_arrays: the names of the arrays of error values. Set it to 'N/A' when plot_type is not set to either 'scatter_error' or 'plot_error'
#### Example
```
from ysospy.plotting_funcs import plotLightCurve
plotLightCurve(x=[sgd,srd],y=[sgm,srm],colors=['green','red'],x_label='HJD',y_label='Mag',plot_title='Example Plot',line_labels=['Green Band','Red Band'],plot_type='scatter',out_type='show',error_arrays='N/A')
```
<img src="https://github.com/thissop/YSOs/blob/main/ysospy/images/example_plotLightCurve.png" width="350" height="230">

*Note that in this example, sgm and srm represent previously defined arrays of stellar magnitudes sorted by their corresponding date arrays, sgd (sorted green dates) and srd (sorted red dates)* 
## variability.py
- **Overview:** this file contains variability characterization routines. 
### sergisonDistribution()
- **Summary:** this is a function for normalizing magnitudes as in Sergison et al. 2019 §4. It returns two outputs, which can be returned individually by calling  the first or second index of the function, which returns either the AH68 metric or an array of the normalized magnitudes, respectively. 
- **Parameters:**
  - x: an array or list of magnitudes that you wish to normalize and or find the AH68 metric for. 
  - percentiles: the AH68 metric is calculated with the 16th and 84th percentiles (as in the paper), but in case you want to calculate a similiar measure of the amplitude of variability in the array, you can enter the percentiles as integer items in a list and set that list equal to the percentiles argument, e.g. percentiles=[5,95] (the range that confines 90% of the data). 
#### Example: 
```
from ysospy.plotting_funcs import sergisonDistribution()
import seaborn as sns
import matplotlib.pyplot as plt
norm_mags = sergisonDistribution(x=srm,percentiles=[16,84])[1] #percentiles for AH68 metric
sns.histplot(norm_mags,kde=True)
plt.xlabel('Normalized Magnitudes')
plt.ylabel('Counts')
plt.show()
```
<img src="https://github.com/thissop/YSOs/blob/main/ysospy/images/sergisonDist.png" width="350" height="230">
*Note that in this example, srm is a predefined magnitudes array. * 

