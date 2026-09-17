import fitz

def highlight_pdf(
    input_path,
    output_path,
    results
):

    doc = fitz.open(input_path)

    for result in results:

        clause = result["clause"]
        page_number = result["page"] - 1

        page = doc[page_number]

        matches = page.search_for(clause)

        for rect in matches:
            annotation = page.add_highlight_annot(rect)
            annotation.update()

    doc.save(output_path)