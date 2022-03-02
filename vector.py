import numpy as np


x = np.array([2, 3])
y = np.array([2, 0])


def cosine_similarity(x, y):
    ans = np.dot(x, y) / (np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))
    return ans


def cosine_test(x, y):
    result = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
    return result


A = cosine_similarity(x, y)
B = cosine_test(x, y)
print(f"標準拔案是：{A}")
print(f"我設定的答案是：{B}")
