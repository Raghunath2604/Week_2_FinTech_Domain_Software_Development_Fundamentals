# FinTech Research Report: Zerodha and Data Analytics

**Question:** How can an Indian brokerage platform use data analytics to improve customer experience and business decisions?  
**Case selected:** Zerodha (Indian brokerage platform).  
**Scope:** Public-source desk research. This is not an assertion about undisclosed internal KPIs or a recommendation to use any financial product.

## 1. Business context

A digital broker connects customers to market infrastructure through account, order, funds, holdings, reporting and support workflows. Customer trust depends on correctness, reliability, security, clarity of charges and timely status updates. Analytics can help teams identify where a journey is failing, where systems degrade under load, and which customer-facing steps need to be simplified.

## 2. What public sources show

Zerodha maintains a technology blog that documents engineering practices. Its public posts describe (a) a logging pipeline migration involving ClickHouse and Vector, (b) infrastructure monitoring using Prometheus, Grafana and VictoriaMetrics, including system and business metrics, and (c) experience operating large PostgreSQL databases. Sources: [Zerodha Tech](https://zerodha.tech/), [Infrastructure monitoring with Prometheus at Zerodha](https://zerodha.tech/blog/infrastructure-monitoring-with-prometheus-at-zerodha/), [Logging at Zerodha](https://zerodha.tech/blog/logging-at-zerodha/), and [Working with PostgreSQL](https://zerodha.tech/blog/working-with-postgresql/).

These are public engineering disclosures. The recommendations below are analyst use cases inferred from the capability of those tools, not claims that Zerodha publishes or uses every specific KPI listed here.

## 3. Where analytics can support customer experience

| User journey | Useful metrics | Potential decision supported |
|---|---|---|
| Account opening / KYC | funnel conversion, median time to complete, rejection reasons, retry rate | Identify confusing steps, broken integrations or document issues |
| Login and app availability | availability, latency percentiles (p50/p95/p99), error rate, crash-free sessions | Detect incidents and prioritize reliability improvements |
| Order placement | order submission success, validation rejections by reason, time to acknowledgement, duplicate-request rate | Separate user-input problems from service or exchange connectivity issues |
| Watchlist / portfolio | refresh latency, stale-data incidents, page-load time | Improve speed and communicate market-data freshness |
| Support | contact rate per 1,000 active users, repeat contacts, first-response time, resolution time | Improve help content and identify product friction |
| Platform operations | logs by error class, traces by request ID, infrastructure saturation, alert noise | Find root causes faster and reduce recurrence |

## 4. Proposed analyst workflow

1. Define a business question (for example: “Did login errors rise after the latest release?”).
2. Agree on metric definitions and event schemas with product/engineering teams.
3. Extract de-identified operational events and business aggregates into a controlled analytics store.
4. Validate event completeness, timestamp zones, duplicate events and known release windows.
5. Compare metrics before/after a release and segment by app version, operating system, network type and region where lawful and appropriate.
6. Investigate root causes with logs/traces, not correlation alone.
7. Recommend a change, define a guardrail metric, monitor rollout and record the result.

## 5. Example measurement framework

- **Reliability:** successful requests / all valid requests; p95 API latency; uptime; incident minutes.
- **Customer journey:** KYC funnel conversion; median onboarding time; percentage of sessions with an error.
- **Order lifecycle:** orders accepted by backend / valid orders submitted; rejection reason mix; reconciliation exceptions. Always distinguish app acknowledgement from exchange execution and final settlement.
- **Support:** issue rate per active customer; repeat contacts; median resolution duration.
- **Data quality:** event delivery lag; missing event percentage; duplicate business event rate; reconciliation difference between operational and analytical counts.

Metrics must have clear denominators and exclusions. A low error rate can still hide severe errors affecting a small but important customer cohort. Market orders and money movement need robust auditability, access control and reconciliations; analytics must never bypass trading or regulatory controls.

## 6. Conclusion

Data analytics is useful in a brokerage because it connects technical health to business outcomes. Monitoring can identify system degradation, structured logs can make failures searchable, database design supports reliable transactional workloads, and business dashboards can reveal friction in onboarding and order journeys. The strongest analysis combines quantitative trends with incident context, customer feedback and controlled experiments while protecting sensitive data.

## Sources

- Zerodha Tech: https://zerodha.tech/
- Zerodha infrastructure monitoring: https://zerodha.tech/blog/infrastructure-monitoring-with-prometheus-at-zerodha/
- Zerodha logging: https://zerodha.tech/blog/logging-at-zerodha/
- Zerodha PostgreSQL: https://zerodha.tech/blog/working-with-postgresql/
- CDSL overview and depository role: https://www.cdslindia.com/About/overview.html
- CDSL investor charter: https://www.cdslindia.com/Investors/InvestorCharter.html
- Zerodha Varsity settlement chapter: https://zerodha.com/varsity/chapter/clearing-and-settlement-process-2/

**Research limitation:** The report uses public source material and general analytics reasoning. It does not claim access to Zerodha's private internal dashboards, event data or customer metrics.
