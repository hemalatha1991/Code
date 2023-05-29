import os

import nipype.interfaces.matlab as mlab

mlab.MatlabCommand.set_default_paths('/usr/local/MATLAB/toolbox_latest/spm12')

import nipype.interfaces.spm as spm

print('Loop over dirs and files:')
path = '/home/hemalatha/follow_up_images/T21/'

subdirs = [x[0] for x in os.walk(path)]
for subdir in subdirs:
    files = os.walk(subdir).__next__()[2]
    if (len(files) > 0):
        norm12 = spm.Normalize12()
        x = []
        for file in files:
            if '_T1W_' in file:
                print(str(os.path.join(subdir, file)))
                norm12.inputs.image_to_align = str(os.path.join(subdir, file))
                x.append(str(os.path.join(subdir, file)))
            else:
                x.append(str(os.path.join(subdir, file)))
        print(str(x))
        norm12.inputs.apply_to_files = x
        norm12.inputs.write_voxel_sizes = [1, 1, 1]
        norm12.run()
