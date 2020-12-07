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

---
Key Generator
---

Input_key.txt file contains two primes (p and q) and an auxiliary number e (probably a prime) so that e>2 and GCD(e, (p-1) × (q-1)) = 1. Here, <p align = "center">
p = __57704576143051__, q = __838744063__, and e = __2237__ <br>
</p> 

Two files- public_key and private_key are created. Public_key would contain ‘modulo’ = p × q and ‘e’. Private_key file contains only ‘p’ and ‘q’. Get primes from here: https://bigprimes.org/


---
Encryption
---

Encryption function takes three parameters. Here, <p align = "center">
Message = __Down the-rabbit hole__, Modulo = __48399370647915464956213__, and e = __2237__ <br>
</p> 

From “modulo”, we got, <p align = "center">
per_char = __9__ and cyln = __23__ <br>
  </p>
  
 > This means- “Ciphertext length is a multiplication of 23 per 9 character of the message”. <If message length is (1-9) output is 23 character. If message length is (10-18) output is 46 characters (23*2). Here message length is- 20. So ciphertext will be 69 characters in decimal>

Then, the message is divided into three portion: 9 + 9 + 2. Here,<p align = "center">
M1 = __Down the-__ <br>
M2 = __rabbit ho__ <br>
M3 = __le__ <br>
</p>

Each part convert to int. Here,<p align = "center">
b1 = __1262410606558359086381__ <br>
b2 = __2109946103777344907375__ <br>
b3 = __27749__ <br>
  </p>
  
  > Convert to int: "Down the-" = "-eht nwoD" =  45 x 2560 + 101 x 2561 + 104 x 2562 + 116 x 2563 + 32 x 2564 + 110 x 2565 + 119 x 2566 + 111 x 2567 + 68 x 2568 = 1262410606558359086381
  
Ciphertext is produced by PowMod() function. Each part contains 23 characters. If less than 23, convert to string and add “0” in the beginning of each part. <br>
* C1 = b1<sup>e</sup> mod modulo = 1262410606558359086381<sup>2237</sup> mod 48399370647915464956213 = __17004190389571278372483__ <br>
* C2 = b2<sup>e</sup> mod modulo = 2109946103777344907375<sup>2237</sup> mod 48399370647915464956213 = __46911152036783136438187__ <br>
* C3 = b3<sup>e</sup> mod modulo = 27749<sup>2237</sup> mod 48399370647915464956213 = __8084009132883873298763__ <br>

Here, C3 has a length 22, less than 23. So a “0” is added before it. Finally
* C = C1+C2+C3 = __170041903895712783724834691115203678313643818708084009132883873298763__ <br>

C is convert to hexadecimal giving the ciphertext, here:
 ```
 Ciphertext: 64EA4F894FB708BD613599C2821799381F581AAAEE8048DD9445AF94B
 ```

