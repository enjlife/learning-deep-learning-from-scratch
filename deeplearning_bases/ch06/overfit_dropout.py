# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from deeplearning_bases.common.multi_layer_net_extend import MultiLayerNetExtend
from deeplearning_bases.common.trainer import Trainer

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

x_train = x_train[:300]
t_train = t_train[:300]

#use_dropout 默认 False
use_dropout = True
dropout_ratio = 0.15
network = MultiLayerNetExtend(input_size=784, hidden_size_list=[100, 100, 100, 100, 100, 100],
                              output_size=10, use_dropout=use_dropout, dropout_ratio=dropout_ratio)

#trainer函数会把network类和类的相关变量包含进来，trainer的变量是选择：network、训练和监督数据、epoch次数、batch_size、梯度计算方式optimizer、梯度学习率和verbose
trainer = Trainer(network, x_train, t_train, x_test, t_test,
                  epochs=201, mini_batch_size=100,
                  optimizer='sgd', optimizer_param={'lr': 0.01}, verbose=True)

trainer.train()

trainer_acc_list, test_acc_list = trainer.train_acc_list, trainer.test_acc_list

markers = {'train': 'o', 'test': 's'}
x = np.arange(len(trainer_acc_list))
plt.plot(x, trainer_acc_list, marker='o', label='train', markevery=10)
plt.plot(x, test_acc_list, marker='s', label='test', markevery=10)
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()