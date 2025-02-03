# This starter code requires functions in the Dolly Zoom Notebook to work

from dolly_zoom import *
import matplotlib.pyplot as plt
import os
import imageio
import numpy as np

# Call this function to generate gif. make sure you hvae rotY() implemented.
def generate_gif():
    n_frames = 30
    if not os.path.isdir("frames"):
        os.mkdir("frames")
    fstr = "frames/%d.png"
    for i, theta in enumerate(np.linspace(0, 2*np.pi, n_frames)):
        fname = fstr % i
        renderCube(f=15, t=(0,0,3), R=rotY(theta))
        plt.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close()

    with imageio.get_writer("cube.gif", mode='I') as writer:
        for i in range(n_frames):
            frame_path = fstr % i
            frame = plt.imread(frame_path)
            frame_8bit = (frame*255).astype(np.uint8)
            writer.append_data(frame_8bit)
            os.remove(frame_path)

    os.rmdir("frames")

def check_commutativity():
    theta = np.pi / 4
    R1 = rotX(theta) @ rotY(theta)
    R2 = rotY(theta) @ rotX(theta)
    
    renderCube(f=15, t=(0,0,3), R=R1)
    plt.title("rotX(π/4), followed by rotY(π/4)")
    plt.show()

    renderCube(f=15, t=(0,0,3), R=R2)
    plt.title("rotY(π/4), followed by rotX(π/4)")
    plt.show()

def find_projection_angles():
    R_diagonal = rotX(np.arctan(1 / np.sqrt(2))) @ rotY(np.pi / 4)
    renderCube(f=15, t=(0,0,3), R=R_diagonal)
    plt.show()
    renderCube(f=3, t=(0,0,3), R=R_diagonal, orthographic=True)
    plt.show()

if __name__ == "__main__":
    generate_gif()
    check_commutativity()
    find_projection_angles()