from everything import *
import sys, time, requests, string

class ApiAi:
    def __init__(self, cfg):
        self.cfg = cfg

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
            print "error"
            return r.text
        print r.json()

if __name__ == "__main__":
    testInstance = ApiAi(cfg)
    testInstance.sendQuery('send money')
