#!/usr/bin/env python3
"""Transcribe the original resume text into public/VB_Google__Resume.pdf.

The original binary was not on this worker VM; this file is built from the
parent-store OCR of VB_Google__Resume.pdf.
"""

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

OUT = "/workspace/public/VB_Google__Resume.pdf"
INK = HexColor("#111827")
MUTED = HexColor("#4b5563")
ACCENT = HexColor("#0e7490")


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name", parent=base["Title"], fontName="Times-Bold", fontSize=16,
            textColor=INK, alignment=1, spaceAfter=2, leading=20,
        ),
        "head": ParagraphStyle(
            "Head", parent=base["Normal"], fontName="Times-Italic", fontSize=10,
            textColor=MUTED, alignment=1, spaceAfter=2, leading=13,
        ),
        "meta": ParagraphStyle(
            "Meta", parent=base["Normal"], fontName="Times-Roman", fontSize=9,
            textColor=MUTED, alignment=1, spaceAfter=10, leading=12,
        ),
        "h": ParagraphStyle(
            "H", parent=base["Heading2"], fontName="Times-Bold", fontSize=11,
            textColor=ACCENT, spaceBefore=8, spaceAfter=4, leading=14,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["Normal"], fontName="Times-Roman", fontSize=9.5,
            textColor=INK, leading=12.5, spaceAfter=3,
        ),
        "role": ParagraphStyle(
            "Role", parent=base["Normal"], fontName="Times-Bold", fontSize=10,
            textColor=INK, leading=13, spaceAfter=1,
        ),
        "sub": ParagraphStyle(
            "Sub", parent=base["Normal"], fontName="Times-Italic", fontSize=9,
            textColor=MUTED, leading=12, spaceAfter=4,
        ),
    }


def main():
    s = styles()
    doc = SimpleDocTemplate(
        OUT, pagesize=letter,
        leftMargin=0.65 * inch, rightMargin=0.65 * inch,
        topMargin=0.5 * inch, bottomMargin=0.5 * inch,
        title="Vijay Baskaran Arjun Dev",
        author="Vijay Baskaran Arjun Dev",
    )
    story = [
        Paragraph("Vijay Baskaran Arjun Dev", s["name"]),
        Paragraph(
            "Head of Software Technologies @ Retailetics | AI/ML Developer | Mobile Systems &amp; Scaled Engineering",
            s["head"],
        ),
        Paragraph(
            "+91 8088413589 &nbsp;·&nbsp; +60 1151135376 &nbsp;·&nbsp; yoursvijii@gmail.com<br/>linkedin.com/in/vijay-baskaran-arjun-dev &nbsp;·&nbsp; github.com/YoursViji/vb-profile<br/>Federal Territory of Kuala Lumpur, Malaysia",
            s["meta"],
        ),
        Paragraph("EXPERIENCE", s["h"]),
        Paragraph("Head of Software Technologies — Retailetics SDN BHD", s["role"]),
        Paragraph("Kuala Lumpur, Malaysia &nbsp;·&nbsp; February 2021 – Present", s["sub"]),
        Paragraph(
            "Retailetics AI-infused Self-Checkout Smart Trolley (ezyCart). Spearheaded an AI-powered self-checkout shopping cart: architecture, stakeholder design, and UX. Built a real-time socket pipeline between IoT devices and the ezyCart Android app for fast sync without slow transfers or redundant permission requests.",
            s["body"],
        ),
        Paragraph(
            "Delivered million-dollar savings with an AI-powered indoor navigation system. Saved over $2M by eliminating thousands of Bluetooth beacon devices.",
            s["body"],
        ),
        Paragraph(
            "Conceptualized, designed, and developed a cross-platform support staff app (Flutter) and an Android TV cart monitor system.",
            s["body"],
        ),
        Paragraph(
            "Conceptualized and developed Lisa — an AI shopping assistant that resolves customer queries and provides real-time product recommendations and promotions.",
            s["body"],
        ),
        Paragraph("Developed and deployed machine learning models for the in-store product line.", s["body"]),
        Paragraph(
            "Automated build pipeline and deployment for merchants and outlets, reducing deployment time across retail sites.",
            s["body"],
        ),
        Paragraph(
            "Led split testing initiatives driving multi-million-dollar revenue growth and stronger in-store customer experiences.",
            s["body"],
        ),
        Paragraph("INDEPENDENT VENTURE", s["h"]),
        Paragraph("Founder — TAN Intelligence", s["role"]),
        Paragraph("AI-powered forex trading indicator", s["sub"]),
        Paragraph(
            "TAN Intelligence is an independent company building an original Artificial Intelligence trading indicator for the forex market. Direction: indicator, then signals, then an automated bot with explicit risk controls. Founder work, not a second employer.",
            s["body"],
        ),
        Paragraph("SKILLS", s["h"]),
        Paragraph("<b>Mobile:</b> Java, Kotlin, Dart, Android SDK, Jetpack Compose, Flutter, Kotlin Multiplatform, iOS", s["body"]),
        Paragraph("<b>Backend:</b> REST, GraphQL, WebSockets, Spring Boot, Postgres, SQLite, microservices", s["body"]),
        Paragraph("<b>AI/ML:</b> TensorFlow, PyTorch, Keras, OpenCV, on-device ML, NLP, model quantization", s["body"]),
        Paragraph("<b>Delivery:</b> Jenkins, Fastlane, Docker, Git, CI/CD, split testing, SOLID, Clean Architecture, MVVM", s["body"]),
        Paragraph("EDUCATION", s["h"]),
        Paragraph("Bachelor of Engineering in Computer Science and Engineering", s["role"]),
        Paragraph("Anna University Chennai", s["sub"]),
        Paragraph("CERTIFICATIONS", s["h"]),
        Paragraph("Mobile iOS &amp; Android development — Target Software, Chennai", s["body"]),
        Paragraph("SOLID Principles — Coursera", s["body"]),
        Paragraph("AI/ML Architecture — IBM", s["body"]),
        Paragraph("Master prompting — Claude and Coursera", s["body"]),
        Spacer(1, 8),
        Paragraph(
            "Contact: yoursvijii@gmail.com · +91 8088413589 · +60 1151135376 · linkedin.com/in/vijay-baskaran-arjun-dev · github.com/YoursViji/vb-profile",
            s["meta"],
        ),
    ]
    doc.build(story)
    print(OUT)


if __name__ == "__main__":
    main()
