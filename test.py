from __future__ import print_function
import torch

x = torch.empty(5,3)
print(x)

x = torch.rand(5,3)
print(x)

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

x = torch.tensor([5.5, 3])
print(x)

#base existed tensor
x = x.new_ones(5, 3, dtype=torch.double)
print(x)
x = torch.rand_like(x, dtype=torch.float)
print(x)
print(x.size())

#addtion
y = torch.rand(5, 3)
print(y)
print(x+y)
print(torch.add(x, y))

result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)

y.add_(x)
print(y)

#like numpy
print(x[:, 1])

#change tensor shape
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)
print(x.size(), y.size(), z.size())

#get value
x = torch.randn(1)
print(x)
print(x.item())



