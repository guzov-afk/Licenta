from imports import *

from Utils import *






def extractFeatures(w,o):    # w = window , o = overlapping
	filesName = os.listdir('../Database/')
	filesName.sort()

	lis = [] #tine contorizarea matricelor pe clase(0,1,...)
	labelStore = []
	for f in range(len(filesName)):     
		file = open('../Database/' + filesName[f])
		csvreader = csv.reader(file)
		header = []
		header = next(csvreader)
		x = []
		y = []
		z = []
		t = []
		for row in csvreader:
			x.append(float(row[0]))
			y.append(float(row[1]))
			z.append(float(row[2]))
			t.append(float(row[3]))
		xwindow = window(x,w,o)
		ywindow = window(y,w,o)
		zwindow = window(z,w,o)
		twindow = window(t,w,o)
		num_rows, num_cols = xwindow.shape
		X = []
		Y = []
		Z = []
		T = []
		for i in range(num_rows):
			X.append(np.array([MAV(xwindow[i]),ZCR(xwindow[i]),WL(xwindow[i]),RMS(xwindow[i]),SSC(xwindow[i],0),HJ(xwindow[i]),Skewness(xwindow[i])]))
			Y.append(np.array([MAV(ywindow[i]),ZCR(ywindow[i]),WL(ywindow[i]),RMS(ywindow[i]),SSC(ywindow[i],0),HJ(ywindow[i]),Skewness(ywindow[i])]))
			Z.append(np.array([MAV(zwindow[i]),ZCR(zwindow[i]),WL(zwindow[i]),RMS(zwindow[i]),SSC(zwindow[i],0),HJ(zwindow[i]),Skewness(zwindow[i])]))
			T.append(np.array([MAV(twindow[i]),ZCR(twindow[i]),WL(twindow[i]),RMS(twindow[i]),SSC(twindow[i],0),HJ(twindow[i]),Skewness(twindow[i])]))
			labelStore.append(int(filesName[f][1]))
		dataStore = np.concatenate((np.array(X),np.array(Y),np.array(Z),np.array(T)),axis=1)
		lis.append(dataStore)
		



	
	dataFinalStore = np.vstack(lis)

	np.save('../Features/Labels.npy',labelStore)
	np.save('../Features/Features.npy',dataFinalStore)
	
	
def makeTestData(w,o):
	filesName = os.listdir('../Test/')
	filesName.sort()

	lis = [] #tine contorizarea matricelor pe clase(0,1,...)
	labelStore = []
	for f in range(len(filesName)):     
		file = open('../Test/' + filesName[f])
		csvreader = csv.reader(file)
		header = []
		header = next(csvreader)
		x = []
		y = []
		z = []
		t = []
		for row in csvreader:
			x.append(float(row[0]))
			y.append(float(row[1]))
			z.append(float(row[2]))
			t.append(float(row[3]))
		xwindow = window(x,w,o)
		ywindow = window(y,w,o)
		zwindow = window(z,w,o)
		twindow = window(t,w,o)
		num_rows, num_cols = xwindow.shape
		X = []
		Y = []
		Z = []
		T = []
		for i in range(num_rows):
			X.append(np.array([MAV(xwindow[i]),ZCR(xwindow[i]),WL(xwindow[i]),RMS(xwindow[i]),SSC(xwindow[i],0),HJ(xwindow[i]),Skewness(xwindow[i])]))
			Y.append(np.array([MAV(ywindow[i]),ZCR(ywindow[i]),WL(ywindow[i]),RMS(ywindow[i]),SSC(ywindow[i],0),HJ(ywindow[i]),Skewness(ywindow[i])]))
			Z.append(np.array([MAV(zwindow[i]),ZCR(zwindow[i]),WL(zwindow[i]),RMS(zwindow[i]),SSC(zwindow[i],0),HJ(zwindow[i]),Skewness(zwindow[i])]))
			T.append(np.array([MAV(twindow[i]),ZCR(twindow[i]),WL(twindow[i]),RMS(twindow[i]),SSC(twindow[i],0),HJ(twindow[i]),Skewness(twindow[i])]))
			labelStore.append(int(filesName[f][1]))
		dataStore = np.concatenate((np.array(X),np.array(Y),np.array(Z),np.array(T)),axis=1)
		lis.append(dataStore)
	return dataStore

	
