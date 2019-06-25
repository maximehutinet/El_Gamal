# ElGamal signature

This project is an implementation of the El Gamal signature algorithm as part of a network security class.

Python 3.7 has been used for this project.

## How to launch the project ?

1. Clone the repository

2. Run the program

```
python ElGamal.py
```

## ElGamal

ElGamal is an asymmetric key encryption algorithm for public-key cryptography which is based on the Diffie–Hellman key exchange.

## The project

The goal of this project was to create a simple version of the ElGamal signature scheme using Python.

### Generation of keys

In order to generate a public key, you need to feed a private key *a* and a prime number *p*.

```python
p = GeneratePrimeNumber()  # Generation of the random prime number p
a = 6  # Private key
g, A = CreatePublicKey(p, a)  # Creation of the public key
```

### Signature of data

To sign a data, you need to pass as argument you private and the generator of your public key to the function *Sign()*.

```python
Y, S, k = Sign(m, p, a, g)  # Signature of the file
```

### Verification of the signature

A function named *Verif()* takes the public key and signature as an argument to verify the signature.

```python
Verif(m, Y, S, A, g, p)
```

### Example

```python
m = HashFile(ReadFile("file.txt"))  # I use the hash of the file as my message

p = GeneratePrimeNumber()  # Generation of the random prime number p
a = 6  # Private key
g, A = CreatePublicKey(p, a)  # Creation of the public key
DisplayValuesKeys(m, p, g, a, A)
Y, S, k = Sign(m, p, a, g)  # Signature of the file
DisplayValuesSignature(Y, S, k)  
DisplayResultSign(Verif(m, Y, S, A, g, p))  
```

Output :

```
Message : 12449830281988762103412211070081262785679669053248832919461373059120
Prime number p = 11
Generator g = 2
A = g^a % p : 9

Public Key (p, g, A) = (11, 2, 9)
Private Key a = 6
Y : 8
S : 4
k : 3

Signature verification :

Signature OK
```
