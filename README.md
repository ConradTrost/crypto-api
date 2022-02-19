## Installation

First, clone this repository onto your local machine.

Make sure python3 and pip are installed, as well as the requests module `pip install requests` or `pip3 install requests`
#
Create and [Alpha Vantage API Key](https://www.alphavantage.co/) (free)

There is currently a limit of 5 requests per minute, and a limit of 500 requests per day with the free tier.

Create a root file 'constants.py' and add the line 
`API_KEY = 'YOUR_API_KEY'`

**Be sure not to commit your API Key**

constants.py is currently in .gitignore. For security reasons, please do not remove from .gitignore. Do not publicly share your API keys.