import sys, time, requests, string

BASE_URL = "https://apisandbox.openbankproject.com"
API_VERSION = "v2.0.0"
CONSUMER_KEY = '1hkd22qklce12luoftpblfaalbcj0t2u1ikqddju'
USERNAME = 'sharrona'
PASSWORD = "ImpendingD00m!"
BANK = 'op.02.us'
LOGGING = True
DL_TOKEN    = { 'Authorization' : 'DirectLogin token=' }
CONTENT_JSON  = { 'content-type'  : 'application/json' }
ACCOUNT = 'bereatest'

### helper functions to help with log in and merging json information
def mergeHeaders(x, y):
    z = x.copy()
    z.update(y)
    return z


def log(m):
    if LOGGING:
        print(m)
        
def setToken(t):
    global DL_TOKEN 
    DL_TOKEN = { 'Authorization' : 'DirectLogin token=%s' % t}


def login(username, password, consumer_key):
    login_url = '{0}/my/logins/direct'.format(BASE_URL)
    login_header  = { 'Authorization' : 'DirectLogin username="%s",password="%s",consumer_key="%s"' % (username, password, consumer_key)}
    # Login and receive authorized token
    log('Login as {0} to {1}'.format(login_header, login_url))
    r = requests.get(login_url, headers=login_header)
    if (r.status_code != 200):
        log("error: could not login")
        log("text: " + r.text)
        return r.text
    t = r.json()['token']
    log("Received token: {0}".format(t))
    setToken(t)
    return t
######################

def getBanks():
    # Prepare headers
    response = requests.get(u"{0}/obp/{1}/banks".format(BASE_URL, API_VERSION), headers=mergeHeaders(DL_TOKEN, CONTENT_JSON))
    return response.json()['banks']

def getAccounts():
    list_of_accounts = []
    response = requests.get(u"{0}/obp/{1}/accounts".format(BASE_URL,API_VERSION), headers=mergeHeaders(DL_TOKEN,CONTENT_JSON))
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
def getPrivateAccounts(bank):
    # Prepare headers
    response = requests.get(u"{0}/obp/{1}/banks/{2}/accounts/private".format(BASE_URL, API_VERSION, bank), headers=mergeHeaders(DL_TOKEN, CONTENT_JSON))
    return response.json()['accounts']

#Goest through all private accounts and just pulls out their names
def getPrivateAccountNames(bank):
    accounts = []
    result = "Your accounts are "
    for i in getPrivateAccounts(bank):
        accounts.append(i['id'])
    for i in accounts:
        result += i + ' '
    return result

#Gets the amount of the balance in an account
def getBalance(bank,account):
    response = requests.get(u"{0}/obp/{1}/my/banks/{2}/accounts/{3}/account".format(BASE_URL, API_VERSION, bank, account), headers=mergeHeaders(DL_TOKEN, CONTENT_JSON))
    balance = response.json()['balance']['amount']
    result = 'Your balance is $' + balance
    return result

#Gets all transactions made on an account
def getTransactions(bank, account):
    
    response = requests.get(u"{0}/obp/{1}/banks/{2}/accounts/{3}/owner/transactions".format(BASE_URL, API_VERSION, bank, account), headers=mergeHeaders(DL_TOKEN, CONTENT_JSON))
    result = 'You have had ' +  str(len(response.json()['transactions'])) + ' transactions'
    return result


def getTransaction(bank_id, account_id, transaction_id):
    response = requests.get(u"{0}/obp/{1}/banks/{2}/accounts/{3}/owner/transactions/{4}/transaction".format(BASE_URL, API_VERSION, bank_id, account_id, transaction_id), headers=mergeHeaders(DL_TOKEN, CONTENT_JSON))
    result = 'This transaction was made on ' + response.json()['details']['completed'].split('T')[0]
    return result


def makePayment(mybank,myaccount,otherbank,otheraccount,amount):
    post_data = {
            "account_id" : '%s' % otheraccount,
            "bank_id" : '%s' % otherbank,
            "amount" : '%s' % amount
            }
    
    response = requests.post(u"{0}/obp/{1}/banks/{2}/accounts/{3}/owner/transactions".format(BASE_URL,API_VERSION,mybank,myaccount),json=post_data,headers=mergeHeaders(DL_TOKEN,CONTENT_JSON))
    return response




#Logs user in
login(USERNAME, PASSWORD, CONSUMER_KEY)






