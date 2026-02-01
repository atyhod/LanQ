def compute_prefix_function(pattern):
    """
    计算模式串的前缀函数（KMP中的部分匹配表）。
    """
    m = len(pattern)
    pi = [0] * m  # 初始化前缀函数数组
    j = 0  # j 是模式串的匹配位置
    for i in range(1, m):  # 从模式串的第二个字符开始
        # 当模式串的第i个字符与第j个字符不匹配时，回溯到前一个最长前缀后缀的位置
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        # 如果字符匹配，扩展匹配
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j  # 更新前缀函数
    return pi

def KMP_search(text, pattern):
    """
    使用KMP算法查找pattern在text中的所有出现位置（1-based index）。
    """
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)  # 计算模式串的前缀函数
    j = 0  # 模式串的位置
    positions = []  # 存储匹配的位置

    for i in range(n):  # 遍历主串
        # 当模式串的字符与当前字符不匹配时，利用前缀函数回溯
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        # 如果字符匹配，扩展模式串
        if text[i] == pattern[j]:
            j += 1
        # 如果整个模式串匹配成功
        if j == m:
            positions.append(i - m + 2)  # 1-based index
            j = pi[j - 1]  # 利用前缀函数，回溯
    return positions

# 以上为KMP算法


n, m, k = map(int, input().split())
text = str(input())
pattern = input().strip()

# 查找模式串在文本中的所有位置
positions = KMP_search(text, pattern)
for pos in positions:
    print(pos)
