#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Maxime Hutinet

import random
import hashlib


def DisplayValuesKeys(m, p, g, a, A):
    print("Message : {}\nPrime number p = {}\nGenerator g = {}\nA = g^a % p : {}\n\nPublic Key (p, g, A) = ({}, "
          "{}, {})\nPrivate Key a = {}".format(m, p, g, A, p, g, A, a))


def DisplayValuesSignature(Y, S, k):
    print("Y : {}\nS : {}\nk : {}".format(Y, S, k))


def DisplayResultSign(resultSign):
    print("\nSignature verification :\n")
    print("Signature OK") if resultSign else print("[ERROR] - The signature is not valid")


# Generate a random prime number
def GeneratePrimeNumber():
    bornInf = 2
    bornSup = 21
    primes = []
    for possiblePrimeNumber in range(bornInf, bornSup):
        isPrime = True
        for num in range(bornInf, possiblePrimeNumber):
            if possiblePrimeNumber % num == 0:
                isPrime = False

        if isPrime:
            primes.append(possiblePrimeNumber)
    return random.choice(primes)


# Compute the Extended Euclidean algorithm
def EGCD(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = EGCD(b % a, a)
        return g, x - (b // a) * y, y


# Return a random EGCD
def GenerateRandomNumberEGCD(p):
    for k in range(2, p - 1):
        if (EGCD(k, p - 1))[0] == 1:
            return k


# Create the public key
def CreatePublicKey(p, a):
    g = A = None

    while A is None:
        g = FindGenerator(p)
        A = pow(g, a, p)
    return g, A


# Read a file
def ReadFile(file):
    myFile = open(file)
    return myFile.read()


# Return the hash sha224 of a file
def HashFile(fileDump):
    return int(hashlib.sha224(fileDump.encode('utf-8')).hexdigest(), 16)


# Compute the modular inverse
def InverseMod(a, m):
    _, x, _ = EGCD(a, m)
    return x % m


# Return the signature of a file
def Sign(m, p, a, g):
    S = Y = k = 0

    k = GenerateRandomNumberEGCD(p)  # We pick a random number k
    Y = pow(g, k, p)
    I = InverseMod(k, p - 1)
    S = I * (m - a * Y) % (p - 1)

    return Y, S, k


# Check the signature of a file
def Verif(m, Y, S, A, g, p):
    resultInt = pow(A, Y) * pow(Y, S) % p
    resultMod = pow(g, m, p)
    return resultMod == resultInt


# Decompose a number in prime factor
def Decompose(n):
    i = 2
    listDecomp = []
    while n > 1:
        while n % i == 0:
            listDecomp.append(i)
            n = n / i
        i = i + 1
    return listDecomp


# Return the prime factors without duplicate
def FindPrimeFactors(n):
    listDecomp = Decompose(n)
    return list(dict.fromkeys(listDecomp))


# Return a random generator
def FindGenerator(p):
    listPrimeFactors = FindPrimeFactors(p - 1)
    listValidation = []
    listGenerator = []
    for i in range(2, p - 1):
        for element in listPrimeFactors:
            listValidation.append((pow(i, (p - 1) / element)) % p)
        if 1 not in listValidation:
            listGenerator.append(i)

    listValidation = []

    return random.choice(listGenerator)  # Here we pick a random number in a list of generator


'''
List of different variables

p -> prime number
g -> generator
a -> private key which can be changed by the user
A -> public key
k -> private key for encryption
m -> message



'''

if __name__ == '__main__':
    m = HashFile(ReadFile("file.txt"))  # I use the hash of the file as my message

    p = GeneratePrimeNumber()  # Generation of the random prime number p
    a = 6  # Private key
    g, A = CreatePublicKey(p, a)  # Creation of the public key
    DisplayValuesKeys(m, p, g, a, A)
    Y, S, k = Sign(m, p, a, g)  # Signature of the file
    DisplayValuesSignature(Y, S, k)  # Here we display the signature result
    DisplayResultSign(Verif(m, Y, S, A, g, p))  # Here we display the result of the verification
