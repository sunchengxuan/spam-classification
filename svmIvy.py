# -*- coding: utf-8 -*-
import nltk
import os
import math
from sklearn import svm

#acturally is 400
def findTop100(train_spam_dir):
	wordlist={}
	wordFreqList={}
	tokenizer = nltk.RegexpTokenizer("[\w]{2,}")
	folder=os.listdir(train_spam_dir)
	for file_name in folder:
		file_dir_name=train_spam_dir+file_name
		if os.path.isfile(file_dir_name):
			tokens=tokenizer.tokenize(open(file_dir_name).read())
			for token in tokens:
				if not wordlist.has_key(token):
					wordlist[token]=1
				else:
					wordlist[token]+=1
	sortedworklist = sorted(wordlist.items(),key=lambda d:d[1],reverse=True)
	keywords=[word[0] for word in sortedworklist[:400]]
##	print keywords
	return keywords

def genVec4File(bigString,keywords):
	vector=[]
	tokenizer = nltk.RegexpTokenizer("[\w]{2,}")
	tokens=tokenizer.tokenize(bigString)
	for word in keywords:
		if word in tokens:
			vector.append(1)
		else:
			vector.append(0)

	return vector
	
def train(keywords):
	train_vec=[]
	expResult=[]
	ham_train_path='/home/sunchengxuan/Downloads/spam-classification/ham/'
	spam_train_path='/home/sunchengxuan/Downloads/spam-classification/spam/'
	ham_folder=os.listdir(ham_train_path)
	spam_folder=os.listdir(spam_train_path)
	for file_name in ham_folder:
		file_dir_name=ham_train_path+file_name
		if os.path.isfile(file_dir_name):
			vec=genVec4File(open(file_dir_name).read(),keywords)
			train_vec.append(vec)
			expResult.append(0)
	for file_name in spam_folder:
		file_dir_name=spam_train_path+file_name
		if os.path.isfile(file_dir_name):
			vec=genVec4File(open(file_dir_name).read(),keywords)
			train_vec.append(vec)
			expResult.append(1)
	clf=svm.SVC()
	clf.fit(train_vec,expResult)
	return clf


def verify(clf,keywords):
	ham_verify_path='/home/sunchengxuan/Downloads/spam-classification/verify-ham/'
	spam_verify_path='/home/sunchengxuan/Downloads/spam-classification/verify-spam/'
	ham_folder=os.listdir(ham_verify_path)
	spam_folder=os.listdir(spam_verify_path)
	ham_total=0
	ham_correct=0
	spam_total=0
	spam_correct=0
	for file_name in ham_folder:
		file_dir_name=ham_verify_path+file_name
		if os.path.isfile(file_dir_name):
			ham_total+=1
			vector=genVec4File(open(file_dir_name).read(),keywords)
			result=clf.predict(vector)
			if result ==0:
				ham_correct+=1

	for file_name in spam_folder:
		file_dir_name=spam_verify_path+file_name
		if os.path.isfile(file_dir_name):
			spam_total+=1
			vector=genVec4File(open(file_dir_name).read(),keywords)
			result=clf.predict(vector)
			if result ==1:
				spam_correct+=1
#	print float(ham_correct)/ham_total	
#	print float(spam_correct)/spam_total
	correct_ratio=float(ham_correct+spam_correct)/(ham_total+spam_total)
	print "correct_ratio is %.2f%%"%(correct_ratio*100)	

keywords=findTop100('/home/sunchengxuan/Downloads/spam-classification/ham/')
clf=train(keywords)
verify(clf,keywords)
