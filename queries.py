QUERY_EXCHANGES = """
query Exchanges {
  exchanges {
    symbol
    companiesCount
  }
}
"""

QUERY_COMPANIES = """
query Companies($exchange: String!, $offset: Int!, $limit: Int!) {
  companies(exchange: $exchange, offset: $offset, limit: $limit) {
    id
    exchangeSymbol
    tickerSymbol
    name
    active
    isETF
  }
}
"""

QUERY_COMPANY = """
query Company($id: ID!) {
  company(id: $id) {
    id
    exchangeSymbol
    tickerSymbol
    name
    active
    isETF
    fundamentals {
      date
      dividends {
        payoutRatioPct
        dividendYieldPct
        exDate
      }
      growth {
        annualRevenueGrowthPct
        profitGrowth1YForecastPct
        epsGrowthForecastPct
        roe3YForecastPct
        yoyEarningsGrowthPct
      }
      financialHealth {
        shortTermAssets
        longTermLiabilities
        shortTermLiabilities
        deRatio
        netDebtToEbitda
        operatingCF
        shareholderEquity
        totalDebt
        totalAssets
        totalLiabilities
        cashAndShortTermInvestments
      }
      governance {
        averageTenureManagement
        averageTenureBoard
        boardIndependence
        ceoCompensation
      }
      profitability {
        roePct
        netMarginPct
        currentPrice
        marketCap
        pegRatio
      }
    }
    owners {
      ownerName
      ownerType
      sharesHeld
      holdingDate
      periodStartDate
      periodEndDate
      rankSharesHeld
      rankSharesSold
    }
    insiderTransactions {
      type
      ownerName
      ownerType
      description
      tradeDateMin
      tradeDateMax
      shares
      priceMin
      priceMax
      transactionValue
      percentageSharesTraded
      percentageChangeTransShares
      isManagementInsider
      filingDate
    }
  }
}
"""
