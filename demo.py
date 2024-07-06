import numpy as np
import matplotlib.pyplot as plt

## we load the data
patients = np.load('\PATH\TO\THE\FILE',allow_pickle=True)

## we access the values of the dictionary
Volumes = np.array([patients[i]['volume']  for i in range(len(patients)) ])
ICP = np.array([patients[i]['ICP']  for i in range(len(patients)) ])

## we change the order of the volume (optional)
Volumes =np.transpose(Volumes,(0,2,3,1))

##we now chech the shapes
print(Volumes.shape,ICP.shape)

## if we want to visualize a slice ( eg.12 of the seventh patient)
plt.figure(figsize=(8,8))
plt.imshow(Volumes[7,:,:,12],cmap='gray')
plt.show()

