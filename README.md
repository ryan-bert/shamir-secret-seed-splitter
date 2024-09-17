# Shamir Secret Seed Splitter

Shamir's Secret Seed Splitter is a Python application designed to securely split and reconstruct private keys or seed phrases using [Shamir's Secret Sharing Scheme (SSSS)](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing). This implementation allows users to split a private key or seed phrase into multiple shares, where only a threshold number of shares are required to reconstruct the original secret.

## Features

- **Private Key Splitting**: Split a private key into multiple shares, each in the format `(x, y)`, where `x` is the share number, and `y` is the encrypted share.
- **Seed Phrase Splitting**: Optionally, split a BIP39-compatible seed phrase into shares.
- **Reconstruction**: Reconstruct the original private key using a minimum threshold of shares.
- **Secure Storage**: Save shares and reconstructed private keys to files for later use.

## Project Structure

```bash
.
├── LICENSE
├── README.md
├── reconstruct
│   ├── input
│   │   ├── share1.txt
│   │   ├── share2.txt
│   │   ├── share3.txt
│   │   ├── share4.txt
│   │   └── share5.txt
│   └── output
│       ├── private_key.txt
│       └── reconstructed_private_key.txt
├── reconstruct.py
├── split
│   ├── input
│   │   ├── private_key.txt
│   │   └── seed_phrase.txt
│   └── output
│       ├── share1.txt
│       ├── share2.txt
│       ├── share3.txt
│       ├── share4.txt
│       └── share5.txt
├── split.py
└── src
    ├── encoding.py
    └── shamir.py
```

## Requirements

- Python 3.6+
- The sympy library for polynomial calculations
- The mnemonic library for handling BIP39-compatible seed phrases

Install the required libraries using:
```bash
pip install -r requirements.txt
```

## Usage

1. Split Mode

You can split a private key or a BIP39 seed phrase into shares by using split.py. The script expects input to be located in the ./split/input directory as either private_key.txt (hexadecimal string) or seed_phrase.txt (space-separated BIP39 seed phrase).

Example Usage
```bash
python split.py
```
You will be prompted to select an input type (private key or seed phrase). After successfully splitting, the shares will be saved in ./split/output/.

2. Reconstruct Mode

You can reconstruct a private key from shares by using reconstruct.py. The script reads all .txt files in the ./reconstruct/input directory, which should contain the shares in the format (x, y).

Example Usage
```bash
python reconstruct.py
```
The reconstructed private key will be saved in ./reconstruct/output/reconstructed_private_key.txt.

File Paths

- Splitting input: ./split/input/private_key.txt or ./split/input/seed_phrase.txt
- Splitting output: ./split/output/share1.txt, ./split/output/share2.txt, …, shareN.txt
- Reconstruction input: ./reconstruct/input/share1.txt, ./reconstruct/input/share2.txt, …, shareN.txt
- Reconstruction output: ./reconstruct/output/reconstructed_private_key.txt

## Code Overview

#### split.py

The main script responsible for splitting a private key or seed phrase into shares using Shamir’s Secret Sharing Scheme. It reads input from files, validates the input, generates shares, and saves them to the output directory.

#### reconstruct.py

This script is responsible for reading the shares from the ./reconstruct/input directory, reconstructing the private key, and saving the result in the output directory.

#### src/shamir.py

Contains the implementation of Shamir’s Secret Sharing Scheme (SSSS). The key functions are:

- secret_split: Splits a given secret (e.g., private key) into a specified number of shares, with a threshold of shares required to reconstruct the secret.
- reconstruct: Uses Lagrange interpolation to reconstruct the secret from a given set of shares.

#### src/encoding.py

Handles the conversion of a BIP39 seed phrase into a private key using HMAC-SHA512 as per the BIP32 specification. The key function:

- seed_phrase_to_private_key: Converts a BIP39 seed phrase into a private key (master key) by deriving it from the seed.