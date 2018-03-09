import h5py
import numpy as np

with h5py.File('resize_dataset.hdf5', 'w') as f:
    d = f.create_dataset('dataset', (100, ),  maxshape=(500, ))
    d[:100] = np.random.randn(100)
    d.resize((200,))
    d[100:200] = np.random.randn(100)

with h5py.File('resize_dataset.hdf5', 'r') as f:
    dset = f['dataset']
    print(dset[99])
    print(dset[199])

with h5py.File('resize_dataset.hdf5', 'a') as f:
    dset = f['dataset']
    dset.resize((300,))
    dset[:200] = 0
    dset[200:300] = np.random.randn(100)

with h5py.File('resize_dataset.hdf5', 'r') as f:
    dset = f['dataset']
    print(dset[99])
    print(dset[199])
    print(dset[299])