import pymupdf
import argparse


def get_bbox(page):
    """Get bounding bbox that excludes white margins"""
    pix = page.get_pixmap()
    # get height top
    for top in range(0, pix.height):
        all_white = True
        for w in range(0, pix.width):
            rgb = pix.pixel(w, top)
            if rgb != (255, 255, 255):
                all_white = False
                break
        if not all_white:
            break
    # get height bottom
    for bottom in range(pix.height-1, top, -1):
        all_white = True
        for w in range(0, pix.width):
            rgb = pix.pixel(w, bottom)
            if rgb != (255, 255, 255):
                all_white = False
                break
        if not all_white:
            break
    # get width left
    for left in range(0, pix.width):
        all_white = True
        for h in range(0, pix.height):
            rgb = pix.pixel(left, h)
            if rgb != (255, 255, 255):
                all_white = False
                break
        if not all_white:
            break
    # get width right
    for right in range(pix.width-1, left, -1):
        all_white = True
        for h in range(0, pix.height):
            rgb = pix.pixel(right, h)
            if rgb != (255, 255, 255):
                all_white = False
                break
        if not all_white:
            break
    left = left if left == 0 else left - 1
    right = right if right == pix.width - 1 else right + 1
    top = top if top == 0 else top - 1
    bottom = bottom if bottom == pix.height - 1 else bottom + 1
    return pymupdf.Rect(left, top, right, bottom)


def pdfcrop(input_path, output_path):
    # Open the PDF file
    pdf_document = pymupdf.open(input_path)

    # iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        rect = get_bbox(page)
        page.set_cropbox(rect)
        
    # Save the cropped PDF to a new file
    pdf_document.save(output_path)
    
    # Close the PDF document
    pdf_document.close()


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='pdfcrop')
    parser.add_argument('filename')
    parser.add_argument('-o', '--output',type=str, default=None,
                        help='output file path')
    args = parser.parse_args()

    assert args.filename.endswith('.pdf'), "filename must end with '.pdf'"
    outfile = args.filename[:-4] + '_cropped.pdf' if args.output is None else args.output

    pdfcrop(args.filename, outfile)
    print(f"PDF cropped successfully: {outfile}")
