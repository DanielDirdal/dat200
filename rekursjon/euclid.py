def storste_felles_divisor(heltall_a, heltall_b):
    if heltall_b == 0:
        return heltall_a
    else:
        return storste_felles_divisor(heltall_b, heltall_a % heltall_b)
if __name__ == "__main__":
    print(storste_felles_divisor(30, 20))
    print(storste_felles_divisor(30, 18))
    print(storste_felles_divisor(27, 18))
    print(storste_felles_divisor(30, 23))
