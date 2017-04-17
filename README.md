# HelloBanking
## Inspiration
We drew our inspiration from the world's need to make technology accessible for everyone. By thinking about the visually impaired and popular banking apps, we realized that banking has not been made easy for everyone. Because of our concern for accessibility and our notice of the approximately 280 million people who are currently considered visually impaired, we created a virtual banking assistant that allows easy access to personal balances and transactions through voice commands powered by machine learning.

## What it does
HelloBanking takes voice commands from the user to make queries to the user's bank. Unlike typical virtual assistants that use very specific commands, HelloBanking uses machine learning to get the gist of what the user desires. For example, "check my account balance," "how much money do I have", and "what is the balance of my account" cause HelloBanking to understand that you desire to know your current bank balance and queries the bank server to obtain it for you.

## How we built it
We built HelloBanking through the utilization of Python libraries, such as requests. We began by first creating a webapp built with Flask that relies on api.ai to understand what queries the user wants from the bank. After successfully creating the webapp, we then integrated our idea into Amazon's Alexa to bring easy banking into the home using Alexa's natural language processing.

## Challenges we ran into
One of the challenges we ran into was obtaining useful bank data. We then, however, discovered OpenBankingProject which suited our needs to receive realistic bank data for the user.

## Accomplishments that we're proud of
Using machine learning to allow banking to be made more accessible for those who may have a difficult time using applications not made easily accessible to everyone. We are also proud of working Alexa and Amazon's great developer tools made for Alexa.

## What we learned
We learned how to use natural language possessing and we learned about the components that make it work. Our close encounter with utterances and intents has made this project invaluable.

## What's next for HelloBanking
The next move for HelloBanking is to encourage banks to integrate HelloBanking so their customers have easier access to their services. Along with integrating real bank data, we would also like to add more features to HelloBanking in order to make more advanced queries and give greater customer service.

## Built With
python,
flask,
api.ai,
chrome,
google-web-speech-api,
flask-ask,
amazon-web-services,
aws-lambda,
alexa,
machine-learning,
natural-language-processing
