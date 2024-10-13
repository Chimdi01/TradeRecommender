# Based on DB data and current events, what is the predicted performance of x ETF/Stock/Bond/Commodities?
#
# Method that takes the requested asset, returns the prediction
#   Returns in numbers
#   Returns graphically

import requests
import finnhub

if __name__ == "__main__":
    # EODHD_API_KEY = "66ba439b448894.67845987"
    # # url = f'https://eodhd.com/api/bulk-fundamentals/NASDAQ?api_token={EODHD_API_KEY}&fmt=json'
    # url = "https://eodhd.com/api/eod/AAPL.US?api_token=66ba439b448894.67845987&fmt=json"
    # print("url is:")
    # print(url)
    # print("body is:")
    #
    # data = requests.get(url).json()
    # print(data)
    #
    # date = data[0]['date']
    # open_price = data[0]['open']
    # high_price = data[0]['high']
    # low_price = data[0]['low']
    # close_price = data[0]['close']
    # adjusted_close = data[0]['adjusted_close']
    # volume = data[0]['volume']
    #
    # print("date: " + date)
    # print("")
    # rtd_url = "https://eodhd.com/api/real-time/AAPL.US?api_token=66ba439b448894.67845987&fmt=json"
    # rtd = requests.get(rtd_url).json()
    # print("real_time: ")
    # print(rtd)

    # Setup client
    finnhub_client = finnhub.Client(api_key="cqtofkpr01qijbg180h0cqtofkpr01qijbg180hg")
    # Basic financials
    print(finnhub_client.company_basic_financials('AAPL', 'all'))

    # weather_api_access.return_requested_values("historical_details_aggregate")