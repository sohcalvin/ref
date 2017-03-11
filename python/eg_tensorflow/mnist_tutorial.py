import tensorflow as tf
print(tf.__version__)
# import tensorflowvisu
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
tf.set_random_seed(0)

mnist = read_data_sets("data", one_hot=True, reshape=False, validation_size=0)
# print(mnist)
# print(type(mnist.test))
# print(mnist.test.next_batch(1))
# exit()
X= tf.placeholder(tf.float32, [None, 28,28,1])

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

init = tf.global_variables_initializer()

Y = tf.nn.softmax(tf.matmul(tf.reshape(X,[-1,784]), W) + b)  # Hold predicted values

Y_ = tf.placeholder(tf.float32, [None, 10]) # Hold correct values

# loss function
cross_entropy = -tf.reduce_sum( Y_ + tf.log(Y))

# accuracy of the trained model, between 0 (worst) and 1 (best)
correct_prediction = tf.equal(tf.argmax(Y, 1), tf.argmax(Y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

optimizer = tf.train.GradientDescentOptimizer(0.003)
train_step = optimizer.minimize(cross_entropy)

# print(type(train_step))

saver = tf.train.Saver()

sess = tf.Session()
sess.run(init)

# r= tf.nn.softmax([1.0,2.0,3.0,4.0,1.0,2.0,3.0])
# print(">>", type(r), ">>", type(train_step))
# exit()
# print(sess.run(r))


for i in range(1) :
    batch_X, batch_Y = mnist.train.next_batch(2)
    train_data = {X : batch_X, Y_ : batch_Y}

    # Training
    sess.run(train_step, feed_dict=train_data)

    # Success
    a, c = sess.run([accuracy, cross_entropy], feed_dict=train_data)

    # Test data
    test_data = {X: mnist.test.images, Y_ : mnist.test.labels}
    a, c = sess.run([accuracy, cross_entropy], feed_dict=test_data)

saver.save(sess, "./csoh_mnist_model/first" )

# sess = tf.Session()
# new_saver = tf.train.import_meta_graph('./csoh_mnist_model/first')
# new_saver.restore(sess, tf.train.latest_checkpoint('./'))
# all_vars = tf.get_collection('vars')
# for v in all_vars:
#     v_ = sess.run(v)
#     print(v_)