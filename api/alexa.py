from everything import *

@ask.launch
def start_skill():
    welcome_message = 'Hello there, I am your bank manager. How can I help?'
    return question(welcome_message)

@ask.intent("Balance")
def check_balance():
    message = bankInstance.getBalance(bank=cfg['bank']['bank_id'],\
                        account=cfg['bank']['account'])
    return statement(message)

@ask.intent("SendMoney")
def send_money(amount, account_name):
    print account_name
    message = bankInstance.makePayment(mybank=cfg['bank']['bank_id'],\
                         myaccount=cfg['bank']['account'],\
                         otheraccount=account_name, amount=str(amount))
    return question(message)

@ask.intent("YesIntent")
def share_headlines():
    message = bankInstance.getBalance(bank=cfg['bank']['bank_id'],\
                        account=cfg['bank']['account'])
    return statement(message)

@ask.session_ended
def no_intent():
    bye_text = 'I am not sure why you asked me to run then, but okay... bye'
    return statement(bye_text)

@ask.intent("showAccounts")
def show_accounts():
    message = bankInstance.showAccounts()
    return question(message)

@ask.intent("LastTransaction")
def get_last_transaction():
    message= bankInstance.getMostRecentTransaction(cfg['bank']['bank_id'],cfg['bank']['account'])
    return question(message)

@ask.intent("NumberTransactions")
def get_num_transactions():
    message = bankInstance.numberOfTransactions()
    return question(message)
    
    
    
    
    
    