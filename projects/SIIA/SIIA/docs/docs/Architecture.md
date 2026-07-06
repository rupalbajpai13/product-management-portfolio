                    Accounts Payable Specialist
                               │
                               ▼
                  SIIIA Investigation Screen
                               │
                               ▼
                Invoice Investigation Agent
                     (Workflow Orchestrator)
                               │
 ┌──────────────┬───────────────┬─────────────────┬─────────────────┐
 ▼              ▼               ▼                 ▼
Invoice     Shipment        Business Rule     Knowledge
Retriever   Retriever       Validation        Retrieval
Agent        Agent            Agent            Agent
 │              │               │                 │
 │              │               │                 │
Invoice DB   PO / ASN      Rule Engine      SAP KBA Repository
                             INV-187          KB1390832
 └──────────────┴───────────────┴─────────────────┘
                               │
                               ▼
                    AI Reasoning Engine (LLM)
                               │
                               ▼
        Root Cause + Evidence + Confidence + Recommendation
                               │
                               ▼
                      Feedback & Telemetry
