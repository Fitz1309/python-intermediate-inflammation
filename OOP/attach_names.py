import numpy as np

data = np.array([[1., 2., 3.],
                 [4., 5., 6.]])

def attach_names(data, names):
    """Create data structure containing patient name and data"""
    assert len(data) == len(names)
    records = []

    for i in range(len(data)):
        records.append({'name': names[i],
                        'data': data[i]})
    return records
    # for i in range(len(data)):
    #     print('name: ' + names[i])
    #     print('data: ' , data[i])

output = attach_names(data, ['Alice', 'Bob', 'John'])
print(output)

