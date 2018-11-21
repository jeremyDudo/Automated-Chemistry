import numpy as np

# units in mm

# dimensions of the bed used for storing vials
bedsize = [200, 200]

# number of vials
num_vials = 100      # TEMP
# diameters of vials
diam_vials = 2      # TEMP

# components A, B, etc...
num_inputs = 2      # TEMP
# diameters of components
diam_inputs = 4     # TEMP

# cleaning components
num_clean = 2      # TEMP
# diameters of cleaning vials
diam_clean = 4     # TEMP

# spacing between vials
spacing = 2.5


# positions algorithm

# number of total components:
num_tot = num_vials + num_inputs + num_clean

dict_inpts = {'num_vials':num_vials, 'num_inputs':num_inputs, 'num_clean':num_clean}

# reference position
ref_pos = [0,0]

def increment_pos(ref, current_diameter, min_spacing, bed_size):
    current_center = [0,0]
    
    current_center[0] = ref[0] + current_diameter + min_spacing
    if ref[1] == 0:
        current_center[1] = current_diameter/2
    else:
        current_center[1] = ref[1]

    if current_center[0] > bed_size[0]:
        current_center[0] = current_diameter/2
        current_center[1] += current_diameter + min_spacing
    
    if current_center[1] > bed_size[1]:
        return [bed_size[0], bed_size[1]]
    
    return current_center

final = []

for index in range(num_tot):
    # inputs
    if index < num_inputs:

        final.append(increment_pos(ref_pos, diam_inputs, spacing, bedsize))

    # clean
    if index < num_inputs+num_clean:
        final.append(increment_pos(ref_pos, diam_clean, spacing, bedsize))

    # vials
    else:
        final.append(increment_pos(ref_pos, diam_vials, spacing, bedsize))
    
    ref_pos = final[-1]
    
# for i in range(len(final)):
    # print(final[i])
    # if final[i] == bedsize:
        # del final[i]

print(final)
