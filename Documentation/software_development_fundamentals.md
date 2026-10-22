# Software Development Fundamentals and Data-Flow Diagram

## Frontend, backend and client-server architecture

- **Frontend / client:** Browser or mobile app that collects input and renders screens.
- **Backend / server:** Enforces business rules, validates data, checks identity/permissions, and orchestrates work.
- **REST API:** An HTTP interface exposing resources and actions. `GET` reads, `POST` creates/submits, `PUT/PATCH` updates, and `DELETE` removes resources where permitted. Methods should be used according to endpoint contract.
- **JSON:** Common text format for structured API payloads, usually objects, arrays, strings, numbers, booleans and null.
- **Authentication vs authorization:** Authentication asks who the user is; authorization asks what the user is allowed to do. API keys, OAuth tokens and sessions must be protected; never hard-code secrets into a public repository.
- **Database:** Persists users, orders, trades, instruments and other records. Transactions and constraints support consistency.
- **Data pipeline:** Extracts data from source systems, validates and transforms it, then loads an analytics store or semantic model.
- **Logging and monitoring:** Record structured events, errors, latency and service metrics. Logs must avoid credentials and unnecessary personal data.
- **Error handling:** Return suitable HTTP status codes, safe error messages and correlation/request IDs; retry transient errors carefully and make write operations idempotent when appropriate.
- **SDLC:** Requirements → design → implementation → code review/testing → deployment → monitoring/maintenance. Analytics work fits across requirements, data modelling, QA and post-release measurement.

## Illustrative trading platform data flow

1. A user submits a search, watchlist or order action in a web/mobile frontend.
2. The client sends a HTTPS request to the API gateway.
3. Authentication, authorization and validation run before business services process the request.
4. The backend queries/writes transactional databases and, for a trade order, integrates with broker/exchange/clearing systems under their controls.
5. Events and safe operational logs are captured with IDs and timestamps.
6. A scheduled or streaming ETL/ELT pipeline validates, de-duplicates and models permitted data for analytics.
7. A warehouse/data mart feeds SQL/Python analysis and a Power BI dashboard.
8. Analysts monitor completion, latency, error rates, failed orders, onboarding funnel and support contacts to help product teams prioritize improvements.

The diagram is conceptual, not a depiction of Bluestock or any particular brokerage's internal architecture. Actual order execution involves regulated market infrastructure and additional controls.
