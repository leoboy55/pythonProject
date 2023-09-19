# Imports
import cryptocompare
# Constants import -> normally add this in .git ignore to protect the api key
import os
# email service
import email_service

# variables
# retrieve api key from windows variables
api_key = os.environ.get('CRYPTOCOMPARE_API_KEY')


def set_api_key():
    cryptocompare.cryptocompare._set_api_key_parameter(api_key)


# checks the current price of Ethereum
def check_ethereum_price(formatted_time):
    # retrieve the Ethereum dictionary
    ethereum_price = cryptocompare.get_price('ETH')
    # print current Ethereum price with date time
    print(f"Current Ethereum price: {ethereum_price} on {formatted_time}")
    # return only the Ethereum price from dictionary rounded with 2 decimals
    return round(ethereum_price['ETH']['EUR'], 2)


# compares notification amount with current amount
def compare_ethereum_price(notification_amount, ethereum_price):
    # ethereum price is greater than notification amount
    if ethereum_price > notification_amount:
        print(f"Target ({notification_amount}) has been reached: {ethereum_price}")
        return True
    else:
        print(f"Target ({notification_amount}) has not been reached: {ethereum_price}")
        # not needed but makes the code more readable
        return False


# saves every interval the current Ethereum price
def save_ethereum_price(ethereum_list, ethereum_price, formatted_time):
    # append Ethereum price to list
    ethereum_list.append((ethereum_price, formatted_time))
    return ethereum_list


# receives ethereum price list and iterates over all prices and converts it into a string
def display_ethereum_prices_in_string(ethereum_price_list):
    price_list_string = ""
    # loop through the list and formats it as a string
    for price, time in ethereum_price_list:
        price_list_string += "\n" + str(price) + " EUR" + " | " + str(time) + " uur"
    return price_list_string


# starts the email notification when the target amount has been reached
def notify_user_mail(ethereum_amount_reached, ethereum_prices_string, notification_amount, ethereum_price):
    # sends email if compare_ethereum_price is true
    if ethereum_amount_reached:
        # start the mail sending proces
        email_service.prepare_mail(ethereum_prices_string, notification_amount, ethereum_price)
