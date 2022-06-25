from imports import *

def window(data, window, overlapping):
	if window > overlapping:
		resultSize = lambda x: x if overlapping == 0 else overlapping*x	
		return np.array([data[i:i+window] for i in range(0, resultSize(np.size(data)), window - overlapping) if np.size(data[i:i+window]) == window])
	else: raise ValueError('Error')
		
# mean absolute value			  			
def MAV(data):
	return np.mean(np.abs(data))

# zero crossing rate
def ZCR(data):
	return ((data[:-1] * data[1:]) < 0).sum()


#waveform length
def WL(data):
	return  (abs(data[:-1]-data[1:])).sum()


#root mean square
def RMS(data):
	return np.sqrt(np.mean(data**2))
	
#slope sign changes
def SSC(data, alpha):
	return  ((data[:-1]-data[1:])*(data[:1]-data[1:]) > alpha).sum()


#hjorth parameters
def HJ(data):
	return np.mean((data-np.mean(data))**2)


def Skewness(data):
	return skew(data)

def Normalization(data):
	#return (data - min(data))/(max(data)-min(data))
	return (data/np.max(np.abs(data))) 

def Standardization(data):
	return (data - np.mean(data))/np.std(data)
	



def PCA2D(data,y):
	target_names = ['0','1','2']



	pca = decomposition.PCA(n_components=3)
	data = pca.fit(data).transform(data)



	plt.figure()
	colors = ['red', 'green', 'black']
	lw = 3

	for color, i, target_name in zip(colors, [0, 1, 2], target_names):
	    plt.scatter(data[y == i, 0], data[y == i, 1],data[y == i,2], color=color, alpha=.8, lw=lw,
		        label=target_name)
	plt.legend(loc='best', shadow=False, scatterpoints=4)
	plt.show()
	
def PCA3D(data,y):
	fig = plt.figure(1, figsize=(4, 3))
	plt.clf()
	ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

	plt.cla()
	pca = decomposition.PCA(n_components=3)
	pca.fit(data)
	data = pca.transform(data)

	for name, label in [('0', 0), ('1', 1), ('2', 2)]:
	    ax.text3D(data[y == label, 0].mean(),
		      data[y == label, 1].mean() + 1.5,
		      data[y == label, 2].mean(), name,
		      horizontalalignment='center',
		      bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
	# Reorder the labels to have colors matching the cluster results
	#y = np.choose(y, [1, 2, 0]).astype(float)
	ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=y, cmap=plt.cm.nipy_spectral,
		   edgecolor='k')

	ax.w_xaxis.set_ticklabels([])
	ax.w_yaxis.set_ticklabels([])
	ax.w_zaxis.set_ticklabels([])

	plt.show()

	




