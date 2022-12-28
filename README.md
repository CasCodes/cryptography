# CryptoUI

CryptoUI is a minimalist GUI for testing the famous RSA, Cesar & Viginere ciphers. It supports encrypt & decrypt. Cesar also includes a 'hack' function which tries to crack the key to a given ciphertext.

<img src="https://user-images.githubusercontent.com/64489325/209791947-dafbc0c1-66e0-44f2-93c9-165eaf05d432.gif" width="600" height="600" />

_RSA demo_

## Install
1. Clone this repo and cd into _cryptoUI/_ (the other files are the ciphers for cli)
2. Make sure all libraries are installed by running `pip install -r requirements.txt` inside the _cryptoUI/_ folder
3. Run `python3 app.py` and open the local server URL displayed in your terminal

## Files
The cryptoUI/ directory contains the GUI + encryptions.
The other files are **the same** encryptions but for command line (CLI)

## rsa_CLI.py
usage:
- Generate new keys with `python3 rsa_CLI -n`
- Encrypt with `python3 rsa_CLI -e 'message'`
- Decrypt with `python3 rsa_CLI -d 'message'`

#### cesar_CLI.py
fully
- encrypt
- decrypt
- **hack** -> This is not implemented in GUI yet

![hacked](https://user-images.githubusercontent.com/64489325/201374248-68419d8d-0352-455b-a61a-03bda7fcd90b.gif)

#### vigenere_CLI.py
ignoring case and non-alphabetic characters
- encrypt
- decrypt

#### fibonnaci_cipher
a (very) simple spin on cesar. Increases the key by the fibonnaci sequence.
