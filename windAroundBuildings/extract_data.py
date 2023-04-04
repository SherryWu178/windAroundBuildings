#Import the useful library
from paraview.simple import *
import numpy as np
from paraview import numpy_support as ns
import vtk

# Get active boundary (actualy a 3D wing from a mesh with pressure data)
Junction = GetActiveSource()

# For several positions on the z axis
for z in np.arange(2e-6,28e-6,2e-6):
    Slice1 = Slice(Input=Junction)
    Slice1.SliceType = "Plane"
    Slice1.SliceOffsetValues = [0.0]
    Slice1.SliceType.Origin = [0.0, 0.0, z]
    Slice1.SliceType.Normal = [0.0, 0.0, 1.0]
    Z.append(Slice1)

# Took two slice as an example but for multiple ones, just repeat the procedure

Slice1 = FindSource("Slice1")
m1 = MergeBlocks(Slice1)
d1 = servermanager.Fetch(m1)
d1.GetCellData()
u1= ns.vtk_to_numpy(d1.GetCellData().GetArray("U"))
#numCells = u1.GetNumberOfCells()

Slice2 = FindSource("Slice2")
m2 = MergeBlocks(Slice2)
d2 = servermanager.Fetch(m2)
d2.GetCellData()
u2=ns.vtk_to_numpy(d2.GetCellData().GetArray("U"))

uvg = (u1+u2)/2