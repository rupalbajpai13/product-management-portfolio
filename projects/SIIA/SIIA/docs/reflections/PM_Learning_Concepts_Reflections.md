# Product Management Learning Concepts — Reflections

| # | PM Concept | What I Did in SIIA |
|---|---|---|
| 1 | **Problem Statement** | Defined the real business pain — AP teams waste time investigating invoice exceptions and depend on technical teams — before jumping to any solution |
| 2 | **Product Vision** | Crafted a crisp, user-centered vision: "Enable finance users to resolve invoice exceptions independently through AI-powered investigation and intelligent recommendations" |
| 3 | **User Personas** | Identified 4 distinct users — AP Specialist, Procurement Specialist, Finance Consultant, SAP Support Consultant — each with different needs and contexts |
| 4 | **User Journey Mapping** | Mapped how users move through the investigation process — from encountering an invoice exception to receiving a resolution |
| 5 | **User Stories & Acceptance Criteria** | Translated user needs into structured stories with clear acceptance criteria — the bridge between discovery and delivery |
| 6 | **MVP Thinking** | Chose the simplified Streamlit linear flow over the full multi-agent architecture for MVP — ship fast, validate, then evolve |
| 7 | **Product Roadmap** | Planned phased delivery — JSON mock data now, SAP OData API later — structured thinking about what gets built and when |
| 8 | **KPIs & Success Metrics** | Defined how to measure whether the product is working — tracking outcomes, not just shipping features |
| 9 | **Architecture as a PM Artifact** | Designed the agent flow and data layer yourself — showing PM ownership of the what and why, not just leaving it to engineers |
| 10 | **Scope Control** | Questioned and removed `validate()` from `InvoiceAgent` when it didn't align with the architecture — disciplined scope management |
| 11 | **Iterative Development** | Started with stub classes → added service layer → wired the agent → kept full architecture as future state — classic iterate and evolve approach |
