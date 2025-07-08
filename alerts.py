def generate_alerts(df):
   
    alerts = []

    for _, row in df.iterrows():
        alert = {
            "region": row["region"],
            "date": row["date"].strftime("%Y-%m-%d"),
            "alert_level": row["risk_level"]
        }
        alerts.append(alert)

    return alerts
