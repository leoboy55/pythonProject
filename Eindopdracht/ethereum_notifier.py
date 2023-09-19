# Goal: Send email notifaction if ethereum hits a target (example = 1600 euro).
# Leonardo Slonek

# Imports
import services
import time
import datetime

# variables
# target amount
notification_amount = 1600.00
# time in seconds when the main function should run again
interval_time = 3600
ethereum_list = []


# checks every 1 hour for the current Ethereum price
def main():
    while True:
        # get the current time
        current_time = datetime.datetime.now()
        # format the current time to year, month, day, hour and min
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M")
        # set connection API
        services.set_api_key()
        # gets the current Ethereum price and prints it with time in the console
        ethereum_price = services.check_ethereum_price(formatted_time)
        # compares the Ethereum price and prints status in the console
        ethereum_amount_reached = services.compare_ethereum_price(notification_amount, ethereum_price)
        # saves the current Ethereum price in a list
        ethereum_price_list = services.save_ethereum_price(ethereum_list, ethereum_price, formatted_time)
        # iterable over price list and saves it as a string
        ethereum_prices_string = services.display_ethereum_prices_in_string(ethereum_price_list)
        # send email to notify if Ethereum has reached notification amount
        services.notify_user_mail(ethereum_amount_reached, ethereum_prices_string, notification_amount, ethereum_price)
        # main runs every interval time
        time.sleep(interval_time)


if __name__ == "__main__":
    main()
