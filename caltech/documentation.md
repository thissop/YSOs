# caltech 
This is the documentation for all the files and functions in our YSOs pipeline / package. 

## plot_data.py
- **Overview:** this file provides a standardized general plotting routine. 
- **Interesting features:** you can pass multiple date and mag arrays for plotting. You can also set whether the output is a plot opened in a new window or a saved file (because if we set it to open new plot for hundreds of files...forget *:(){ :|:& };:* that would probably ddos your computer just as easily xD).  
- **Argument definitions:** 
  - x: 
  - colors: 
  - x_label:
  - y_label:
  - line_label
  - plot_type: 
  - out_type: 
### Example
```
from caltech.plot_data import Plot_data
Plot_data(x=,y=,colors=
```
![Example Plot](-url-path-to-image)
