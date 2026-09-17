prompt = f"""
You are a privacy and security expert.

Analyze this privacy policy clause:

Clause:
{clause}

Detected Permissions:
{', '.join(labels)}

Return the response in exactly this format:

Why Flagged:
<response>

Commonness:
<response>

User Impact:
<response>

Recommendation:
<response>

Keep each section concise and user-friendly.
"""