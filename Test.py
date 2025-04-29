import torch
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
import random
# PyTorch3D
try:
    import pytorch3d
    from pytorch3d.loss import chamfer_distance
    from pytorch3d.ops import sample_points_from_meshes
    print("PyTorch3D is installed and ready.")
except ImportError:
    print("PyTorch3D is not installed. Please follow the instructions above.")