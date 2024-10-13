# create the initial historical data by querying the right APIs and websockets to retrieve the needed info over time

import finnhub
import sqlite3
import psycopg2
from psycopg2 import sql

# Setup client
finnhub_client = finnhub.Client(api_key="cqtofkpr01qijbg180h0cqtofkpr01qijbg180hg")
# Basic financials
basic_financials = finnhub_client.company_basic_financials('AAPL', 'all')

# tenDayAverageTradingVolume = basic_financials['metric']['10DayAverageTradingVolume']
# thirteenWeekPriceReturnDaily = basic_financials['metric']['13WeekPriceReturnDaily']
# twentySixWeekPriceReturnDaily = basic_financials['metric']['26WeekPriceReturnDaily']
# threeMonthADReturnStd = basic_financials['metric']['3MonthADReturnStd']
# threeMonthAverageTradingVolume = basic_financials['metric']['3MonthAverageTradingVolume']
# fiftyTwoWeekHigh = basic_financials['metric']['52WeekHigh']
# fiftyTwoWeekHighDate = basic_financials['metric']['52WeekHighDate']
# fiftyTwoWeekLow = basic_financials['metric']['52WeekLow']
# fiftyTwoWeekLowDate = basic_financials['metric']['52WeekLowDate']
# fiftyTwoWeekPriceReturnDaily = basic_financials['metric']['52WeekPriceReturnDaily']
# fiveDayPriceReturnDaily = basic_financials['metric']['5DayPriceReturnDaily']
# assetTurnoverAnnual = basic_financials['metric']['assetTurnoverAnnual']
# assetTurnoverTTM = basic_financials['metric']['assetTurnoverTTM']
# beta = basic_financials['metric']['beta']
# bookValuePerShareAnnual = basic_financials['metric']['bookValuePerShareAnnual']
# bookValuePerShareQuarterly = basic_financials['metric']['bookValuePerShareQuarterly']
# bookValueShareGrowth5Y = basic_financials['metric']['bookValueShareGrowth5Y']
# capexCagr5Y = basic_financials['metric']['capexCagr5Y']
# cashFlowPerShareAnnual = basic_financials['metric']['cashFlowPerShareAnnual']
# cashFlowPerShareQuarterly = basic_financials['metric']['cashFlowPerShareQuarterly']
# cashFlowPerShareTTM = basic_financials['metric']['cashFlowPerShareTTM']
# cashPerSharePerShareAnnual = basic_financials['metric']['cashPerSharePerShareAnnual']
# cashPerSharePerShareQuarterly = basic_financials['metric']['cashPerSharePerShareQuarterly']
# currentDividendYieldTTM = basic_financials['metric']['currentDividendYieldTTM']
# currentEv_freeCashFlowAnnual = basic_financials['metric']['currentEv/freeCashFlowAnnual']
# currentEv_freeCashFlowTTM = basic_financials['metric']['currentEv/freeCashFlowTTM']
# currentRatioAnnual = basic_financials['metric']['currentRatioAnnual']
# currentRatioQuarterly = basic_financials['metric']['currentRatioQuarterly']
# dividendGrowthRate5Y = basic_financials['metric']['dividendGrowthRate5Y']
# dividendPerShareAnnual = basic_financials['metric']['dividendPerShareAnnual']
# dividendPerShareTTM = basic_financials['metric']['dividendPerShareTTM']
# dividendYieldIndicatedAnnual = basic_financials['metric']['dividendYieldIndicatedAnnual']
# ebitdPerShareAnnual = basic_financials['metric']['ebitdPerShareAnnual']
# ebitdPerShareTTM = basic_financials['metric']['ebitdPerShareTTM']
# ebitdaCagr5Y = basic_financials['metric']['ebitdaCagr5Y']
# ebitdaInterimCagr5Y = basic_financials['metric']['ebitdaInterimCagr5Y']
# enterpriseValue = basic_financials['metric']['enterpriseValue']
# epsAnnual = basic_financials['metric']['epsAnnual']
# epsBasicExclExtraItemsAnnual = basic_financials['metric']['epsBasicExclExtraItemsAnnual']
# epsBasicExclExtraItemsTTM = basic_financials['metric']['epsBasicExclExtraItemsTTM']
# epsExclExtraItemsAnnual = basic_financials['metric']['epsExclExtraItemsAnnual']
# epsExclExtraItemsTTM = basic_financials['metric']['epsExclExtraItemsTTM']
# epsGrowth3Y = basic_financials['metric']['epsGrowth3Y']
# epsGrowth5Y = basic_financials['metric']['epsGrowth5Y']
# epsGrowthQuarterlyYoy = basic_financials['metric']['epsGrowthQuarterlyYoy']
# epsGrowthTTMYoy = basic_financials['metric']['epsGrowthTTMYoy']
# epsInclExtraItemsAnnual = basic_financials['metric']['epsInclExtraItemsAnnual']
# epsInclExtraItemsTTM = basic_financials['metric']['epsInclExtraItemsTTM']
# epsNormalizedAnnual = basic_financials['metric']['epsNormalizedAnnual']
# epsTTM = basic_financials['metric']['epsTTM']
# focfCagr5Y = basic_financials['metric']['focfCagr5Y']
# grossMargin5Y = basic_financials['metric']['grossMargin5Y']
# grossMarginAnnual = basic_financials['metric']['grossMarginAnnual']
# grossMarginTTM = basic_financials['metric']['grossMarginTTM']
# inventoryTurnoverAnnual = basic_financials['metric']['inventoryTurnoverAnnual']
# inventoryTurnoverTTM = basic_financials['metric']['inventoryTurnoverTTM']
# longTermDebt_equityAnnual = basic_financials['metric']['longTermDebt/equityAnnual']
# longTermDebt_equityQuarterly = basic_financials['metric']['longTermDebt/equityQuarterly']
# marketCapitalization = basic_financials['metric']['marketCapitalization']
# monthToDatePriceReturnDaily = basic_financials['metric']['monthToDatePriceReturnDaily']
# netIncomeEmployeeAnnual = basic_financials['metric']['netIncomeEmployeeAnnual']
# netIncomeEmployeeTTM = basic_financials['metric']['netIncomeEmployeeTTM']
# netInterestCoverageAnnual = basic_financials['metric']['netInterestCoverageAnnual']
# netInterestCoverageTTM = basic_financials['metric']['netInterestCoverageTTM']
# netMarginGrowth5Y = basic_financials['metric']['netMarginGrowth5Y']
# netProfitMargin5Y = basic_financials['metric']['netProfitMargin5Y']
# netProfitMarginAnnual = basic_financials['metric']['netProfitMarginAnnual']
# netProfitMarginTTM = basic_financials['metric']['netProfitMarginTTM']
# operatingMargin5Y = basic_financials['metric']['operatingMargin5Y']
# operatingMarginAnnual = basic_financials['metric']['operatingMarginAnnual']
# operatingMarginTTM = basic_financials['metric']['operatingMarginTTM']
# payoutRatioAnnual = basic_financials['metric']['payoutRatioAnnual']
# payoutRatioTTM = basic_financials['metric']['payoutRatioTTM']
# pbAnnual = basic_financials['metric']['pbAnnual']
# pbQuarterly = basic_financials['metric']['pbQuarterly']
# pcfShareAnnual = basic_financials['metric']['pcfShareAnnual']
# pcfShareTTM = basic_financials['metric']['pcfShareTTM']
# peAnnual = basic_financials['metric']['peAnnual']
# peBasicExclExtraTTM = basic_financials['metric']['peBasicExclExtraTTM']
# peExclExtraAnnual = basic_financials['metric']['peExclExtraAnnual']
# peExclExtraTTM = basic_financials['metric']['peExclExtraTTM']
# peInclExtraTTM = basic_financials['metric']['peInclExtraTTM']
# peNormalizedAnnual = basic_financials['metric']['peNormalizedAnnual']
# peTTM = basic_financials['metric']['peTTM']
# pfcfShareAnnual = basic_financials['metric']['pfcfShareAnnual']
# pfcfShareTTM = basic_financials['metric']['pfcfShareTTM']
# pretaxMargin5Y = basic_financials['metric']['pretaxMargin5Y']
# pretaxMarginAnnual = basic_financials['metric']['pretaxMarginAnnual']
# pretaxMarginTTM = basic_financials['metric']['pretaxMarginTTM']
# priceRelativeTo_SP50013Week = basic_financials['metric']['priceRelativeToS&P50013Week']
# priceRelativeTo_SP50026Week = basic_financials['metric']['priceRelativeToS&P50026Week']
# priceRelativeTo_SP5004Week = basic_financials['metric']['priceRelativeToS&P5004Week']
# priceRelativeTo_SP50052Week = basic_financials['metric']['priceRelativeToS&P50052Week']
# priceRelativeTo_SP500Ytd = basic_financials['metric']['priceRelativeToS&P500Ytd']
# psAnnual = basic_financials['metric']['psAnnual']
# psTTM = basic_financials['metric']['psTTM']
# ptbvAnnual = basic_financials['metric']['ptbvAnnual']
# ptbvQuarterly = basic_financials['metric']['ptbvQuarterly']
# quickRatioAnnual = basic_financials['metric']['quickRatioAnnual']
# quickRatioQuarterly = basic_financials['metric']['quickRatioQuarterly']
# receivablesTurnoverAnnual = basic_financials['metric']['receivablesTurnoverAnnual']
# receivablesTurnoverTTM = basic_financials['metric']['receivablesTurnoverTTM']
# revenueEmployeeAnnual = basic_financials['metric']['revenueEmployeeAnnual']
# revenueEmployeeTTM = basic_financials['metric']['revenueEmployeeTTM']
# revenueGrowth3Y = basic_financials['metric']['revenueGrowth3Y']
# revenueGrowth5Y = basic_financials['metric']['revenueGrowth5Y']
# revenueGrowthQuarterlyYoy = basic_financials['metric']['revenueGrowthQuarterlyYoy']
# revenueGrowthTTMYoy = basic_financials['metric']['revenueGrowthTTMYoy']
# revenuePerShareAnnual = basic_financials['metric']['revenuePerShareAnnual']
# revenuePerShareTTM = basic_financials['metric']['revenuePerShareTTM']
# revenueShareGrowth5Y = basic_financials['metric']['revenueShareGrowth5Y']
# roa5Y = basic_financials['metric']['roa5Y']
# roaRfy = basic_financials['metric']['roaRfy']
# roaTTM = basic_financials['metric']['roaTTM']
# roe5Y = basic_financials['metric']['roe5Y']
# roeRfy = basic_financials['metric']['roeRfy']
# roeTTM = basic_financials['metric']['roeTTM']
# roi5Y = basic_financials['metric']['roi5Y']
# roiAnnual = basic_financials['metric']['roiAnnual']
# roiTTM = basic_financials['metric']['roiTTM']
# tangibleBookValuePerShareAnnual = basic_financials['metric']['tangibleBookValuePerShareAnnual']
# tangibleBookValuePerShareQuarterly = basic_financials['metric']['tangibleBookValuePerShareQuarterly']
# tbvCagr5Y = basic_financials['metric']['tbvCagr5Y']
# totalDebt_totalEquityAnnual = basic_financials['metric']['totalDebt/totalEquityAnnual']
# totalDebt_totalEquityQuarterly = basic_financials['metric']['totalDebt/totalEquityQuarterly']
# yearToDatePriceReturnDaily = basic_financials['metric']['yearToDatePriceReturnDaily']

one_time_metrics = [
    basic_financials['metric']['10DayAverageTradingVolume'],
    basic_financials['metric']['13WeekPriceReturnDaily'],
    basic_financials['metric']['26WeekPriceReturnDaily'],
    basic_financials['metric']['3MonthADReturnStd'],
    basic_financials['metric']['3MonthAverageTradingVolume'],
    basic_financials['metric']['52WeekHigh'],
    basic_financials['metric']['52WeekHighDate'],
    basic_financials['metric']['52WeekLow'],
    basic_financials['metric']['52WeekLowDate'],
    basic_financials['metric']['52WeekPriceReturnDaily'],
    basic_financials['metric']['5DayPriceReturnDaily'],
    basic_financials['metric']['assetTurnoverAnnual'],
    basic_financials['metric']['assetTurnoverTTM'],
    basic_financials['metric']['beta'],
    basic_financials['metric']['bookValuePerShareAnnual'],
    basic_financials['metric']['bookValuePerShareQuarterly'],
    basic_financials['metric']['bookValueShareGrowth5Y'],
    basic_financials['metric']['capexCagr5Y'],
    basic_financials['metric']['cashFlowPerShareAnnual'],
    basic_financials['metric']['cashFlowPerShareQuarterly'],
    basic_financials['metric']['cashFlowPerShareTTM'],
    basic_financials['metric']['cashPerSharePerShareAnnual'],
    basic_financials['metric']['cashPerSharePerShareQuarterly'],
    basic_financials['metric']['currentDividendYieldTTM'],
    basic_financials['metric']['currentEv/freeCashFlowAnnual'],
    basic_financials['metric']['currentEv/freeCashFlowTTM'],
    basic_financials['metric']['currentRatioAnnual'],
    basic_financials['metric']['currentRatioQuarterly'],
    basic_financials['metric']['dividendGrowthRate5Y'],
    basic_financials['metric']['dividendPerShareAnnual'],
    basic_financials['metric']['dividendPerShareTTM'],
    basic_financials['metric']['dividendYieldIndicatedAnnual'],
    basic_financials['metric']['ebitdPerShareAnnual'],
    basic_financials['metric']['ebitdPerShareTTM'],
    basic_financials['metric']['ebitdaCagr5Y'],
    basic_financials['metric']['ebitdaInterimCagr5Y'],
    basic_financials['metric']['enterpriseValue'],
    basic_financials['metric']['epsAnnual'],
    basic_financials['metric']['epsBasicExclExtraItemsAnnual'],
    basic_financials['metric']['epsBasicExclExtraItemsTTM'],
    basic_financials['metric']['epsExclExtraItemsAnnual'],
    basic_financials['metric']['epsExclExtraItemsTTM'],
    basic_financials['metric']['epsGrowth3Y'],
    basic_financials['metric']['epsGrowth5Y'],
    basic_financials['metric']['epsGrowthQuarterlyYoy'],
    basic_financials['metric']['epsGrowthTTMYoy'],
    basic_financials['metric']['epsInclExtraItemsAnnual'],
    basic_financials['metric']['epsInclExtraItemsTTM'],
    basic_financials['metric']['epsNormalizedAnnual'],
    basic_financials['metric']['epsTTM'],
    basic_financials['metric']['focfCagr5Y'],
    basic_financials['metric']['grossMargin5Y'],
    basic_financials['metric']['grossMarginAnnual'],
    basic_financials['metric']['grossMarginTTM'],
    basic_financials['metric']['inventoryTurnoverAnnual'],
    basic_financials['metric']['inventoryTurnoverTTM'],
    basic_financials['metric']['longTermDebt/equityAnnual'],
    basic_financials['metric']['longTermDebt/equityQuarterly'],
    basic_financials['metric']['marketCapitalization'],
    basic_financials['metric']['monthToDatePriceReturnDaily'],
    basic_financials['metric']['netIncomeEmployeeAnnual'],
    basic_financials['metric']['netIncomeEmployeeTTM'],
    basic_financials['metric']['netInterestCoverageAnnual'],
    basic_financials['metric']['netInterestCoverageTTM'],
    basic_financials['metric']['netMarginGrowth5Y'],
    basic_financials['metric']['netProfitMargin5Y'],
    basic_financials['metric']['netProfitMarginAnnual'],
    basic_financials['metric']['netProfitMarginTTM'],
    basic_financials['metric']['operatingMargin5Y'],
    basic_financials['metric']['operatingMarginAnnual'],
    basic_financials['metric']['operatingMarginTTM'],
    basic_financials['metric']['payoutRatioAnnual'],
    basic_financials['metric']['payoutRatioTTM'],
    basic_financials['metric']['pbAnnual'],
    basic_financials['metric']['pbQuarterly'],
    basic_financials['metric']['pcfShareAnnual'],
    basic_financials['metric']['pcfShareTTM'],
    basic_financials['metric']['peAnnual'],
    basic_financials['metric']['peBasicExclExtraTTM'],
    basic_financials['metric']['peExclExtraAnnual'],
    basic_financials['metric']['peExclExtraTTM'],
    basic_financials['metric']['peInclExtraTTM'],
    basic_financials['metric']['peNormalizedAnnual'],
    basic_financials['metric']['peTTM'],
    basic_financials['metric']['pfcfShareAnnual'],
    basic_financials['metric']['pfcfShareTTM'],
    basic_financials['metric']['pretaxMargin5Y'],
    basic_financials['metric']['pretaxMarginAnnual'],
    basic_financials['metric']['pretaxMarginTTM'],
    basic_financials['metric']['priceRelativeToS&P50013Week'],
    basic_financials['metric']['priceRelativeToS&P50026Week'],
    basic_financials['metric']['priceRelativeToS&P5004Week'],
    basic_financials['metric']['priceRelativeToS&P50052Week'],
    basic_financials['metric']['priceRelativeToS&P500Ytd'],
    basic_financials['metric']['psAnnual'],
    basic_financials['metric']['psTTM'],
    basic_financials['metric']['ptbvAnnual'],
    basic_financials['metric']['ptbvQuarterly'],
    basic_financials['metric']['quickRatioAnnual'],
    basic_financials['metric']['quickRatioQuarterly'],
    basic_financials['metric']['receivablesTurnoverAnnual'],
    basic_financials['metric']['receivablesTurnoverTTM'],
    basic_financials['metric']['revenueEmployeeAnnual'],
    basic_financials['metric']['revenueEmployeeTTM'],
    basic_financials['metric']['revenueGrowth3Y'],
    basic_financials['metric']['revenueGrowth5Y'],
    basic_financials['metric']['revenueGrowthQuarterlyYoy'],
    basic_financials['metric']['revenueGrowthTTMYoy'],
    basic_financials['metric']['revenuePerShareAnnual'],
    basic_financials['metric']['revenuePerShareTTM'],
    basic_financials['metric']['revenueShareGrowth5Y'],
    basic_financials['metric']['roa5Y'],
    basic_financials['metric']['roaRfy'],
    basic_financials['metric']['roaTTM'],
    basic_financials['metric']['roe5Y'],
    basic_financials['metric']['roeRfy'],
    basic_financials['metric']['roeTTM'],
    basic_financials['metric']['roi5Y'],
    basic_financials['metric']['roiAnnual'],
    basic_financials['metric']['roiTTM'],
    basic_financials['metric']['tangibleBookValuePerShareAnnual'],
    basic_financials['metric']['tangibleBookValuePerShareQuarterly'],
    basic_financials['metric']['tbvCagr5Y'],
    basic_financials['metric']['totalDebt/totalEquityAnnual'],
    basic_financials['metric']['totalDebt/totalEquityQuarterly'],
    basic_financials['metric']['yearToDatePriceReturnDaily']
]

annual_metrics = ['bookValue', 'cashRatio', 'currentRatio', 'ebitPerShare', 'eps', 'ev', 'fcfMargin', 'grossMargin',
                  'inventoryTurnover', 'longtermDebtTotalAsset',
                  'longtermDebtTotalCapital', 'longtermDebtTotalEquity', 'netDebtToTotalCapital',
                  'netDebtToTotalEquity', 'netMargin', 'operatingMargin', 'payoutRatio',
                  'pb', 'pe', 'pfcf', 'pretaxMargin', 'ps', 'ptbv', 'quickRatio', 'receivablesTurnover', 'roa',
                  'roe', 'roic', 'rotc', 'salesPerShare', 'sgaToSale',
                  'tangibleBookValue', 'totalDebtToEquity', 'totalDebtToTotalAsset', 'totalDebtToTotalCapital',
                  'totalRatio']

quarterly_metrics = ['assetTurnoverTTM', 'bookValue', 'cashRatio', 'currentRatio', 'ebitPerShare', 'eps', 'ev',
                     'fcfMargin', 'fcfPerShareTTM', 'grossMargin',
                     'inventoryTurnoverTTM', 'longtermDebtTotalAsset',
                     'longtermDebtTotalCapital', 'longtermDebtTotalEquity', 'netDebtToTotalCapital',
                     'netDebtToTotalEquity', 'netMargin', 'operatingMargin', 'payoutRatioTTM',
                     'pb', 'peTTM', 'pfcfTTM', 'pretaxMargin', 'psTTM', 'ptbv', 'quickRatio',
                     'receivablesTurnoverTTM', 'roaTTM',
                     'roeTTM', 'roicTTM', 'rotcTTM', 'salesPerShare', 'sgaToSale',
                     'tangibleBookValue', 'totalDebtToEquity', 'totalDebtToTotalAsset', 'totalDebtToTotalCapital',
                     'totalRatio']

# PostgreSQL connection details
conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cursor = conn.cursor()

# Modify the table to include a 'timeframe' column
create_table_query = '''
CREATE TABLE IF NOT EXISTS financial_metrics (
    id SERIAL PRIMARY KEY,
    metric_name VARCHAR(255),
    period DATE,
    value DECIMAL,
    timeframe VARCHAR(10)  -- New column to indicate 'annual' or 'quarterly'
);
'''
cursor.execute(create_table_query)
conn.commit()

# Insert a new metric into the table, now with the 'timeframe' column
def insert_metric(metric_name, period, value, timeframe):
    insert_query = '''
    INSERT INTO financial_metrics (metric_name, period, value, timeframe)
    VALUES (%s, %s, %s, %s);
    '''
    cursor.execute(insert_query, (metric_name, period, value, timeframe))
    conn.commit()

# Function to extract and insert financial data with the timeframe (annual/quarterly)
def process_and_insert_financial_data(basic_financials):
    for timeframe in basic_financials['series']:  # e.g., 'annual', 'quarterly'
        for metric, entries in basic_financials['series'][timeframe].items():
            for entry in entries:
                period = entry['period']
                value = entry['v']
                # Insert metric into the DB along with the timeframe (annual/quarterly)
                insert_metric(metric, period, value, timeframe)

def process_single_data_points(metric_list):
    for metric in metric_list:
        insert_metric(metric.key, None, metric, None)


# Call the function to insert financial data into the DB
process_and_insert_financial_data(basic_financials)

# Close the connection
cursor.close()
conn.close()
