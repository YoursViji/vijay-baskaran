export const profile = {
  name: "Vijay Baskar",
  headline: "Principal AI Engineer | Lead GenAI & Agentic Systems Architect",
  kicker: "Generative AI · Agentic systems · Edge vision",
  summary:
    "Principal AI & Systems Engineer with 13+ years architecting production Generative AI, real-time computer vision, agentic pipelines, and scalable enterprise platforms.",
  location: "Federal Territory of Kuala Lumpur, Malaysia",
  email: "yoursvijii@gmail.com",
  phone: "+60 1151135376",
  phones: [{ display: "+60 1151135376", href: "tel:+601151135376" }],
  company: {
    name: "Retailetics",
    legalName: "Retailetics SDN BHD",
    href: "https://retailetics.com",
  },
  resumeHref: `${process.env.NEXT_PUBLIC_BASE_PATH ?? ""}/VB_Resume.pdf`,
  resumeLabel: "VB_Resume.pdf",
  github: {
    href: "https://github.com/YoursViji/vijay-baskaran",
    label: "github.com/YoursViji/vijay-baskaran",
  },
  linkedin: {
    href: "https://www.linkedin.com/in/vb1707/",
    label: "linkedin.com/in/vb1707",
  },
} as const;

export const bring = [
  {
    title: "Agentic",
    copy: "Multi-agent orchestration with LangGraph, CrewAI, AutoGen, MCP, ReAct, and LLM routing with fallbacks, rate limits, and token budgeting.",
  },
  {
    title: "RAG",
    copy: "Advanced RAG: hybrid BM25 search, multi-query, cross-encoder rerank, and vector stores (Pinecone, Qdrant, Milvus, Weaviate, pgvector, FAISS).",
  },
  {
    title: "CV / Edge",
    copy: "Production vision and SLAM — YOLO v8/v10/v11, RT-DETR, Kimera-VIO, OpenCV — plus ONNX / TensorRT / TF Lite inference under 100ms on-device.",
  },
  {
    title: "Quant / ML",
    copy: "Time-series and deep-learning models for custom trading indicators, plus PyTorch, JAX, TensorFlow, XGBoost, LoRA/PEFT, and evals.",
  },
  {
    title: "Infra",
    copy: "FastAPI, Pydantic, Celery, Node.js, Spring Boot, WebSockets, AWS Bedrock / SageMaker, GCP Vertex AI, Databricks, Docker, and CI/CD for ML.",
  },
] as const;

export const experience = [
  {
    company: "Retailetics SDN BHD",
    title: "Principal AI Engineer | Lead GenAI & Agentic Systems Architect",
    location: "Kuala Lumpur, Malaysia",
    dates: "March 2023 – Present",
    href: "https://retailetics.com",
    summary:
      "Lead GenAI, agentic systems, and computer vision for Retailetics’ in-store stack — self-checkout, RAG assistants, and sub-100ms edge inference.",
    bullets: [
      "Architected agentic and computer-vision self-checkout (ezyCart) with RT-DETR, YOLO, and Kimera-VIO; ML indoor navigation saved over $2M by replacing thousands of Bluetooth beacons.",
      "Shipped a GenAI/RAG shopping assistant and AI recipe generation with LangChain and LlamaIndex — cuisine suggestions, cooking video, and missing-item add-to-cart.",
      "Built FastAPI and Spring Boot WebSocket IoT pipelines between devices and the ezyCart Android app for real-time sync.",
      "Deployed ONNX and TensorFlow Lite on-device models with sub-100ms edge inference for checkout vision and on-cart assist.",
    ],
  },
  {
    company: "Retailetics SDN BHD",
    title: "Senior Staff Software Engineer",
    location: "Kuala Lumpur, Malaysia",
    dates: "February 2021 – March 2023",
    href: "https://retailetics.com",
    summary:
      "Led software for ezyCart, kiosks, wayfinding, staff tools, and shopper apps so people skip the queue and stores still see the aisle.",
    bullets: [
      "Spearheaded the AI-infused self-checkout smart trolley (ezyCart): architecture, stakeholder design, and a real-time socket pipeline between IoT devices and the ezyCart Android app.",
      "Shipped the self-checkout kiosk on the same stack — scan, bag on the trays, and pay without a cashier line; integrated Tap to Pay and NFC.",
      "Delivered ML-based indoor navigation and product finder; ran A/B and split testing across merchants.",
      "Built a Flutter support-staff app, Android TV cart monitor, Flutter SDK lite, ezyList, stock audit, Voice Assist, and Lisa AI shopping assistant.",
    ],
  },
  {
    company: "Colan Infotech",
    title: "Senior Software Engineer",
    location: "Chennai, India",
    dates: "November 2012 – February 2021",
    href: null,
    summary:
      "Shipped 20+ Android, iOS, and Flutter apps plus the backends and ML prototypes they talk to.",
    bullets: [
      "Delivered 20+ production mobile apps (Android/iOS): native Kotlin/Java and Flutter, with MVVM, Jetpack Compose, and CI/CD (Jenkins, GitLab, Bitrise); reduced ANR crashes by 70% and lifted app performance by 30%.",
      "Architected scalable backends using Spring Boot, AWS, Firebase, and REST APIs — microservices for 500K+ users with 40% faster response time.",
      "Built Python prototypes with TensorFlow, PyTorch, and Scikit-learn for on-device and backend ML experiments.",
    ],
  },
] as const;

export const workGroups = [
  {
    title: "AI systems",
    intro:
      "Agentic pipelines, RAG, computer vision / SLAM, and on-device inference from production retail work.",
    items: [
      {
        slug: "agentic",
        title: "Agentic orchestration",
        image: "/work/ai-agentic-orchestration.jpg",
        tag: "LangGraph · MCP",
        copy: "Multi-agent graphs that plan, call tools, and fall back under rate limits — the same agentic pattern behind Lisa, voice assist, and in-aisle recipe flows.",
      },
      {
        slug: "rag",
        title: "RAG retrieval",
        image: "/work/ai-rag-retrieval.jpg",
        tag: "LangChain · LlamaIndex",
        copy: "Hybrid search and rerank over product facts, promos, and recipes so the shopping assistant answers from store data instead of guessing.",
      },
      {
        slug: "vision-slam",
        title: "Vision & SLAM",
        image: "/work/ai-vision-slam.jpg",
        tag: "YOLO · RT-DETR · Kimera-VIO",
        copy: "Real-time detection and visual odometry on the cart: find the SKU, walk the path, and skip the beacon grid that used to cost millions.",
      },
      {
        slug: "edge",
        title: "Edge inference",
        image: "/work/ai-edge-inference.jpg",
        tag: "ONNX · TF Lite",
        copy: "Quantized models on kiosk and cart hardware with sub-100ms inference — checkout vision that does not wait on a round-trip.",
      },
    ],
  },
  {
    title: "In the store",
    intro:
      "ezyCart, kiosks, recipes, payments, wayfinding, and Lisa — Retailetics product work.",
    items: [
      {
        slug: "smart-trolley",
        title: "ezyCart smart trolley",
        image: "/work/smart-trolley.png",
        tag: "AI self-checkout",
        copy: "Retailetics’ AI-infused self-checkout cart. Architecture, UX, and a live socket pipeline from IoT hardware into the ezyCart Android app.",
      },
      {
        slug: "self-checkout-kiosk",
        title: "Self-checkout kiosk",
        image: "/work/self-checkout-kiosk-hero.png",
        tag: "Station checkout",
        copy: "The same scan-bag-pay flow on a fixed kiosk so shoppers who are not on a cart still leave without a cashier line.",
      },
      {
        slug: "ai-recipe",
        title: "AI recipe builder",
        image: "/work/ai-recipe-builder.png",
        tag: "GenAI · RAG",
        copy: "As products land in the cart, AI builds recipes from the basket, plays the cooking video, and flags missing items.",
      },
      {
        slug: "lisa-ai",
        title: "Lisa AI shopping assistant",
        image: "/work/lisa-ai-assistant.png",
        tag: "RAG assistant",
        copy: "Lisa answers shopper questions and surfaces live product recommendations and promotions between the shelves.",
      },
      {
        slug: "payments",
        title: "Tap to Pay & NFC",
        image: "/work/tap-nfc-payments.png",
        tag: "Payments",
        copy: "Multiple payment gateways on cart and kiosk — Tap to Pay, NFC, and the usual card and QR rails — so checkout is not stuck on one acquirer.",
      },
      {
        slug: "product-finder",
        title: "Product finder",
        image: "/work/product-finder.png",
        tag: "Search · navigate",
        copy: "Search a product and walk the path to the shelf. Indoor navigation that replaced thousands of beacons and saved over $2M.",
      },
    ],
  },
  {
    title: "Merchant and shopper apps",
    intro:
      "A lite SDK for small vendors, a list app for households, and floor tools for staff.",
    items: [
      {
        slug: "flutter-sdk",
        title: "ezyCart Flutter SDK (lite)",
        image: "/work/ezycart-flutter-sdk.png",
        tag: "Phone · tablet",
        copy: "A Flutter SDK lite of ezyCart so small vendors can integrate scan-and-pay into their own mobile apps — phone and tablet.",
      },
      {
        slug: "ezylist",
        title: "ezyList",
        image: "/work/ezylist-app.png",
        tag: "Shopping list",
        copy: "Build a list, share it with friends and family so everyone can update it, find nearby stores with price and availability, navigate there, purchase in one scan, get the receipt, and unlock member promos.",
      },
      {
        slug: "staff-monitor",
        title: "Staff app & cart monitor",
        image: "/work/staff-app-tv-monitor.png",
        tag: "Flutter · Android TV",
        copy: "Cross-platform Flutter app for support staff, with an Android TV view of live carts so the floor can help without walking the whole store.",
      },
    ],
  },
] as const;

export const skillGroups = [
  {
    title: "Generative AI & Agentic",
    items: [
      "LangGraph",
      "CrewAI",
      "AutoGen",
      "LangChain",
      "LlamaIndex",
      "LangSmith",
      "Langflow",
      "MCP",
      "Multi-Agent Orchestration",
      "ReAct",
      "LLM abstraction (routing, fallbacks, rate limits, token budgeting)",
      "n8n",
    ],
  },
  {
    title: "LLMs",
    items: [
      "GPT-4o",
      "Claude",
      "Gemini",
      "Llama 3 / Mistral",
      "FinGPT",
      "Ollama",
      "vLLM",
      "Prompt Engineering",
      "Evals",
      "LoRA / PEFT",
      "Hugging Face Transformers",
    ],
  },
  {
    title: "RAG",
    items: [
      "Advanced RAG",
      "Hybrid Search BM25",
      "Multi-query",
      "Cross-encoder rerank",
      "Pinecone",
      "Qdrant",
      "Milvus",
      "Weaviate",
      "pgvector",
      "FAISS",
      "Supabase",
    ],
  },
  {
    title: "CV / SLAM",
    items: [
      "YOLO v8/v10/v11",
      "RT-DETR",
      "Kimera-VIO",
      "OpenCV",
      "OCR",
      "Detection / segmentation",
    ],
  },
  {
    title: "DL / ML",
    items: [
      "PyTorch",
      "JAX",
      "TensorFlow",
      "Scikit-learn",
      "XGBoost",
      "NumPy",
      "Pandas",
      "Time-series",
      "ONNX",
      "TensorRT",
      "TF Lite",
    ],
  },
  {
    title: "Backend",
    items: [
      "Python",
      "FastAPI",
      "Pydantic",
      "Celery",
      "Node.js",
      "Spring Boot",
      "REST",
      "GraphQL",
      "WebSockets",
    ],
  },
  {
    title: "MLOps",
    items: [
      "AWS Bedrock",
      "SageMaker",
      "GCP Vertex AI",
      "Databricks",
      "Langfuse",
      "Docker",
      "CI/CD for ML",
    ],
  },
  {
    title: "Mobile (supporting)",
    items: [
      "Kotlin",
      "Java",
      "Jetpack Compose",
      "Flutter",
      "Android",
      "iOS",
    ],
  },
] as const;

export const education = {
  degree: "Bachelor of Engineering in Computer Science and Engineering",
  school: "Anna University Chennai",
} as const;

export const certifications = [
  {
    name: "Mobile iOS & Android development",
    issuer: "Target Software, Chennai",
  },
  {
    name: "SOLID Principles",
    issuer: "Coursera",
  },
  {
    name: "AI/ML Architecture",
    issuer: "IBM",
  },
  {
    name: "Master prompting",
    issuer: "Claude and Coursera",
  },
] as const;

export const tanIntelligence = {
  company: "TAN Intelligence",
  role: "Founder",
  tag: "Independent venture",
  title: "Custom trading indicators",
  image: "/work/tan-intelligence.png",
  intro:
    "Proprietary custom trading indicators across commodities, FX, and crypto.",
  summary:
    "End-to-End Quantitative Systems: Engineered and deployed proprietary algorithmic trading models and custom indicators across Commodities, FX, and Crypto, operating systematically for over 6 years.",
  body: [
    "Automated Architecture & Telegram Pipelines: Built custom 5-minute and 15-minute signal engine pipelines integrated with Telegram alerts and low-latency automated execution AI-bots via REST and WebSockets.",
    "Strategy & Market Structure: Developed rule-based frameworks applying Smart Money Concepts (SMC), liquidity sweeps, and dynamic position-sizing protocols to optimize risk-adjusted returns.",
    "Execution & Backtesting Rigor: Automated multi-broker execution (TradingView, MetaTrader) using Python and Pine Script; backtested and forward-tested strategies to maintain a sub-5% maximum drawdown limit.",
    "Top Skills: Quantitative Finance • Algorithmic Trading • Python • Pine Script • Automated Execution • API Integration (WebSockets/REST) • Risk Management",
  ],
} as const;

export const goals = {
  shortTerm: {
    title: "Deepening production GenAI, agents, and MLOps",
    ai: "Take the agentic, RAG, and vision systems already in the store stack further: tool-calling graphs, evals, retrieval quality, and MLOps so an experiment becomes a service.",
    ml: "On Machine Learning, the work stays practical: train, evaluate, quantize, and serve — including on-device paths that do not wait on a round-trip.",
  },
  longTerm: {
    title: "Building a profitable AI/ML trading indicator and bot system",
    copy: "The research-to-product path is sequential: an original indicator, a signal layer that is honest about confidence, then a bot that can execute with hard risk limits. Profit is the product goal. It is not a track record.",
  },
} as const;

export const nav = [
  { href: "#experience", label: "Experience" },
  { href: "#work", label: "Work" },
  { href: "#tan", label: "TAN" },
  { href: "#goals", label: "Goals" },
  { href: "#skills", label: "Skills" },
  { href: "#education", label: "Education" },
  { href: "#contact", label: "Contact" },
] as const;
