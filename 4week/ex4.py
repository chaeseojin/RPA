def sumfunc(n):
    return sum(range(1, n + 1))

num = int(input("1 이상의 정수를 입력하세요: "))
if num < 1:
    print("잘못입력하였습니다.")
else:
    total = sumfunc(num)
    print(f"1부터 {num}까지의 합은 {total}입니다.")