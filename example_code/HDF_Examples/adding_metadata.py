import time
import numpy as np
import h5py
import os

arr = np.random.randn(1000)

with h5py.File('groups.hdf5', 'w') as f:
    g = f.create_group('Base_Group')
    d = g.create_dataset('default', data=arr)

    g.attrs['Date'] = time.time()
    g.attrs['User'] = 'Me'

    d.attrs['OS'] = os.name

    metadata = {'Date': time.time(),
                'User': 'Me',
                'OS': os.name,}

    f.attrs.update(metadata)

    for k in g.attrs.keys():
        print('{} => {}'.format(k, g.attrs[k]))

    for j in d.attrs.keys():
        print('{} => {}'.format(j, d.attrs[j]))

    for m in f.attrs.keys():
        print('{} => {}'.format(m, f.attrs[m]))

### ADDING A DICTIONARY ###
import json

with h5py.File('groups_dict.hdf5', 'w') as f:
    g = f.create_group('Base_Group')
    d = g.create_dataset('default', data=arr)

    metadata = {'Date': time.time(),
                'User': 'Me',
                'OS': os.name,}

    m = g.create_dataset('metadata', data=json.dumps(metadata))

with h5py.File('groups_dict.hdf5', 'r') as f:
    metadata = json.loads(f['Base_Group/metadata'][()])
    for k in metadata:
        print('{} => {}'.format(k, metadata[k]))