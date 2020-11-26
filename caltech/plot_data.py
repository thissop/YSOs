def Plot_data(x,y,colors,x_label,y_label,plot_title,line_labels,plot_type,out_type,error_arrays):
    #Imports
    import matplotlib.pyplot as plt 
    import numpy as np
    
    #Action
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    item_index = 0
    for item in x:
        if plot_type == 'scatter':
            plt.scatter(item,y[item_index],s=2,c=(colors[item_index]),label=line_labels[item_index])
        elif plot_type == 'plot':
            plt.plot(item,y[item_index],markersize=2,linewidth=1,color=colors[item_index],label=line_labels[item_index])
        elif plot_type == 'scatter_error':
            plt.error(item,y[item_index],yerr=error_arrays[item_index],marker='o',color=colors[item_index],ms=2,linewidth=0,label=line_labels[item_index])
        elif plot_type == 'plot_error':
            plt.error(item,y[item_index],yerr=error_arrays[item_index],marker='o',color=colors[item_index],ms=2,linewidth=0,label=line_labels[item_index])
        item_index = item_index+1
    #Calculate maximum and minimum magnitudes for ylim
    
    conglomerate_list = []
    for item in y:
        for elem in item:
            conglomerate_list.append(elem)
    
    global_max = np.max(conglomerate_list)+0.2
    global_min = np.min(conglomerate_list)-0.2


    plt.legend()
    plt.ylim(global_max,global_min)

    if out_type == 'save':
        plt.show()
    else: 
        plt.savefig(out_type)
