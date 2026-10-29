#!/usr/bin/env python3
"""Build the Vijay Baskar AI interview bank PDF: Basic → Intermediate → Advanced."""

from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

from common import header_footer, qa, styles
from level1_basic import QUESTIONS as L1
from level2_intermediate import QUESTIONS as L2
from level3_advanced import QUESTIONS as L3
from level_errors import QUESTIONS as LERR

OUT = Path("/tmp/Vijay_Baskar_AI_Interview_Guide.pdf")

# First-question → subsection title (structure, not numbering).
SECTIONS = {
    "What is Python and why is it used in AI?": "Python",
    "What is OOP? Class vs object?": "Object-oriented programming",
    "What is Big-O? Best / average / worst case?": "Data structures and Big-O",
    "What is HTTP? Methods GET POST PUT PATCH DELETE?": "HTTP, REST, and JSON",
    "What is SQL? Primary key vs foreign key?": "SQL",
    "What is Git? commit, branch, merge, rebase?": "Git",
    "What is a process vs thread?": "Linux, OS, and networking",
    "Java vs Kotlin for Android?": "Java, Kotlin, Android, and Flutter (fresher)",
    "What is JSON Schema / OpenAPI?": "Tests, CI, security, and config",
    "Supervised vs unsupervised vs reinforcement learning?": "Machine learning fundamentals",
    "What is computer vision in production?": "Computer vision and spatial AI",
    "Why FastAPI for AI services?": "Backend, APIs, and DevOps",
    "Jetpack: Room, Hilt, Navigation, WorkManager, DataStore?": "Mobile (Android / Flutter)",
    "What is Generative AI? What is an LLM?": "LLM, RAG, and agents (intermediate)",
    "What is a backtest vs paper vs live?": "Trading hygiene",
    "AWS Bedrock in one minute?": "Cloud (Bedrock, Vertex, SageMaker)",
    "What does HTTP 400 mean on an LLM or RAG API, and what do you do?": "HTTP, vendor, RAG, and GPU errors",
    "Design a RAG pipeline that handles 10 million documents.": "25 most-asked industry questions",
    "How do you handle document updates and deletions in RAG?": "RAG at scale",
    "When is a multi-agent system worse than one agent?": "Agents, tools, and memory",
    "What is MLOps for LLM apps (not only sklearn)?": "Evals, safety, and MLOps",
    "Prefill vs decode and why TTFT cares?": "Serving, inference, and platforms",
    "Design an enterprise RAG assistant (whiteboard).": "System design, leadership, and this resume",
}


def add_questions(story, items, n, s):
    for q, kid, tech, examples in items:
        heading = SECTIONS.get(q)
        if heading:
            story.append(Paragraph(heading, s["h2"]))
        n += 1
        story.extend(qa(n, q, kid, tech, examples))
    return n


def main():
    s = styles()
    n1, n2, n3, nerr = len(L1), len(L2), len(L3), len(LERR)
    total = n1 + n2 + n3 + nerr

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.48 * inch,
        bottomMargin=0.38 * inch,
        title="Vijay Baskar — AI Interview Bank",
        author="Vijay Baskar",
        subject="Basic → Intermediate → Advanced interview Q/A/example bank",
    )

    story = []
    story.append(Paragraph("Vijay Baskar — AI Interview Bank", s["cover"]))
    story.append(
        Paragraph(
            "Full question bank structured Basic → Intermediate → Advanced. "
            "Red = question. Blue = simple answer + interview answer. Green = example from real work. "
            f"{total} questions ({n1} basic, {n2} intermediate, {nerr} error-codes, {n3} advanced). "
            "Every answer is complete sentences: a simple explanation, an interview answer, and a real-work example.",
            s["sub"],
        )
    )
    story.append(
        Paragraph(
            "How to use this book. Intern / fresher: Level 1 end-to-end, then ML + HTTP/SQL from Level 2. "
            "Mid: Level 2, plus the 25 industry questions at the start of Level 3. "
            "Senior / staff / principal: Level 3, and be ready to drop to a Level 1 SQL index or Git force-push "
            "if they probe fundamentals. Speak only known metrics: $2M indoor-nav beacon savings, sub-100ms edge "
            "inference, sub-5% trading drawdown, 70% ANR reduction, 30% app performance, 500K users / 40% faster backends. "
            "TAN Intelligence is an independent venture, not a second employer.",
            s["body"],
        )
    )
    story.append(Paragraph("How this book is structured", s["h"]))
    story.append(
        Paragraph(
            f"<b>Level 1 — Basic ({n1} questions).</b> Fresher fundamentals first: Python, OOP, data structures and Big-O, "
            "HTTP/REST/JSON/JWT, SQL, Git, Linux, Java/Kotlin/Android/Flutter, tests, CI, and config. "
            "If you cannot explain a LEFT JOIN or a decorator, do not skip ahead.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            f"<b>Level 2 — Intermediate ({n2} questions).</b> Core ML, computer vision and spatial AI, FastAPI/Spring Boot "
            "backends, mobile production (ANR, coroutines, Flutter), LLM/RAG/agents intro, trading hygiene, and cloud. "
            "This is the mid-level IC loop: ship a model, an API, and a client without pretending to be a research lab.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            f"<b>Error codes ({nerr} questions).</b> HTTP 400/401/403/404/409/422/429/500/502/503/504, OpenAI and Anthropic "
            "codes such as insufficient_quota, context_length_exceeded, rate_limit, content_filter, model_not_found, and "
            "timeout, plus 422 validation, vector-DB failures, GPU OOM, and tokenizer mismatch. Full-sentence meaning and "
            "what you would actually do.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            f"<b>Level 3 — Advanced ({n3} questions).</b> The 25 most-asked industry questions first, then RAG at scale, "
            "agents/tools/memory, evals/safety/MLOps, serving (vLLM, KV cache, LoRA, SSE), system design, and leadership "
            "stories from ezyCart, indoor navigation, and TAN. Production GenAI, not a notebook.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "Identity. This bank is for Vijay Baskar (LinkedIn vb1707). Do not mix with the Arjun Dev profile. "
            "Examples use Retailetics work (ezyCart, Lisa, vision/SLAM, ONNX/TF Lite) and Colan mobile/backend history. "
            "If you did not measure it, do not invent a dollar figure.",
            s["note"],
        )
    )

    story.append(PageBreak())
    story.append(Paragraph("Level 1 — Basic (fresher fundamentals)", s["h"]))
    story.append(
        Paragraph(
            "Python, OOP, data structures, HTTP, SQL, Git, Linux, Java/Kotlin/Flutter, tests and CI. "
            "Answer in two layers: a sentence a new grad would say, then the interview version.",
            s["note"],
        )
    )
    n = add_questions(story, L1, 0, s)

    story.append(PageBreak())
    story.append(Paragraph("Level 2 — Intermediate (core ML, CV, backend, mobile)", s["h"]))
    story.append(
        Paragraph(
            "Machine learning, computer vision, APIs, mobile production, LLM/RAG intro, trading, cloud. "
            "Connect every answer to a system you would actually ship.",
            s["note"],
        )
    )
    n = add_questions(story, L2, n, s)

    story.append(PageBreak())
    story.append(Paragraph("Error codes — HTTP, LLM, RAG, and serving", s["h"]))
    story.append(
        Paragraph(
            "Meanings in full sentences, then the interview action: retry, fail closed, fallback, or page. "
            "Checkout scanning does not share fate with chat GPUs.",
            s["note"],
        )
    )
    n = add_questions(story, LERR, n, s)

    story.append(PageBreak())
    story.append(Paragraph("Level 3 — Advanced (GenAI, agents, RAG, MLOps, production)", s["h"]))
    story.append(
        Paragraph(
            "Starts with the 25 industry questions (RAG, cost, agents, eval/safety, serving, production). "
            "Then senior RAG, agents, evals, serving, whiteboard design, and resume probes.",
            s["note"],
        )
    )
    n = add_questions(story, L3, n, s)

    if n != total:
        raise SystemExit(f"numbering mismatch: emitted {n}, expected {total}")

    story.append(Spacer(1, 10))
    story.append(
        Paragraph(
            f"End of bank — {total} questions. Rehearse out loud. If an example is not yours, skip it.",
            s["note"],
        )
    )

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"Wrote {OUT}  questions={total}  bytes={OUT.stat().st_size}")


if __name__ == "__main__":
    main()
