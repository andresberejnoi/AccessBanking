from everything import *
import sys, time, requests, string

DL_TOKEN    = { 'Authorization' : 'DirectLogin token=' }
CONTENT_JSON  = { 'content-type'  : 'application/json' }


class BankingApi:
    def __init__(self, cfg):
        self.cfg = cfg

    def mergeHeaders(self, x, y):
        z = x.copy()
        z.update(y)
        return z

    def log(self, m):
        print(m)

    def setToken(self, t):
        global DL_TOKEN
        DL_TOKEN = { 'Authorization' : 'DirectLogin token=%s' % t}


    def login(self, username, password):
        login_url = '{0}/my/logins/direct'.format(self.cfg['bank']['base_url'])
        auth_body = 'DirectLogin username={0},password={1},consumer_key={2}'\
                        .format(username, password,\
                                self.cfg['bank']['consumer_key'])
        login_header  = { 'Authorization' : auth_body}
        self.log('Login as {0} to {1}'.format(login_header, login_url))
        r = requests.get(login_url, headers=login_header)
        if (r.status_code != 200):
            self.log("error: could not login")
            self.log("text: " + r.text)
            return r.text
        t = r.json()['token']
        self.log("Received token: {0}".format(t))
        self.setToken(t)
        return t

    def getBanks(self):
        # Prepare headers
        response = requests.get(u"{0}/obp/{1}/banks"\
                                .format(self.cfg['bank']['base_url'],\
                                        self.cfg['bank']['api_version']),\
                                        headers=self.mergeHeaders(DL_TOKEN, CONTENT_JSON))
        return response.json()['banks']

    def getAccounts(self):
        list_of_accounts = []
        response = requests.get(u"{0}/obp/{1}/accounts"\
                                .format(self.cfg['bank']['base_url'],\
                                        self.cfg['bank']['api_version']),\
                                        headers=self.mergeHeaders(DL_TOKEN,CONTENT_JSON))
        for i in response.json():
            for j in i['views_available']:

                if type(j) == dict:
                    if j['is_public'] == False:
                        list_of_accounts.append(i)
        result = "Your accounts are "
        for i in list_of_accounts:
            result += 'bank ' +  i['bank_id'] + ' '
            result += 'with id ' +  i['id'] + ' '

        return result

    #Gets all private accounts and their information
    def getPrivateAccounts(self, bank):
        # Prepare headers
        response = requests.get(u"{0}/obp/{1}/banks/{2}/accounts/private"\
                                .format(self.cfg['bank']['base_url'],\
                                        self.cfg['bank']['api_version'],\
                                        bank),\
                                        headers=self.mergeHeaders(DL_TOKEN, CONTENT_JSON))

        return response.json()['accounts']

    #Goest through all private accounts and just pulls out their names
    def getPrivateAccountNames(self, bank):
        accounts = []
        result = "Your accounts are "
        for i in getPrivateAccounts(bank):
            accounts.append(i['id'])
        for i in accounts:
            result += i + ' '
        return result

    #Gets the amount of the balance in an account
    def getBalance(self, bank, account):
        response = requests.get(u"{0}/obp/{1}/my/banks/{2}/accounts/{3}/account"\
                    .format(self.cfg['bank']['base_url'],\
                            self.cfg['bank']['api_version'],\
                            bank,\
                            account),\
                            headers=self.mergeHeaders(DL_TOKEN, CONTENT_JSON))
        balance = response.json()['balance']['amount']
        result = 'Your balance is $' + balance
        return result

    #Gets all transactions made on an account
    def getTransactions(self, bank, account):

        response = requests.get(u"{0}/obp/{1}/banks/{2}/accounts/{3}/owner/transactions"\
                                .format(self.cfg['bank']['base_url'],\
                                        self.cfg['bank']['api_version'],\
                                        bank,\
                                        account),\
                                        headers=self.mergeHeaders(DL_TOKEN, CONTENT_JSON))
        result = 'You have had ' +  str(len(response.json()['transactions'])) + ' transactions'
        return result


    def getTransaction(self, bank, account, transaction_id):
        response = requests.get(u"{0}/obp/{1}/banks/{2}/accounts/{3}/owner/transactions/{4}/transaction"\
                                .format(self.cfg['bank']['base_url'],\
                                        self.cfg['bank']['api_version'],\
                                        bank, account, transaction_id),\
                                        headers=self.mergeHeaders(DL_TOKEN, CONTENT_JSON))
        result = 'This transaction was made on ' + response.json()['details']['completed'].split('T')[0]
        return result


    def makePayment(self, mybank, myaccount, otherbank, otheraccount, amount):
        post_data = {
                "account_id" : '%s' % otheraccount,\
                "bank_id" : '%s' % otherbank,\
                "amount" : '%s' % amount
                }
        response = requests.post(u"{0}/obp/{1}/banks/{2}/accounts/{3}/owner/transactions"\
                    .format(self.cfg['bank']['base_url'],\
                            self.cfg['bank']['api_version'],\
                            mybank, myaccount),\
                            json=post_data,\
                            headers=self.`mergeHeaders(DL_TOKEN,CONTENT_JSON))
        return response