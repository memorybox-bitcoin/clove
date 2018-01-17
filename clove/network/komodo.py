from clove.network.base import BaseNetwork


class Komodo(BaseNetwork):
    """
    Class with all the necessary KMD network information based on
    https://github.com/jl777/komodo/blob/master/src/chainparams.cpp
    (date of access: 01/18/2018)
    """
    name = 'komodo'
    symbols = ('KMD', )
    seeds = (
        'seeds.komodoplatform.com',
        'seeds.komodo.mewhub.com',
    )
    port = 7770


class TestNetKomodo(Komodo):
    """
    Class with all the necessary KMD testing network information based on
    https://github.com/jl777/komodo/blob/master/src/chainparams.cpp
    (date of access: 01/18/2018)
    """
    name = 'test-komodo'
    # TODO Gather testing dns seeds
    seeds = ()
    port = 17779
