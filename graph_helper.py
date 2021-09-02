import math
import numpy as np
def smoothen_graph(graph, step):
    graph_len = len(graph)
    avg_list = np.array([])
    
    # Get the size of the array with the given step
    size = math.floor(graph_len/step)
    rng = np.arange(size*step,step = step)
    for i in rng:
        if i+step-1 < graph_len:
            # Get the median of [st] number of consecutive pixels
            avg_list = np.append(avg_list, np.median(graph[i:i+step-1]))
    
    return (avg_list, size)