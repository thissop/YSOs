import matplotlib.pyplot as plt 
from astropy.io import ascii
from matplotlib import rcParams
import numpy as np
import seaborn as sns
from scipy import interpolate

#Useful functions
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

#Get data .... change the two paths below on your own work 
green_path = '/home/thaddaeus/FMU/HRL/LAH/secondExercise/ZTF18aaxykqu_light_curve_files/lc_203230.44+435741.9_g.tbl'
red_path = '/home/thaddaeus/FMU/HRL/LAH/secondExercise/ZTF18aaxykqu_light_curve_files/lc_203230.44+435741.9_r.tbl'
g = ascii.read(green_path,format='ipac',delimiter='|')
r = ascii.read(red_path,format='ipac',delimiter='|')

green_dates = np.array(g['hjd'])-(2.458*10**6)
green_mags = np.array(g['mag'])
red_dates = np.array(r['hjd'])-(2.458*10**6)
red_mags = np.array(r['mag'])

#sort the data
srd = sort_data(unsorteddates=red_dates,unsortedmags=red_mags)[0] #red dates
srm = sort_data(unsorteddates=red_dates,unsortedmags=red_mags)[1] #red mags
sgd = sort_data(unsorteddates=green_dates,unsortedmags=green_mags)[0] #green dates
sgm = sort_data(unsorteddates=green_dates,unsortedmags=green_mags)[1] #green mags

#Interpolate for missing green data
f = interpolate.interp1d(sgd,sgm,kind='slinear')
new_sgd = []
for item in srd:
    if item not in sgd:
        if item < max(sgd) and item > min(sgd):
            new_sgd.append(item)

new_sgd=np.array(new_sgd)
new_sgm = f(new_sgd)
srm = srm[:-1] #size matching should be automated (later)

#plot
sns.set_style('darkgrid')
rcParams['font.family']='Nimbus Roman'
plt.title('Color-Magnitude Diagram for ZTF18aaxykqu')
plt.ylabel('G')
plt.xlabel('(G-R)')
plt.scatter((new_sgm-srm),new_sgm,c='black',s=2)

plt.show()
