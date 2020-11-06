import ascii 

r = ascii.read('./lightcurves/ztf/lc_’+cfilename+'_r.tbl', format='ipac', delimiter='|')

columns,rows = len(r[0]),len(r)
print 'number of columns =',columns
print 'number of rows =',rows
print 'example line: '
print(r[0])

#Where the variable “cfilename” has been previously set to be the object coordinates— as a string — e.g. "20:32:30.44+43:57:41.9"

#Note: the path './lightcurves/ztf/lc_’+cfilename+'_r.tbl' is not going to be the same path as the one on your computer lol. 
