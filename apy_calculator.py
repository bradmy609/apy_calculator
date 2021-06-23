#calc_apy function takes in apr, number of daily compounds, initial investment, days invested, and deposit fee, and calculates the resulting profit, final balance, and apy.
def calc_apy(apr, num_daily_compounds, initial_investment=100, days=365, dfee = 0.00):
    daily_apr = apr/365
    original_investment = initial_investment
    dep_fee = dfee * initial_investment
    initial_investment -= dep_fee
    profit = 0

    if num_daily_compounds >= 1:
        compound_apr = daily_apr/num_daily_compounds
        for i in range(days):
            for number_compounds in range(num_daily_compounds):
                profit += ((initial_investment+profit) * compound_apr)

    elif num_daily_compounds < 1:
        days_per_compound = 1 / num_daily_compounds
        num_compounds = days//days_per_compound
        remaining_duration = days % days_per_compound
        for i in range(int(num_compounds)):
            profit += (initial_investment+profit) * days_per_compound * daily_apr
        if remaining_duration != 0:
            profit += (initial_investment+profit) * remaining_duration * daily_apr

    apy = (profit/original_investment)
    final_value = initial_investment+profit
    pool_apr = apr
    return pool_apr, profit, final_value, apy

#tres_commas function will take in the number of digits in the profit integer and place commas after every 3 digits.
def tres_commas(profit_string, digits):
    if digits <= 3:
        return profit_string
    elif digits <= 6 and digits >= 4:
        result = "${},{}".format(profit_string[-digits:-3], profit_string[-3:])
        return result
    elif digits <= 9 and digits >= 7:
        result = "${},{},{}".format(profit_string[-digits:-6], profit_string[-6:-3], profit_string[-3:])
        return result

#Parameters for calc_apy function (Input apr as whole number)
initial_investment = 100
apr = 3
num_daily_compounds = 0.1
days = 365
deposit_fee = 0.00

pool_apr, profit, final_value, apy = (calc_apy(apr, num_daily_compounds, initial_investment, days, deposit_fee))
profit_as_string = str(int(profit))
digits = len(str(int(profit)))
result = tres_commas(profit_as_string, digits)

print('Deposit Fee: {}%'.format(deposit_fee*100))
print('Pool APR: {}%'.format(int(pool_apr*100)))
print('Pool APY: {}% -- (Calculated after deposit fee)'.format(int(apy*100)))
print('Initial investment USD: ${}.00'.format(int(initial_investment)))
print('Days invested: {}'.format(days))
print('Profit in USD: ${}.00'.format(int(profit)))
print('Profit %: {}%'.format(int(apy*100)))
print('Total value returned: ${}'.format(int(final_value)))
print('')
print('There are {} digits in the profit integer.'.format(digits))

print(result)
