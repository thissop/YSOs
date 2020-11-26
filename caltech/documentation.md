# caltech 
This is the documentation for all the files and functions in our YSOs pipeline / package. 

## plot_data.py
- **Overview:** this file provides a standardized general plotting routine. 
- **Interesting features:** you can pass multiple date and mag arrays for plotting on a figure and you can also set whether the output is a saved plot or an opened plot (we're probably going to use the saved plot function when we get into lots of data because it would be very annoying to have tens of plots opening up).  
- **Argument definitions:** 
  - x: 
### Example
```
from caltech.plot_data import Plot_data
Plot_data(x=,y=,colors=
