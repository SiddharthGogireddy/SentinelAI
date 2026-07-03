from risk_levels import RISK_DATABASE


def build_alert(labels):

    alerts = []

    for label in labels:

        if label in RISK_DATABASE:
            alerts.append(RISK_DATABASE[label])

    return alerts
