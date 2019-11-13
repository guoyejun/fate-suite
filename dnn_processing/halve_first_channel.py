import tensorflow as tf
import numpy as np

# in case that you want to run this script with an image, uncomment all the lines

#import imageio
#in_img = imageio.imread('in.bmp')
#in_img = in_img.astype(np.float32)/255.0
#in_data = in_img[np.newaxis, :]

filter_data = np.array([0.5, 0, 0, 0, 1., 0, 0, 0, 1.]).reshape(1,1,3,3).astype(np.float32)
filter = tf.Variable(filter_data)
x = tf.placeholder(tf.float32, shape=[1, None, None, 3], name='dnn_in')
y = tf.nn.conv2d(x, filter, strides=[1, 1, 1, 1], padding='VALID', name='dnn_out')

sess=tf.Session()
sess.run(tf.global_variables_initializer())

graph_def = tf.graph_util.convert_variables_to_constants(sess, sess.graph_def, ['dnn_out'])
tf.train.write_graph(graph_def, '.', 'halve_first_channel.pb', as_text=False)

print("halve_first_channel.pb generated, please use \
path_to_ffmpeg/tools/python/convert.py to generate halve_first_channel.model\n")

#output = sess.run(y, feed_dict={x: in_data})
#output = output * 255.0
#output = output.astype(np.uint8)
#imageio.imsave("out.bmp", np.squeeze(output))
