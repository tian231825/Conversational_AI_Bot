import random

import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.cluster import KMeans
import multiprocessing
from sklearn.metrics import silhouette_score
from sklearn.datasets import load_iris


# def train_cluster(train_vecs, model_name=None, start_k=2):
# 	SSE = []
# 	SSE_d1 = []  # sse的一阶导数
# 	SSE_d2 = []  # sse的二阶导数
# 	models = []  # 保存每次的模型
# 	num = train_vecs.shape[0]
# 	x_data = []
# 	for i in range(start_k, int(math.sqrt(len(train_vecs))) + 1):
# 		# print(i)
# 		x_data.append(i)
# 		kmeans_model = KMeans(n_clusters=i)
# 		kmeans_model.fit(train_vecs)
# 		SSE.append(kmeans_model.inertia_)  # 保存每一个k值的SSE值
# 		# print('{} Means SSE loss = {}'.format(i, kmeans_model.inertia_))
# 		models.append(kmeans_model)
# 	plt.plot(x_data[:8], SSE[:8])
# 	plt.xlabel('i')
# 	plt.ylabel('SSE')
# 	plt.show()
# 	# angle_sum(SSE)
#
# 	# 求二阶导数，通过sse方法计算最佳k值
# 	# print(SSE)
# 	SSE_length = len(SSE)
# 	for i in range(1, SSE_length):
# 		SSE_d1.append((SSE[i - 1] - SSE[i]) / 2)
# 	if len(SSE_d1) == 2:
# 		best_model = models[1]
# 	else:
# 		for i in range(1, len(SSE_d1) - 1):
# 			SSE_d2.append((SSE_d1[i - 1] - SSE_d1[i]) / 2)
# 		# print(SSE_d2)
# 		best_model = models[SSE_d2.index(max(SSE_d2)) + 1]
# 	# plt.plot(x_data[:8], SSE_d1[:8])
# 	# plt.xlabel('i')
# 	# plt.ylabel('SSE_d1')
# 	# plt.show()
# 	# plt.plot(x_data[:8], SSE_d2[:8])
# 	# plt.xlabel('i')
# 	# plt.ylabel('SSE_d2')
# 	# plt.show()
# 	return best_model

def train_cluster(train_vecs, model_name=None, start_k=2):
	print('training cluster')
	scores = []
	models = []
	try:
		for i in range(start_k, int(math.sqrt(len(train_vecs)))):
			kmeans_model = KMeans(n_clusters=i)
			kmeans_model.fit(train_vecs)
			score = silhouette_score(train_vecs, kmeans_model.labels_, metric='euclidean')
			scores.append(score)  # 保存每一个k值的score值, 在这里用欧式距离
			# print('{} Means score loss = {}'.format(i, score))
			models.append(kmeans_model)
		i = scores.index(max(scores)) + 2
		# print('最佳聚类数：' + str(i))
		best_model = models[scores.index(max(scores))]
		return i, best_model
	except  ValueError:
		# print('最佳聚类数：1')
		kmeans_model = KMeans(n_clusters=1)
		kmeans_model.fit(train_vecs)
		return 1,kmeans_model





# filePath:文件地址
# k:自定义k值
# 返回点的所属类别标签 ndarray格式数组
def kmeans(filePath, k):
	dataSet = []
	fileIn = open(filePath)
	for line in fileIn.readlines():
		temp = []
		lineArr = line.strip().split('\t')
		for i in range(len(lineArr)):
			temp.append(float(lineArr[i]))
		dataSet.append(temp)
	fileIn.close()
	X = np.array(dataSet)
	estimator = KMeans(n_clusters=k)
	estimator.fit(X)  # 聚类
	label_pred = estimator.labels_
	print(label_pred)
	return label_pred


# 自动选取最优k值 k范围可调 默认最小2 最大20
# filePath:文件地址
# 返回点的所属类别标签
def kmeans_auto(filePath, k_min=2):
	dataSet = []
	fileIn = open(filePath)
	for line in fileIn.readlines():
		temp = []
		lineArr = line.strip().split(' ')
		for i in range(len(lineArr)):
			temp.append(float(lineArr[i]))
		dataSet.append(temp)
	fileIn.close()
	X = np.array(dataSet)
	model = train_cluster(X, model_name=None, start_k=k_min)
	label_pred = model.labels_
	# print(label_pred)
	return label_pred


# array:numpy ndarray格式数组
# k:自定义k值
# 返回点的所属类别标签
def kmeans_array(array, k):
	estimator = KMeans(n_clusters=k)
	estimator.fit(array)
	label_pred = estimator.labels_
	print(label_pred)
	return label_pred


# 自动选取最优k值 k范围可调 默认最小2 最大20
# array:numpy ndarray格式数组
# 返回点的所属类别标签
def kmeans_auto_array(array, k_min=2):
	k, model = train_cluster(array, model_name=None, start_k=k_min)
	label_pred = model.labels_
	# print(label_pred)
	return k,label_pred


def output(filePath):
	with open(filePath, 'r', encoding='utf-8') as f:
		lines = f.readlines()
		out = []
		for line in lines:
			attrs = line.strip().split(" ")
			list_i = []
			for ele in attrs:
				list_i.append(float(ele))
			out.append(list_i)
	return out


def skip(array, k):
	out = []
	for list_i in array:
		li = []
		for j in range(len(list_i)):
			if j == k:
				pass
			else:
				li.append(list_i[j])
		out.append(li)
	return out

def writeFile(filepath, data):
    with open(filepath, 'a', newline='', encoding='utf-8')as f:
        for i in range(len(data)):
            f.write(str(data[i]) + " ")
        f.write("\n")


#对每一轮进行聚类测试
#输入：array:待聚类数组
#attr_num:剩余属性数目
#s_id:目标服务人员id
def rounds(array, attr_num, s_id):
	# 搞测试
	min_k = 1000000
	min_label = []
	pick = 1000
	hh = 0
	list_k = []
	list_label = []
	list_data = []
	for i in range(1, attr_num):
		list_i = []
		for array_i in array:
			list_att = []
			temp = array_i[i]
			list_att.append(temp)
			list_i.append(list_att)
		data = np.array(list_i)
		k, label = kmeans_auto_array(data)
		list_k.append(k)
		list_label.append(label)
		list_data.append(data)
		if k < min_k:
			min_k = k
			min_label = label
			pick = i
	ran_i = []
	for i in range(len(list_k)):
		if list_k[i] == min_k:
			ran_i.append(i)
	# print(ran_i)
	pick = ran_i[random.randint(0, len(ran_i) - 1)]
	# print(pick)
	min_label = list_label[pick]
	# print(min_label)
	data = list_data[pick]
	# print(data)
	classification = []
	classification_num = []
	for num in range(min_k):
		list_t = []
		list_t1 = []
		for inx in range(len(min_label)):
			if num == min_label[inx]:
				list_t.append(inx)
				# print(data[inx])
				list_t1.append(float(data[inx][0]))
		classification.append(list_t)
		classification_num.append(list_t1)
	# print(classification)
	# print(classification_num)
	pick = pick + 1
	# print(min_k)
	# print(min_label)
	# print(pick)
	min_edge = []
	max_edge = []
	for i in range(min_k):
		min_edge.append(min(classification_num[i]))
		max_edge.append(max(classification_num[i]))
	min_edge = sorted(min_edge)
	max_edge = sorted(max_edge)
	fin_k = min_k
	for i in range(min_k - 1):
		if max_edge[i] >= min_edge[i + 1]:
			print("有事啊啊啊啊啊啊啊")
			hh = 1
	dataSet = array
	out = []
	# temp = dataSet[0][pick]
	for h in dataSet:
		if h[0] == s_id:
			temp = h[pick]
	for j in range(len(classification_num)):
		if float(temp) in classification_num[j]:
			for num in classification[j]:
				out.append(dataSet[num])
	# print(out)
	next = skip(out, pick)
	# print(next)
	return next, hh


#按类型进行聚类测试
def final(filePath, type):
	data = output(filePath)
	sum_out = []
	error_list = []
	for list_i in data:
		s_id = list_i[0]
		init = 10
		flag = 1
		epoch = 1
		out = []
		data_1 = output(filePath)
		while flag == 1:
			data_1, error = rounds(data_1, init, s_id)
			if error == 1:
				error_list.append(s_id)
				writeFile("kmeans_test_1.txt", [s_id, type, "有错啊啊啊啊啊啊啊啊啊啊"])
				continue
			end_num = len(data_1)
			if end_num <= 8:
				flag = 0
			elif init == 2:
				flag = 0
			epoch = epoch + 1
			init = init - 1
			print(end_num)
			print(data_1)
		out.append(s_id)
		out.append(type)
		out.append(end_num)
		out.append(epoch)
		writeFile("kmeans_test_1.txt", out)
		print(out)
		print(error_list)

	# sum_out.append(out)
final("k_1.txt", 1)
final("k_2.txt", 2)
final("k_3.txt", 3)
final("k_4.txt", 4)
final("k_5.txt", 5)
final("k_6.txt", 6)
final("k_12.txt", 12)
final("k_13.txt", 13)
final("k_14.txt", 14)
final("k_16.txt", 16)
final("k_23.txt", 23)
final("k_24.txt", 24)
final("k_25.txt", 25)
final("k_8.txt", 56)
final("k_123.txt", 123)
final("k_124.txt", 124)