import tensorflow as tf
from tensorflow import float32


a=[1,2,3]
b=[4,5,6]

c = tf.concat([a,b],0)

# k  = tf.convert_to_tensor(a, dtype=float32, name="user_bias")

d = tf.reshape(c,[2,3])

e = tf.reshape(d,[1,2,3])


sess = tf.Session()
sess.run(tf.global_variables_initializer())






x = sess.run([c])
y = sess.run(d)
z = sess.run(e)
print(x)
print(y)
print(z)