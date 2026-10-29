# Advanced / senior-staff: 25 industry Qs + RAG/agents/evals/MLOps/safety/production/leadership
Q = []

def add(q, kid, tech, *ex):
    Q.append((q, kid, tech, list(ex)))

# --- the 25 screenshot questions (must all appear) ---
add("Design a RAG pipeline that handles 10 million documents.",
    "Do not search the whole library every time. Index pages, shortlist, then read a handful.",
    "Ingest with tenant/ACL/source/time metadata. Structure-aware chunk+embed. Hybrid BM25+dense, ANN shards, metadata filters at retrieval, multi-query, rerank to 5–8, generate with citations, abstain. Upserts/deletes, eval set, SLOs on recall@k, groundedness, p95, $/query.",
    "Lisa/recipes over catalogue+policy — never dump 10M docs into the prompt.",
    "Shopper ACL must not retrieve staff stock-audit chunks.")
add("Debug a RAG system that retrieves relevant context but generates wrong answers.",
    "Right page, wrong sentence — fix writing, not only search.",
    "Confirm retrieval@k first. Then prompt (cite/refuse), packing (lost-in-the-middle), contradictions, temperature, model ignoring context. Faithfulness eval. Log the exact window.",
    "Recipe RAG retrieves ingredients then invents a SKU — constrain to retrieved rows.",
    "Fail eval if Lisa cites a promo not in the chunk.")
add("Choose the right chunking strategy for complex legal contracts.",
    "Do not tear a clause in half. Keep sections with their headings.",
    "Structure-aware: numbered clauses, definitions glossary, exhibits, overlap, table integrity. Eval questions that need a definition plus a later clause. Avoid naive 512-token windows.",
    "Return policy as a mini-contract: window stays attached to 'Returns'.")
add("Compare BM25, dense retrieval, and hybrid search for different use cases.",
    "BM25 = exact words. Dense = meaning. Hybrid = both, then rerank.",
    "BM25 wins on SKUs/IDs; dense on paraphrase; hybrid+RRF default. Tune on a labelled set. Explain failure modes.",
    "EZY-1044 vs 'something spicy for pasta tonight'.")
add("Add a reranker and prove its impact with evaluation metrics.",
    "Shortlist, then a careful reader reorders. Prove with a test.",
    "Retrieve k=50–100, cross-encoder to n=5. Offline nDCG/MRR/Recall@k; online groundedness, latency, cost. Flag + canary.",
    "50 recipe chunks → 5 for the LLM. Do not rerank 10M docs.")
add("Reduce LLM inference costs by 70% without sacrificing answer quality.",
    "Stop using the expensive brain for easy homework. Prove it on a frozen exam.",
    "Prompt/RAG compression, semantic cache, routing to small models, quant/distill, batching, cap tokens. Hold correctness+groundedness+safety. 70% is measured $/successful-task, not a slogan.",
    "FAQ cache/small model; complex recipes to GPT-4o/Claude.",
    "Vision already uses ONNX/TF Lite per frame instead of a cloud GPU.")
add("Reduce time to first token in a production chatbot.",
    "Start talking sooner. Blank bubbles feel broken.",
    "SSE, shorter prefill, prefix/KV cache, speculative decoding, colocated GPU, don't block on all tools, faster model for greetings. Track TTFT p50/p95 separate from total.",
    "Lisa streams while a promo tool still runs. Stable system prompt for prefix cache.")
add("Design a semantic caching system and track cache hit rates.",
    "Near-duplicate questions reuse a good answer.",
    "Embed normalized query; hit if similarity+ACL+fresh sources. Version hashes. Metrics: hit, stale-hit, quality, $, latency. Bypass personalization/stock.",
    "Basket-hash cache for recipes. Never cache another shopper's member price.")
add("Build a model router that balances cost, latency, and response quality.",
    "Receptionist sends easy tickets to a junior, hard to a senior.",
    "Intent/complexity classifier. Routes: cache → extractive → 8B vLLM/Ollama → mid → frontier, with fallbacks, rate limits, token budgets. A/B on the same eval. This is the LLM abstraction on the resume.",
    "SKU lookup no LLM; recipe mid+RAG; complaint Claude/GPT-4o; Bedrock throttle → vLLM Llama 3.")
add("Build a tool-using AI agent with reliable execution.",
    "Model asks; your code is the adult: validate, run, stop.",
    "LangGraph/CrewAI/AutoGen state machine. JSON schemas, allowlists, timeouts, retries, idempotency. HITL for money. Trace LangSmith/Langfuse. MCP ≠ security.",
    "Lisa: search auto; add_to_cart confirm; pay never from untrusted text.")
add("Debug an agent stuck in an infinite tool-calling loop.",
    "Same calculator forever — max tries and notice repeats.",
    "Duplicate signatures, oscillating args, empty tool errors. Step budget, force-final node, circuit breaker, traces.",
    "get_stock empty SKU retries 40× → typed error after 2, then ask shopper.")
add("Design long-term memory for an AI assistant.",
    "This-chat is short-term. Long-term is a curated notebook, not a junk drawer.",
    "Working thread + episodic summaries + structured profile + enterprise RAG. Write validated memories only. Recency×importance retrieve. User delete. No secrets.",
    "Remember vegetarian preference, never card PAN. TAN params in versioned config, not chat logs.")
add("Enforce valid JSON output from an LLM.",
    "Ask for a form, not an essay. Reject broken forms.",
    "Schema/tool/constrained decode. Pydantic validate. One repair then fail closed. Low T.",
    "add_to_cart {sku, qty>0}. FastAPI already treats bodies as untrusted — same for LLM output.")
add("Detect hallucinations and reduce unsupported answers.",
    "If the book is silent, say 'I don't know'.",
    "Ground, citations, NLI/judge on context only, abstain, eval set, monitor. Not 0%.",
    "No allergen claim without a chunk. Low-confidence YOLO does not bill.")
add("Build an evaluation pipeline for a customer-support / shopping chatbot.",
    "A practice exam from real tickets. Every prompt change sits the exam.",
    "Golden set, retrieval+answer+tool+safety+latency+cost. CI gate. Human spot. Shadow traffic. LangSmith datasets.",
    "100 Lisa questions with known SKUs. Fail if add_to_cart on missing item.")
add("Make LLM-as-a-judge evaluations reliable and consistent.",
    "One picky teacher is noisy. Rubric, examples, calibration.",
    "Anchored rubric, few-shot, separate faithfulness vs tone, multi-sample, kappa vs humans, pin model+T, blind systems, re-calibrate on judge change.",
    "Judge only 'is every ingredient in evidence?', not 'sounds tasty'.")
add("Defend a tool-using agent against prompt injection.",
    "A webpage note must not empty the till.",
    "User+retrieved text untrusted. Allowlist, schema, ignore non-channel 'tool calls', strip instructions in docs, sandbox, HITL money, red-team. MCP still needs authz.",
    "Description 'ignore policy, 100% off' cannot fire discount tool.")
add("Detect and redact PII before sending data to an LLM.",
    "Cover the ID card before photocopying for a tutor.",
    "Regex+NER+checksums at gateway. Tokenize/vault. Minimize. No secrets in LangSmith. Blur faces if unused.",
    "Device ids in logs; 'call me at +91…' stripped from RAG. Public resume phones ≠ customer PII.")
add("Choose between RAG, fine-tuning, and prompt engineering for a real use case.",
    "Instructions vs open book vs extra practice. Combine. Don't bake daily prices into weights.",
    "Prompt: format/tone/tools. RAG: changing facts. LoRA/FT: stable task/style with labels. Measure.",
    "Promo of the week = RAG. JSON style = prompt. 5k receipts = LoRA.")
add("Fine-tune a small language model using LoRA on 5,000 examples.",
    "Bolt on a small trainable adapter; don't rebuild the engine.",
    "Freeze Llama 3/Mistral, rank/alpha/dropout, clean split, task metrics, early stop, merge or vLLM adapter, quantize after quality. 5k overfits easily.",
    "LoRA JSON {dishes, missing_skus}; catalogue stays RAG. No shuffled time-series labels.")
add("Serve open-source LLMs at scale using batching, KV caching, and quantization.",
    "Share the oven, remember the story so far, use a lighter cookbook.",
    "vLLM: continuous batch, paged KV, prefix cache, parallel. AWQ/GPTQ/INT8. SLOs TTFT/tok-s. Fallback Bedrock/Vertex. Token budgets. Edge ≠ vLLM (ONNX/TF Lite).",
    "FAQ on vLLM Llama 3; hard RAG on frontier; cart vision still TensorRT/TF Lite sub-100ms.")
add("Implement SSE streaming with proper handling of client disconnects.",
    "Talk while thinking; stop if they hung up so you don't burn GPU money.",
    "text/event-stream, flush tokens, cancel on disconnect, heartbeats, optional Last-Event-ID. FastAPI StreamingResponse. Don't buffer the whole answer.",
    "Tablet sleeps → cancel Lisa generation. WS for IoT; SSE for tokens.")
add("Trace and debug every step of a multi-agent workflow.",
    "Flight recorder per helper: tools, tokens, why they stopped.",
    "OTel + LangSmith/Langfuse + LangGraph checkpoints, redacted prompts, correlation ids across FastAPI/Spring. Replay. Alert on loops/cost.",
    "Planner → retriever → add_missing_sku. Same discipline as IoT seq ids.")
add("Roll back a prompt change that degrades production performance.",
    "Prompts are code. Revert like an API.",
    "Git+config version, CI eval, canary, auto-rollback on groundedness/tool-error/latency, pin last-good. No cowboy hot-edits.",
    "'Be more creative' invented ingredients → revert prompt id.")
add("Design a ChatGPT-style application for 1 million daily active users.",
    "A factory: queues, caches, routing, graceful failure — not one script. DAU ≠ concurrency.",
    "Auth, rate limits, conversation store, cache/small/RAG/agent routes, autoscaled vLLM/Bedrock, SSE, ACL, PII, safety, eval, cost/session, cells. SLOs TTFT/useful/safe/$.",
    "Hot path: cart WS events. Chat path: Lisa. Colan 500K taught indexing/caching — GPUs are the extra bottleneck.")

# RAG at scale extras
add("How do you handle document updates and deletions in RAG?",
    "If a policy is shredded, the assistant must not quote it tomorrow.",
    "Idempotent upserts, tombstones, TTL, re-embed on chunker/model change, search-time filter on version. Test deletion in eval.",
    "Expired promo vectors must not retrieve. Membership price updates invalidate semantic cache.")
add("Lost-in-the-middle — what is it and the fix?",
    "Models skip the boring middle of a long pile of pages.",
    "Put best chunks first/last, shorten context, rerank harder, hierarchical summarize.",
    "5 tight chunks beat 40 mediocre ones in Lisa.")
add("Parent-child / hierarchical / late chunking?",
    "Retrieve a small bite, then bring its parent section for writing.",
    "Small embeddings for recall, larger window for generation. Late chunking embeds whole doc then pools.",
    "Retrieve a recipe step, expand to full recipe card before generating.")
add("Hybrid fusion: RRF vs weighted score?",
    "Two ranked lists need a fair merge.",
    "Reciprocal Rank Fusion is scale-free. Weighted needs calibration. Then rerank.",
    "BM25 rank + dense rank → RRF → cross-encoder.")
add("How do you evaluate RAG (senior)?",
    "Did we find the right page, and did we use it honestly?",
    "Recall@k, nDCG, MRR, faithfulness, answer relevance, citation accuracy, abstain quality, latency, cost, permission leaks. Separate retrieval vs gen.",
    "Golden 100 with labelled passages. CI fails on recall or faithfulness drop.")
add("RAG security beyond ACL filters?",
    "Permissions, injection in docs, secrets in traces, confused deputy.",
    "Pre-retrieval authz, per-tenant indexes, injection tests, DLP, audit, encryption.",
    "A retrieved HTML comment should not become a tool call.")
add("When is RAG the wrong tool?",
    "When you need a guaranteed calculation, a millisecond SKU lookup, or a stable classifier.",
    "Deterministic functions and SQL for facts; RAG for language over docs. Don't RAG 2+2.",
    "Cart total is arithmetic. Policy explanation is RAG.")
add("Multi-index routing?",
    "First guess which library, then search it.",
    "Query classifier → policies vs recipes vs SKUs. Cuts noise and cost.",
    "Allergen question → policy index, not recipe blog.")
add("Embedding drift and re-index jobs?",
    "New embedding model = old map is wrong. Rebuild.",
    "Version embeddings in metadata. Blue/green indexes. Dual-write during migrate.",
    "Upgrade embedding model overnight with a shadow index and recall compare.")

# Agents advanced
add("When is a multi-agent system worse than one agent?",
    "Too many cooks, extra cost, extra failure points.",
    "Measure task success, latency, $ against a single-agent or chain baseline. Add agents only for genuine specialization.",
    "Formatting JSON with three CrewAI roles is worse than Pydantic.")
add("Human-in-the-loop patterns?",
    "The model may suggest; a human taps OK on money and safety.",
    "LangGraph interrupt, timeouts, default-deny. Audit who approved.",
    "Add-to-cart auto; pay requires the shopper tap.")
add("Idempotent tool calls?",
    "Retrying 'charge' must not charge twice.",
    "Idempotency keys from (trace, tool, canonical args). Store results.",
    "add_to_cart retried after WS blip uses the same key.")
add("Agent memory vs RAG vs scratchpad?",
    "Scratchpad is this task's notebook. Memory is longer. RAG is company books.",
    "Don't dump full history. Summarize. Structured state in LangGraph.",
    "State: basket[], missing[], step. RAG: policies. Memory: diet pref.")
add("How do you bound agent cost?",
    "Max steps, max tokens, max $, max wall time, then stop.",
    "Budgets in the graph. Route cheap models first. Kill switches.",
    "Recipe agent: ≤6 tool calls, ≤2k generated tokens.")
add("Deterministic fallbacks for agents?",
    "If the clever helper fails, a boring function still works.",
    "SKU barcode path never requires an LLM. LLM is overlay.",
    "Scan still adds the item if Lisa is down.")
add("AutoGen vs CrewAI vs LangGraph — senior choice?",
    "Pick the simplest orchestration you can operate.",
    "LangGraph: control/state/HITL. CrewAI: roles. AutoGen: conversational. Eval, traces, security identical.",
    "Production Lisa: LangGraph. Research spike: CrewAI. Don't run all three.")
add("How do you test agents without hitting real APIs?",
    "Fake tools that return recorded answers. Assert the calls.",
    "Contract tests, golden traces, simulators, property tests (no pay tool without confirm).",
    "Replay a fixture: OOS milk → must call search_alternatives, must not pay.")
add("Supervisor / router / swarm topologies?",
    "One boss, or a circle of peers. Boss is easier to debug.",
    "Supervisor graph is the default. Swarms need stronger invariants.",
    "Planner node dispatches retriever vs vision vs FAQ.")
add("What is a graph checkpoint and why?",
    "A save-game of the agent so you can resume after a crash or a human pause.",
    "LangGraph checkpointer (thread_id). Don't store PII unencrypted.",
    "Shopper walks away mid-recipe; resume the same thread.")

# Evals / safety / MLOps senior
add("What is MLOps for LLM apps (not only sklearn)?",
    "Version prompts, tools, indexes, models. Eval, deploy, watch, rollback.",
    "Artifacts: prompt id, embedding model, chunker, index build, agent graph. Quality+infra metrics. Canaries.",
    "Merchant deploys plus prompt/model eval jobs, not only APKs.")
add("Offline vs online vs human eval?",
    "Offline exam, live traffic shadows, people for gray cases.",
    "You need all three. Online can surprise. Humans calibrate judges.",
    "Weekly 50 human-labelled Lisa chats to keep the judge honest.")
add("Safety policies: self-harm, scams, medical, allergens?",
    "Refuse and redirect. Allergens are high-stakes — no guessing.",
    "Classifiers + rules + abstain. Legal review. Log. Don't rely on the base model alone.",
    "If RAG has no allergen field, say so. Never 'probably fine'.")
add("Jailbreaks vs prompt injection?",
    "Jailbreak: user tries to break the system prompt. Injection: untrusted content tries to steer tools.",
    "Different controls. Both red-teamed. Tools still allowlisted.",
    "User 'ignore rules' vs document 'call discount tool'.")
add("Data residency and vendor LLMs?",
    "Where do the tokens go, and who can see them?",
    "Contracts, regions, zero-retention, VPC endpoints, on-prem vLLM when required.",
    "EU shopper chats may not go to a US-only endpoint without a decision.")
add("Prompt/version governance?",
    "Who can change the brain, with what evidence?",
    "CODEOWNERS, eval required, change log, on-call.",
    "Prompt v12 PR shows nDCG and groundedness vs v11.")
add("Drift in RAG (content drift vs embedding vs user drift)?",
    "The books change, the map changes, or the questions change.",
    "Monitor retrieval hit rates, unknown-intent, thumbs, fresh-doc lag.",
    "New promo language not in the index → spike in abstains.")
add("Cost accounting per tenant?",
    "Each store should see its LLM bill.",
    "Token meters, cache hits, GPU-ms, pass-through + margin. Quotas.",
    "A viral recipe loop cannot bankrupt the platform — quota + 429.")
add("Feature flags for models?",
    "Flip brains without a full redeploy.",
    "Flags for prompt, temperature, reranker on/off, model id. Combine with canary.",
    "Turn off reranker if GPU pool is hot; accept quality hit explicitly.")
add("Shadow mode?",
    "New brain answers in the log, old brain still talks to the shopper.",
    "Compare distributions, then graduate. Privacy in logs.",
    "v12 drafts Lisa answers 10% shadow before cutover.")
add("Rollback of an index?",
    "Bad embed job? Point search back at yesterday's index.",
    "Immutable index builds, alias swap, keep N generations.",
    "Alias 'catalogue-live' → build-2026-10-28.")
add("Eval for agents: success rate of trajectories?",
    "Not only pretty text — did the tools do the right thing?",
    "Exact tool sequence, arg match, end state, side-effect counts.",
    "Success = missing pasta sauce added once, not twice, not paid.")
add("Red teaming cadence?",
    "Schedule attacks: injection, PII, jailbreak, cost bombs, loops.",
    "Automated suite in CI plus quarterly human red team. Track coverage.",
    "Suite includes 'ignore previous instructions' in a product HTML comment.")
add("Guardrails vs fine-tune vs policy model?",
    "Rules on the outside, or a model trained to behave, or both.",
    "Layered: regex/PII → policy classifier → base LLM → output filter.",
    "Output filter strips accidental card numbers even if the LLM slipped.")
add("What should block an AI deploy?",
    "Failed tests, eval regressions, secret scan, vuln, missing canary plan.",
    "Write the gate list. Quality is a blocker, not a dashboard nice-to-have.",
    "Groundedness -3% blocks. Copy tweak that doesn't touch eval may still need review.")

# Serving / systems
add("Prefill vs decode and why TTFT cares?",
    "Prefill reads the prompt; decode writes the next word. First word waits on prefill.",
    "Long RAG prompts kill TTFT. KV cache helps later tokens more than the first.",
    "Cut system+history+chunks before buying more GPUs.")
add("Continuous batching vs static batch?",
    "Seat new diners as seats free, don't wait for a full table of 8.",
    "vLLM paged attention. Fairness vs utilization. Deadlines.",
    "Many Lisa sessions share a GPU without waiting for lockstep.")
add("Speculative decoding?",
    "A small model guesses a few tokens; the big one checks.",
    "Helps decode speed when draft is good. Extra complexity.",
    "Useful on FAQ-like chats; less if outputs are highly random.")
add("Multi-LoRA serving?",
    "Many small adapters on one base model.",
    "vLLM LoRA slots. Memory vs convenience. Don't mix tenants' adapters by accident.",
    "Per-merchant tone adapter; shared catalogue RAG.")
add("GPU vs CPU vs NPU placement?",
    "Big GPUs in the cloud. NPU/CPU on the cart. Don't mix jobs blindly.",
    "Profile. Thermal. Batch. Precision.",
    "YOLO on NPU; LLM on GPU; BM25 on CPU.")
add("Backpressure when GPUs are full?",
    "A waiting line with a max length, then say 429/503, don't melt.",
    "Queue+timeout+shed. Load balancer least-outstanding. Degradation: smaller model.",
    "If vLLM queue > 200ms p95, route FAQs to cache only.")
add("How do you design multi-region LLM?",
    "Don't put one GPU in one basement for the planet.",
    "Sticky sessions vs stateless. Data residency. KV cache is regional. Failover.",
    "MY vs IN shoppers — residency + latency.")
add("Exactly-once LLM side effects?",
    "You usually can't. Make tools idempotent; accept at-least-once.",
    "Outbox pattern, keys, at-least-once tools.",
    "Retry add_to_cart with the same key after a 502.")
add("Schema evolution for tool JSON?",
    "Add optional fields; don't rename in place.",
    "Version tools. Agents pin a version. Pydantic extra=forbid on money tools.",
    "add_to_cart v2 adds notes?: str optional.")
add("How do you do CI for prompts?",
    "PR runs the golden set. Numbers in the comment.",
    "Fail on delta. Store traces as artifacts. Don't call prod keys in CI if avoidable — use recorded fixtures + a cheap model.",
    "GitHub Action: pytest + ragas/langsmith eval.")
add("Canary a vision model on devices?",
    "1% of carts get the new ONNX, rest stay.",
    "Device cohorts, crash/thermal/mAP-proxy, instant disable flag.",
    "Night shift cohort first — lighting is harsher.")
add("Feature store vs just SQL?",
    "A feature store is a disciplined way to get the same features at train and serve.",
    "Worth it at scale/many models. Overkill for one XGBoost.",
    "Promo propensity features in Databricks; checkout SKU is not a feature store problem.")
add("Online vs offline features for XGBoost?",
    "Offline: batch tables. Online: low-latency lookup at request.",
    "Skew if code paths differ. Point-in-time correctness.",
    "Don't train on a rolling 30d average that isn't available live.")

# System design / leadership (from playbooks)
add("Design an enterprise RAG assistant (whiteboard).",
    "Secure librarian: permissions, pages, quotes, grades.",
    "Users, SLOs, ingest, chunk, hybrid, rerank, ACL, grounded gen, citations, eval, telemetry, delete/update, cost. Trade-offs.",
    "Sources → indexes → retrieve → rerank → LLM → validate → telemetry.")
add("Design a tool-using agent (whiteboard).",
    "Approved tools, stop rules, human for danger.",
    "State machine, schemas, least privilege, budgets, HITL, persistence, traces, deterministic fallback, idempotent tools.",
    "Search inventory freely; purchase requires confirmation.")
add("Design a real-time vision pipeline (whiteboard).",
    "Camera → prepare → recognize → event. Watch FPS and end-to-end ms.",
    "Capture, preprocess, infer, post, track, timestamp, backpressure, device metrics, fallback.",
    "ezyCart: frame to SKU event on WebSocket under 100ms model budget.")
add("Design WebSockets for thousands of carts.",
    "Many phone calls. Don't let one bad cart kill the PBX.",
    "Shard by store, heartbeats, backpressure, sticky vs broker (Kafka), replay, auth per device, horizontal gateways.",
    "IoT gateway Spring Boot/FastAPI, partition key store_id.")
add("Investigate a slow API (senior).",
    "Find the slow station with traces, not guesses.",
    "Compare baseline, traces, EXPLAIN, deps, resources, reproduce load, one fix.",
    "SQL 80% of p95 — index, don't rewrite FastAPI.")
add("Deduplicate records in Python (talk through).",
    "Remember ids you've seen; keep first or last — say which.",
    "O(n) set. Define collision policy. Stable sort if needed.",
    "seen=set(); for e in events: if e.id not in seen: keep.")
add("Bounded retry pattern?",
    "Retry a few times with waits, then fail. Don't retry forever. Don't retry non-idempotent blindly.",
    "jittered exponential backoff, retry-after, max attempts, classify retryable errors.",
    "429/503 yes; 400 validation no.")
add("SQL index example you can write?",
    "CREATE INDEX ... then EXPLAIN.",
    "Composite order, covering indexes, write cost.",
    "CREATE INDEX idx_orders_customer_id ON orders(customer_id);")
add("How do you make architecture decisions?",
    "Requirements, options, risks, cost, write it down, test.",
    "ADRs. Bake-offs. Revisit. Edge vs cloud, chain vs agent.",
    "YOLO vs RT-DETR decided by mAP+ms on store video.")
add("Production incident response?",
    "Stop the leak, then find the hole, tell people, learn without blame.",
    "Mitigate → diagnose → recover → RCA. Metrics first: error, latency, GPU, queue.",
    "Missing device events: net, broker, schema, last deploy, replay by event id.")
add("Engineering disagreement?",
    "Shared goal, evidence, maybe a test, record the call.",
    "Disagree and commit. No ego bake-offs.",
    "Two retrievers on the same golden set.")
add("How do you mentor?",
    "Why, then how, then they drive.",
    "Slices, reviews, increasing ownership. Teach trade-offs.",
    "Pair on API design; they present the ADR.")
add("How do you prioritize?",
    "Impact, risk, urgency, effort. Brakes before paint.",
    "Make trade-offs visible. Kill zombie work.",
    "Checkout correctness > cosmetic dashboard.")
add("Tell me about a failure (framework)?",
    "Real story: situation, my part, impact, fix, process change. Don't invent.",
    "STAR. What you'd do differently.",
    "Use a genuine integration/perf miss — e.g. missed seq-id causing duplicate scans in staging.")
add("How do you measure project success?",
    "Did people get the job done, reliably, at acceptable cost — not 'the model exists'.",
    "Adoption, task completion, quality, latency, reliability, cost, risk.",
    "Lisa: answer quality, add-to-cart success, TTFT, $.")
add("Why should we hire you as Principal AI?",
    "I connect models, retrieval, agents, APIs, edge vision, and apps — and I can say no to fake metrics.",
    "13+ years, Principal AI / Lead GenAI & Agentic at Retailetics, ezyCart+RAG+edge, $2M nav, TAN R&D, mobile supporting. 90-day plan: evals+SLOs first.",
    "AI + systems + delivery. Honest about tools I have not run at scale.")
add("How do you answer when you have not used a tool deeply?",
    "Say conceptual vs hands-on, map to a pattern, propose a 1-week spike with metrics. Don't bluff.",
    "Interviewers reward learning plans over theater.",
    "'I have hybrid search in prod; I have not operated X at 10M docs; here's the POC.'")
add("Prototype vs production AI?",
    "Science fair vs a trolley people lean on.",
    "Eval, authz, observability, versioning, rollback, support, cost. Production is a system.",
    "A Colab RAG is not Lisa.")
add("How do you describe impact honestly?",
    "Baseline, action, measurement, period, team vs me.",
    "Every resume number: method. $2M beacons, sub-100ms, sub-5% DD, 70% ANR, 30% perf, 500K/40%.",
    "No $X million placeholders.")
add("ezyCart in 60 seconds?",
    "Smart trolley: cameras, sensors, tablet, backend, AI checkout.",
    "Edge vision (YOLO/RT-DETR), Kimera-VIO nav, WS IoT, Android, FastAPI/Spring, RAG recipes/Lisa, sub-100ms, fail-safe.",
    "Camera/sensors → edge AI → app/backend → pay.")
add("Indoor navigation $2M story — what they will probe?",
    "Software localization vs thousands of beacons.",
    "Baseline cost, accuracy metric, failure (textureless), your role vs team, how savings were calculated.",
    "Don't just say '$2M'; walk the arithmetic you actually used.")
add("TAN Intelligence — how to talk about it?",
    "Independent venture, not a second employer. Custom indicators, 6 years, Telegram 5m/15m, SMC rules, Pine/Python, sub-5% DD.",
    "Leakage, costs, walk-forward. Not investment advice. Risk limits.",
    "Keep it off the Experience list; keep it on the R&D story.")
add("90-day plan if hired?",
    "Week 1–2: SLOs, evals, traces, cost. Then the riskiest quality or latency gap. Then a small agent/RAG improvement behind a flag.",
    "Don't boil the ocean. Ship a measured win.",
    "Stand up golden set + Langfuse before a new agent framework.")
add("How do you work with PMs and legal on AI?",
    "Translate risk: allergens, PII, hallucination, cost. Offer options with numbers.",
    "Red lines in writing. Eval as a shared language.",
    "Legal: abstain on medical/allergen without source.")
add("On-call for LLM systems?",
    "Pages on error, tail latency, cost spike, loop, safety filter down.",
    "Runbooks: rollback prompt, disable tool, shed to FAQ cache.",
    "Cost anomaly at 2am: kill runaway agent graph.")
add("Capacity planning for tokens?",
    "Guess QPS × tokens × $/token × cache hit. Stress.",
    "Peak vs average. Seasonal retail. Headroom.",
    "Weekend recipe traffic vs weekday SKU lookups.")
add("How do you keep mobile supporting skills without leading with them?",
    "They are how AI reaches the floor, not the headline.",
    "Kotlin/Compose/Flutter/Android/iOS as the last mile of vision+agents. Don't apply as a pure Android IC if the role is Principal AI — unless they want both.",
    "WS into ezyCart Android is the punchline, not RecyclerView trivia — but you can still answer ANR.")
add("Thread safety on Android vs in the agent backend?",
    "UI thread vs IO. Backend: don't share mutable agent state across requests.",
    "Immutable messages, per-thread state, locks only when needed.",
    "One LangGraph thread_id per cart session, not a global dict.")
add("How would you introduce evals to a team that only ships APKs?",
    "Start with 30 labelled questions and a CI number. Don't start with a platform.",
    "Show a caught regression. Then invest in LangSmith.",
    "The 'creative' prompt that invented ingredients is the story.")
add("SQL vs vector vs BM25 — who owns the truth?",
    "Transactional truth in SQL. Language search in BM25/vectors. Don't duplicate poorly.",
    "Price/stock from SQL/API at answer time even if RAG mentioned an old price.",
    "Lisa quotes promo from SQL live, not from a week-old chunk alone.")
add("Event sourcing for carts?",
    "Store what happened (scanned, removed), rebuild state.",
    "Great for replay/debug; harder reads. Mix with snapshots.",
    "Replay a cart to debug a double charge.")
add("Backpressure on camera frames?",
    "If infer is slow, drop frames, don't queue 10 seconds of past.",
    "Always latest-frame policy for checkout. Count via tracking, not every frame.",
    "Keep last frame only; track IDs across kept frames.")
add("How do you version ONNX models on device?",
    "A file with a version, a flag, a rollback.",
    "Signed artifacts, compatible input shapes, A/B cohort, disk space.",
    "yolo-store-v17.onnx with min app version.")
add("Coordinator vs IC at Principal level?",
    "You still touch the critical path, but you also set the quality bar and unblock.",
    "Design reviews, eval gates, mentoring, saying no to unmeasured agents.",
    "You might write the LangGraph skeleton and the eval harness, not every tool.")
add("What is a kill switch?",
    "A big red button that disables the clever path.",
    "Per-feature flags, default to deterministic checkout if AI is sick.",
    "Disable Lisa globally; scanning still works.")
add("Observability for hallucinations in prod?",
    "You won't label all chats. Sample, user flags, critic on a slice, retrieval-empty rate.",
    "Don't wait for a viral wrong-allergen story.",
    "Thumbs-down + 'unsupported claim' critic on 5% traffic.")
add("How do you handle multilingual RAG (Tamil/EN/MS)?",
    "Embed in a multilingual model or translate-then-search. Eval per language.",
    "Tokenizer cost differs. Don't assume English chunking.",
    "Tamil recipe query against EN catalogue — translation + hybrid.")
add("Streaming tool calls (parallel tools)?",
    "Ask stock and promo at once if independent.",
    "Fan-out with timeouts. Merge. Don't parallel a tool that depends on the other.",
    "get_stock and get_allergens together; add_to_cart after both.")
add("What is structured output / outlines / grammar decoding?",
    "Force the model to speak JSON by construction, not by begging.",
    "Constrained decoding vs post-validate. Still validate.",
    "Outlines/json_schema for tool args.")
add("Chain-of-thought in production?",
    "Hidden thinking can help some models; it can also leak and cost tokens.",
    "Don't stream raw CoT to shoppers. Don't treat CoT as evidence of truth.",
    "Use it internally; show shoppers the grounded short answer.")
add("How do you prevent cost bombs (infinite generate)?",
    "max_tokens, stop sequences, step budgets, per-tenant quotas, anomaly alerts.",
    "Hard limits in the gateway, not only in the prompt.",
    "Gateway kills runs > $0.50 or > 30s.")
add("A/B testing LLM apps vs classic A/B?",
    "Outputs are random; you need more samples and quality metrics, not only conversion.",
    "Holdout, CUPED if you have it, guardrail metrics (safety).",
    "Don't ship a wittier Lisa that hallucinates more even if clicks rise.")
add("Knowledge graphs vs vector RAG?",
    "Graphs are explicit relations; vectors are fuzzy similarity. Hybrid exists.",
    "Use graphs when relations are the product (allergens, substitutes). Vectors for prose.",
    "SKU substitute graph + vector recipes.")
add("How do you do RAG over tables?",
    "Don't embed a CSV as a blob blindly. Preserve rows, maybe text-to-SQL with tight allowlists.",
    "Row-level chunks, schema linking, or constrained SQL. Test numeric exactness.",
    "Nutrition table: retrieve the row, don't round-trip an LLM for 2+2.")
add("Code interpreter / sandboxed tools?",
    "Let the model run code in a jail, not on the checkout host.",
    "No network, timeouts, resource limits. Still injection risk.",
    "Don't give a sandboxed python that can hit the payment API.")
add("How do you explain attention to a hiring manager who is not ML?",
    "It's a highlighter for the useful words in the sentence.",
    "Then offer the Q/K/V sentence if they want depth.",
    "Connecting 'it' to 'trolley' in the shopper question.")
add("Staff/principal system design checklist you actually follow?",
    "Clarify, SLOs, scale, draw, data, failure, security, observe, trade-off, validate.",
    "Say it as a habit, then apply to their prompt.",
    "Always name p95, ACL, eval, one failure mode.")
add("How do you keep from gold-plating agents?",
    "Start as a function, then a chain, then an agent if eval says so.",
    "Complexity budget. Revisit quarterly.",
    "SKU lookup stayed a function. Recipes earned a graph.")
add("Mobile + AI interview: what they might still ask?",
    "ANR, coroutines, Compose, Flutter BLoC, offline, WS reconnect — supporting, not the headline.",
    "Tie every answer back to how the model reaches the shopper.",
    "Main-thread policy + device WS + on-device TF Lite.")
add("How would you onboard a new embedding model with 10M docs?",
    "Shadow index, dual retrieve, compare recall, alias swap, keep rollback.",
    "Cost of re-embed, backfill SLA, query routing during migrate.",
    "Build catalogue-v2 overnight, shadow 2 days, swap alias.")
add("What is a 'cell' or 'bulkhead' in an AI platform?",
    "Blast-radius boxes so one noisy tenant doesn't drown GPUs.",
    "Per-tenant queues, separate pools for batch embed vs interactive chat.",
    "Embed jobs cannot starve Lisa TTFT.")
add("How do you handle model deprecation from a vendor?",
    "Abstraction, dual-run, eval parity, date in the calendar.",
    "Never hardcode gpt-x in 40 repos. One router.",
    "GPT-4o → successor behind the same interface after eval.")
add("Security review questions you pre-empt?",
    "Where PII goes, tool authz, injection, logs, residency, supply chain of models.",
    "Bring a diagram. Don't wait to be asked.",
    "Slide: data flow from cart camera to event (no raw video stored) vs chat to LLM (redacted).")
add("How do you document an agent for the next engineer?",
    "Graph picture, tool contracts, budgets, eval, runbook, known failure modes.",
    "README + ADR + golden traces.",
    "Lisa README shows the graph and the pay-tool never-list.")
add("Final: what is production GenAI in one sentence?",
    "A measured, permissioned, observable, reversible system that uses models where they earn their keep.",
    "Not a prompt in a slide. Quality + safety + SLO + cost + rollback.",
    "ezyCart + Lisa + edge vision + FastAPI/Spring + evals — that's the bar.")

QUESTIONS = Q
