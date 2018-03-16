
from clove.network.bitcoin.base import BitcoinBaseNetwork


class InsaneCoin(BitcoinBaseNetwork):
    """
    Class with all the necessary INSN network information based on
    http://www.github.com/CryptoCoderz/INSN/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'insanecoin'
    symbols = ('INSN', )
    seeds = ('insn.cryptocoderz.com',
             'insane.cryptocoderz.com')
    port = 10255
    message_start = b'\xa4\x3c\x2e\xf9'
    base58_prefixes = {
        'PUBKEY_ADDR': 102,
        'SCRIPT_ADDR': 57,
        'SECRET_KEY': 55
    }
    source_code_url = 'http://www.github.com/CryptoCoderz/INSN/blob/master/src/chainparams.cpp'
