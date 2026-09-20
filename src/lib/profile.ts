export const profile = {
  name: "Vijay Baskaran",
  headline:
    "Head of Software Technologies @ Retailetics | AI/ML Developer | Mobile Systems & Scaled Engineering",
  location: "Federal Territory of Kuala Lumpur, Malaysia",
  email: "yoursvijii@gmail.com",
  phones: [{ display: "+60 1151135376", href: "tel:+601151135376" }],
  company: {
    name: "Retailetics",
    legalName: "Retailetics SDN BHD",
    href: "https://retailetics.com",
  },
} as const;

export const experience = [
  {
    company: "Retailetics SDN BHD",
    title: "Head of Software Technologies",
    location: "Kuala Lumpur, Malaysia",
    dates: "February 2021 – Present",
    href: "https://retailetics.com",
    summary:
      "I lead software for Retailetics’ in-store stack — ezyCart, self-checkout kiosks, wayfinding, payments, staff tools, and shopper apps — so people skip the queue and stores still see what happens between the aisles.",
    bullets: [
    "Spearheaded Retailetics’ AI-infused self-checkout smart trolley (ezyCart): architecture, stakeholder design, and a real-time socket pipeline between IoT devices and the ezyCart Android app.",
    "Shipped the self-checkout kiosk on the same stack — scan, bag on the trays, and pay without a cashier line.",
    "Built an AI recipe system on ezyCart: as items go in, the cart suggests recipes by cuisine, plays the cooking video, and lets shoppers add missing products to the basket.",
    "Integrated multiple payment gateways, including Tap to Pay and NFC, so checkout works on cart and kiosk.",
    "Product finder: search a SKU and navigate to its location in the aisle.",
    "In-aisle upselling and cross-selling through ads in the same cart system.",
    "Stock auditing on the smart cart so the floor can count, scan, and flag gaps without a separate handheld round.",
    "Voice Assist AI for customer queries, product facts, and promo info — hands-free help on the cart, in the same spirit as a phone assistant.",
    "Monitoring and troubleshooting for every active cart and self-checkout station.",
    "Delivered an AI-powered indoor navigation system that saved over $2M by removing thousands of Bluetooth beacons.",
    "Flutter support-staff app and Android TV cart monitor, plus a Flutter SDK lite of ezyCart so small vendors can embed scan-and-pay in their own phone and tablet apps.",
    "ezyList: shared shopping lists with friends and family, nearby stores with price and availability, navigate to the store, purchase in one scan, digital receipt, and member-only promos.",
    "Lisa AI shopping assistant, machine-learning models across the line, automated merchant deploys, and split testing.",
    ],
  },
  {
    company: "Colan Infotech",
    title: "Senior Software Engineer",
    location: "Chennai",
    dates: null,
    href: null,
    summary:
      "Senior Software Engineer in Chennai, shipping Android, iOS, and Flutter apps plus the backends they talk to.",
    bullets: [
      "Built and shipped 20+ Android/iOS and Flutter apps.",
      "Worked native Kotlin/Java and Flutter across those products.",
      "Set up CI/CD with Jenkins, GitLab, and Bitrise.",
      "Built mobile backends on AWS, Firebase, and REST.",
    ],
  },
] as const;

export const workGroups = [
  {
    title: "In the store",
    intro:
      "ezyCart, kiosks, recipes, payments, wayfinding, ads, audit, voice, and fleet ops — Retailetics product work.",
    items: [
      {
        slug: "smart-trolley",
        title: "ezyCart smart trolley",
        image: "/work/smart-trolley.png",
        tag: "AI self-checkout",
        copy: "Retailetics’ AI-infused self-checkout cart. Architecture, UX, and a live socket pipeline from IoT hardware into the ezyCart Android app — scan, pay, and skip the queue.",
      },
      {
        slug: "self-checkout-kiosk",
        title: "Self-checkout kiosk",
        image: "/work/self-checkout-kiosk-hero.png",
        tag: "Station checkout",
        copy: "The same scan-bag-pay flow on a fixed kiosk: trays, scale, and screen so shoppers who are not on a cart still leave without a cashier line.",
      },
      {
        slug: "ai-recipe",
        title: "AI recipe builder",
        image: "/work/ai-recipe-builder.png",
        tag: "ezyCart",
        copy: "As products land in the cart, AI builds recipes from the basket, lists cuisines, plays the cooking video, and flags missing items so they can go straight into the cart.",
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
      {
        slug: "upsell-ads",
        title: "Upsell & cross-sell ads",
        image: "/work/upsell-cross-sell-ads.png",
        tag: "In-aisle media",
        copy: "The same cart system runs ads that upsell and cross-sell against what is already in the basket — while the shopper is still in the aisle.",
      },
      {
        slug: "stock-audit",
        title: "Stock auditing",
        image: "/work/stock-auditing.png",
        tag: "Smart cart",
        copy: "Use the smart cart as an audit tool: scan the shelf, count, and flag gaps without sending a separate device around the store.",
      },
      {
        slug: "voice-assist",
        title: "Voice Assist AI",
        image: "/work/voice-assist-ai.png",
        tag: "Hands-free",
        copy: "Voice assist for customer queries, product facts, and promo info — on-cart help in the same spirit as a phone assistant, without pulling out a phone.",
      },
      {
        slug: "fleet-monitor",
        title: "Cart & kiosk monitoring",
        image: "/work/fleet-monitoring.png",
        tag: "Ops",
        copy: "A monitoring system to watch and troubleshoot every active cart and self-checkout station from one place.",
      },
      {
        slug: "lisa-ai",
        title: "Lisa AI shopping assistant",
        image: "/work/lisa-ai-assistant.png",
        tag: "In-aisle AI",
        copy: "Lisa answers shopper questions and surfaces live product recommendations and promotions between the shelves.",
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
    title: "Mobile systems",
    items: [
      "Android",
      "Kotlin",
      "Java",
      "Jetpack Compose",
      "Flutter",
      "Dart",
      "Kotlin Multiplatform",
      "iOS",
    ],
  },
  {
    title: "Backend & scale",
    items: [
      "REST APIs",
      "GraphQL",
      "WebSockets",
      "Spring Boot",
      "Postgres",
      "SQLite",
      "Microservices",
    ],
  },
  {
    title: "AI / ML",
    items: [
      "TensorFlow",
      "PyTorch",
      "Keras",
      "OpenCV",
      "On-device ML",
      "NLP",
      "Model quantization",
    ],
  },
  {
    title: "In-store systems",
    items: [
      "ezyCart",
      "Self-checkout kiosk",
      "AI recipe builder",
      "NFC / Tap to Pay",
      "Product finder",
      "Voice assist",
      "Stock audit",
      "ezyList",
      "Flutter SDK lite",
    ],
  },
  {
    title: "Delivery",
    items: [
      "Jenkins",
      "Fastlane",
      "Docker",
      "Git",
      "CI/CD",
      "Split testing",
    ],
  },
  {
    title: "Engineering craft",
    items: [
      "SOLID",
      "Clean Architecture",
      "MVVM",
      "MVP",
      "BLoC",
      "Technical leadership",
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
  title: "AI-powered forex trading indicator",
  image: "/work/tan-intelligence.png",
  summary:
    "TAN Intelligence is my own company. I am building an original Artificial Intelligence trading indicator for the forex market — founder work, not a second employer on the timeline.",
  body: [
    "The product starts as an indicator: models that read FX structure and turn it into a clear, inspectable overlay a trader can actually use.",
    "The longer system direction is indicator, then signals, then an automated bot with explicit risk controls. That is the build path — not a live book, AUM, or performance claim.",
  ],
} as const;

export const goals = {
  shortTerm: {
    title: "Mastering Artificial Intelligence technologies and Machine Learning",
    ai: "I am taking the AI already in the store stack — vision, prompting, on-device inference — and going deeper on what is shipping now: agentic systems that plan and call tools, multimodal models that can read a chart with the surrounding text, edge ML that does not wait on a round-trip, retrieval-augmented generation for grounded research, and MLOps so an experiment can become a service.",
    ml: "On Machine Learning, the work is practical: train, evaluate, and productionize models — data, metrics, and the path into a real runtime, not a notebook that never leaves the laptop.",
  },
  longTerm: {
    title: "Building a profitable AI/ML trading indicator and bot system",
    copy: "The research-to-product path is sequential and forex-first: an original indicator, a signal layer that is honest about confidence, then a bot that can execute with hard risk limits. Profit is the product goal. It is not a track record.",
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
