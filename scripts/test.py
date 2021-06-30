import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms


print(torch.get_num_interop_threads())
print(torch.cuda.is_available())