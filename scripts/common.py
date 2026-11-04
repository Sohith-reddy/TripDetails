"""Shared layout helpers for the trip-plan PDFs (ReportLab Platypus)."""
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table,
    TableStyle,
)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", FONT_DIR + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", FONT_DIR + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVM", FONT_DIR + "DejaVuSansMono.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DVB", italic="DV", boldItalic="DVB")

PAGE_W, PAGE_H = A4
MARGIN = 15 * mm
CONTENT_W = PAGE_W - 2 * MARGIN

INK = colors.HexColor("#1f2933")
MUTED = colors.HexColor("#52606d")
LINE = colors.HexColor("#cbd2d9")
ZEBRA = colors.HexColor("#f5f7fa")

PREPARED = "Prepared 4 Nov 2026 · Prices are researched estimates, not live quotes. Re-check on IRCTC / airline / HRTC before paying."


def styles(accent):
    base = dict(fontName="DV", textColor=INK, leading=13.2, fontSize=9.4)
    return {
        "title": ParagraphStyle("title", fontName="DVB", fontSize=22, leading=27,
                                textColor=colors.white),
        "subtitle": ParagraphStyle("subtitle", fontName="DV", fontSize=11, leading=15,
                                   textColor=colors.white),
        "h1": ParagraphStyle("h1", fontName="DVB", fontSize=14.5, leading=19,
                             textColor=accent, spaceBefore=10, spaceAfter=5, keepWithNext=1),
        "h2": ParagraphStyle("h2", fontName="DVB", fontSize=11.2, leading=15,
                             textColor=INK, spaceBefore=7, spaceAfter=3, keepWithNext=1),
        "p": ParagraphStyle("p", spaceAfter=4, allowWidows=0, allowOrphans=0, **base),
        "small": ParagraphStyle("small", fontName="DV", fontSize=7.8, leading=10.2,
                                textColor=MUTED, allowWidows=0, allowOrphans=0),
        "src": ParagraphStyle("src", fontName="DV", fontSize=7.1, leading=9.0,
                              textColor=MUTED, leftIndent=8, bulletIndent=0),
        "cell": ParagraphStyle("cell", fontName="DV", fontSize=8.3, leading=10.8,
                               textColor=INK),
        "cellb": ParagraphStyle("cellb", fontName="DVB", fontSize=8.3, leading=10.8,
                                textColor=INK),
        "head": ParagraphStyle("head", fontName="DVB", fontSize=8.4, leading=10.8,
                               textColor=colors.white),
        "bullet": ParagraphStyle("bullet", leftIndent=11, bulletIndent=2,
                                 spaceAfter=1.8, **base),
        "daytitle": ParagraphStyle("daytitle", fontName="DVB", fontSize=10.2,
                                   leading=13, textColor=colors.white),
        "center": ParagraphStyle("center", alignment=TA_CENTER, **base),
    }


class PlanDoc:
    """Collects flowables and renders a styled A4 PDF."""

    def __init__(self, path, title, subtitle, accent, tag):
        self.path = path
        self.title = title
        self.subtitle = subtitle
        self.accent = colors.HexColor(accent)
        self.light = _tint(self.accent, 0.88)
        self.tag = tag
        self.s = styles(self.accent)
        self.story = []
        self._pending = []
        self._cover()

    def _add(self, *flowables):
        """Append flowables; glue any pending heading to the first one so headings never strand."""
        fl = list(flowables)
        if self._pending and fl:
            fl = [KeepTogether(self._pending + [fl[0]])] + fl[1:]
            self._pending = []
        self.story.extend(fl)

    # ---------- page furniture ----------
    def _on_page(self, canv, doc):
        canv.saveState()
        canv.setFillColor(self.accent)
        canv.rect(0, PAGE_H - 9 * mm, PAGE_W, 9 * mm, stroke=0, fill=1)
        canv.setFillColor(colors.white)
        canv.setFont("DVB", 8.5)
        canv.drawString(MARGIN, PAGE_H - 6 * mm, self.tag)
        canv.setFont("DV", 8)
        canv.drawRightString(PAGE_W - MARGIN, PAGE_H - 6 * mm,
                             "Hyderabad → North · 24 Dec 2026 – 3 Jan 2027")
        canv.setStrokeColor(LINE)
        canv.line(MARGIN, 11 * mm, PAGE_W - MARGIN, 11 * mm)
        canv.setFillColor(MUTED)
        canv.setFont("DV", 6.8)
        canv.drawString(MARGIN, 7 * mm, PREPARED)
        canv.drawRightString(PAGE_W - MARGIN, 7 * mm, f"Page {doc.page}")
        canv.restoreState()

    def _cover(self):
        s = self.s
        block = Table(
            [[Paragraph(self.title, s["title"])],
             [Paragraph(self.subtitle, s["subtitle"])]],
            colWidths=[CONTENT_W],
        )
        block.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), self.accent),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ("TOPPADDING", (0, 0), (-1, 0), 14),
            ("BOTTOMPADDING", (0, -1), (-1, -1), 14),
        ]))
        self.story += [Spacer(1, 4), block, Spacer(1, 8)]

    # ---------- content helpers ----------
    def h1(self, text):
        self._pending += [Paragraph(text, self.s["h1"]), _rule(self.accent)]

    def h2(self, text):
        self._pending.append(Paragraph(text, self.s["h2"]))

    def p(self, text):
        self._add(Paragraph(text, self.s["p"]))

    def small(self, text):
        self._add(Paragraph(text, self.s["small"]))

    def bullets(self, items):
        self._add(*[Paragraph(it, self.s["bullet"], bulletText="•") for it in items], Spacer(1, 3))

    def space(self, h=6):
        self._add(Spacer(1, h))

    def page_break(self):
        self._add(PageBreak())

    def callout(self, title, text, kind="info"):
        palette = {
            "info": (self.light, self.accent),
            "warn": (colors.HexColor("#fff4e5"), colors.HexColor("#c2410c")),
            "good": (colors.HexColor("#e7f8ee"), colors.HexColor("#15803d")),
        }
        bg, edge = palette[kind]
        title_style = ParagraphStyle("ct", parent=self.s["cellb"], textColor=edge,
                                     fontSize=9.2, leading=12)
        body = text if isinstance(text, list) else [text]
        rows = [[Paragraph(title, title_style)]]
        for b in body:
            rows.append([Paragraph(b, self.s["cell"])])
        t = Table(rows, colWidths=[CONTENT_W])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), bg),
            ("LINEBEFORE", (0, 0), (0, -1), 3, edge),
            ("LEFTPADDING", (0, 0), (-1, -1), 9),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 2.2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
            ("TOPPADDING", (0, 0), (-1, 0), 6),
            ("BOTTOMPADDING", (0, -1), (-1, -1), 6),
        ]))
        self._add(KeepTogether(t), Spacer(1, 7))

    def table(self, rows, widths, header=True, bold_first_col=False, total_row=False):
        """rows: list of lists of strings. widths: fractions of content width."""
        s = self.s
        data = []
        for r_i, row in enumerate(rows):
            cells = []
            for c_i, val in enumerate(row):
                if header and r_i == 0:
                    st = s["head"]
                elif (bold_first_col and c_i == 0) or (total_row and r_i == len(rows) - 1):
                    st = s["cellb"]
                else:
                    st = s["cell"]
                cells.append(Paragraph(str(val), st))
            data.append(cells)
        t = Table(data, colWidths=[w * CONTENT_W for w in widths], repeatRows=1 if header else 0)
        style = [
            ("GRID", (0, 0), (-1, -1), 0.4, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]
        if header:
            style.append(("BACKGROUND", (0, 0), (-1, 0), self.accent))
        start = 1 if header else 0
        for i in range(start, len(rows)):
            if (i - start) % 2 == 1:
                style.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
        if total_row:
            style.append(("BACKGROUND", (0, len(rows) - 1), (-1, len(rows) - 1), self.light))
        t.setStyle(TableStyle(style))
        self._add(t, Spacer(1, 7))

    def day(self, label, title, items, stay=None, cost=None):
        """A day card: coloured header bar + bullet list + stay/cost footer."""
        s = self.s
        rows = [[Paragraph(f"{label}  ·  {title}", s["daytitle"])]]
        for it in items:
            rows.append([Paragraph("• " + it, s["cell"])])
        foot = []
        if stay:
            foot.append(f"<b>Stay:</b> {stay}")
        if cost:
            foot.append(f"<b>Day spend (per person):</b> {cost}")
        if foot:
            rows.append([Paragraph(" &nbsp;&nbsp;|&nbsp;&nbsp; ".join(foot), s["cell"])])
        t = Table(rows, colWidths=[CONTENT_W])
        st = [
            ("BACKGROUND", (0, 0), (-1, 0), self.accent),
            ("BOX", (0, 0), (-1, -1), 0.6, self.accent),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("TOPPADDING", (0, 0), (-1, 0), 4),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 4),
        ]
        if foot:
            st += [("BACKGROUND", (0, -1), (-1, -1), self.light),
                   ("TOPPADDING", (0, -1), (-1, -1), 4),
                   ("BOTTOMPADDING", (0, -1), (-1, -1), 4)]
        t.setStyle(TableStyle(st))
        self._add(KeepTogether(t), Spacer(1, 6))

    def budget(self, rows, group_note):
        """rows: (item, shoestring, recommended, note). Totals are computed here."""
        head = [["Item (per person, 6 sharing)", "Shoestring", "Recommended", "Notes"]]
        body, lo, hi = [], 0, 0
        for item, a, b, note in rows:
            lo += a
            hi += b
            body.append([item, _inr(a), _inr(b), note])
        total = [["<b>TOTAL per person</b>", f"<b>{_inr(lo)}</b>", f"<b>{_inr(hi)}</b>", group_note]]
        self.table(head + body + total, [0.34, 0.13, 0.14, 0.39], total_row=True)
        return lo, hi

    def sources(self, items):
        self.h1("Sources checked")
        self.small("Reddit and direct page fetches (Airbnb, IRCTC, erail, ConfirmTkt) were blocked from this environment, so everything "
                   "here comes from web-search results: Airbnb listing snippets, rail timetable aggregators, Team-BHP, Tripoto, travel blogs and local news. "
                   "Live seat availability and live prices could not be checked; use the checklists above to verify.")
        self.space(3)
        for it in items:
            self._add(Paragraph(it, self.s["src"], bulletText="–"))

    def build(self):
        doc = SimpleDocTemplate(
            self.path, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
            topMargin=14 * mm, bottomMargin=15 * mm, title=self.title,
            author="Trip planning notes", subject=self.subtitle,
        )
        doc.build(self.story, onFirstPage=self._on_page, onLaterPages=self._on_page)


def totals(rows):
    """Sum shoestring / recommended columns of budget rows so summaries match the table."""
    return sum(r[1] for r in rows), sum(r[2] for r in rows)


def k(n):
    """₹ in thousands with one decimal, e.g. 24550 -> '₹24.6k'."""
    return f"₹{n / 1000:.1f}k"


def _inr(n):
    """Indian digit grouping: 123456 -> ₹1,23,456."""
    s = str(int(round(n)))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        groups = []
        while len(head) > 2:
            groups.insert(0, head[-2:])
            head = head[:-2]
        if head:
            groups.insert(0, head)
        s = ",".join(groups) + "," + tail
    return "₹" + s


def _rule(color):
    t = Table([[""]], colWidths=[CONTENT_W], rowHeights=[1.2])
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), 1.2, color),
                           ("TOPPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    t.keepWithNext = 1
    return t


def _tint(c, f):
    return colors.Color(c.red + (1 - c.red) * f, c.green + (1 - c.green) * f,
                        c.blue + (1 - c.blue) * f)
