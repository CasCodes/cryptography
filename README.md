# CryptoUI

CryptoUI is a minimalist GUI for testing the famous Cesar & Viginere ciphers. It supports encrypt & decrypt. Cesar also includes a 'hack' function which tries to crack the key to a given ciphertext.

![Screenshot from 2022-11-11 10-18-32](https://user-images.githubusercontent.com/64489325/201308071-63792b56-5d08-4613-8b59-fe635bd3bc5d.png)

## Install
1. Clone this repo and cd into _cryptoUI/_ (the other files are the ciphers for cli)
2. Make sure all libraries are installed by running `pip install -r requirements.txt` inside the _cryptoUI/_ folder
3. Run `python3 app.py` and open the local server URL displayed in your terminal

## Files
The cryptoUI/ directory contains the GUI + encryptions.
The other files are **the same** encryptions but for command line (CLI)

#### cesar_CLI.py
fully
- encrypt
- decrypt
- **hack** -> This is not implemented in GUI yet

#### vigenere_CLI.py
ignoring case and non-alphabetic characters
- encrypt
- decrypt

#### fibonnaci_cipher
a (very) simple spin on cesar. Increases the key by the fibonnaci sequence.
