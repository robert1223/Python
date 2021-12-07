# 這是測試branch的程式
def recursion(a):
    if a == 1:
        return 1
    return a * recursion(a-1)


if __name__ == "__main__":
    a = 5
    answer = recursion(a)
    print(answer)
