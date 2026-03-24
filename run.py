import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import shutil
import namelist
import sys
from scripts import generate_land_masks
from util import compute

def run_model():
    f_base = '%s/%s/' % (namelist.output_directory, namelist.exp_name)
    os.makedirs(f_base, exist_ok = True)
    print('Saving model output to %s' % f_base)

    #generate_land_masks.generate_land_masks()
    #compute.compute_downscaling_inputs()

    print('Running tracks for North Atlantic basin...')
    fn_track = compute.run_downscaling('NA')
    return fn_track
