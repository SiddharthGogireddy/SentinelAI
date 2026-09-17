import fitz


def highlight_pdf(input_path, output_path, results):

    doc = fitz.open(input_path)

    colors = {
        "high": (1, 0, 0),      # Red
        "medium": (1, 1, 0),    # Yellow
        "low": (0, 1, 0),       # Green
    }

    for result in results:

        clause = result["clause"]
        page_number = result["page"] - 1

        page = doc[page_number]

        matches = page.search_for(clause)

        risk_level = "low"

        if result["alerts"]:
            risk_level = result["alerts"][0]["level"].lower()

        color = colors.get(
            risk_level,
            (0, 1, 0)
        )

        for rect in matches:

            highlight = page.add_highlight_annot(rect)

            highlight.set_colors(
                stroke=color
            )

            highlight.update()

    doc.save(output_path)
    doc.close()