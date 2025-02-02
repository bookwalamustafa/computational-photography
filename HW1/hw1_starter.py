# hw1_starter.py
# This starter code requires functions in dolly_zoom.py to work

from dolly_zoom import *
import matplotlib.pyplot as plt
import os
import imageio
import numpy as np

def generate_gif():
    """
    Generates 'cube.gif' by rotating the cube from 0 to 2π 
    around the Y-axis, saving frames, then combining them into one GIF.
    """
    n_frames = 30
    if not os.path.isdir("frames"):
        os.mkdir("frames")
    fstr = "frames/%d.png"
    
    # Generate frames
    for i, theta in enumerate(np.linspace(0, 2*np.pi, n_frames)):
        fname = fstr % i
        # Render the cube (makes a figure in memory, doesn't show)
        renderCube(f=15, t=(0,0,3), R=rotY(theta))
        # Save the figure to a PNG
        plt.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close()  # close the figure to avoid memory issues

    # Create the GIF from those frames
    with imageio.get_writer("cube.gif", mode='I') as writer:
        for i in range(n_frames):
            frame_path = fstr % i
            # Read the PNG using matplotlib
            frame = plt.imread(frame_path)  # returns float array in [0..1]
            # Usually imageio can handle float images directly.
            # If you want to be safe, convert them to 8-bit:
            frame_8bit = (frame*255).astype(np.uint8)
            writer.append_data(frame_8bit)
            # Remove the individual PNG
            os.remove(frame_path)

    # Clean up the empty frames folder
    os.rmdir("frames")
    print("Successfully generated 'cube.gif'.")

def check_commutativity():
    """
    Rotates the cube using:
      1) rotX(π/4) then rotY(π/4)
      2) rotY(π/4) then rotX(π/4)
    Shows that 3D rotations generally do not commute.
    """
    theta = np.pi / 4
    R1 = rotX(theta) @ rotY(theta)
    R2 = rotY(theta) @ rotX(theta)
    
    # First orientation
    renderCube(f=3, t=(0,0,3), R=R1)
    plt.title("rotX(π/4), then rotY(π/4)")
    plt.show()

    # Second orientation
    renderCube(f=3, t=(0,0,3), R=R2)
    plt.title("rotY(π/4), then rotX(π/4)")
    plt.show()

def find_projection_angles():
    """
    Demonstrates choosing rotation angles so that one cube diagonal
    'collapses' into a single point in the perspective projection.
    Also renders the same orientation in orthographic projection.
    """
    # Example angles that cause diagonal collapse
    thetaY = -np.pi / 4
    thetaX = np.arctan(1 / np.sqrt(2))  # ~35.264 deg

    R_diagonal = rotX(thetaX) @ rotY(thetaY)
    print("Using R = rotX({:.3f}) @ rotY({:.3f})".format(thetaX, thetaY))

    # Perspective Projection
    renderCube(f=3, t=(0,0,3), R=R_diagonal)
    plt.title("Diagonal Collapse (Perspective)")
    plt.show()

    # Orthographic Projection
    renderCube(f=3, t=(0,0,3), R=R_diagonal, orthographic=True)
    plt.title("Diagonal Collapse (Orthographic)")
    plt.show()

if __name__ == "__main__":
    # 1) Generate rotating cube GIF
    generate_gif()

    # 2) Check commutativity of rotations
    check_commutativity()

    # 3) Show diagonal collapse in perspective, then orthographic
    find_projection_angles()
