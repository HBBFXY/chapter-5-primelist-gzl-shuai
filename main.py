def PrimeList(N):
    """
    返回小于N的所有质数，以空格分隔
    """
    if N <= 2:
        return ""
    
    # 使用埃拉托斯特尼筛法
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # 将i的倍数标记为非质数
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集所有质数
    primes = [str(i) for i in range(2, N) if is_prime[i]]
    
    return " ".join(primes)

# 测试函数
if __name__ == "__main__":
    # 测试用例
    test_cases = [2, 10, 20, 30, 50]
    
    for n in test_cases:
        print(f"PrimeList({n}) = '{PrimeList(n)}'")
