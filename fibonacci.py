def fibonacci(n):
  """
  피보나치 수열을 계산하는 함수입니다.

  Args:
    n: 피보나치 수열의 n번째 항을 구합니다. (n은 0 이상의 정수)

  Returns:
    피보나치 수열의 n번째 항을 반환합니다.
    만약 n이 음수일 경우, 에러 메세지를 출력합니다.
  """
  if n < 0:
    print("피보나치 수열은 0 이상의 정수에 대해서만 정의됩니다.")
    return None
  elif n <= 1:
    return n
  else:
    a, b = 0, 1
    for _ in range(2, n + 1):
      a, b = b, a + b
    return b

# 0부터 100까지 피보나치 수열 출력
for i in range(101):
    print(f"fibonacci({i}) = {fibonacci(i)}")
