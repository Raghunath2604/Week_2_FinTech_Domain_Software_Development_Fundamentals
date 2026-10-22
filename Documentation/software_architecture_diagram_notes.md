# Software Architecture Diagram Notes

See `software_architecture_data_flow.png`. The diagram follows the sample flow: user/client -> frontend -> API gateway -> backend -> transactional database; selected event/log data and controlled extracts flow into ETL/ELT -> analytics store -> SQL/Python -> Power BI -> product/operations decisions. Dashed feedback indicates that incidents and product metrics inform engineering improvements. Security, permissions, audit logging, reconciliation and privacy are controls across the system.

The architecture is illustrative only; it is not a representation of Bluestock, Zerodha, or another company's private production environment.
