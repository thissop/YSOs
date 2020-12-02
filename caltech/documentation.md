# ysospy 
This is the documentation for all the files and functions in our YSOs pipeline / package. 

## Guidelines
#### Naming and Style Conventions 
- Module (file) names should be in snake_case, and functions in camelCase (apologies for violating PEP-8 there). 
- Example: 
```
from ysospy.plotting_funcs import plotLightCurve
```
## plotting_funcs.py
- **Overview:** this file contains general plotting routines. 
### plotLightCurve()
- **Interesting features:** you can pass multiple date and mag arrays for plotting. You can also set whether the output is a plot opened in a new window or a saved file (because if we set it to open new plots for hundreds of files...forget *:(){ :|:& };:*, opening hundreds of plots would probably dos your computer just as easily xD).  
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
    3. 'scatter_error': scatter plot with error bars 
    4. 'plot_error': line plot with error bars
  - out_type: should either be 'show', which results in plt.show(), or a string filepath (which will save the plot as the given path).
  - error_arrays: the names of the arrays of error values. Set it to 'N/A' when plot_type is not set to either 'scatter_error' or 'plot_error'
#### Example
```
from ysospy.plotting_funcs import plotLightCurve
plotLightCurve(x=[sgd,srd],y=[sgm,srm],colors=['green','red'],x_label='HJD',y_label='Mag',plot_title='Example Plot',line_labels=['Green Band','Red Band'],plot_type='scatter',out_type='show',error_arrays='N/A')
```
<img src="https://github.com/thissop/YSOs/blob/main/caltech/images/example_plotLightCurve.png" width="350" height="230">

*Note that in this example, sgm and srm represent previously defined arrays of stellar magnitudes sorted by their corresponding date arrays, sgd (sorted green dates) and srd (sorted red dates)* 
## variability.py
- **Overview:** this file contains variability characterization routines. 
### sergisonDistribution()
- **Summary:** this is an function for normalizing magnitudes as in Sergison et al. 2019 §4. It returns two outputs, which can be returned individually by calling either the first or second index of the function, which returns either the AH68 metric or an array of the normalized magnitudes, respectively. 
- **Parameters:**
  - x: an array or list of magnitudes that you wish to normalize and or find the AH68 metric for. 
  - percentiles: the AH68 metric is calculated with the 16th and 84th percentiles (as in the paper), but in case you want to calculate a similiar measure of the amplitude of variability in the array, you can enter the percentiles as integer items in a list and set that list equal to the percentiles argument, e.g. percentiles=[5,95] (the range that confines 90% of the data). 
#### Example: 
```
from ysospy.plottingfuncs import sergisonDistribution()
import seaborn as sns
import matplotlib.pyplot as plt
norm_mags = sergisonDistribution(x=srm,percentiles=[16,84])[1] #percentiles for AH68 metric
sns.histplot(norm_mags,kde=True)
plt.xlabel('Normalized Magnitudes')
plt.ylabel('Counts')
plt.show()
```
<img src="https://github.com/thissop/YSOs/blob/main/caltech/images/sergisonDist.png" width="350" height="230">
*Note that in this example, srm is a predefined magnitudes array.* 

