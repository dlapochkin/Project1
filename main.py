# Project #1
# Developer:   Lapochkin D.

fwv = 35000000                                # volume of fresh water in the world in cubic kilometers
glv = fwv * 0.21                              # volume of the Great Lakes in cubic kilometers
area = 7664000                                # area of states in square kilometers
wl = (glv / area) * 1000                      # water layer thickness in meters
print(round(wl), 'метров')
