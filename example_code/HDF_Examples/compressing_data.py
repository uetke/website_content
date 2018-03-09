import h5py
import numpy as np

arr = 128 * np.random.randn(100000)

with h5py.File('integer_1_compr.hdf5', 'w') as f:
    d = f.create_dataset('dataset', (100000,), dtype='i1', compression="gzip", compression_opts=4)
    d[:] = arr
    f.flush()

with h5py.File('integer_8_compr.hdf5', 'w') as f:
    d = f.create_dataset('dataset', (100000,), dtype='i8', compression="gzip", compression_opts=4)
    d[:] = arr
    f.flush()

with h5py.File('float_compr.hdf5', 'w') as f:
    d = f.create_dataset('dataset', (100000,), dtype='f16', compression="gzip", compression_opts=4)
    d[:] = arr
    f.flush()
