# -*- coding: utf-8 -*-

import numpy as np
#1.生成一個等差數列，首數為 0，尾數為 20，公差為 1 的數列。
a = np.arange(0,21,1)
print(a)
#2.呈上題，將以上數列取出偶數。
even = a[a%2==0]
print(even)

#3.呈 1 題，將數列取出 3 的倍數。
triple = a[a%3==0]
print(triple)
