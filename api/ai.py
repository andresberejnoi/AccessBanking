from everything import *
import sys, time, requests, string

class ApiAi:
    def __init__(self, cfg):
        self.cfg = cfg
        self.bankapi = BankingApi(self.cfg)

    def sendQuery(self, query):

        payload = {'v': cfg['api-ai']['v'],\
                    'query': query,\
                    'timezone': cfg['api-ai']['timezone'],\
                    'lang': cfg['api-ai']['lang'],\
                    'sessionId': cfg['api-ai']['sessionId']
                }
        login_header = {'Authorization' : 'Bearer {0}'\
                                    .format(cfg['api-ai']['access_token']),\
                        'Content-Type': 'application/json'}

        r = requests.post(cfg['api-ai']['base_url'], headers=login_header, data=json.dumps(payload))
        if (r.status_code != 200):
            print ("error")
            return r.text
        return r.json()

    def balance(self):
        
        return self.bankapi.getBalance(bank=self.cfg['bank']['bank_id'],\
                            account=self.cfg['bank']['account'])
        
    def numberOfTransactions(self):
    
        return self.bankapi.getNumberOfTransactions(bank=self.cfg['bank']['bank_id'],\
                                         account=self.cfg['bank']['account'])
    
    def showAccounts(self):
    
        return self.bankapi.getPrivateAccountNames(bank=self.cfg['bank']['bank_id'])
    
    def lastTransaction(self):
    
        return self.bankapi.getMostRecentTransaction(bank=self.cfg['bank']['bank_id'],\
                                          account=self.cfg['bank']['account'])
    
    def indexedTransaction(self):

        return self.bankapi.getTransactionNumber(bank=self.cfg['bank']['bank_id'],\
                                      account=self.cfg['bank']['account'],transaction_number=1)
        
    def makePayment(self,otherbank,otheraccount,amount):
    
        return self.bankapi.makePayment(mybank=self.cfg['bank']['bank_id'],\
                             myaccount=self.cfg['bank']['account'],\
                             otherbank=otherbank,otheraccount=otheraccount,amount=amount)
    
    def methodChoice(self,data):
        
        if data['result']['parameters']['options'] == 'balance':
            return self.balance()
        
        elif data['result']['parameters']['options'] == 'number of transactions':
            return self.numberOfTransactions()
        
        elif  data['result']['parameters']['options'] == 'show accounts':
            return self.showAccounts()
        
        elif data['result']['parameters']['options'] == 'last transaction':
            return self.lastTransaction()
        
        elif data['result']['parameters']['options'] == 'indexed transaction':
            return self.indexedTransaction()
        
        elif data['result']['parameters']['options'] == 'make a payment':
            return self.makePayment(data['result']['parameters']['bank'],\
                                    data['result']['parameters']['account'],\
                                    str(data['result']['parameters']['amount']['amount']))
        
        

if __name__ == "__main__":
    testInstance = ApiAi(cfg)
    #data = testInstance.sendQuery('Make a payment of $20 to op.02.us to account berearecv')
    data = testInstance.sendQuery('whats my balance')
    print(testInstance.methodChoice(data))
    
    
