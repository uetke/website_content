import numpy as np
import h5py

with h5py.File('several_datasets.hdf5', 'w') as f:
    dset_int_1 = f.create_dataset('integers', (10, ), dtype='i1')
    dset_int_8 = f.create_dataset('integers8', (10, ), dtype='i8')
    dset_complex = f.create_dataset('complex', (10, ), dtype='c16')

    dset_int_1[0] = 1200
    dset_int_8[0] = 1200.1
    dset_complex[0] = 3 + 4j

with h5py.File('several_datasets.hdf5', 'r') as f:
    int_1 = f['integers'][0]
    int_8 = f['integers8'][0]
    comp = f['complex'][0]
    print('Retrieved integer 1: {}'.format(int_1))
    print('Retrieved integer 8: {}'.format(int_8))
    print('Retrieved complex number: {}'.format(comp))


arr = np.random.randn(100000)

f = h5py.File('integer_1.hdf5', 'w')
d = f.create_dataset('dataset', (100000,), dtype='i1')
d[:] = arr
f.close()

f = h5py.File('integer_8.hdf5', 'w')
d = f.create_dataset('dataset', (100000,), dtype='i8')
d[:] = arr
f.close()

f = h5py.File('float.hdf5', 'w')
d = f.create_dataset('dataset', (100000,), dtype='f16')
d[:] = arr
f.close()