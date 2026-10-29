#!/usr/bin/env python3
"""ATS-friendly single-column resumes. No tables, icons, or graphics."""

from pathlib import Path

from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate

pdfmetrics.registerFont(
    TTFont("LS", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf")
)
pdfmetrics.registerFont(
    TTFont("LSB", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf")
)

INK = HexColor("#111111")
MUTED = HexColor("#333333")

ROOT = Path(__file__).resolve().parent
IDENTITIES = {
    "arjun": {
        "name": "Vijay Baskaran Arjun Dev",
        "out": Path("/tmp/vb-profile/public/VB_Google__Resume.pdf"),
        "linkedin": "linkedin.com/in/vijay-baskaran-arjun-dev",
        "github": "github.com/YoursViji/vb-profile",
        "phones": "+91 8088413589 | +60 1151135376",
        "place": "Bengaluru, India",
    },
    "baskar": {
        "name": "Vijay Baskar",
        "out": Path("/tmp/vijay-baskaran/public/VB_Resume.pdf"),
        "linkedin": "linkedin.com/in/vb1707",
        "github": "github.com/YoursViji/vijay-baskaran",
        "phones": "+91 8088413589 | +60 1151135376",
        "place": "Bengaluru, India",
    },
}

# When this file lives in a site's scripts/ folder, write only that site's PDF.
if ROOT.name == "scripts":
    site = ROOT.parent.name
    if site == "vb-profile":
        IDENTITIES = {"arjun": {**IDENTITIES["arjun"], "out": ROOT.parent / "public" / "VB_Google__Resume.pdf"}}
    elif site == "vijay-baskaran":
        IDENTITIES = {"baskar": {**IDENTITIES["baskar"], "out": ROOT.parent / "public" / "VB_Resume.pdf"}}

HEADLINE = "Principal AI Engineer | Lead GenAI & Agentic Systems Architect"

SUMMARY = (
    "Principal AI & Systems Engineer with 13+ years architecting production "
    "Generative AI, real-time computer vision, agentic pipelines, and scalable "
    "enterprise platforms. Lead GenAI and agentic systems for in-store retail: "
    "multi-agent orchestration (LangGraph, CrewAI, AutoGen, MCP, ReAct), advanced "
    "RAG (hybrid BM25, multi-query, cross-encoder rerank, Pinecone, Qdrant, "
    "Milvus, Weaviate, pgvector, FAISS), and edge vision (YOLO v8/v10/v11, "
    "RT-DETR, Kimera-VIO, OpenCV) with ONNX / TensorRT / TF Lite inference under "
    "100ms. Shipped ezyCart self-checkout, a GenAI/RAG shopping assistant, AI "
    "recipe generation, and Lisa. Independent quantitative trading indicators "
    "for 6+ years. Supporting mobile experience in Kotlin, Java, Jetpack Compose, "
    "Flutter, Android, and iOS."
)

SKILLS = [
    (
        "Generative AI & Agentic",
        "LangGraph, CrewAI, AutoGen, LangChain, LlamaIndex, LangSmith, Langflow, "
        "MCP, Multi-Agent Orchestration, ReAct, LLM abstraction (routing, fallbacks, "
        "rate limits, token budgeting), n8n",
    ),
    (
        "LLMs",
        "GPT-4o, Claude, Gemini, Llama 3 / Mistral, FinGPT, Ollama, vLLM, Prompt "
        "Engineering, evals, LoRA/PEFT, Hugging Face Transformers",
    ),
    (
        "RAG",
        "Advanced RAG, Hybrid Search BM25, multi-query, cross-encoder rerank, "
        "Pinecone, Qdrant, Milvus, Weaviate, pgvector, FAISS, Supabase",
    ),
    (
        "CV / SLAM",
        "YOLO v8/v10/v11, RT-DETR, Kimera-VIO, OpenCV, OCR, detection/segmentation",
    ),
    (
        "DL / ML",
        "PyTorch, JAX, TensorFlow, Keras, Scikit-learn, XGBoost, NumPy, Pandas, "
        "time-series, ONNX, TensorRT, TF Lite",
    ),
    (
        "Backend",
        "Python, FastAPI, Pydantic, Celery, Node.js, Spring Boot, REST, GraphQL, "
        "WebSockets, SQL, PostgreSQL, Firebase, AWS",
    ),
    (
        "MLOps",
        "AWS Bedrock, SageMaker, GCP Vertex AI, Databricks, Langfuse, Docker, "
        "CI/CD for ML, Jenkins, GitHub Actions, GitLab CI",
    ),
    (
        "Mobile (supporting)",
        "Kotlin, Java, Jetpack Compose, Flutter, Android, iOS, Dart, MVVM",
    ),
]


def styles():
    return {
        "name": ParagraphStyle(
            "Name",
            fontName="LSB",
            fontSize=16,
            leading=19,
            textColor=INK,
            alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "head": ParagraphStyle(
            "Head",
            fontName="LS",
            fontSize=10,
            leading=13,
            textColor=INK,
            alignment=TA_CENTER,
            spaceAfter=3,
        ),
        "meta": ParagraphStyle(
            "Meta",
            fontName="LS",
            fontSize=8.5,
            leading=11,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "h": ParagraphStyle(
            "H",
            fontName="LSB",
            fontSize=11,
            leading=14,
            textColor=black,
            alignment=TA_LEFT,
            spaceBefore=8,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "Body",
            fontName="LS",
            fontSize=9,
            leading=11.4,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=3,
        ),
        "role": ParagraphStyle(
            "Role",
            fontName="LSB",
            fontSize=10,
            leading=13,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=0,
        ),
        "sub": ParagraphStyle(
            "Sub",
            fontName="LS",
            fontSize=8.5,
            leading=11,
            textColor=MUTED,
            alignment=TA_LEFT,
            spaceAfter=3,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            fontName="LS",
            fontSize=9,
            leading=11.4,
            textColor=INK,
            alignment=TA_LEFT,
            leftIndent=12,
            firstLineIndent=-10,
            spaceAfter=2,
        ),
    }


def story_for(person: dict):
    s = styles()
    name = person["name"]
    return [
        Paragraph(name, s["name"]),
        Paragraph(HEADLINE, s["head"]),
        Paragraph(
            f"{person['phones']} | yoursvijii@gmail.com<br/>"
            f"{person['linkedin']}<br/>"
            f"{person['place']}",
            s["meta"],
        ),
        Paragraph("SUMMARY", s["h"]),
        Paragraph(SUMMARY, s["body"]),
        Paragraph("SKILLS", s["h"]),
        *[
            Paragraph(f"<b>{label}:</b> {items}", s["body"])
            for label, items in SKILLS
        ],
        Paragraph("EXPERIENCE", s["h"]),
        Paragraph(
            "Principal AI Engineer | Lead GenAI &amp; Agentic Systems Architect - Retailetics SDN BHD",
            s["role"],
        ),
        Paragraph("Kuala Lumpur, Malaysia | March 2023 - Present", s["sub"]),
        Paragraph(
            "Lead GenAI, agentic systems, and computer vision for Retailetics in-store stack: self-checkout, RAG assistants, and sub-100ms edge inference.",
            s["body"],
        ),
        Paragraph(
            "- Architected agentic and computer-vision self-checkout (ezyCart) with RT-DETR, YOLO, and Kimera-VIO; ML indoor navigation saved over $2M by replacing thousands of Bluetooth beacons.",
            s["bullet"],
        ),
        Paragraph(
            "- Shipped a GenAI/RAG shopping assistant and AI recipe generation with LangChain and LlamaIndex: cuisine suggestions, cooking video, and missing-item add-to-cart.",
            s["bullet"],
        ),
        Paragraph(
            "- Built FastAPI and Spring Boot WebSocket IoT pipelines between devices and the ezyCart Android app for real-time sync.",
            s["bullet"],
        ),
        Paragraph(
            "- Deployed ONNX and TensorFlow Lite on-device models with sub-100ms edge inference for checkout vision and on-cart assist.",
            s["bullet"],
        ),
        Paragraph("Senior Staff Software Engineer - Retailetics SDN BHD", s["role"]),
        Paragraph("Kuala Lumpur, Malaysia | February 2021 - March 2023", s["sub"]),
        Paragraph(
            "Led software for ezyCart, kiosks, wayfinding, staff tools, and shopper apps.",
            s["body"],
        ),
        Paragraph(
            "- Spearheaded the AI-infused self-checkout smart trolley (ezyCart): architecture, stakeholder design, and a real-time socket pipeline between IoT devices and the ezyCart Android app.",
            s["bullet"],
        ),
        Paragraph(
            "- Shipped the self-checkout kiosk on the same stack (scan, bag, pay) and integrated Tap to Pay and NFC.",
            s["bullet"],
        ),
        Paragraph(
            "- Delivered ML-based indoor navigation and product finder; ran A/B and split testing across merchants.",
            s["bullet"],
        ),
        Paragraph(
            "- Built a Flutter support-staff app, Android TV cart monitor, Flutter SDK lite, ezyList, stock audit, Voice Assist, and Lisa AI shopping assistant.",
            s["bullet"],
        ),
        Paragraph("Senior Software Engineer - Colan Infotech", s["role"]),
        Paragraph("Chennai, India | November 2012 - February 2021", s["sub"]),
        Paragraph(
            "Shipped 20+ Android, iOS, and Flutter apps plus the backends and ML prototypes they talk to.",
            s["body"],
        ),
        Paragraph(
            "- Delivered 20+ production mobile apps (Android/iOS): native Kotlin/Java and Flutter, with MVVM, Jetpack Compose, and CI/CD (Jenkins, GitLab, Bitrise); reduced ANR crashes by 70% and lifted app performance by 30%.",
            s["bullet"],
        ),
        Paragraph(
            "- Architected scalable backends using Spring Boot, AWS, Firebase, and REST APIs; designed Spring Boot microservices for 500K+ users with 40% faster response time.",
            s["bullet"],
        ),
        Paragraph(
            "- Built Python prototypes with TensorFlow, PyTorch, and Scikit-learn for on-device and backend ML experiments.",
            s["bullet"],
        ),
        Paragraph("INDEPENDENT VENTURE", s["h"]),
        Paragraph("TAN Intelligence - Founder (not an employer)", s["role"]),
        Paragraph("Proprietary custom trading indicators | Independent venture", s["sub"]),
        Paragraph(
            "- End-to-End Quantitative Systems: Engineered and deployed proprietary algorithmic trading models and custom indicators across Commodities, FX, and Crypto, operating systematically for over 6 years.",
            s["bullet"],
        ),
        Paragraph(
            "- Automated Architecture and Telegram Pipelines: Built custom 5-minute and 15-minute signal engine pipelines integrated with Telegram alerts and low-latency automated execution AI-bots via REST and WebSockets.",
            s["bullet"],
        ),
        Paragraph(
            "- Strategy and Market Structure: Developed rule-based frameworks applying Smart Money Concepts (SMC), liquidity sweeps, and dynamic position-sizing protocols to optimize risk-adjusted returns.",
            s["bullet"],
        ),
        Paragraph(
            "- Execution and Backtesting Rigor: Automated multi-broker execution (TradingView, MetaTrader) using Python and Pine Script; backtested and forward-tested strategies to maintain a sub-5% maximum drawdown limit.",
            s["bullet"],
        ),
        Paragraph("EDUCATION", s["h"]),
        Paragraph(
            "Bachelor of Engineering in Computer Science and Engineering",
            s["role"],
        ),
        Paragraph(
            "Anna University / GGR College of Engineering, Vellore, India | 2007 - 2011",
            s["sub"],
        ),
        Paragraph("CERTIFICATIONS", s["h"]),
        Paragraph(
            "Mobile iOS &amp; Android development - Target Software, Chennai",
            s["body"],
        ),
        Paragraph("SOLID Principles - Coursera", s["body"]),
        Paragraph("AI/ML Architecture - IBM", s["body"]),
        Paragraph("Master prompting - Claude and Coursera", s["body"]),
    ]


def build(person: dict) -> None:
    person["out"].parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(person["out"]),
        pagesize=letter,
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.42 * inch,
        bottomMargin=0.42 * inch,
        title=person["name"],
        author=person["name"],
        subject=HEADLINE,
    )
    doc.build(story_for(person))
    print(person["out"], person["out"].stat().st_size)


def main():
    for person in IDENTITIES.values():
        build(person)
        # keep a copy of the generator next to each site
    Path("/tmp/vb-profile/scripts").mkdir(exist_ok=True)
    Path("/tmp/vijay-baskaran/scripts").mkdir(exist_ok=True)


if __name__ == "__main__":
    main()
