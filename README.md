# spam-classification
First, I mixed the all easy-ham and hard-ham in 1 folder as ham files, and spam as spam files.
Then, 30% of ham files was picked out as verify-ham files, and 30% of spam files as verify-spam files.

So the train data was seperately located in path '/home/sunchengxuan/Downloads/spam-classification/ham/' and '/home/sunchengxuan/Downloads/spam-classification/spam/',
the verify data was seperatedly located in path '/home/sunchengxuan/Downloads/spam-classification/verify-ham/' and '/home/sunchengxuan/Downloads/spam-classification/verify-spam/'

Acturally, the predicted result of clf.predict() is a Vector, in the python code, I tried to compare the result(Vector) to a number(0 or 1). So some deprecated warning will pop up.

As for how to use sklearn package, please refer to http://blog.csdn.net/puqutogether/article/details/43194159
