import yfinance as yf
import datetime

def get_stock_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    ticker = 'AAPL'
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime(2023, 1, 1)

    # Розділіть запит на частини (на приклад, на рік)
    years = [start_date.year + i for i in range((end_date.year - start_date.year) + 1)]
    for i in range(len(years) - 1):
        partial_start_date = datetime.datetime(years[i], start_date.month, start_date.day)
        partial_end_date = datetime.datetime(years[i + 1], start_date.month, start_date.day)

        stock_data = get_stock_data(ticker, partial_start_date, partial_end_date)

        if stock_data is not None:
            print(stock_data.head())

if __name__ == "__main__":
    main()
