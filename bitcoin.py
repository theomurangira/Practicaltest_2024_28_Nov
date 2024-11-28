'''
In this file, implement a program that:

-> Expects the user to specify two  command-line arguments:
   the number of Bitcoins (a float), and the currency they have.
   If the first command-line argument cannot be converted to a float,
   the program should exit via sys.exit with an error message. 
   The same error message should be used if the second command-line argument 
   is not a valid currency (The only currenices supported are "GBP","USD" and "EUR"). 
-> Queries the API for the CoinDesk Bitcoin Price Index at
   https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, 
   among whose nested keys is the current price of Bitcoin as a float.
 -> Outputs the current cost of the number of  Bitcoins specified by the first command-line 
    argument in the currency specified by the second command-line argument.
    The result should be displayed with four decimal places, using , as a thousands separator.

'''