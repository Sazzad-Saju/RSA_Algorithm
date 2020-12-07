# RSA_Algorithm
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

<p align = "center">
<img src = "images/RSA.png" width = "200"> <br> 
<a href="#Introduction">Introduction •  </a><a href="#key-generation">Key Generator</a> • <a href="#encryption">Encryption</a> • <a href="#decryption">Decryption</a>
</p>

---
Introduction
---

This RSA algorithm works for any prime number and generates output in hexadecimal. But select only large primes for better security. The program Keygenerator creates a public key for encryption and a private key for decryption. Suppose, Alice and Bob are communicating in a hybrid cryptosystem. Alice sends Bob a symmetric-encrypted message. But Bob doesn’t have the symmetric-key. So, he sends his public key to Alice. Alice encrypts the symmetric-key with Bob’s public key and transmit. The private key is kept secrect and only Bob can decrypt using it. Thus a secure communication is established. Here the processes are explained with an example below:

