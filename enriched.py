# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np

nXele = 20                                                                     # Number of elements in the x-direction
nYele = 20                                                                     # Number of elements in the y-direction
lXele = 1/20
lYele = 1/20


nNode  = (nXele+1)*(nYele+1)                                                   # The number of nodes in the domain
NODES  = np.zeros([nNode,100])                                                 # Matrix storing nodal information
XY     = np.zeros([nNode,3])                                                   # Matrix storing nodal position

# Create global node numbering (NN), global xy coordinates (XY), and index of enriched nodes (NODES)
# XY  = [NodeNumber,X-Coordinate,Y-Coordinate]
# NODES = [NodeNumber,EnrichedNodeNumber]
nNode = 0
NN = np.zeros([nXele+1,nYele+1])
for iYNode in np.arange(np.size(NN,0)):
    for iXNode in np.arange(np.size(NN,1)):
        NN[iXNode,iYNode] = nNode+1
        XY[nNode,:] = [nNode+1, iXNode*lXele, iYNode*lYele]
        NODES[nNode,0] = nNode+1
        nNode = nNode+1

# Create a global connectivity matrix (CONNEC) and elemental coordinate matricies
# CONNEC  = [ElementNumber,LocalNode1,LocalNode2,LocalNode3,LocalNode4,InclusionElementNum]
nElem = 0
CONNEC = np.zeros([nXele*nYele,5])
for i in range(nYele):
    for j in range(nXele):
        N1 = NN[j,i]
        N2 = NN[j+1,i]
        N3 = NN[j+1,i+1]
        N4 = NN[j,i+1]
        CONNEC[nElem,:] = [nElem+1, N1, N2, N3, N4]
        nElem = nElem+1;
