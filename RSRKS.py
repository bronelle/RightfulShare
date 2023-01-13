# this is the Rightful Share Record-Keeping System
# Fri 13 Jan 2023

def AddChain():
    chain = {}
    chain['handle'] = {} # wallets
    chain['queue'] = {} # revenue streams
    return chain

def AddQueue(currency):
    queue = {}
    queue['currency'] = currency
    queue['transactions'] = []
    queue['processed'] = 0
    return queue

def AddHandle(nickname, note):
    handle = {}
    handle['nickname'] = nickname
    handle['note'] = note
    handle['contributions'] = []
    return handle

def AddTransaction(amount, handle, link):
    transaction = {}
    transaction['amount'] = amount
    transaction['handle'] = handle
    transaction['link'] = link
    return transaction

def AddPool():
    pool = {}
    pool['value'] = []
    return pool

def AddValue(currency):
    value = {}
    value['amount'] = 0
    value['currency'] = currency
    return value

def AddContribution(pool, amount):
    contribution = {}
    contribution['pool'] = pool
    contribution['amount'] = amount
    return contribution

# # # run # # #
RSR = {}
RSR['chain'] = {}
RSR['pool'] = {}
RSR['community'] = {}

RSR['chain']['ETH'] = AddChain()

RSR['chain']['ETH']['handle']['0x2527fedd0eb265b82126c7fec1ede54199302ecd'.lower()] = AddHandle('', 'Patrick.AskNFTY @patrickasknfty on gitcoin')
RSR['chain']['ETH']['handle']['0x3abdC9ed5f5dE6A74CFeb42a82087C853E160E76'.lower()] = AddHandle('therealstone.eth','Anna Stone from GoodDollar')
RSR['chain']['ETH']['handle']['0x4ae7ffa2291adf1fbd4b02650d25b2f54d5e90b8'.lower()] = AddHandle('leilastein.eth', '')
RSR['chain']['ETH']['handle']['0x5e50da7ba4158d80d1eefc587bd88309364bb870'.lower()] = AddHandle('','visperaza @visperaza on gitcoin')
RSR['chain']['ETH']['handle']['0x6B175474E89094C44Da98b954EedeAC495271d0F'.lower()] = AddHandle('gitcoin', 'contract')
RSR['chain']['ETH']['handle']['0x6eeb37b9757dca963120f61c7e0e0160469a44d3'.lower()] = AddHandle('merifdez.eth', 'meri91 @meri91 on gitcoin')
RSR['chain']['ETH']['handle']['0x7a738effd10bf108b7617ec8e96a0722fa54c547'.lower()] = AddHandle('habitat.eth', '')
RSR['chain']['ETH']['handle']['0x7da740d237575470b19284ec013fb5ea1f680f00'.lower()] = AddHandle('riskyasset.eth', '')
RSR['chain']['ETH']['handle']['0x7e54c31020Fd3399E649e6497e47B99e0CBA1925'.lower()] = AddHandle('Rightful Share', 'wallet for gitcoin')
RSR['chain']['ETH']['handle']['0xb31ef912c68b1f52b693d7e23dfa4a7f22f209be'.lower()] = AddHandle('strfsh.eth', '')
RSR['chain']['ETH']['handle']['0xc7d0961e09ef783b02e951b3a0704236ae7cabb5'.lower()] = AddHandle('', 'civileddie @civileddie on gitcoin')
RSR['chain']['ETH']['handle']['0xdeb0804d5e54d49c1923da459730e66b60eead6b'.lower()] = AddHandle('', 'New Atlantis DAO @newatlantisdao on gitcoin')
RSR['chain']['ETH']['handle']['0xf2b22e4cfa1f9d20d6fec2e7225e14e72de5ca59'.lower()] = AddHandle('tianysaurus.eth', '')

RSR['chain']['ETH']['handle']
RSR['chain']['ETH']['handle']
    
RSR['chain']['ETH']['queue']['gitcoin-DAI'] = AddQueue('DAI')
RSR['chain']['ETH']['queue']['gitcoin-USDC'] = AddQueue('USDC')
RSR['chain']['ETH']['queue']['gitcoin-ETH'] = AddQueue('ETH')

RSR['chain']['ETH']['queue']['gitcoin-DAI']['transactions'].append(AddTransaction(30, '0x3abdc9ed5f5de6a74cfeb42a82087c853e160e76'.lower(), 'https://etherscan.io/tx/0x4835ea11208e7fc831e2a8d32290cbf714b42c270af85cac82ee50ac1ecf5746'))
RSR['chain']['ETH']['queue']['gitcoin-DAI']['transactions'].append(AddTransaction(5, '0x7a738effd10bf108b7617ec8e96a0722fa54c547'.lower(), 'https://etherscan.io/tx/0x40eacc35542a797afcdffda4e20dcfaa6865fc7d963e8c747a454e196cf889d4'))
RSR['chain']['ETH']['queue']['gitcoin-DAI']['transactions'].append(AddTransaction(25, '0x3abdc9ed5f5de6a74cfeb42a82087c853e160e76'.lower(), 'https://etherscan.io/tx/0x0cc04179a501b661214d1a74ea6d7d030dda84a4b041ab9bc620f8aa461f994e'))
RSR['chain']['ETH']['queue']['gitcoin-DAI']['transactions'].append(AddTransaction(25, '0xf2b22e4cfa1f9d20d6fec2e7225e14e72de5ca59'.lower(), 'https://etherscan.io/tx/0x68831ea2c2fc4622fbe03753b87df631a2c28fd56058430722264b9b01dc0e9e'))
RSR['chain']['ETH']['queue']['gitcoin-DAI']['transactions'].append(AddTransaction(206.3377441645403, '0x6B175474E89094C44Da98b954EedeAC495271d0F'.lower(), 'https://etherscan.io/tx/0x5dfd9ea2b3e3721eb7b0f750f489f772d3a27b35144770c5e5069460309e937b'))

RSR['chain']['ETH']['queue']['gitcoin-USDC']['transactions'].append(AddTransaction(25, '0x7da740d237575470b19284ec013fb5ea1f680f00'.lower(), 'https://etherscan.io/tx/0x539de29e83f1c31c0e09ab1b827cd731700eb890836f0774dd1dec06250120f3'))
RSR['chain']['ETH']['queue']['gitcoin-USDC']['transactions'].append(AddTransaction(10, '0xdeb0804d5e54d49c1923da459730e66b60eead6b'.lower(), 'https://etherscan.io/tx/0xb7538c05e10f321f3ce37801b444405291e555ef72471882830a71745f9f4d3b'))

RSR['chain']['ETH']['queue']['gitcoin-ETH']['transactions'].append(AddTransaction(0.002, '0x2527fedd0eb265b82126c7fec1ede54199302ecd'.lower(), 'https://etherscan.io/tx/0xbc5aa7cabf29d28613733f66223106427ed0e7aef600c9160afa474877e01eb7'))
RSR['chain']['ETH']['queue']['gitcoin-ETH']['transactions'].append(AddTransaction(0.00065, '0x4ae7ffa2291adf1fbd4b02650d25b2f54d5e90b8'.lower(), 'https://etherscan.io/tx/0x8e717f41180d97c531dbab235257d12fd0e2173f1f4f466c0085afa56e24b3fe'))
RSR['chain']['ETH']['queue']['gitcoin-ETH']['transactions'].append(AddTransaction(0.02, '0x6eeb37b9757dca963120f61c7e0e0160469a44d3'.lower(), 'https://etherscan.io/tx/0xb04fcc2c1d7fb03ebc580b12cc66228628fa8ef2f9aeb7199563f72675d52938'))
RSR['chain']['ETH']['queue']['gitcoin-ETH']['transactions'].append(AddTransaction(1, '0xb31ef912c68b1f52b693d7e23dfa4a7f22f209be'.lower(), 'https://etherscan.io/tx/0x3fbd6de5dd58a4853677c8bd361491b92faf0e89c3608f922c1f579bb5320213'))
RSR['chain']['ETH']['queue']['gitcoin-ETH']['transactions'].append(AddTransaction(0.04, '0xc7d0961e09ef783b02e951b3a0704236ae7cabb5'.lower(), 'https://etherscan.io/tx/0xb8b4ee9cc483b52ef280e3886439382b6fe6d2c2042427f8d1638e8969e09aa9'))
RSR['chain']['ETH']['queue']['gitcoin-ETH']['transactions'].append(AddTransaction(0.001, '0x5e50da7ba4158d80d1eefc587bd88309364bb870'.lower(), 'https://etherscan.io/address/0x7e54c31020Fd3399E649e6497e47B99e0CBA1925#internaltx'))

RSR['pool']['gitcoin-DAI'] = AddPool()

RSR['pool']['gitcoin-DAI']['value'].append(AddValue(RSR['chain']['ETH']['queue']['gitcoin-DAI']['currency']))

for transaction in RSR['chain']['ETH']['queue']['gitcoin-DAI']['transactions']:
    RSR['pool']['gitcoin-DAI']['value'][0]['amount'] += transaction['amount']
    RSR['chain']['ETH']['handle'][transaction['handle']]['contributions'].append(AddContribution('gitcoin-DAI', transaction['amount']))
    RSR['chain']['ETH']['queue']['gitcoin-DAI']['processed'] += 1
    



