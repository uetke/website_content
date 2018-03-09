import numpy as np
import h5py

arr = np.random.randn(1000)

with h5py.File('groups.hdf5', 'w') as f:
    g = f.create_group('Base_Group')
    gg = g.create_group('Sub_Group')

    d = g.create_dataset('default', data=arr)
    dd = gg.create_dataset('default', data=arr)



with h5py.File('groups.hdf5', 'r') as f:
    for k in f.keys():
        print(k)
        for j in f[k].keys():
            print(j)


    d = f['Base_Group/default']
    dd = f['Base_Group/Sub_Group/default']
    print(d[1])
    print(dd[1])

def get_all(name):
    print(name)

with h5py.File('groups.hdf5', 'r') as f:
    f.visit(get_all)

def get_all(name):
    if 'Sub_Group' in name:
        return name

with h5py.File('groups.hdf5', 'r') as f:
    g = f.visit(get_all)
    print(g)
    d = f[g]['default']
    print(d[1])


def get_objects(name, obj):
   if 'Sub_Group' in name:
      return obj

with h5py.File('groups.hdf5', 'r') as f:
   group = f.visititems(get_objects)
   data = group['default']
   print('First data element: {}'.format(data[0]))