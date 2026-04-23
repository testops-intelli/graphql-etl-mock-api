from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict, Optional

from db import (
    fetch_exchanges,
    fetch_companies,
    fetch_company_base,
    fetch_company_financials,
    fetch_owners,
    fetch_insider_transactions,
)
from mappers import map_fundamentals_grouped

app = FastAPI()

class GraphQLRequest(BaseModel):
    operation: str
    variables: Optional[Dict[str, Any]] = None

@app.get("/")
def root():
    return {"status": "ok", "message": "Mock GraphQL-style API is running"}


@app.post("/graphql")
def graphql_endpoint(request: GraphQLRequest):
    try:
        variables = request.variables or {}

        if request.operation == "exchanges":
            limit = int(variables.get("limit", 100))
            offset = int(variables.get("offset", 0))

            rows = fetch_exchanges(limit=limit, offset=offset)
            return {"data": {"exchanges": rows}}

        if request.operation == "companies":
            exchange = variables["exchange"]
            limit = int(variables.get("limit", 100))
            offset = int(variables.get("offset", 0))

            rows = fetch_companies(exchange=exchange, limit=limit, offset=offset)
            return {"data": {"companies": rows}}

        if request.operation == "company":
            company_id = variables["id"]

            base = fetch_company_base(company_id)
            if not base:
                return {"data": {"company": None}}

            ticker = base["tickerSymbol"]
            exchange = base["exchangeSymbol"]

            financials_row = fetch_company_financials(ticker=ticker, exchange=exchange)
            owners = fetch_owners(ticker=ticker, exchange=exchange)
            insider_transactions = fetch_insider_transactions(ticker=ticker, exchange=exchange)

            company_payload = {
                "id": base["id"],
                "exchangeSymbol": base["exchangeSymbol"],
                "tickerSymbol": base["tickerSymbol"],
                "name": base["name"],
                "active": base["active"],
                "isETF": base["isETF"],
                "fundamentals": map_fundamentals_grouped(financials_row),
                "owners": owners,
                "insiderTransactions": insider_transactions,
            }

            return {"data": {"company": company_payload}}

        return {"error": f"Unsupported operation: {request.operation}"}

    except Exception as e:
        return {
            "status": "error",
            "error_type": type(e).__name__,
            "error": str(e)
        }
