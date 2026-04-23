def map_fundamentals_grouped(row):
    if not row:
        return None

    return {
        "date": row.get("date"),
        "dividends": {
            "payoutRatioPct": row.get("Payout Ratio (%)"),
            "dividendYieldPct": row.get("Dividend Yield %"),
            "exDate": row.get("Ex-Date"),
        },
        "growth": {
            "annualRevenueGrowthPct": row.get("Annual Revenue Growth %"),
            "profitGrowth1YForecastPct": row.get("Profit Growth 1 Year Forecast %"),
            "epsGrowthForecastPct": row.get("EPS Growth p.a. Forecast %"),
            "roe3YForecastPct": row.get("ROE 3Y Forecast %"),
            "yoyEarningsGrowthPct": row.get("YoY Earnings growth %"),
        },
        "financialHealth": {
            "shortTermAssets": row.get("Short Term Assets"),
            "longTermLiabilities": row.get("Long Term Liabilities"),
            "shortTermLiabilities": row.get("Short Term Liabilities"),
            "deRatio": row.get("D/E Ratio"),
            "netDebtToEbitda": row.get("Net Debt to Ebitda"),
            "operatingCF": row.get("Operating CF"),
            "shareholderEquity": row.get("Shareholder equity"),
            "totalDebt": row.get("Total Debt"),
            "totalAssets": row.get("Total Assets"),
            "totalLiabilities": row.get("Total Liabilities"),
            "cashAndShortTermInvestments": row.get("Cash and Short term Investments"),
        },
        "governance": {
            "averageTenureManagement": row.get("Average Tenure of Management"),
            "averageTenureBoard": row.get("Average Tenure of Board"),
            "boardIndependence": row.get("Board Independence"),
            "ceoCompensation": row.get("CEO Compensation"),
        },
        "profitability": {
            "roePct": row.get("ROE %"),
            "netMarginPct": row.get("Net margin %"),
            "currentPrice": row.get("Current Price"),
            "marketCap": row.get("Market Cap"),
            "pegRatio": row.get("PEG Ratio"),
        }
    }
