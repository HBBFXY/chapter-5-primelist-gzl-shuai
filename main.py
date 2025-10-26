import math

def PrimeList(N):
    primes = []
    for i in range(2, N):
        is_prime = True
        # 检查从2到sqrt(i)是否有因子
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(i))
    # 用空格连接所有质数字符串
    return ' '.join(primes)
