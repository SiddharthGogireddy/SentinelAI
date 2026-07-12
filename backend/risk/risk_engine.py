from backend.risk.risk_levels import RISK_DATABASE


def build_alert(labels, evidence=None):

    alerts = []

    for label in labels:

        if label in RISK_DATABASE:

            risk = RISK_DATABASE[label].copy()

            risk["evidence"] = evidence

            alerts.append(risk)

    return alerts