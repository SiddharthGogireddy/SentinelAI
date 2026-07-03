import re

RULES = {
    "camera": ["camera", "video call", "video"],
    "microphone": ["microphone", "voice call", "voice"],
    "location": ["location", "gps", "nearby"],
    "contacts": ["contacts", "contact syncing", "address book"],
    "photos": ["photos", "gallery", "images"],
    "storage": ["files", "storage", "upload"],
    "clipboard": ["clipboard", "copy", "paste"],
    "cookies": ["cookies", "cookie"],
    "analytics": ["analytics", "usage statistics", "performance"],
    "device_information": [
        "device",
        "ip address",
        "browser",
        "operating system",
    ],
    "payment_information": [
        "payment",
        "billing",
        "credit card",
        "bank account",
    ],
    "third_party_sharing": [
        "third party",
        "advertising partners",
        "share information",
    ],
}
def suggest_labels(clause: str):

    clause = clause.lower()

    labels = []

    for label, keywords in RULES.items():

        for keyword in keywords:

            if keyword in clause:

                labels.append(label)
                break

    return labels