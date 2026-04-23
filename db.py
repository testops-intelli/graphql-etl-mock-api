import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    return psycopg2.connect(
        dbname=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5432")
    )


def fetch_exchanges(limit: int, offset: int):
    sql = """
        SELECT
            exchange AS symbol,
            company_count AS "companiesCount"
        FROM public.exchanges
        ORDER BY exchange
        LIMIT %s OFFSET %s
    """
    conn = None
    cur = None
    try:
        conn = get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql, (limit, offset))
        rows = cur.fetchall()
        return [dict(r) for r in rows]
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def fetch_companies(exchange: str, limit: int, offset: int):
    sql = """
        SELECT
            id,
            "exchangeSymbol",
            "tickerSymbol",
            name,
            active,
            "IsETF" AS "isETF"
        FROM public.companies
        WHERE "exchangeSymbol" = %s
        ORDER BY "tickerSymbol"
        LIMIT %s OFFSET %s
    """
    conn = None
    cur = None
    try:
        conn = get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql, (exchange, limit, offset))
        rows = cur.fetchall()
        return [dict(r) for r in rows]
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def fetch_company_base(company_id: str):
    sql = """
        SELECT
            id,
            "exchangeSymbol",
            "tickerSymbol",
            name,
            active,
            "IsETF" AS "isETF"
        FROM public.companies
        WHERE id = %s
    """
    conn = None
    cur = None
    try:
        conn = get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql, (company_id,))
        row = cur.fetchone()
        return dict(row) if row else None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def fetch_company_financials(ticker: str, exchange: str):
    sql = """
        SELECT
            ticker,
            exchange,
            date,
            "Payout Ratio (%%)",
            "Dividend Yield %%",
            "Ex-Date",
            "Annual Revenue Growth %%",
            "Profit Growth 1 Year Forecast %%",
            "EPS Growth p.a. Forecast %%",
            "ROE 3Y Forecast %%",
            "YoY Earnings growth %%",
            "Short Term Assets",
            "Long Term Liabilities",
            "Short Term Liabilities",
            "D/E Ratio",
            "Net Debt to Ebitda",
            "Operating CF",
            "Shareholder equity",
            "Total Debt",
            "Total Assets",
            "Total Liabilities",
            "Cash and Short term Investments",
            "Average Tenure of Management",
            "Average Tenure of Board",
            "Board Independence",
            "CEO Compensation",
            "ROE %%",
            "Net margin %%",
            "Current Price",
            "Market Cap",
            "PEG Ratio"
        FROM public.company_financials
        WHERE ticker = %s
          AND exchange = %s
        LIMIT 1
    """
    conn = None
    cur = None
    try:
        conn = get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql, (ticker, exchange))
        row = cur.fetchone()
        return dict(row) if row else None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def fetch_owners(ticker: str, exchange: str):
    sql = """
        SELECT
            owner_name AS "ownerName",
            owner_type AS "ownerType",
            "sharesHeld",
            "holdingDate",
            "periodStartDate",
            "periodEndDate",
            "rankSharesHeld",
            "rankSharesSold"
        FROM public.owners
        WHERE ticker = %s
          AND exchange = %s
        ORDER BY "holdingDate" DESC NULLS LAST, "rankSharesHeld" ASC NULLS LAST
    """
    conn = None
    cur = None
    try:
        conn = get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql, (ticker, exchange))
        rows = cur.fetchall()
        return [dict(r) for r in rows]
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def fetch_insider_transactions(ticker: str, exchange: str):
    sql = """
        SELECT
            type,
            owner_name AS "ownerName",
            owner_type AS "ownerType",
            description,
            "tradeDateMin",
            "tradeDateMax",
            shares,
            "priceMin",
            "priceMax",
            "transactionValue",
            "percentageSharesTraded",
            "percentageChangeTransShares",
            "isManagementInsider",
            "filingDate"
        FROM public.insider_transactions
        WHERE ticker = %s
          AND exchange = %s
        ORDER BY "filingDate" DESC NULLS LAST, "tradeDateMax" DESC NULLS LAST
    """
    conn = None
    cur = None
    try:
        conn = get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql, (ticker, exchange))
        rows = cur.fetchall()
        return [dict(r) for r in rows]
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
