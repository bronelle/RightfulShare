# this is the Rightful Share Record-Keeping System
# Fri 13 Jan 2023

def AddChain():
    chain = {}
    chain['handle'] = {} # wallets
    chain['transactions'] = []
    chain['queue'] = {} # revenue streams
    return chain

def AddQueue():
    queue = {}
    return queue

# # # run # # #
records = {}
records['chain'] = {}
records['pool'] = {}
records['community'] = {}

records['chain']['ETH'] = AddChain()
records['chain']['ETH']['queue']['gitcoin'] = AddQueue()
