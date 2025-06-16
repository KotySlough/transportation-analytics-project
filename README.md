# Project: Strategic Carrier Performance Analysis

### Objective
This project analyzes quarterly transportation data for a fictional shipper to evaluate carrier performance. The goal is to move beyond simple cost analysis and provide a holistic view of carrier value by incorporating both cost-efficiency and service quality (on-time delivery). The final output is a strategic recommendation for future freight allocation.

### Methodology
The analysis was conducted using Python with the Pandas library and follows these steps:
1.  **Load & Merge:** Two separate data sources (shipment costs and delivery logs) were loaded and merged into a single DataFrame.
2.  **Feature Engineering:** New, more insightful metrics were created from the raw data:
    - `CostPerMile`: To normalize cost across different lane lengths.
    - `OnTimePercentage`: To measure service reliability against promised delivery dates.
3.  **Aggregation:** Data was grouped by carrier to calculate their average cost per mile, overall on-time percentage, and total shipment volume.
4.  **Synthesis:** The aggregated data was analyzed to categorize carriers and provide a strategic recommendation.

### Key Findings & Report
The final performance summary is as follows:

| Carrier           | AverageCostPerMile | OnTimePercentage | TotalShipments |
|-------------------|--------------------|------------------|----------------|
| Alpha Logistics   | 0.71               | 50%              | 2              |
| Omega Transport   | 1.11               | 50%              | 3              |
| Speedy Freight    | 1.23               | 50%              | 4              |


### Strategic Recommendations

Based on the analysis:

-   **Alpha Logistics:** Emerges as the most cost-effective carrier (`$0.71/mile`). Despite a 50% on-time record in this small sample, their significant cost advantage warrants further investigation. **Recommendation:** Consider for less time-sensitive freight where cost is the primary driver.
-   **Omega Transport & Speedy Freight:** Show significantly higher costs per mile. Their on-time performance does not currently justify this cost premium. **Recommendation:** Initiate performance reviews with these carriers to understand the cost drivers. Consider reducing their freight volume in favor of more cost-effective options if performance doesn't improve.

This project demonstrates the power of using data to move from a tactical, cost-based approach to a strategic, value-based carrier management strategy.
