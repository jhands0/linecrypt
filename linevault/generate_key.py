import sympy
import math

class generate_key():
    def __init__(self, key_size: int, passphrase: str):
        self.key_size = key_size
        self.passphrase = passphrase
        self.prime_1 = 0
        self.prime_2 = 0
        self.rsa_modulus = 0
        self.euler_totient = 0

    def generate_primes(self, passphrase: str, key_size: int):
        start = 0
        end = len(passphrase) - 1
        mid = start + ((end - start) // 2)

        first_half = 0
        second_half = 0
        for i in range(mid + 1):
            first_half += ord(passphrase[:i])
        
        for i in range(mid, end + 1):
            second_half += ord(passphrase[mid:i])

        self.prime_1 = sympy.randprime(first_half, 2**key_size/2)
        self.prime_2 = sympy.randprime(second_half, 2**key_size/2)

    def validate_primes(self, prime_1: int, prime_2: int, key_size: int):
        while self.prime_1 == self.prime_2 or (prime_1)*(prime_2) > 2 ** self.key_size:
            generate_primes(self.passphrase, key_size)

    def generate_rsa_modulus(self, prime_1: int, prime_2: int):
        self.rsa_modulus = prime_1 * prime_2

    def generate_euler_tointent(self, prime_1: int, prime_2: int):
        self.euler_totient = (prime_1 - 1) * (prime_2 - 1)
    