
# begin

def Init():
    record = {}
    record['platform'] = {}
    record['platform']['RS'] = {}
    record['platform']['RS']['handle'] = {}
    record['platform']['ETH'] = {}
    record['platform']['ETH']['handle'] = {}
    record['platform']['handle'] = {}
    record['contribution'] = {}
    return record

record = Init()

#

record['platform']['RS']['handle']['karen'] = {'name': 'Karen Jooste', 'role': 'Founder'}
record['platform']['RS']['handle']['leila'] = {'name': 'Leila Stein', 'role': 'Board Member'}
record['platform']['RS']['handle']['bronwyn'] = {'name': 'Bronwyn Ellerbeck', 'role': 'Board Member'}

record['platform']['ETH']['handle']['0x07fde37f0e622deec96d17120f99c929d7fb1785'.lower()] = {'ens': '', 'gitcoin': '@lthrift'}
record['platform']['ETH']['handle']['0x16c43cb88bcc4a966819542321d595581220f53a'.lower()] = {'ens': '', 'gitcoin': '@l03tj3'}
record['platform']['ETH']['handle']['0x2527fedd0eb265b82126c7fec1ede54199302ecd'.lower()] = {'ens': '', 'gitcoin': '@patrickasknfty'}
record['platform']['ETH']['handle']['0x3abdC9ed5f5dE6A74CFeb42a82087C853E160E76'.lower()] = {'ens': 'therealstone.eth', 'gitcoin': '@annastone-86'}
record['platform']['ETH']['handle']['0x4ae7ffa2291adf1fbd4b02650d25b2f54d5e90b8'.lower()] = {'ens': 'leilastein.eth', 'gitcoin': '@leila-za'}
record['platform']['ETH']['handle']['0x5e50da7ba4158d80d1eefc587bd88309364bb870'.lower()] = {'ens': '', 'gitcoin': '@visperaza'}
record['platform']['ETH']['handle']['0x6B175474E89094C44Da98b954EedeAC495271d0F'.lower()] = {'ens': '', 'gitcoin': '@gitcoinbot'}
record['platform']['ETH']['handle']['0x6eeb37b9757dca963120f61c7e0e0160469a44d3'.lower()] = {'ens': 'merifdez.eth', 'gitcoin': '@meri91'}
record['platform']['ETH']['handle']['0x7a738effd10bf108b7617ec8e96a0722fa54c547'.lower()] = {'ens': 'habitat.eth', 'gitcoin': '@todd-x-y'}
record['platform']['ETH']['handle']['0x7da740d237575470b19284ec013fb5ea1f680f00'.lower()] = {'ens': 'riskyasset.eth', 'gitcoin': '@chandlerdekock'}
record['platform']['ETH']['handle']['0x7e54c31020Fd3399E649e6497e47B99e0CBA1925'.lower()] = {'ens': '', 'gitcoin': '@karenjooste'}
record['platform']['ETH']['handle']['0xb31ef912c68b1f52b693d7e23dfa4a7f22f209be'.lower()] = {'ens': 'strfsh.eth', 'gitcoin': '@strfsh-eth'}
record['platform']['ETH']['handle']['0xc7d0961e09ef783b02e951b3a0704236ae7cabb5'.lower()] = {'ens': '', 'gitcoin': '@civileddie'}
record['platform']['ETH']['handle']['0xdeb0804d5e54d49c1923da459730e66b60eead6b'.lower()] = {'ens': '', 'gitcoin': '@newatlantisdao'}
record['platform']['ETH']['handle']['0xf2b22e4cfa1f9d20d6fec2e7225e14e72de5ca59'.lower()] = {'ens': 'tianysaurus.eth', 'gitcoin': '@tosfan4ever'}

#

def AddContribution(chain, currency, transactions):
    contribution = {}
    contribution['initial'] = {}
    contribution['initial']['chain'] = chain
    contribution['initial']['currency'] = currency
    contribution['initial']['amount'] = 0
    contribution['contributers'] = []
    for i in range(len(transactions)):
        contribution['initial']['amount'] += transactions[i]['amount']
        exists = False        
        for j in range(len(contribution['contributers'])):
            if transactions[i]['handle'] == contribution['contributers'][j]['handle']:
                exists = True
                contribution['contributers'][j]['amount'] += transactions[i]['amount']
        if exists == False:
            contributer = {}
            contributer['handle'] = transactions[i]['handle']
            contributer['amount'] = transactions[i]['amount']
            contribution['contributers'].append(contributer)
    for i in range(len(contribution['contributers'])):
        contribution['contributers'][i]['percentage'] = contribution['contributers'][i]['amount']/contribution['initial']['amount']
    return contribution

transactions = []


record['contribution']['gitcoin-DAI'] = AddContribution('ETH', 'DAI',
                                                        [{'amount':30, 'handle': '0x3abdc9ed5f5de6a74cfeb42a82087c853e160e76'.lower(), 'link': 'https://etherscan.io/tx/0x4835ea11208e7fc831e2a8d32290cbf714b42c270af85cac82ee50ac1ecf5746'},
                                                         {'amount':5, 'handle': '0x7a738effd10bf108b7617ec8e96a0722fa54c547'.lower(), 'link': 'https://etherscan.io/tx/0x40eacc35542a797afcdffda4e20dcfaa6865fc7d963e8c747a454e196cf889d4'},
                                                         {'amount':25, 'handle': '0x3abdc9ed5f5de6a74cfeb42a82087c853e160e76'.lower(), 'link': 'https://etherscan.io/tx/0x0cc04179a501b661214d1a74ea6d7d030dda84a4b041ab9bc620f8aa461f994e'},
                                                         {'amount':25, 'handle': '0xf2b22e4cfa1f9d20d6fec2e7225e14e72de5ca59'.lower(), 'link':' https://etherscan.io/tx/0x68831ea2c2fc4622fbe03753b87df631a2c28fd56058430722264b9b01dc0e9e'},
                                                         {'amount':206.3377441645403, 'handle': '0x6B175474E89094C44Da98b954EedeAC495271d0F'.lower(), 'link': 'https://etherscan.io/tx/0x5dfd9ea2b3e3721eb7b0f750f489f772d3a27b35144770c5e5069460309e937b'}])

record['contribution']['gitcoin-USDC'] = AddContribution('ETH', 'USDC',
                                                         [{'amount': 25, 'handle': '0x7da740d237575470b19284ec013fb5ea1f680f00'.lower(), 'link': 'https://etherscan.io/tx/0x539de29e83f1c31c0e09ab1b827cd731700eb890836f0774dd1dec06250120f3'},
                                                          {'amount': 10, 'handle': '0xdeb0804d5e54d49c1923da459730e66b60eead6b'.lower(), 'link': 'https://etherscan.io/tx/0xb7538c05e10f321f3ce37801b444405291e555ef72471882830a71745f9f4d3b'}])

record['contribution']['gitcoin-ETH'] = AddContribution('ETH', 'ETH',
                                                        [{'amount': 0.002, 'handle': '0x2527fedd0eb265b82126c7fec1ede54199302ecd'.lower(), 'link': 'https://etherscan.io/tx/0xbc5aa7cabf29d28613733f66223106427ed0e7aef600c9160afa474877e01eb7'},
                                                         {'amount': 0.00065, 'handle': '0x4ae7ffa2291adf1fbd4b02650d25b2f54d5e90b8'.lower(), 'link': 'https://etherscan.io/tx/0x8e717f41180d97c531dbab235257d12fd0e2173f1f4f466c0085afa56e24b3fe'},
                                                         {'amount': 0.02, 'handle': '0x6eeb37b9757dca963120f61c7e0e0160469a44d3'.lower(), 'link': 'https://etherscan.io/tx/0xb04fcc2c1d7fb03ebc580b12cc66228628fa8ef2f9aeb7199563f72675d52938'},
                                                         {'amount': 1, 'handle': '0xb31ef912c68b1f52b693d7e23dfa4a7f22f209be'.lower(), 'link': 'https://etherscan.io/tx/0x3fbd6de5dd58a4853677c8bd361491b92faf0e89c3608f922c1f579bb5320213'},
                                                         {'amount': 0.04, 'handle': '0xc7d0961e09ef783b02e951b3a0704236ae7cabb5'.lower(), 'link': 'https://etherscan.io/tx/0xb8b4ee9cc483b52ef280e3886439382b6fe6d2c2042427f8d1638e8969e09aa9'},
                                                         {'amount': 0.001, 'handle': '0x5e50da7ba4158d80d1eefc587bd88309364bb870'.lower(), 'link': 'https://etherscan.io/address/0x7e54c31020Fd3399E649e6497e47B99e0CBA1925#internaltx'}])                                          

record['contribution']['gitcoin-MATIC'] = AddContribution('MATIC', 'MATIC',
                                                          [{'amount': 4, 'handle': '0x07fde37f0e622deec96d17120f99c929d7fb1785'.lower(), 'link': 'https://polygonscan.com/tx/0xe79bd0c646b62c0df12352cae39bc7de16c00da75d1d84685d8d9744ef9c4281'},
                                                           {'amount': 120, 'handle': '0x16c43cb88bcc4a966819542321d595581220f53a'.lower(), 'link': 'https://polygonscan.com/tx/0x3a8180a71d05c637d1d4890be166347e558f2147b441575e090d1f080b24a291'}])

# display

def DisplayContributions(record):
    for contribution in record['contribution']:
        print('\nContribution Pool : ' + contribution)
        print('Raised : ' + str(record['contribution'][contribution]['initial']['amount']) + ' ' + record['contribution'][contribution]['initial']['currency'])
        print('\n\tContributers\tShare\t\tgitcoin username')
        print('\t------------------------------------------------')
        for i in range(len(record['contribution'][contribution]['contributers'])):
            handle = record['contribution'][contribution]['contributers'][i]['handle']
            percentage = round(record['contribution'][contribution]['contributers'][i]['percentage']*100,2)
            if percentage < 10:
                percent = ' ' + str(percentage) + ' %'
            else:
                percent = str(percentage) + ' %'
            print('\t' + handle[:4] + '...' + handle[-2:] + '\t' + percent
                  + '\t\t' + record['platform']['ETH']['handle'][handle]['gitcoin'])


DisplayContributions(record)












