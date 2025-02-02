# dolly_zoom.py
# Rendering a cube with varying focal length / width
# Drexel CS 435 Winter 24-25

import matplotlib
import matplotlib.pyplot as plt
from itertools import product
import numpy as np

### Helper stuff
def rr():
    # Return a random rotation matrix
    U, _, Vt = np.linalg.svd(np.random.uniform(size=(3,3)))
    # Don't change the handedness...
    return np.dot(U, Vt) / np.linalg.det(U) / np.linalg.det(Vt)

def generateCube():
    """
    Return an Nx6 collection of the lines of a unit cube ranging in
    x, y from -0.5 to 0.5, and z from 0 to 1, with edges identified.
    """
    lines = []
    for x,y,z in product([0,1],[0,1],[0,1]):
        for dx, dy, dz in [(1,0,0),(-1,0,0),
                           (0,1,0),(0,-1,0),
                           (0,0,1),(0,0,-1)]:
            xp, yp, zp = x+dx, y+dy, z+dz
            # If still inside [0,1]^3, it's a valid edge
            if min([xp,yp,zp]) >= 0 and max([xp,yp,zp]) <= 1:
                lines.append((x-0.5,y-0.5,z-0.5,
                              xp-0.5,yp-0.5,zp-0.5))
    return np.vstack(lines)

def xyrange(pL):
    """
    Given Nx4 lines [u1, v1, u2, v2],
    return the range of u and the range of v for the entire set.
    """
    X = np.vstack([pL[:,0], pL[:,2]])
    Y = np.vstack([pL[:,1], pL[:,3]])
    return np.max(X) - np.min(X), np.max(Y) - np.min(Y)

def projectLines(f, R, t, L, orthographic=False):
    """
    Given:
      f  -- scalar focal length
      R  -- 3x3 rotation matrix
      t  -- 3-element translation vector
      L  -- Nx6 lines [x1, y1, z1, x2, y2, z2]
      orthographic -- if True, do orthographic projection instead of perspective

    Return:
      Nx4 lines [u1, v1, u2, v2] in projected 2D coords.
    """
    pL = np.zeros((L.shape[0],4))
    for i in range(L.shape[0]):
        # Rotate + translate each endpoint
        p  = R @ L[i,:3] + t
        pp = R @ L[i,3:] + t
        
        if orthographic:
            # Orthographic: (u, v) = (x, y)
            pL[i,:2] = p[0],  p[1]
            pL[i,2:] = pp[0], pp[1]
        else:
            # Perspective: (u, v) = (x*f/z, y*f/z)
            pL[i,:2] = (p[0]*f/p[2],  p[1]*f/p[2])
            pL[i,2:] = (pp[0]*f/pp[2], pp[1]*f/pp[2])
    return pL

def renderCube(f=1, scaleFToSize=None, t=(0,0,1), R=np.eye(3), orthographic=False):
    """
    Render the cube using either perspective or orthographic projection.
    """
    L = generateCube()
    t = np.array(t)
    pL = projectLines(f, R, t, L, orthographic=orthographic)

    # If we want to rescale f to match a desired image size, do that now
    if scaleFToSize is not None:
        xRange, yRange = xyrange(pL)
        geoMean = (xRange * yRange) ** 0.5
        f = (f / geoMean) * scaleFToSize
        pL = projectLines(f, R, t, L, orthographic=orthographic)

    # Make a new figure (don't show it yet!)
    plt.figure()
    projection_type = "Orthographic" if orthographic else "Perspective"
    plt.title(f"Cube ({projection_type}) @ [x={t[0]}, y={t[1]}, z={t[2]}], f={f:.2f}")

    color_cycle = ['yellow', 'red', 'orange', 'green', 'cyan', 'brown', 'blue']
    # color_cycle = ['red', 'green', 'blue', 'orange', 'magenta', 'purple']

    # Plot each edge
    for i in range(pL.shape[0]):
        u1, v1, u2, v2 = pL[i,:]
        # Using a visible color like black or red
        edge_color = color_cycle[i % len(color_cycle)]
        plt.plot((u1, u2), (v1, v2), color=edge_color, linewidth=2)

    plt.axis('square')
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    # DO NOT call plt.show() here if we are auto-saving frames
    # plt.show()

def rotY(theta):
    """
    Rotation about the y-axis by 'theta' (radians), right-hand rule.
    """
    return np.array([
        [ np.cos(theta),  0, np.sin(theta)],
        [           0,    1,           0 ],
        [-np.sin(theta),  0, np.cos(theta)]
    ])

def rotX(theta):
    """
    Rotation about the x-axis by 'theta' (radians), right-hand rule.
    """
    return np.array([
        [1,            0,             0           ],
        [0, np.cos(theta),  -np.sin(theta)],
        [0, np.sin(theta),   np.cos(theta)]
    ])
