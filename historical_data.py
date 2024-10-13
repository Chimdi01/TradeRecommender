# Based on the parameters passed in, amend or create the historical data
#   - method that takes the parameters passed in and accesses the APIs that return the required data
# Based on the parameters passed in, return the historical data
#   - method that takes the parameters passed in and accesses the DB to return the required data

import finnhub
import pandas as pd

if __name__ == "__main__":
    # Setup client
    finnhub_client = finnhub.Client(api_key="cqtofkpr01qijbg180h0cqtofkpr01qijbg180hg")
    # Basic financials
    basic_financials = finnhub_client.company_basic_financials('AAPL', 'all')

    tenDayAverageTradingVolume = basic_financials['metric']['10DayAverageTradingVolume']
    thirteenWeekPriceReturnDaily = basic_financials['metric']['13WeekPriceReturnDaily']
    twentySixWeekPriceReturnDaily = basic_financials['metric']['26WeekPriceReturnDaily']
    threeMonthADReturnStd = basic_financials['metric']['3MonthADReturnStd']
    threeMonthAverageTradingVolume = basic_financials['metric']['3MonthAverageTradingVolume']
    fiftyTwoWeekHigh = basic_financials['metric']['52WeekHigh']
    fiftyTwoWeekHighDate = basic_financials['metric']['52WeekHighDate']
    fiftyTwoWeekLow = basic_financials['metric']['52WeekLow']
    fiftyTwoWeekLowDate = basic_financials['metric']['52WeekLowDate']
    fiftyTwoWeekPriceReturnDaily = basic_financials['metric']['52WeekPriceReturnDaily']
    fiveDayPriceReturnDaily = basic_financials['metric']['5DayPriceReturnDaily']
    assetTurnoverAnnual = basic_financials['metric']['assetTurnoverAnnual']
    assetTurnoverTTM = basic_financials['metric']['assetTurnoverTTM']
    beta = basic_financials['metric']['beta']
    bookValuePerShareAnnual = basic_financials['metric']['bookValuePerShareAnnual']
    bookValuePerShareQuarterly = basic_financials['metric']['bookValuePerShareQuarterly']
    bookValueShareGrowth5Y = basic_financials['metric']['bookValueShareGrowth5Y']
    capexCagr5Y = basic_financials['metric']['capexCagr5Y']
    cashFlowPerShareAnnual = basic_financials['metric']['cashFlowPerShareAnnual']
    cashFlowPerShareQuarterly = basic_financials['metric']['cashFlowPerShareQuarterly']
    cashFlowPerShareTTM = basic_financials['metric']['cashFlowPerShareTTM']
    cashPerSharePerShareAnnual = basic_financials['metric']['cashPerSharePerShareAnnual']
    cashPerSharePerShareQuarterly = basic_financials['metric']['cashPerSharePerShareQuarterly']
    currentDividendYieldTTM = basic_financials['metric']['currentDividendYieldTTM']
    currentEv_freeCashFlowAnnual = basic_financials['metric']['currentEv/freeCashFlowAnnual']
    currentEv_freeCashFlowTTM = basic_financials['metric']['currentEv/freeCashFlowTTM']
    currentRatioAnnual = basic_financials['metric']['currentRatioAnnual']
    currentRatioQuarterly = basic_financials['metric']['currentRatioQuarterly']
    dividendGrowthRate5Y = basic_financials['metric']['dividendGrowthRate5Y']
    dividendPerShareAnnual = basic_financials['metric']['dividendPerShareAnnual']
    dividendPerShareTTM = basic_financials['metric']['dividendPerShareTTM']
    dividendYieldIndicatedAnnual = basic_financials['metric']['dividendYieldIndicatedAnnual']
    ebitdPerShareAnnual = basic_financials['metric']['ebitdPerShareAnnual']
    ebitdPerShareTTM = basic_financials['metric']['ebitdPerShareTTM']
    ebitdaCagr5Y = basic_financials['metric']['ebitdaCagr5Y']
    ebitdaInterimCagr5Y = basic_financials['metric']['ebitdaInterimCagr5Y']
    enterpriseValue = basic_financials['metric']['enterpriseValue']
    epsAnnual = basic_financials['metric']['epsAnnual']
    epsBasicExclExtraItemsAnnual = basic_financials['metric']['epsBasicExclExtraItemsAnnual']
    epsBasicExclExtraItemsTTM = basic_financials['metric']['epsBasicExclExtraItemsTTM']
    epsExclExtraItemsAnnual = basic_financials['metric']['epsExclExtraItemsAnnual']
    epsExclExtraItemsTTM = basic_financials['metric']['epsExclExtraItemsTTM']
    epsGrowth3Y = basic_financials['metric']['epsGrowth3Y']
    epsGrowth5Y = basic_financials['metric']['epsGrowth5Y']
    epsGrowthQuarterlyYoy = basic_financials['metric']['epsGrowthQuarterlyYoy']
    epsGrowthTTMYoy = basic_financials['metric']['epsGrowthTTMYoy']
    epsInclExtraItemsAnnual = basic_financials['metric']['epsInclExtraItemsAnnual']
    epsInclExtraItemsTTM = basic_financials['metric']['epsInclExtraItemsTTM']
    epsNormalizedAnnual = basic_financials['metric']['epsNormalizedAnnual']
    epsTTM = basic_financials['metric']['epsTTM']
    focfCagr5Y = basic_financials['metric']['focfCagr5Y']
    grossMargin5Y = basic_financials['metric']['grossMargin5Y']
    grossMarginAnnual = basic_financials['metric']['grossMarginAnnual']
    grossMarginTTM = basic_financials['metric']['grossMarginTTM']
    inventoryTurnoverAnnual = basic_financials['metric']['inventoryTurnoverAnnual']
    inventoryTurnoverTTM = basic_financials['metric']['inventoryTurnoverTTM']
    longTermDebt_equityAnnual = basic_financials['metric']['longTermDebt/equityAnnual']
    longTermDebt_equityQuarterly = basic_financials['metric']['longTermDebt/equityQuarterly']
    marketCapitalization = basic_financials['metric']['marketCapitalization']
    monthToDatePriceReturnDaily = basic_financials['metric']['monthToDatePriceReturnDaily']
    netIncomeEmployeeAnnual = basic_financials['metric']['netIncomeEmployeeAnnual']
    netIncomeEmployeeTTM = basic_financials['metric']['netIncomeEmployeeTTM']
    netInterestCoverageAnnual = basic_financials['metric']['netInterestCoverageAnnual']
    netInterestCoverageTTM = basic_financials['metric']['netInterestCoverageTTM']
    netMarginGrowth5Y = basic_financials['metric']['netMarginGrowth5Y']
    netProfitMargin5Y = basic_financials['metric']['netProfitMargin5Y']
    netProfitMarginAnnual = basic_financials['metric']['netProfitMarginAnnual']
    netProfitMarginTTM = basic_financials['metric']['netProfitMarginTTM']
    operatingMargin5Y = basic_financials['metric']['operatingMargin5Y']
    operatingMarginAnnual = basic_financials['metric']['operatingMarginAnnual']
    operatingMarginTTM = basic_financials['metric']['operatingMarginTTM']
    payoutRatioAnnual = basic_financials['metric']['payoutRatioAnnual']
    payoutRatioTTM = basic_financials['metric']['payoutRatioTTM']
    pbAnnual = basic_financials['metric']['pbAnnual']
    pbQuarterly = basic_financials['metric']['pbQuarterly']
    pcfShareAnnual = basic_financials['metric']['pcfShareAnnual']
    pcfShareTTM = basic_financials['metric']['pcfShareTTM']
    peAnnual = basic_financials['metric']['peAnnual']
    peBasicExclExtraTTM = basic_financials['metric']['peBasicExclExtraTTM']
    peExclExtraAnnual = basic_financials['metric']['peExclExtraAnnual']
    peExclExtraTTM = basic_financials['metric']['peExclExtraTTM']
    peInclExtraTTM = basic_financials['metric']['peInclExtraTTM']
    peNormalizedAnnual = basic_financials['metric']['peNormalizedAnnual']
    peTTM = basic_financials['metric']['peTTM']
    pfcfShareAnnual = basic_financials['metric']['pfcfShareAnnual']
    pfcfShareTTM = basic_financials['metric']['pfcfShareTTM']
    pretaxMargin5Y = basic_financials['metric']['pretaxMargin5Y']
    pretaxMarginAnnual = basic_financials['metric']['pretaxMarginAnnual']
    pretaxMarginTTM = basic_financials['metric']['pretaxMarginTTM']
    priceRelativeTo_SP50013Week = basic_financials['metric']['priceRelativeToS&P50013Week']
    priceRelativeTo_SP50026Week = basic_financials['metric']['priceRelativeToS&P50026Week']
    priceRelativeTo_SP5004Week = basic_financials['metric']['priceRelativeToS&P5004Week']
    priceRelativeTo_SP50052Week = basic_financials['metric']['priceRelativeToS&P50052Week']
    priceRelativeTo_SP500Ytd = basic_financials['metric']['priceRelativeToS&P500Ytd']
    psAnnual = basic_financials['metric']['psAnnual']
    psTTM = basic_financials['metric']['psTTM']
    ptbvAnnual = basic_financials['metric']['ptbvAnnual']
    ptbvQuarterly = basic_financials['metric']['ptbvQuarterly']
    quickRatioAnnual = basic_financials['metric']['quickRatioAnnual']
    quickRatioQuarterly = basic_financials['metric']['quickRatioQuarterly']
    receivablesTurnoverAnnual = basic_financials['metric']['receivablesTurnoverAnnual']
    receivablesTurnoverTTM = basic_financials['metric']['receivablesTurnoverTTM']
    revenueEmployeeAnnual = basic_financials['metric']['revenueEmployeeAnnual']
    revenueEmployeeTTM = basic_financials['metric']['revenueEmployeeTTM']
    revenueGrowth3Y = basic_financials['metric']['revenueGrowth3Y']
    revenueGrowth5Y = basic_financials['metric']['revenueGrowth5Y']
    revenueGrowthQuarterlyYoy = basic_financials['metric']['revenueGrowthQuarterlyYoy']
    revenueGrowthTTMYoy = basic_financials['metric']['revenueGrowthTTMYoy']
    revenuePerShareAnnual = basic_financials['metric']['revenuePerShareAnnual']
    revenuePerShareTTM = basic_financials['metric']['revenuePerShareTTM']
    revenueShareGrowth5Y = basic_financials['metric']['revenueShareGrowth5Y']
    roa5Y = basic_financials['metric']['roa5Y']
    roaRfy = basic_financials['metric']['roaRfy']
    roaTTM = basic_financials['metric']['roaTTM']
    roe5Y = basic_financials['metric']['roe5Y']
    roeRfy = basic_financials['metric']['roeRfy']
    roeTTM = basic_financials['metric']['roeTTM']
    roi5Y = basic_financials['metric']['roi5Y']
    roiAnnual = basic_financials['metric']['roiAnnual']
    roiTTM = basic_financials['metric']['roiTTM']
    tangibleBookValuePerShareAnnual = basic_financials['metric']['tangibleBookValuePerShareAnnual']
    tangibleBookValuePerShareQuarterly = basic_financials['metric']['tangibleBookValuePerShareQuarterly']
    tbvCagr5Y = basic_financials['metric']['tbvCagr5Y']
    totalDebt_totalEquityAnnual = basic_financials['metric']['totalDebt/totalEquityAnnual']
    totalDebt_totalEquityQuarterly = basic_financials['metric']['totalDebt/totalEquityQuarterly']
    yearToDatePriceReturnDaily = basic_financials['metric']['yearToDatePriceReturnDaily']

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


    # Function to extract values for any metric
    def extract_financial_data(data, metric, frequency='annual'):
        try:
            return [(entry['period'], entry['v']) for entry in data['series'][frequency][metric]]
        except KeyError:
            return f"Metric '{metric}' not found in {frequency} data."


    # print(basic_financials)

    book_value_data = extract_financial_data(basic_financials, 'bookValue')
    print(book_value_data)



bookValue_annual = (basic_financials['series']['annual']['bookValue'][0]['v'],
                    basic_financials['series']['annual']['bookValue'][0]['period'])
cashRatio_annual = (basic_financials['series']['annual']['cashRatio'][0]['v'],
                    basic_financials['series']['annual']['cashRatio'][0]['period'])
currentRatio_annual = (basic_financials['series']['annual']['currentRatio'][0]['v'],
                       basic_financials['series']['annual']['currentRatio'][0]['period'])
ebitPerShare_annual = (basic_financials['series']['annual']['ebitPerShare'][0]['v'],
                       basic_financials['series']['annual']['ebitPerShare'][0]['period'])
eps_annual = (basic_financials['series']['annual']['eps'][0]['v'],
              basic_financials['series']['annual']['eps'][0]['period'])
ev_annual = (basic_financials['series']['annual']['ev'][0]['v'],
             basic_financials['series']['annual']['ev'][0]['period'])
fcfMargin_annual = (basic_financials['series']['annual']['fcfMargin'][0]['v'],
                    basic_financials['series']['annual']['fcfMargin'][0]['period'])
grossMargin_annual = (basic_financials['series']['annual']['grossMargin'][0]['v'],
                      basic_financials['series']['annual']['grossMargin'][0]['period'])
inventoryTurnover_annual = (basic_financials['series']['annual']['inventoryTurnover'][0]['v'],
                            basic_financials['series']['annual']['inventoryTurnover'][0]['period'])
longtermDebtTotalAsset_annual = (basic_financials['series']['annual']['longtermDebtTotalAsset'][0]['v'],
                                 basic_financials['series']['annual']['longtermDebtTotalAsset'][0]['period'])
longtermDebtTotalCapital_annual = (basic_financials['series']['annual']['longtermDebtTotalCapital'][0]['v'],
                                   basic_financials['series']['annual']['longtermDebtTotalCapital'][0]['period'])
longtermDebtTotalEquity_annual = (basic_financials['series']['annual']['longtermDebtTotalEquity'][0]['v'],
                                  basic_financials['series']['annual']['longtermDebtTotalEquity'][0]['period'])
netDebtToTotalCapital_annual = (basic_financials['series']['annual']['netDebtToTotalCapital'][0]['v'],
                                basic_financials['series']['annual']['netDebtToTotalCapital'][0]['period'])
netDebtToTotalEquity_annual = (basic_financials['series']['annual']['netDebtToTotalEquity'][0]['v'],
                               basic_financials['series']['annual']['netDebtToTotalEquity'][0]['period'])
netMargin_annual = (basic_financials['series']['annual']['netMargin'][0]['v'],
                    basic_financials['series']['annual']['netMargin'][0]['period'])
operatingMargin_annual = (basic_financials['series']['annual']['operatingMargin'][0]['v'],
                          basic_financials['series']['annual']['operatingMargin'][0]['period'])
payoutRatio_annual = (basic_financials['series']['annual']['payoutRatio'][0]['v'],
                      basic_financials['series']['annual']['payoutRatio'][0]['period'])
pb_annual = (basic_financials['series']['annual']['pb'][0]['v'],
             basic_financials['series']['annual']['pb'][0]['period'])
pe_annual = (basic_financials['series']['annual']['pe'][0]['v'],
             basic_financials['series']['annual']['pe'][0]['period'])
pfcf_annual = (basic_financials['series']['annual']['pfcf'][0]['v'],
               basic_financials['series']['annual']['pfcf'][0]['period'])
ps_annual = (basic_financials['series']['annual']['ps'][0]['v'],
             basic_financials['series']['annual']['ps'][0]['period'])
ptbv_annual = (basic_financials['series']['annual']['ptbv'][0]['v'],
               basic_financials['series']['annual']['ptbv'][0]['period'])
quickRatio_annual = (basic_financials['series']['annual']['quickRatio'][0]['v'],
                     basic_financials['series']['annual']['quickRatio'][0]['period'])
receivablesTurnover_annual = (basic_financials['series']['annual']['receivablesTurnover'][0]['v'],
                              basic_financials['series']['annual']['receivablesTurnover'][0]['period'])
roa_annual = (basic_financials['series']['annual']['roa'][0]['v'],
              basic_financials['series']['annual']['roa'][0]['period'])
roe_annual = (basic_financials['series']['annual']['roe'][0]['v'],
              basic_financials['series']['annual']['roe'][0]['period'])
roic_annual = (basic_financials['series']['annual']['roic'][0]['v'],
               basic_financials['series']['annual']['roic'][0]['period'])
rotc_annual = (basic_financials['series']['annual']['rotc'][0]['v'],
               basic_financials['series']['annual']['rotc'][0]['period'])
salesPerShare_annual = (basic_financials['series']['annual']['salesPerShare'][0]['v'],
                        basic_financials['series']['annual']['salesPerShare'][0]['period'])
sgaToSale_annual = (basic_financials['series']['annual']['sgaToSale'][0]['v'],
                    basic_financials['series']['annual']['sgaToSale'][0]['period'])
tangibleBookValue_annual = (basic_financials['series']['annual']['tangibleBookValue'][0]['v'],
                            basic_financials['series']['annual']['tangibleBookValue'][0]['period'])
totalDebtToEquity_annual = (basic_financials['series']['annual']['totalDebtToEquity'][0]['v'],
                            basic_financials['series']['annual']['totalDebtToEquity'][0]['period'])
totalDebtToTotalAsset_annual = (basic_financials['series']['annual']['totalDebtToTotalAsset'][0]['v'],
                                basic_financials['series']['annual']['totalDebtToTotalAsset'][0]['period'])
totalDebtToTotalCapital_annual = (basic_financials['series']['annual']['totalDebtToTotalCapital'][0]['v'],
                                  basic_financials['series']['annual']['totalDebtToTotalCapital'][0]['period'])
totalRatio_annual = (basic_financials['series']['annual']['totalRatio'][0]['v'],
                     basic_financials['series']['annual']['totalRatio'][0]['period'])

##########################################      QUARTERLY   #######################################

bookValue_quarterly = (basic_financials['series']['quarterly']['bookValue'][0]['v'],
                       basic_financials['series']['quarterly']['bookValue'][0]['period'])
cashRatio_quarterly = (basic_financials['series']['quarterly']['cashRatio'][0]['v'],
                       basic_financials['series']['quarterly']['cashRatio'][0]['period'])
currentRatio_quarterly = (basic_financials['series']['quarterly']['currentRatio'][0]['v'],
                          basic_financials['series']['quarterly']['currentRatio'][0]['period'])
ebitPerShare_quarterly = (basic_financials['series']['quarterly']['ebitPerShare'][0]['v'],
                          basic_financials['series']['quarterly']['ebitPerShare'][0]['period'])
eps_quarterly = (basic_financials['series']['quarterly']['eps'][0]['v'],
                 basic_financials['series']['quarterly']['eps'][0]['period'])
ev_quarterly = (basic_financials['series']['quarterly']['ev'][0]['v'],
                basic_financials['series']['quarterly']['ev'][0]['period'])
fcfMargin_quarterly = (basic_financials['series']['quarterly']['fcfMargin'][0]['v'],
                       basic_financials['series']['quarterly']['fcfMargin'][0]['period'])
fcfPerShareTTM_quarterly = (basic_financials['series']['quarterly']['fcfPerShareTTM'][0]['v'],
                            basic_financials['series']['quarterly']['fcfPerShareTTM'][0]['period'])
grossMargin_quarterly = (basic_financials['series']['quarterly']['grossMargin'][0]['v'],
                         basic_financials['series']['quarterly']['grossMargin'][0]['period'])
inventoryTurnoverTTM_quarterly = (basic_financials['series']['quarterly']['inventoryTurnoverTTM'][0]['v'],
                                  basic_financials['series']['quarterly']['inventoryTurnoverTTM'][0]['period'])
longtermDebtTotalAsset_quarterly = (basic_financials['series']['quarterly']['longtermDebtTotalAsset'][0]['v'],
                                    basic_financials['series']['quarterly']['longtermDebtTotalAsset'][0]['period'])
longtermDebtTotalCapital_quarterly = (basic_financials['series']['quarterly']['longtermDebtTotalCapital'][0]['v'],
                                      basic_financials['series']['quarterly']['longtermDebtTotalCapital'][0][
                                          'period'])
longtermDebtTotalEquity_quarterly = (basic_financials['series']['quarterly']['longtermDebtTotalEquity'][0]['v'],
                                     basic_financials['series']['quarterly']['longtermDebtTotalEquity'][0][
                                         'period'])
netDebtToTotalCapital_quarterly = (basic_financials['series']['quarterly']['netDebtToTotalCapital'][0]['v'],
                                   basic_financials['series']['quarterly']['netDebtToTotalCapital'][0]['period'])
netDebtToTotalEquity_quarterly = (basic_financials['series']['quarterly']['netDebtToTotalEquity'][0]['v'],
                                  basic_financials['series']['quarterly']['netDebtToTotalEquity'][0]['period'])
netMargin_quarterly = (basic_financials['series']['quarterly']['netMargin'][0]['v'],
                       basic_financials['series']['quarterly']['netMargin'][0]['period'])
operatingMargin_quarterly = (basic_financials['series']['quarterly']['operatingMargin'][0]['v'],
                             basic_financials['series']['quarterly']['operatingMargin'][0]['period'])
payoutRatioTTM_quarterly = (basic_financials['series']['quarterly']['payoutRatioTTM'][0]['v'],
                            basic_financials['series']['quarterly']['payoutRatioTTM'][0]['period'])
pb_quarterly = (basic_financials['series']['quarterly']['pb'][0]['v'],
                basic_financials['series']['quarterly']['pb'][0]['period'])
peTTM_quarterly = (basic_financials['series']['quarterly']['pe'][0]['v'],
                   basic_financials['series']['quarterly']['peTTM'][0]['period'])
pfcfTTM_quarterly = (basic_financials['series']['quarterly']['pfcfTTM'][0]['v'],
                     basic_financials['series']['quarterly']['pfcfTTM'][0]['period'])
psTTM_quarterly = (basic_financials['series']['quarterly']['psTTM'][0]['v'],
                   basic_financials['series']['quarterly']['psTTM'][0]['period'])
ptbv_quarterly = (basic_financials['series']['quarterly']['ptbv'][0]['v'],
                  basic_financials['series']['quarterly']['ptbv'][0]['period'])
quickRatio_quarterly = (basic_financials['series']['quarterly']['quickRatio'][0]['v'],
                        basic_financials['series']['quarterly']['quickRatio'][0]['period'])
receivablesTurnoverTTM_quarterly = (basic_financials['series']['quarterly']['receivablesTurnoverTTM'][0]['v'],
                                    basic_financials['series']['quarterly']['receivablesTurnoverTTM'][0]['period'])
roaTTM_quarterly = (basic_financials['series']['quarterly']['roaTTM'][0]['v'],
                    basic_financials['series']['quarterly']['roaTTM'][0]['period'])
roeTTM_quarterly = (basic_financials['series']['quarterly']['roeTTM'][0]['v'],
                    basic_financials['series']['quarterly']['roeTTM'][0]['period'])
roicTTM_quarterly = (basic_financials['series']['quarterly']['roicTTM'][0]['v'],
                     basic_financials['series']['quarterly']['roicTTM'][0]['period'])
rotcTTM_quarterly = (basic_financials['series']['quarterly']['rotcTTM'][0]['v'],
                     basic_financials['series']['quarterly']['rotcTTM'][0]['period'])
salesPerShare_quarterly = (basic_financials['series']['quarterly']['salesPerShare'][0]['v'],
                           basic_financials['series']['quarterly']['salesPerShare'][0]['period'])
sgaToSale_quarterly = (basic_financials['series']['quarterly']['sgaToSale'][0]['v'],
                       basic_financials['series']['quarterly']['sgaToSale'][0]['period'])
tangibleBookValue_quarterly = (basic_financials['series']['quarterly']['tangibleBookValue'][0]['v'],
                               basic_financials['series']['quarterly']['tangibleBookValue'][0]['period'])
totalDebtToEquity_quarterly = (basic_financials['series']['quarterly']['totalDebtToEquity'][0]['v'],
                               basic_financials['series']['quarterly']['totalDebtToEquity'][0]['period'])
totalDebtToTotalAsset_quarterly = (basic_financials['series']['quarterly']['totalDebtToTotalAsset'][0]['v'],
                                   basic_financials['series']['quarterly']['totalDebtToTotalAsset'][0]['period'])
totalDebtToTotalCapital_quarterly = (basic_financials['series']['quarterly']['totalDebtToTotalCapital'][0]['v'],
                                     basic_financials['series']['quarterly']['totalDebtToTotalCapital'][0][
                                         'period'])
totalRatio_quarterly = (basic_financials['series']['quarterly']['totalRatio'][0]['v'],
                        basic_financials['series']['quarterly']['totalRatio'][0]['period'])