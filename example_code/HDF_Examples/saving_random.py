import h5py
import numpy as np

### WRITE AND READ A RANDOM ARRAY TO HDF5 FILE ###
arr = np.random.randn(1000)

with h5py.File('random.hdf5', 'w') as f:
    dset = f.create_dataset("default", data=arr)

with h5py.File('random.hdf5', 'r') as f:
    data = f['default']
    print(min(data))
    print(max(data))
    print(data[2:5])
    print(type(data))

### READ SPECIFIC VALUES FROM DISK ###
with h5py.File('random.hdf5', 'r') as f:
   data_set = f['default']
   data = data_set[:10]

print(data[1])
# print(data_set[1]) # It will give errors because the file is already closed
print('data type: {}'.format(type(data)))
print('data_set type: {}'.format(type(data_set)))

### WRITE TO SPECIFIC POSITION OF DATA SET ###
with h5py.File('random.hdf5', 'w') as f:
    dset = f.create_dataset("default", (1000,))
    dset[10:20] = arr[50:60]

with h5py.File('random.hdf5', 'r') as f:
    data = f['default'][:20]
print(data[:])


### THIS DOESN'T SAVE ANYTHING TO DISK ###
arr = np.random.randn(1000)

with h5py.File('random_nothing.hdf5', 'w') as f:
    dset = f.create_dataset("default", (1000,))
    dset = arr

with h5py.File('random_nothing.hdf5', 'r') as f:
    data = f['default'][:]
print("Minimum: {}, Maximum: {}".format(min(data), max(data)))