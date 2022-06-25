from imports import *
from Utils import *
from loadData import *
import tensorflow as tf
import time
from tensorflow.keras.models import load_model
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import plotly.express as px
from sklearn.decomposition import PCA






extractFeatures(150,100)
data = np.load('../Features/Features.npy')
data = Normalization(data)
y = np.load('../Features/Labels.npy')
#PCA2D(data,y)
pca = PCA()
Xt = pca.fit_transform(data)
plot = plt.scatter(Xt[:,0], Xt[:,1], c=y)
plt.legend(handles=plot.legend_elements()[0], labels=[0,1,2])
plt.show()
print(data.shape)
print(y.shape)
X_train, X_test, y_train, y_test = train_test_split(
      data, y, test_size=0.1, random_state=42,stratify=y)


y_train = tf.keras.utils.to_categorical(y_train, num_classes=3)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=3)


inputs = tf.keras.Input(shape=(28,))


rez = tf.keras.layers.Dense(8, activation='relu')(inputs)

rez = tf.keras.layers.Dense(16, activation='relu')(rez)

rez = tf.keras.layers.Dense(8, activation='relu')(rez)

rez = tf.keras.layers.Dense(3, activation='softmax')(rez) 

callbacks = [
    tf.keras.callbacks.TensorBoard(log_dir='./logs/' + datetime.datetime.now().strftime("%Y%M%D-%H%M%S")),
    tf.keras.callbacks.ModelCheckpoint('../Models/Model.h5',verbose=1,save_best_only=True)
]

model = tf.keras.Model(inputs=inputs, outputs=rez)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc']) # categorical cross entropy

model.fit(X_train,y_train,epochs=1000,callbacks=callbacks,validation_split=0.1)

print(X_test.shape)
print(X_test[1,None])

#model = load_model('../Models/Model.h5')
predictions = model.predict(X_test)
print(predictions.shape)
print(y_test.shape)

toc = time.time()
result = model.predict(X_test)
tic = time.time()

print("prediction time : ", tic-toc)
y_test_arg=np.argmax(y_test,axis=1)
y_pred = np.argmax(model.predict(X_test),axis=1)

cf_matrix = confusion_matrix(y_test_arg, y_pred)
print(cf_matrix)


#ax = sns.heatmap(cf_matrix, annot=True, cmap='Blues')
ax = sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, 
            fmt='.2%', cmap='Blues')


ax.set_title('Matrice de confuzie\n\n')
ax.set_xlabel('\nCategoria prezisă')
ax.set_ylabel('Categoria actuală')

## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['Picior drept','Picior stâng', 'Repaus'])
ax.yaxis.set_ticklabels(['Picior drept','Picior stâng', 'Repaus'])

## Display the visualization of the Confusion Matrix.
plt.show()







