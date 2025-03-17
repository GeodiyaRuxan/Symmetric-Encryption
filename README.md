# Secure Cloud Cryptography

This project demonstrates the use of cryptographic techniques, specifically symmetric encryption, to securely store and retrieve sensitive data in cloud environments. The main objective of this project is to ensure data confidentiality through encryption before storing it in cloud systems.

## Table of Contents

- [Introduction](#introduction)
- [Project Setup](#project-setup)

## Introduction

Cryptography plays a critical role in ensuring data security, particularly in cloud computing, where data is often stored and transmitted over the internet. This project uses the `cryptography` library in Python to demonstrate how symmetric encryption techniques can be applied to protect sensitive data before it's uploaded to cloud environments.

The project implements:
- **Symmetric encryption** to encrypt a text file.
- **Decryption** functionality to retrieve the original data.

## Project Setup

Follow these steps to get the project up and running on your local machine:

### Prerequisites

Make sure you have Python 3.x installed on your system. You will also need to install the required Python libraries.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/GeodiyaRuxan/secure-cloud-cryptography.git
   cd secure-cloud-cryptography

2. Navigate to the project directory
   After cloning, move into the project folder by running the following command:

   ```bash
   cd secure-cloud-cryptography

3. Install Python and dependencies
Make sure Python is installed. To check, run the following command:

    ```bash
    python --version

4. Add your file to be encrypted
Make sure you have a file named secret.txt (or any other file you wish to encrypt) in the root of the project directory.

5. Running the Scripts
To Encrypt a File:
To encrypt the secret.txt file, run the following command:


     ```bash
     python encryption_demo.py
    ```
This will generate an encrypted file named secret.txt.encrypted in the same directory.

To Decrypt the File:
To decrypt the secret.txt.encrypted file, run the following command:

   ```bash
     python decryption_demo.py
```
This will output the decrypted file as decrypted_secret.txt.

Usage
This project provides a simple demonstration of how to encrypt and decrypt sensitive files using symmetric encryption in Python.

Encrypting Files:
When you run the encryption_demo.py script, it will create a secret.key (if not already present) and use it to encrypt the content of secret.txt.
The result will be stored in a new file named secret.txt.encrypted.
Decrypting Files:
The decryption_demo.py script will use the same secret.key file to decrypt the encrypted content and output the result as decrypted_secret.txt.
This setup can be used as a basis for integrating file encryption and decryption into cloud storage workflows. You can modify the scripts to handle cloud APIs (e.g., AWS, Azure, Google Cloud) for storing and retrieving encrypted files.
