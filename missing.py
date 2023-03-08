# ===================================================||
# DONATE (BTC) : 36yuDHFQtMj1h26wF8F46MMqeUfGyzcMmX  ||
# Website : shinpham.online                          ||
# Email : shinpham.dev@gmail.com                     ||
# Github.com/Shinphamdev                             ||
# ===================================================||

#  ||===============================================||
#     ╔═══╗╔╗ ╔╗╔══╗╔═╗ ╔╗    ╔═══╗╔╗ ╔╗╔═══╗╔═╗╔═╗
#     ║╔═╗║║║ ║║╚╣╠╝║║╚╗║║    ║╔═╗║║║ ║║║╔═╗║║║╚╝║║
#     ║╚══╗║╚═╝║ ║║ ║╔╗╚╝║    ║╚═╝║║╚═╝║║║ ║║║╔╗╔╗║
#     ╚══╗║║╔═╗║ ║║ ║║╚╗║║    ║╔══╝║╔═╗║║╚═╝║║║║║║║
#     ║╚═╝║║║ ║║╔╣╠╗║║ ║║║    ║║   ║║ ║║║╔═╗║║║║║║║
#     ╚═══╝╚╝ ╚╝╚══╝╚╝ ╚═╝    ╚╝   ╚╝ ╚╝╚╝ ╚╝╚╝╚╝╚╝
#  ||===============================================||   
#  ||           Website : shinpham.online           ||
#  ||           Email   : shinpham.dev@gmail.com    ||
#  ||           Github.com/Shinphamdev              ||    
#  ||===============================================||                      


#-----------------------------------------------------
import string
import argparse
import sys
import trotter
from tqdm import tqdm
from time import sleep
from hdwallet import HDWallet
from hdwallet.symbols import BTC
from btc_com import explorer as btc_explorer

shinpham='''
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
               
               '''

def write_to_log(data):
    with open("banlace.txt", "a") as file:
        file.write(data + '\n')


def complete_key(missing_key_string, missing_letters):
    for letter in missing_letters:
        missing_key_string = missing_key_string.replace('*', letter, 1)
    return missing_key_string


def fetch_balance_for_btc_address(btc_address):
    address_info = btc_explorer.get_address(btc_address)
    return address_info.balance, address_info.tx_count


def btc_address_from_private_key(my_secret, secret_type='WIF'):
    assert secret_type in ['WIF', 'classic', 'extended', 'mnemonic', 'mini']
    hdwallet = HDWallet(symbol=BTC)
    match secret_type:
        case 'WIF':
            hdwallet.from_wif(wif=my_secret)
        case 'classic':
            hdwallet.from_private_key(private_key=my_secret)
        case 'mnemonic':
            raise "Mnemonic secrets not implemented"
        case 'mini':
            raise "Mini private key not implemented"
        case 'extended':
            hdwallet.from_xprivate_key(xprivate_key=my_secret)
        case _:
            raise "I don't know how to handle this type."

    return hdwallet.p2pkh_address()


def parse_arguments():
    cli_argument_parser = argparse.ArgumentParser(
        description='Recover incomplete or damaged BTC private keys',
        epilog="2023 © Shin Phạm - All rights reserved."
    )
    cli_argument_parser.add_argument("--missingkey", help="private key with unknown characters replaced by *", metavar="MY**KEY", default=None)
    cli_argument_parser.add_argument("--address", help="the target BTC address if known", default=None)
    cli_argument_parser.add_argument("--fetchbalances", help="display BTC balance for potential addresses (slower)", action='store_true', default=False)
    cli_argument_parser.add_argument("--mode", help="sequential or random", default='sequential', choices=['sequential', 'random'])
    namespace_arguments = cli_argument_parser.parse_args()
    if namespace_arguments.missingkey is None:
        cli_argument_parser.print_help()
        cli_argument_parser.exit("Error: No masked key was provided.")
    return namespace_arguments
cli_arguments = parse_arguments()

if __name__ == '__main__':
    missing_key = cli_arguments.missingkey
    target_address = cli_arguments.address
    fetch_balances = cli_arguments.fetchbalances
    mode = cli_arguments.mode
    missing_length = missing_key.count('*')
    key_length = len(missing_key)
    print(shinpham)


    print(f"Privatekey Missing  {missing_length} characters : {missing_key}    Wallet Address :{target_address}")
    match key_length:
        case 51 | 52:
            secret_type = 'WIF'
            allowed_characters = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        case 64:
            secret_type = 'classic'
            allowed_characters = string.digits + "ABCDEF"
        case 111:
            secret_type = 'extended'
            allowed_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
        case _:
            secret_type = 'unhandled'
            allowed_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

    missing_letters_master_list = trotter.Amalgams(missing_length, allowed_characters)

    try:
        max_loop_length = len(missing_letters_master_list)
    except OverflowError:
        max_loop_length = sys.maxsize
        if mode == 'sequential':
            print(f"Warning: Some letters will not be processed in sequential mode because "
                  f"the possible space is too large. Try random mode.")

    for i in tqdm(range(max_loop_length)):
        if mode == 'sequential':
            potential_key = complete_key(missing_key, missing_letters_master_list[i])
        elif mode == 'random':
            potential_key = complete_key(missing_key, missing_letters_master_list.random())

        try:
            address = btc_address_from_private_key(potential_key, secret_type=secret_type)

            if target_address:
                if address != cli_arguments.address:
                    continue

            print(f" Complete PrivateKey: {potential_key} Address: {address}")
            print(f" ")
            print(f"DONATE (BTC) : 36yuDHFQtMj1h26wF8F46MMqeUfGyzcMmX ")
            print(f" ")
            if fetch_balances:
                balance, tx_count = fetch_balance_for_btc_address(address)
                print(f"tx_count: {tx_count} balance: {balance}")

            write_to_log(f"key: {potential_key} address: {address}")

        except ValueError:
            pass

