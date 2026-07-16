                    Accounts Payable Specialist
                               │
                               ▼
                    Investigation Orchestrator Agent
                               │
        ┌──────────────┬──────────────┬──────────────┐
        ▼              ▼              ▼              ▼
  Invoice Agent   Shipment Agent   Rule Agent   Knowledge Agent
        │              │              │              │
        ▼              ▼              ▼              ▼
 Invoice Data     Shipment Data   Business Rules    SAP KBAs
        │              │              │              │
        └──────────────┴──────────────┴──────────────┘
                               │
                               ▼
                   Evidence Evaluation Agent
                               │
              Is evidence sufficient?
                  │                    │
                YES                    NO
                  │                    │
                  ▼                    ▼
          Explanation Agent      Historical Case Agent
                                      │
                                      ▼
                              Similar Incident Search
                                      │
                                      ▼
                              Explanation Agent
                                      │
                                      ▼
                     Root Cause + Confidence + Recommendation
                                      │
                                      ▼
                            Feedback Collection Agent


                            Simplified version : Streamlit UI

↓

Investigation Agent

↓

Invoice Agent

↓

JSON

↓

Rule Agent

↓

Knowledge Agent

↓

GPT

↓

Response



