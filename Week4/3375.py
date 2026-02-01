def compute_prefix_function(pattern):
    """
    计算模式串的前缀函数（KMP中的部分匹配表）。
    """
    m = len(pattern)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi

def KMP_search(text, pattern):
    """
    使用KMP算法查找pattern在text中的所有出现位置（1-based index）。
    """
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    j = 0  # 模式串的位置
    positions = []

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            positions.append(i - m + 2)  # 1-based index
            j = pi[j - 1]

    return positions

def solve(s1, s2):
    # 第1部分：查找s2在s1中的所有出现位置
    positions = KMP_search(s1, s2)
    
    # 第2部分：计算s2的前缀函数
    pi = compute_prefix_function(s2)
    
    # 输出结果
    for pos in positions:
        print(pos)
    print(" ".join(map(str, pi)))

# 读取输入
s1 = input().strip()
s2 = input().strip()

solve(s1, s2)
