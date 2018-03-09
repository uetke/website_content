import h5py
import numpy as np

arr1 = np.random.randn(10000)
arr2 = np.random.randn(10000)

with h5py.File('complex_read.hdf5', 'w') as f:
    f.create_dataset('array_1', data=arr1)
    f.create_dataset('array_2', data=arr2)

with h5py.File('complex_read.hdf5', 'r') as f:
    d1 = f['array_1']
    d2 = f['array_2']

    data = d2[d1[:]>0]

print('The length of data without a for loop: {}'.format(len(data)))

with h5py.File('complex_read.hdf5', 'r') as f:
    d1 = f['array_1']
    d2 = f['array_2']

    data = []

    for i in range(len(d1)):
        if d1[i] > 0:
            data.append(d2[i])

print('The length of data with a for loop: {}'.format(len(data)))
