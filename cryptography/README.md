# Cryptography

## Magic tools

- [dcode cipher identifier](https://www.dcode.fr/cipher-identifier)
- [cryptool cipher identifier](https://www.cryptool.org/en/cto/ncid)
- [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool)
- [Ciphey](https://github.com/Ciphey/Ciphey)
  - `docker run -it --rm remnux/ciphey "pvcurl vf gur orfg"`
- [Ares](https://github.com/bee-san/Ares)

  - intends to fully replace Ciphey
  - `cargo install project_ares --locked`
  - `ares`

- [cryptool, windows app](https://www.cryptool.org/en/)

- [tholman-transposition](https://tholman.com/other/transposition/) - transposition ciphers/

- [quipquip](https://www.quipqiup.com/) - solve simple substitution ciphers
- [guballa](https://www.guballa.de/substitution-solver) - substitution-solver

### Rainbow tables

- [crackstation](https://crackstation.net/)

## encryption tools

- gpg
  - `gpg --decrypt message.gpg --output original_message.txt`
- openssl
  - `openssl aes-256-cbc -d -in encrypted_message -out original_message.txt`
  - `openssl pkeyutl -decrypt -in ciphertext_message -inkey private-key-bob.pem`
  - `openssl rsa -in private-key-bob.pem -text -noout` - inpsect private key; The values of p, q, N, e, and d are prime1, prime2, modulus, publicExponent, and privateExponent, respectively.

## Obscure algorithms

- [Twin hex cypher](https://www.calcresult.com/misc/cyphers/twin-hex.html)
- [spam-mimic, spammimic](https://www.spammimic.com/explain.shtml)
- [symbols-ciphers](https://www.dcode.fr/symbols-ciphers)

## Math

- [sagemath](https://www.sagemath.org/)

  - [install](https://doc.sagemath.org/html/en/reference/spkg/_sagemath.html) - use on Ubuntu, Arch, WSL...

- [factor db](http://factordb.com/) - quickly factor large numbers
- [alpertron calculators](https://www.alpertron.com/CALTORS.HTM)

### RSA

1. Choose two random prime numbers, p and q. Calculate N = p × q.
2. Choose two integers e and d such that e × d = 1 mod ϕ(N), where ϕ(N) = N − p − q + 1. This step will let us generate the public key (N,e) and the private key (N,d).
3. The sender can encrypt a value x by calculating y = xe mod N. (Modulus)
4. The recipient can decrypt y by calculating x = yd mod N. Note that yd = xed = xkϕ(N) + 1 = (xϕ(N))k × x = x. This step explains why we put a restriction on the choice of e and d.

- get info about public key
  - `openssl rsa -inform PEM -text -noout -pubin -in pubkey.pem` - e, N
  - try to crack the rsa (factor N, find phi)...

### AES

- sometimes online tools will fail, so try to decipher AES in python...

## Notes

- https://ir0nstone.gitbook.io/crypto/
- https://cryptohack.gitbook.io/cryptobook/

