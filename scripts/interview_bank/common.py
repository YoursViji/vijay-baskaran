"""Shared PDF helpers."""
from xml.sax.saxutils import escape

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, Spacer

pdfmetrics.registerFont(TTFont("LS", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("LSB", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"))

RED = HexColor("#C1121F")
BLUE = HexColor("#1D4ED8")
GREEN = HexColor("#047857")
INK = HexColor("#111827")
MUTED = HexColor("#374151")


def styles():
    return {
        "cover": ParagraphStyle("cover", fontName="LSB", fontSize=20, leading=24, textColor=INK, spaceAfter=6),
        "sub": ParagraphStyle("sub", fontName="LS", fontSize=10.5, leading=14, textColor=MUTED, spaceAfter=6),
        "h": ParagraphStyle("h", fontName="LSB", fontSize=13, leading=16, textColor=INK, spaceBefore=10, spaceAfter=5),
        "h2": ParagraphStyle("h2", fontName="LSB", fontSize=10.5, leading=13.5, textColor=INK, spaceBefore=7, spaceAfter=3),
        "body": ParagraphStyle("body", fontName="LS", fontSize=8.7, leading=11.4, textColor=INK, spaceAfter=3),
        "q": ParagraphStyle("q", fontName="LSB", fontSize=9.4, leading=12.2, textColor=RED, spaceBefore=6, spaceAfter=2),
        "a": ParagraphStyle("a", fontName="LS", fontSize=8.6, leading=11.3, textColor=BLUE, spaceAfter=1.5),
        "e": ParagraphStyle("e", fontName="LS", fontSize=8.6, leading=11.3, textColor=GREEN, spaceAfter=1.5),
        "note": ParagraphStyle("note", fontName="LS", fontSize=8.2, leading=10.8, textColor=MUTED, spaceAfter=3),
    }


def qa(n, question, kid, tech, examples):
    s = styles()
    bits = [
        Paragraph(f"Q{n}. {escape(question)}", s["q"]),
        Paragraph(f"<b>Answer (simple).</b> {escape(kid)}", s["a"]),
        Paragraph(f"<b>Answer (interview).</b> {escape(tech)}", s["a"]),
    ]
    for ex in examples:
        bits.append(Paragraph(f"<b>Example.</b> {escape(ex)}", s["e"]))
    bits.append(Spacer(1, 3))
    # KeepTogether only when the block is likely to fit on one page.
    # Long senior answers must be allowed to split or reportlab overflows.
    text_len = len(question) + len(kid) + len(tech) + sum(len(x) for x in examples)
    if text_len < 900:
        return [KeepTogether(bits)]
    return bits


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(RED)
    canvas.rect(0, letter[1] - 26, letter[0], 26, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("LSB", 8.5)
    canvas.drawString(0.6 * inch, letter[1] - 16, "Vijay Baskar  |  AI Interview Bank  |  Basic → Intermediate → Advanced")
    canvas.setFillColor(GREEN)
    canvas.rect(0, 0, letter[0], 20, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("LS", 7.5)
    canvas.drawString(0.6 * inch, 7, "Question = red    Answer = blue    Example = green")
    canvas.drawRightString(letter[0] - 0.6 * inch, 7, f"Page {doc.page}")
    canvas.restoreState()
