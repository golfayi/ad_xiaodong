import numpy as np
import pdb
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data import sampler
from DeepFM.deepfm import DeepFM
from DeepFM.dataset import CriteoDataset

# 900000 items for training, 10000 items for valid, of all 1000000 items
Num_train = 9000

root_path = '/home/xiaodong/Desktop/tencent_ad/ad_xiaodong/data/sample_data/'
# load data
train_data = CriteoDataset(root_path, train=True)
loader_train = DataLoader(train_data, batch_size=100,
                          sampler=sampler.SubsetRandomSampler(range(Num_train)))
val_data = CriteoDataset(root_path, train=True)
loader_val = DataLoader(val_data, batch_size=100,
                        sampler=sampler.SubsetRandomSampler(range(Num_train, 10000)))

feature_sizes = np.loadtxt(root_path + 'feature_sizes.txt', delimiter=',')
feature_sizes = [int(x) for x in feature_sizes]
print(feature_sizes)
# pdb.set_trace()
model = DeepFM(feature_sizes, use_cuda=True)
optimizer = optim.Adam(model.parameters(), lr=1e-4, weight_decay=0.0)
model.fit(loader_train, loader_val, optimizer, epochs=100, verbose=True)