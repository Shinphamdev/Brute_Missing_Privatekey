# Brute_Missing_Privatekey
The Privatekey Missing Recovery Tool is written in python to help users recover the missing bitcoin privatekey between 1 and 6 characters in the safest way.
Bitcoin missing privatekey brute force written in Python with simplicity and speed in mind

## Functions
- Compare multiple characters with wallet addresses to speed up finding lost characters
- Split workload across multiple CPU cores

## Setup

**THIS IS FOR EDUCATIONAL PURPOSES ONLY, YOU ARE RESPONSIBLE FOR YOUR ACTIONS**

### CMD install
1. Install [Python](https://www.python.org/downloads/)
2. Install git and clone this repo:
```bash
$ git clone https://github.com/Shinphamdev/Brute_Missing_Privatekey.git
```

```bash
$ cd Brute_Missing_Privatekey
```
```bash
$ pip install trotter
```
```bash
$ pip install HDWallet
```
```bash
$ pip install tqdm
```


## Usage
```bash
$ python missing.py --missingkey=KwDiBf89QgGbjEhKnhXJuH7LrhcVkatbczm7Y9ZaB56U1jLNU*** --address 1NLbHuJebVwUZ1XqDjsAyfTRUPwDQbemfv
```

Where "*" is replaced by the missing character in the corresponding position

## For example
Characters you may be missing at the beginning at the end or in the middle
```bash
python missing.py --missingkey=KwD**f89QgGbjEhKnhXJuH**rhcVkatbczm7Y9ZaB56U1jLN**Xh --address 1NLbHuJebVwUZ1XqDjsAyfTRUPwDQbemfv
```
After we launch it will look like this
```bash
                         =================================================
                        ||                                               ||
                        || ╔═══╗╔╗ ╔╗╔══╗╔═╗ ╔╗    ╔═══╗╔╗ ╔╗╔═══╗╔═╗╔═╗ ||
                        || ║╔═╗║║║ ║║╚╣╠╝║║╚╗║║    ║╔═╗║║║ ║║║╔═╗║║║╚╝║║ ||
                        || ║╚══╗║╚═╝║ ║║ ║╔╗╚╝║    ║╚═╝║║╚═╝║║║ ║║║╔╗╔╗║ ||
                        || ╚══╗║║╔═╗║ ║║ ║║╚╗║║    ║╔══╝║╔═╗║║╚═╝║║║║║║║ ||
                        || ║╚═╝║║║ ║║╔╣╠╗║║ ║║║    ║║   ║║ ║║║╔═╗║║║║║║║ ||
                        || ╚═══╝╚╝ ╚╝╚══╝╚╝ ╚═╝    ╚╝   ╚╝ ╚╝╚╝ ╚╝╚╝╚╝╚╝ ||
                        ||===============================================||
                        ||           Website : shinpham.online           ||
                        ||           Email   : shinpham.dev@gmail.com    ||
                        ||           Github.com/Shinphamdev              ||
                        ||===============================================||
                        ||-----------Recovering Privatekey...------------||
                         =================================================


Privatekey Missing  6 characters : KwD**f89QgGbjEhKnhXJuH**rhcVkatbczm7Y9ZaB56U1jLN**Xh    Wallet Address :1NLbHuJebVwUZ1XqDjsAyfTRUPwDQbemfv
  0%|                                                              | 198027/38068692544 [00:08<471:47:39, 22413.55it/s]
  ```
  For more missing characters, it will take longer to find the correct private key, depending on your computer configuration.
  For about 3 to 5 characters it can take you several hours to find the exact private key that is missing from your address.
  
  ## Result
  
  The above wallet address I am using the privatekey of the Bitcoin 115 puzzle so that is just an example
  When a valid private is found and matches the wallet address
  It will automatically save and balance.txt
  Private key :
  ```bash
  KwDiBf89QgGbjEhKnhXJuH7LrhcVkatbczm7Y9ZaB56U1jLNU2Xh
  ```
  Address : 
 ```bash
 1NLbHuJebVwUZ1XqDjsAyfTRUPwDQbemfv
 ```
 ```bash
                          =================================================
                        ||                                               ||
                        || ╔═══╗╔╗ ╔╗╔══╗╔═╗ ╔╗    ╔═══╗╔╗ ╔╗╔═══╗╔═╗╔═╗ ||
                        || ║╔═╗║║║ ║║╚╣╠╝║║╚╗║║    ║╔═╗║║║ ║║║╔═╗║║║╚╝║║ ||
                        || ║╚══╗║╚═╝║ ║║ ║╔╗╚╝║    ║╚═╝║║╚═╝║║║ ║║║╔╗╔╗║ ||
                        || ╚══╗║║╔═╗║ ║║ ║║╚╗║║    ║╔══╝║╔═╗║║╚═╝║║║║║║║ ||
                        || ║╚═╝║║║ ║║╔╣╠╗║║ ║║║    ║║   ║║ ║║║╔═╗║║║║║║║ ||
                        || ╚═══╝╚╝ ╚╝╚══╝╚╝ ╚═╝    ╚╝   ╚╝ ╚╝╚╝ ╚╝╚╝╚╝╚╝ ||
                        ||===============================================||
                        ||           Website : shinpham.online           ||
                        ||           Email   : shinpham.dev@gmail.com    ||
                        ||           Github.com/Shinphamdev              ||
                        ||===============================================||
                        ||-----------Recovering Privatekey...------------||
                         =================================================


Privatekey Missing  3 characters : KwDiBf89QgGbjEhKnhXJuH7LrhcVkatbczm7Y9ZaB56U1jLNU***    Wallet Address :1NLbHuJebVwUZ1XqDjsAyfTRUPwDQbemfv
  2%|█▋                                                                       | 4649/195112 [00:00<00:08, 23047.42it/s]
  Complete PrivateKey: KwDiBf89QgGbjEhKnhXJuH7LrhcVkatbczm7Y9ZaB56U1jLNU2Xh Address: 1NLbHuJebVwUZ1XqDjsAyfTRUPwDQbemfv

DONATE (BTC) : 36yuDHFQtMj1h26wF8F46MMqeUfGyzcMmX
```
## Donate

If you find it useful, please donate to me 1 cup of coffee
 ```bash
DONATE (BTC) : 36yuDHFQtMj1h26wF8F46MMqeUfGyzcMmX
```
## Follow me
 ```bash
Webite    : https://shinpham.online/
Instagram : https://www.instagram.com/shinpham.dev/
Facebook  : https://www.facebook.com/thachquisal.net
Youtube   : https://www.youtube.com/@shinpham.developers
Gmail     : shinpham.dev@gmail.com
```
