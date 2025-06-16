import pandas as pd

# 1. LOAD & MERGE
shipments_df = pd.read_csv('shipments_data.csv')
deliveries_df = pd.read_csv('delivery_logs.csv')
df = pd.merge(shipments_df, deliveries_df, on='ShipmentID')

# 2. FEATURE ENGINEERING
df['CostPerMile'] = df['ShipmentCost'] / df['DistanceMiles']
df['PromisedDeliveryDate'] = pd.to_datetime(df['PromisedDeliveryDate'])
df['ActualDeliveryDate'] = pd.to_datetime(df['ActualDeliveryDate'])
df['IsOnTime'] = (df['ActualDeliveryDate'] <= df['PromisedDeliveryDate']).astype(int)

# 3. AGGREGATE & ANALYZE
carrier_performance = df.groupby('Carrier').agg(
    AverageCostPerMile=('CostPerMile', 'mean'),
    OnTimePercentage=('IsOnTime', 'mean'),
    TotalShipments=('ShipmentID', 'count')
).reset_index()

# 4. FORMAT & OUTPUT
carrier_performance['OnTimePercentage'] = carrier_performance['OnTimePercentage'] * 100
carrier_performance['AverageCostPerMile'] = carrier_performance['AverageCostPerMile'].round(2)
carrier_performance['OnTimePercentage'] = carrier_performance['OnTimePercentage'].round(0).astype(str) + '%'

print("--- Carrier Performance Analysis ---")
print(carrier_performance.to_string(index=False))

# 5. SAVE REPORT
carrier_performance.to_csv('carrier_summary_report.csv', index=False)
print("\nAnalysis complete. Summary report saved to carrier_summary_report.csv")
