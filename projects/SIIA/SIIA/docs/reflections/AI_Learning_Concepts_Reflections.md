# AI Learning Concepts — Reflections

| # | AI Concept | What I Did in SIIA |
|---|---|---|
| 1 | **Multi-Agent Architecture** | Split intelligence across specialized agents — `InvoiceAgent`, `ShipmentAgent`, `RuleAgent`, `KnowledgeAgent`, `OrchestratorAgent` — each with a single responsibility |
| 2 | **Orchestrator Pattern** | Designed `OrchestratorAgent` as the central coordinator that delegates tasks to sub-agents and aggregates results |
| 3 | **Agent Specialization (Single Responsibility)** | Removed `validate()` from `InvoiceAgent` and moved it to `RuleAgent` — each agent does one thing well |
| 4 | **Tool Use / Service Layer** | `InvoiceAgent` does not directly access data — it calls `InvoiceService`, mirroring how LLM agents use tools via function calling |
| 5 | **RAG (Retrieval Augmented Generation)** | `KnowledgeAgent` retrieves SAP KBAs and injects them as context before the LLM generates a response — grounding answers in real knowledge |
| 6 | **Evidence Evaluation** | Designed `EvidenceEvaluationAgent` as a quality gate — only proceeds to explanation if sufficient evidence is available, avoiding low-confidence responses |
| 7 | **Fallback with Historical Cases** | When evidence is insufficient, `HistoricalCaseAgent` searches past incidents — a fallback pattern to prevent hallucination |
| 8 | **Feedback Loop** | Designed `FeedbackCollectionAgent` to collect user corrections and close the learning loop — inspired by RLHF (Reinforcement Learning from Human Feedback) |
| 9 | **Simplified vs Full Architecture** | Built a linear Streamlit MVP flow alongside the full multi-agent architecture — reflecting real AI product thinking: start simple, evolve to complexity |
