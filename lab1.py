from Crypto.Cipher import AES


class secret:
    def __repr__(self) -> str:
        encrypted = 'd0326fb8d0bfb1c5394991e7dcdf59b37889f2256772b8daad85dbeaff4483ed64cbb2b933d797bd530c8c92f57466d1c861c9f4931bc6631c38f375c64c40c4'
        return AES.new(b'\x00'*16, AES.MODE_ECB).decrypt(bytes.fromhex(encrypted)).decode()


def square(nums):
    """square returns a list of the numbers in nums squared *without* mutating nums."""
    out = nums
    for i, v in enumerate(nums):
        out[i] = v * v
    return out


def main():
    print('      uniqname:', 'TODO')
    print('openssl output:', 'TODO')

    print()

    s = secret()
    print('secret string:', 'TODO')

    print()

    a = [1, 2, 3, 4]
    print('a before function call:', a)
    b = square(a)
    print(' a after function call:', a)
    print('                     b:', b)


# main isn't called automatically;
# we need to check if the file is being
# invoked as a script then call it manually.
if __name__ == '__main__':
    main()
