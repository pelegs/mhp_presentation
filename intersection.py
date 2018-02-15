import numpy as np

# note if gy == 0 and gx == 0 then the circles are tangent and there is only one solution
# but that one solution will just be duplicated as the code is currently written
def intersection(x1, y1, r1, x2, y2, r2):
    if x1==x2 and y1==y2 and r1==r2:
        return list()

    cdx = x1-x2
    cdy = y2-y2
    R = np.sqrt(cdx**2 + cdy**2)
    if not(np.abs(r1 - r2) <= R and R <= r1 + r2):
        return list()

    R2 = R**2
    R4 = R**4
    a = (r1*r1 - r2*r2) / (2 * R2)
    r2r2 = (r1**2 - r2**2)
    c = np.sqrt(2 * (r1*r1 + r2*r2) / R2 - (r2r2 * r2r2) / R4 - 1)
    
    fx = (x1+x2) / 2 + a * (x2 - x1)
    gx = c * (y2 - y1) / 2
    ix1 = fx + gx
    ix2 = fx - gx

    fy = (y1+y2) / 2 + a * (y2 - y1)
    gy = c * (x1 - x2) / 2
    iy1 = fy + gy
    iy2 = fy - gy

    return (np.rad2deg(np.arctan2(iy1-y1, ix1-x1)),
	    np.rad2deg(np.arctan2(iy2-y1, ix2-x1)))

pts = intersection(195, 0, 260, 0, 0, 292)
pts = intersection(-220, -220, 310, 0, 0, 292)
print(pts)
