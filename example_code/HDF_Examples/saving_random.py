import h5py
import numpy as np

arr = np.random.randn(1000)

with h5py.File('random.hdf5', 'w') as f:
    dset = f.create_dataset("default", (1000,))
    dset[:] = arr

with h5py.File('random.hdf5', 'r') as f:
    data = f['default']
    print(min(data))
    print(max(data))
    print(data[2:5])
    print(type(data))

f = h5py.File('random.hdf5', 'r')
data = f['default'][:10]
f.close()
print(data[1])

f = h5py.File('random.hdf5', 'w')
dset = f.create_dataset("default", (1000,))
dset[10:20] = arr[50:60]
f.close()

f = h5py.File('random.hdf5', 'r')
data = f['default'][:20]
f.close()
print(data)