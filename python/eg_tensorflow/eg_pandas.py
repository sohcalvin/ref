
import pandas as pd
import numpy as np
import tensorflow as tf
df = pd.read_csv('u.data', sep='\t', names=['user','item','rate', 'time'])

msk = np.random.rand(len(df)) < 0.7
df_train = df[msk]
user_indecies = [x-1 for x in df_train.user.values]
item_indecies = [x-1 for x in df_train.item.values]
rates = df_train.rate.values


feature_len = 10
U = tf.Variable(initial_value=tf.truncated_normal([943,feature_len]), name='users')
P = tf.Variable(initial_value=tf.truncated_normal([feature_len,1682]), name='items')

result = tf.matmul(U, P)

result_flatten = tf.reshape(result, [-1])
R = tf.gather(result_flatten, user_indecies * tf.shape(result)[1] +
              item_indecies, name='extracting_user_rate')

print(result)
print(result_flatten)
#
# print(df_train)
# print(msk)
#
# print(df_train.user.values)