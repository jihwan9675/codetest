M, N, K = map(int, input().split())
secret = ''.join(list(map(str, input().split())))
btn_list = ''.join(list(map(str, input().split())))

if secret in btn_list:
    print("secret")
else:
    print("normal")
