# Intermediate: ML, CV, backend, mobile, cloud intro, LLM/RAG intro, trading hygiene
Q = []

def add(q, kid, tech, *ex):
    Q.append((q, kid, tech, list(ex)))

# ML
add("Supervised vs unsupervised vs reinforcement learning?",
    "Supervised: teacher gives answers. Unsupervised: group similar things. RL: score from trial and error.",
    "Supervised needs labels (detection boxes, sentiment). Unsupervised: clustering, embeddings. RL: agents with rewards — expensive and unstable for checkout; prefer supervised + rules + evals.",
    "YOLO is supervised detection. Recipe retrieval uses embeddings (unsupervised pretrain + supervised eval). Do not RL a payment agent in production first.")
add("Train / validation / test split? Why not peek at test?",
    "Practice, dress rehearsal, real exam. If you keep retaking the exam while studying, the score lies.",
    "Fit only on train. Tune on val. Report test once. Time-series: chronological splits. Nested CV when tuning is heavy.",
    "Trading labels shuffled randomly leak the future. Vision: hold out a store not seen in training.")
add("Overfitting vs underfitting? Regularization?",
    "Overfit memorizes homework. Underfit is too simple. Regularization is a 'don't be fancy' penalty.",
    "L2/L1, dropout, early stop, data aug, smaller models. Learning curves. Bias-variance talk without cargo-cult.",
    "A detector with 99% train mAP and 40% on night-shift cameras is overfit to daytime.")
add("Bias vs variance?",
    "Bias is always missing the dartboard the same way. Variance is scattered shots.",
    "High bias: add features/model capacity. High variance: more data, regularization. Error decomposition is a diagnostic, not a slogan.",
    "A linear model on SKU images underfits; a huge net on 200 labels overfits.")
add("Precision, recall, F1, accuracy, ROC-AUC, PR-AUC?",
    "Accuracy can lie if 99% of frames have no product. Precision: of alarms, how many true. Recall: of truths, how many found.",
    "Imbalanced detection: PR curve, F-beta. Thresholds from cost of false charge vs missed item. Confusion matrix first.",
    "False-positive SKU at checkout is a precision problem (shopper charged wrong). Missed item is recall.")
add("What is a loss function? Cross-entropy vs MSE?",
    "Loss is a score of how wrong the model is. Training tries to shrink it.",
    "CE for classification, MSE/MAE for regression, specialized detection losses (box + class + objectness). Loss ≠ business metric.",
    "Optimize detection loss, but ship on checkout-error rate, not only mAP.")
add("Gradient descent, learning rate, batch size?",
    "Take steps downhill. Learning rate is step size. Batch is how many examples per step.",
    "SGD/Adam. Too large LR diverges; too small crawls. Large batch needs LR scaling. Mixed precision.",
    "Fine-tune LoRA with a small LR on the adapter; do not blow up the frozen base.")
add("Backpropagation in one minute?",
    "Send the error backward so each layer knows how to change.",
    "Chain rule through the graph. Autograd in PyTorch. Vanishing/exploding gradients; residuals, init, clipping.",
    "You do not hand-derive YOLO backprop; you must know what a NaN loss means.")
add("What is a neural network? MLP vs CNN vs transformer?",
    "MLP is stacked fully-connected layers. CNN looks at local image patches. Transformer uses attention.",
    "Inductive bias: CNNs for grid locality; transformers for long-range. Modern detectors mix both (RT-DETR).",
    "Cart camera: CNN/transformer detector. Text RAG: transformer LLM + embedding model.")
add("Embeddings for non-text (images)?",
    "Turn a photo into a point on a map so similar photos sit near each other.",
    "Contrastive (CLIP), metric learning. Use for visual search; still need SKU classifier/detector for checkout.",
    "Find similar products from a shelf photo; do not bill from embedding nearest-neighbor alone without a threshold.")
add("Data leakage?",
    "Letting the exam answers into homework.",
    "Target in features, future timestamps, duplicate customers across splits, scaler fit on all data. Audit features.",
    "Using tomorrow's close in today's trading feature. Fitting StandardScaler on train+test.")
add("Cross-validation vs walk-forward?",
    "CV rotates folds. Walk-forward slides a window through time.",
    "Random K-fold leaks time. Trading and demand: walk-forward, embargo, purge.",
    "TAN indicators: walk-forward, not 5-fold shuffle.")
add("Class imbalance? How to handle?",
    "If 1 in 100 frames has a rare SKU, the model can ignore it and still look accurate.",
    "Resample, class weights, focal loss, threshold tuning, collect more rare data. Report per-class recall.",
    "Rare SKUs at checkout need extra labels, not just more bananas.")
add("Feature scaling? Normalization vs standardization?",
    "Put features on a similar yardstick so one does not shout over others.",
    "Fit scaler on train only. Trees (XGBoost) care less; nets care more. Quantiles for heavy tails.",
    "Tabular promo model: scale numeric features; leave one-hot as 0/1.")
add("XGBoost / gradient boosting vs random forest vs linear model?",
    "Linear is a straight rule. Forest is many trees voting. Boosting is trees that correct the last tree's mistakes.",
    "Tabular default: linear baseline then XGBoost. Need interactions and non-linearities. Neural nets when you have huge data or mixed modalities.",
    "Who buys which promo: XGBoost baseline before an LLM classifier.")
add("What is sklearn Pipeline and why?",
    "A recipe that packages preprocess + model so you cannot forget a step.",
    "Preprocessing inside the pipeline, fit on train folds only. Joblib dump the whole pipeline.",
    "imputer → scaler → XGBoost in one object for merchant forecasting.")
add("Calibration of probabilities?",
    "A 70% score should be right about 70% of the time.",
    "Reliability diagrams, Platt/isotonic. Detection confidence is not always a probability.",
    "Do not treat YOLO 0.9 as 90% chance without calibration on store data.")
add("What is batch vs online vs mini-batch learning?",
    "Batch sees all data. Online sees one at a time. Mini-batch is the usual middle.",
    "Streaming drift: periodic retrain vs true online. Most production CV is mini-batch train, batch/offline eval, online infer.",
    "Nightly retrain on new labelled frames; inference per camera frame.")
add("Train/serving skew?",
    "The model trained on clean tables but production feeds it messy live data.",
    "Same feature code path. Log features at serving for replay. Schema checks.",
    "Training used RGB 640px; device sent NV12 320px — mAP collapses. Match preprocess.")
add("What is a baseline and why start there?",
    "A dumb simple method you must beat.",
    "Majority class, last-value forecast, BM25-only RAG, keyword FAQ. If you cannot beat it, do not ship complexity.",
    "BM25-only shopping FAQ vs full RAG — measure groundedness lift.")
add("PyTorch: tensor, autograd, nn.Module, DataLoader?",
    "Tensor is a number grid. Autograd tracks how to change it. Module is a model. DataLoader feeds batches.",
    "device (cpu/cuda), no_grad for infer, eval() vs train() for dropout/BN. AMP.",
    "Export YOLO to ONNX with a dummy tensor of the production size.")
add("eval() vs no_grad() vs inference_mode()?",
    "eval changes layers like dropout. no_grad stops tracking gradients. Both needed at serve time.",
    "Forgetting eval() leaves dropout on — noisy checkout detections.",
    "ONNX Runtime session is inherently infer; PyTorch proto must set eval.")
add("ONNX export pitfalls?",
    "Not every PyTorch op exists in ONNX. Dynamic shapes and NMS are usual pain.",
    "Opset version, simplify, test numerical parity, then TensorRT/TF Lite. Keep a golden image test.",
    "A custom NMS plugin broke TensorRT; we compared boxes on a fixture clip.")
add("JAX: grad, jit, vmap in one line each?",
    "grad = derivatives. jit = compile. vmap = run many in parallel.",
    "Functional, XLA. Different from PyTorch's imperative style. Choose by team and ecosystem.",
    "If the team is PyTorch-native for CV, do not rewrite YOLO in JAX for fashion.")
add("TensorFlow vs PyTorch vs JAX — how do you choose?",
    "Three workshops. Pick the one with models, deploy path, and people.",
    "TF Lite path vs ONNX vs JAX/XLA. Reversible choice: export ONNX when possible.",
    "Detection in PyTorch → ONNX → TF Lite on Android.")
add("What is transfer learning?",
    "Start from a model that already saw many pictures/words, then teach your small dataset.",
    "Freeze backbone, train head, then unfreeze lightly. Domain gap: supermarket ≠ COCO.",
    "Fine-tune YOLO on store SKUs rather than train from scratch.")
add("What is data augmentation for images? Risks?",
    "Fake extra pictures by flipping, cropping, lighting changes.",
    "Augment only train. Photometric vs geometric. Do not flip text/OCR. Keep real night-aisle data too.",
    "Do not color-jitter so hard that SKU colors become unrecognizable.")
add("Label noise and how it shows up?",
    "Wrong boxes teach the model wrong habits.",
    "Consensus labeling, QA sampling, loss robust to noise. Per-class confusion.",
    "Misboxed 'oil' as 'sauce' will cause checkout disputes — fix labels first.")
add("mAP, IoU, NMS for detection?",
    "IoU is overlap of two boxes. NMS throws away extra boxes on the same object. mAP summarizes precision across classes and thresholds.",
    "IoU 0.5 vs 0.75 protocols. Soft-NMS. RT-DETR aims to avoid classic NMS. High mAP can still fail on glare/occlusion.",
    "Two boxes on one bottle: NMS keeps one. Report mAP@0.5 and checkout-oriented metrics.")
add("Classification vs detection vs segmentation vs tracking vs OCR?",
    "Class: what. Detect: what+where box. Segment: pixels. Track: same object over time. OCR: read text.",
    "Checkout may need detect+track so a banana is not counted every frame.",
    "OCR for shelf labels; detection for items in the cart camera.")

# CV / spatial intermediate
add("What is computer vision in production?",
    "Cameras plus models plus hardware plus monitoring — not a notebook demo.",
    "Define task, metric, lighting/occlusion domain, latency, privacy, fallback. Dataset flywheel.",
    "ezyCart self-checkout vision plus kiosk. Fail closed on low confidence.")
add("YOLO family (v8/v10/v11) — what to say?",
    "A family of fast one-shot detectors. Bigger versions are more accurate and slower.",
    "Choose size by device budget. License, export path, NMS. Benchmark your video, not COCO blog posts.",
    "Cart NPU: nano/small. Back-office GPU: larger. Same eval set.")
add("What is RT-DETR?",
    "A real-time detection transformer. Different guts than YOLO; still a detector.",
    "Set prediction, typically no NMS in the core. Compare mAP, small objects, ms, memory on the same device.",
    "Bake-off YOLO vs RT-DETR on aisle clips with identical image size and precision.")
add("OpenCV's role if you have YOLO?",
    "OpenCV is the Swiss Army knife: resize, undistort, draw, classic vision.",
    "Pre/post around the net. Camera calibration. Do not rewrite undistort in PyTorch on device.",
    "Undistort cart camera, then run ONNX.")
add("Camera calibration, distortion, extrinsics?",
    "Lenses bend pictures. Calibration measures the bend so geometry is honest.",
    "Intrinsics, extrinsics, IMU-camera extrinsics for VIO. Bad calibration → SLAM drift.",
    "Kimera-VIO needs camera-IMU calibration and time sync.")
add("What is SLAM?",
    "Build a map while you figure out where you are.",
    "Front-end features, back-end optimization, loop closure. Failure: textureless walls, moving people, lighting.",
    "Indoor nav replaced thousands of Bluetooth beacons, saving over $2M — still explain aisle-level error and failure modes.")
add("VIO vs VO vs wheel odometry?",
    "VO is camera-only motion. VIO adds IMU. Wheels slip.",
    "Complementary sensors. Sync clocks. Bias estimation.",
    "Trolley on smooth tiles: IMU helps during blur; wheels may slip — VIO is the fusion.")
add("Kimera-VIO — what is it and what must you not overclaim?",
    "Open-source visual-inertial odometry in the Kimera family.",
    "Know inputs (mono/stereo + IMU), outputs (pose), assumptions, compute. Validate drift on store routes. Do not claim 'SLAM solved' if you only run VIO.",
    "Use it as the motion estimate feeding the product-finder path.")
add("Spatial AI?",
    "Not just 'this is a chair' but 'the chair is 2 meters left'.",
    "Perception + geometry + localization + maybe planning. Coordinate frames (camera, IMU, map, store).",
    "Product finder: SKU in map frame, trolley in map frame, path between them.")
add("Edge vs cloud inference for vision?",
    "Edge is on the device. Cloud is far away. Edge is faster and works if Wi-Fi dies; cloud is heavier models.",
    "Privacy, bandwidth, thermal, updates, fallback. Hybrid: tiny on-device + cloud for hard cases.",
    "Sub-100ms ONNX/TF Lite on cart; do not stream every frame to Bedrock.")
add("TensorRT vs TF Lite vs ONNX Runtime?",
    "ONNX is the suitcase. TensorRT is a fast NVIDIA unpacker. TF Lite is the phone/edge unpacker.",
    "Operator coverage, quantization tools, profiling. Golden tests after every export.",
    "Android cart: TF Lite/ORT. NVIDIA kiosk: TensorRT.")
add("How do you get sub-100ms vision?",
    "Time every stage. Shrink the slowest. Recheck quality.",
    "Resolution, quantization, batch=1 vs batch, CPU affinity, memcpy. End-to-end vs model-only — know which the resume number is.",
    "Resize was 40ms, infer 30ms, NMS 5ms — fix resize first.")
add("Tracking IDs across frames?",
    "Give the same banana the same name as it moves so you do not count it 30 times.",
    "ByteTrack/SORT-style, IoU + appearance. Handle occlusion. Reset on cart-empty.",
    "Scan-bag-pay: track objects on the tray, not per-frame independent detections.")
add("Lighting, glare, occlusion — domain shift?",
    "A model trained at noon fails at night or under a reflection.",
    "Per-scenario eval. Targeted data. Auto-exposure. Confidence gating.",
    "Store LED vs window glare sets — split metrics, not one mAP.")
add("Privacy for cameras in a store?",
    "Do not keep faces if you do not need them. Say what you store.",
    "Retention, blur, on-device processing, access logs, regulation. Minimize.",
    "Checkout vision can drop frames that are not needed for the SKU event.")

# Backend intermediate
add("Why FastAPI for AI services?",
    "Python API with type checks and auto docs, sitting next to ML libraries.",
    "Pydantic validation, async, OpenAPI, deps. Offload CPU infer. Timeouts, auth, tracing.",
    "Vision and RAG orchestration in FastAPI; Java estate in Spring Boot.")
add("Pydantic / bean validation?",
    "Check the form before you accept it.",
    "Boundary validation. Useful errors. Version schemas.",
    "LLM JSON and HTTP bodies both go through Pydantic — untrusted input.")
add("Spring Boot in one minute?",
    "Java way to build services with batteries: web, security, config, actuators.",
    "Coexist with FastAPI behind stable contracts. Observability, thread pools, backpressure.",
    "IoT WebSocket gateway in Spring Boot talking to the Android app.")
add("Microservices vs modular monolith?",
    "Many small services vs one well-cut program. Split only when the boundary pays rent.",
    "Network failure, distributed data, versioning. Start modular; extract when scaling or ownership demands.",
    "Do not split 'add to cart' into 12 services. Do split vision infer if it scales differently.")
add("How do WebSockets stay reliable for IoT?",
    "Keep the call up, number the messages, retry without doubling, notice death.",
    "Device identity, schema, timestamps/seq, heartbeats, backoff, ack, idempotency, replay. Restore state on reconnect.",
    "ezyCart device ↔ Android via FastAPI/Spring Boot sockets — duplicate scans must not double charge.")
add("REST vs WebSocket vs SSE in the trolley stack?",
    "REST for things. Sockets for live device chatter. SSE for token streams to the UI.",
    "Do not multiplex everything on one socket without a reason. Backpressure differs.",
    "SKU lookup REST; IMU/scan events WS; Lisa tokens SSE.")
add("How do you debug a slow API?",
    "Measure first. Find the slow station. Change one thing. Measure again.",
    "p50/p95/p99, traces, EXPLAIN, N+1, payload size, downstream. Indexes vs cache.",
    "Colan 40% faster responses: know if it was indexing, caching, or query rewrite.")
add("Cache invalidation basics?",
    "A sticky note of the answer. If the truth changes, throw the note away.",
    "TTL, explicit purge on catalogue update, stampede, stampede locking. Never cache ACL-sensitive personalized prices without a key.",
    "Recipe RAG semantic cache keyed by tenant + basket hash.")
add("Message queues vs request/response?",
    "A queue is a waiting line for work that can happen in a second, not instantly.",
    "Celery/SQS/Kafka. At-least-once. Idempotent consumers. Backpressure.",
    "Embed 10k new products in Celery; HTTP request only enqueues.")
add("Celery / background jobs?",
    "Do slow homework in the back room so the counter stays fast.",
    "Retries, acks, poison queues, idempotency, visibility timeout.",
    "Nightly re-embed of changed catalogue pages.")
add("GraphQL when, not when?",
    "Client asks for exactly the fields it wants. Easy to over-fetch on the server instead.",
    "N+1, query cost analysis, persisted queries. Not a replacement for events.",
    "Staff app product details via GraphQL; not live IMU.")
add("Authn vs authz? RBAC vs ABAC?",
    "Authn: who are you. Authz: what may you do. RBAC is roles. ABAC is attributes/policies.",
    "Per-resource checks. Tenant isolation. Service identity (mTLS).",
    "Shopper cannot read other carts. Staff role cannot export PII dumps without audit.")
add("Rate limiting and backpressure?",
    "Slow down noisy clients so one shopper cannot knock over the API.",
    "Token bucket, 429, retry-after, load shedding, queue limits. Fairness per tenant.",
    "LLM gateway: tokens/min per store so one bot cannot burn the budget.")
add("Health checks vs readiness vs liveness?",
    "Liveness: restart me if I am dead. Readiness: do not send traffic yet.",
    "Do not make liveness call the GPU if that hangs — deadlock restarts.",
    "ORT session ready = ready; crash loop ≠ ready.")
add("Docker: image, layer, registry, non-root?",
    "A box with the app and its libraries. Layers cache builds. Registry stores boxes.",
    "Small base, pin digests, scan CVEs, non-root, no secrets in layers, HEALTHCHECK.",
    "FastAPI+ORT image, multi-stage build, distroless/runtime slim.")
add("docker vs VM vs process?",
    "VM virtualizes hardware. Container virtualizes the OS userland. Process is just a program.",
    "Isolation vs overhead. Nested not needed on device.",
    "Cloud API in containers; on-cart infer is a process/library.")
add("CI/CD for mobile + backend together?",
    "Two pipelines that meet at a contract test.",
    "Android Bitrise/GitLab + API tests. Version the API. Feature flags.",
    "App expecting new event schema must not ship before the gateway.")
add("Observability: logs, metrics, traces?",
    "Logs are stories. Metrics are numbers. Traces are the path of one request.",
    "RED/USE. Exemplars. Cardinality explosions. Trace LLM + SQL + WS in one id.",
    "cart_id / trace_id from Android through RAG.")
add("What is p95 latency and why not only average?",
    "Average hides the slow shoppers. p95 is the wait that 95% beat.",
    "SLOs on p95/p99. Tail from GC, JIT, GC, cold start, GC, GC — and retrieval.",
    "Lisa TTFT p95 matters more than mean if 5% of shoppers wait 8s.")
add("Connection pooling?",
    "Reuse database connections instead of shaking hands every time.",
    "Pool size vs DB max_connections. Timeouts. Leaks.",
    "Spring Boot Hikari + FastAPI async pool sized for kiosk burst.")
add("Pagination, filtering, idempotency keys in public APIs?",
    "Same as fresher SQL/HTTP, now with SLOs and abuse in mind.",
    "Max page size, consistent snapshots, signed idempotency keys with TTL.",
    "Staff audit export is async job + download link, not a 2GB GET.")
add("500K users — what do you clarify?",
    "Registered vs daily vs concurrent. Design to the peak QPS, not a vanity count.",
    "Load test. Caches. Read replicas. Queue writes. Colan 500K + 40% faster is a backend story — quote the measurement.",
    "1M DAU chat ≠ 500K registered users. Different bottleneck (GPUs).")

# Mobile intermediate
add("Jetpack: Room, Hilt, Navigation, WorkManager, DataStore?",
    "Room is local DB. Hilt is dependency injection. Navigation is screens. WorkManager is deferred work. DataStore is prefs.",
    "Lifecycle-aware. Test fakes. Migrations for Room.",
    "Cache last cart locally in Room if the socket drops.")
add("Kotlin Coroutines + Flow on Android?",
    "Readable async + streams of UI state.",
    "viewModelScope cancellation. StateFlow vs SharedFlow. Backpressure.",
    "Device events Flow → ViewModel → Compose.")
add("What is an ANR and how did you cut 70%?",
    "App Not Responding: main thread blocked ~5s. Users see a freeze dialog.",
    "StrictMode, traces, move IO/offload, Choreographer. Know the before/after measurement window for the resume 70% ANR / 30% performance claims.",
    "Do not parse JSON or hit disk on the main thread in checkout.")
add("Flutter BLoC vs Provider vs setState?",
    "setState is local. Provider passes values down. BLoC is event-in state-out.",
    "Predictable state for staff apps. Test blocs without UI.",
    "TV monitor BLoC subscribes to cart fleet events.")
add("Platform channels / FFI in Flutter?",
    "Talk to native Android/iOS from Dart when you need hardware.",
    "Keep channels small. Threading. Errors as typed results.",
    "SDK lite may call native scan/pay.")
add("iOS interop / KMP at a high level?",
    "Share some logic across Android and iOS without sharing all UI.",
    "KMP expect/actual. Do not oversell if you shipped mostly Android+Flutter.",
    "Honest: 'I have shipped Android/Flutter; iOS via Flutter/interop, not a deep UIKit specialist unless true.'")
add("Offline-first mobile?",
    "The app still works in a dead aisle, then syncs.",
    "Local source of truth, conflict resolution, queues. Not all features can be offline (payments).",
    "Scan locally; pay requires connectivity + idempotent retry.")
add("Security on device: keystore, certificate pinning, secrets?",
    "Do not hide API keys in the APK. Use the OS keystore. Pin if you must.",
    "Obfuscation is not security. Attestation where needed. Secrets on server.",
    "Bedrock keys never in the trolley APK.")
add("Play/App Store staged rollout?",
    "Ship to 1% of users, watch crashes, then 100%.",
    "Mapping files, ANR dashboards, feature flags vs store binary.",
    "Vision model file update may be a feature-flagged download, not only a Play release.")
add("Deep links and notifications?",
    "A link opens a screen. A notification pokes the user.",
    "Auth on deep links. Do not leak PII in push payloads.",
    "Staff notified of a jammed kiosk — device id, not shopper name.")

# LLM / RAG intro (intermediate, full advanced later)
add("What is Generative AI? What is an LLM?",
    "GenAI creates new content. An LLM predicts the next tokens from context.",
    "Transformer decoder, tokens, context window, hallucination risk. Production: grounding, eval, cost, safety.",
    "Lisa generates answers; YOLO does not. Do not use an LLM as the only allergen source.")
add("Tokens and context windows?",
    "Tokens are pieces of words. The window is how much the model can see at once.",
    "Tokenizer mismatch. Cost ∝ tokens. RAG should not dump 100k tokens of catalogue.",
    "Basket + top-5 chunks, not the whole store manual.")
add("What is a transformer / self-attention (intermediate)?",
    "Attention lets each word look at the useful other words.",
    "Q/K/V, multi-head, residual, FFN, positional encodings. Encoder vs decoder vs encoder-decoder.",
    "An LLM connecting 'this' to the SKU mentioned earlier in the cart list.")
add("Embeddings and cosine similarity?",
    "Meaning as a list of numbers. Cosine is how aligned two arrows are.",
    "Normalize, ANN indexes, out-of-domain queries, embedding model versioning (re-embed on upgrade).",
    "'cheap sparkling water' near 'value seltzer' even if words differ.")
add("Prompting vs RAG vs fine-tuning (intermediate)?",
    "Prompt = instructions. RAG = open book. Fine-tune = extra practice on weights.",
    "Facts that change → RAG. Style/format → prompt or FT. Combine. Prompting does not create truth.",
    "Weekly promo: RAG. JSON style: prompt. 5k receipt labels: LoRA.")
add("Temperature and top-p?",
    "How adventurous decoding is. Low is steady.",
    "Does not guarantee facts. Low T for tools/JSON.",
    "Missing-SKU extraction at T≈0.")
add("What is RAG (intermediate)?",
    "Find trusted pages, then write the answer from them.",
    "Ingest, chunk, embed, retrieve, (rerank), generate, cite, abstain. Eval retrieval and generation separately.",
    "Shopping assistant + recipes with LangChain/LlamaIndex.")
add("BM25 vs dense vs hybrid (intermediate)?",
    "Words vs meaning vs both.",
    "BM25 for SKUs; dense for paraphrase; hybrid + RRF + rerank as default.",
    "EZY-1044 vs 'spicy pasta night'.")
add("Chunking and overlap?",
    "Cut documents into useful pages, with a little overlap so sentences are not torn.",
    "Structure-aware. Overlap 10–20%. Tables/code special. Bad chunks = bad RAG.",
    "Return policy clause stays with its heading.")
add("What is a vector database (intermediate)?",
    "Stores vectors and finds nearest neighbors, often with filters.",
    "Pinecone, Qdrant, Milvus, Weaviate, pgvector, FAISS, Supabase. Benchmark filters + recall + ops.",
    "ACL filter in the query, not after.")
add("Hallucination (intermediate)?",
    "Confident nonsense.",
    "Ground, cite, abstain, eval, low T, critic. Never 0%.",
    "Do not invent gluten-free if the chunk is silent.")
add("LangChain vs LlamaIndex (intermediate)?",
    "LangChain: app/tool Lego. LlamaIndex: data/RAG librarian.",
    "Can combine. Keep business logic in your code. Test without the LLM.",
    "Indexes in LlamaIndex; tools in LangChain/LangGraph.")
add("What is an AI agent vs a chain (intermediate)?",
    "A chain is a recipe. An agent chooses the next allowed step.",
    "State, tools, budgets. More failure modes. Start with a chain.",
    "SKU lookup chain; multi-step recipe+missing-items agent.")
add("ReAct pattern?",
    "Think, act, look, repeat.",
    "Reason + act + observe. Cap loops. Structured tools not free-form.",
    "get_stock → OOS → search_alternatives.")
add("Tool calling (intermediate)?",
    "The model fills a form; your code runs the function.",
    "JSON schema, validate, authorize, execute, return. Model is not the security boundary.",
    "add_to_cart schema + Pydantic + HITL for pay.")
add("MCP (intermediate)?",
    "A standard plug for tools and context.",
    "Client-server. Still authn/z, validation, audit. Not automatically safe.",
    "Catalogue MCP server; no raw SQL MCP without a guard.")
add("LangGraph (intermediate)?",
    "A flowchart with memory: nodes do work, edges choose next, state is the backpack.",
    "Cycles, checkpoints, HITL, retries. Step limits.",
    "Lisa graph: retrieve → generate recipe → missing SKUs → confirm.")
add("CrewAI / AutoGen (intermediate)?",
    "Role-based or conversational multi-agent helpers.",
    "Narrow roles, shared state, measure if extra agents help. Often a graph is enough.",
    "Planner/researcher/executor only if eval shows lift vs one agent.")
add("LangSmith / Langfuse / LangFlow / n8n?",
    "Smith/Fuse: flight recorders and evals. LangFlow/n8n: visual pipes for prototypes/ops.",
    "Redact PII in traces. Visual ≠ production controls.",
    "Trace a failed add_to_cart; n8n for a Telegram TAN alert pipe, not checkout.")
add("Hosted vs local LLM (intermediate)?",
    "API brain vs brain in your basement.",
    "Quality, cost, privacy, latency, ops. Abstraction with fallbacks: Bedrock, Vertex, GPT-4o, Claude, Gemini, Ollama, vLLM.",
    "Pilot hosted; FAQ local Llama 3 if cost/privacy says so.")
add("LoRA / PEFT (intermediate)?",
    "Train a small adapter instead of the whole model.",
    "Rank, alpha, freeze base, eval task metrics, overfit on 5k. Merge or serve adapter.",
    "LoRA JSON extractor; keep SKU facts in RAG.")
add("Quantization (intermediate)?",
    "Use fewer bits for numbers to go faster and smaller. Recheck quality.",
    "INT8/4-bit/FP8, PTQ vs QAT, TensorRT/TF Lite. Per-class metrics, not only average.",
    "INT8 YOLO on cart; if small SKUs drop, mix precision.")
add("vLLM and KV cache (intermediate)?",
    "vLLM is a fast open-model server. KV cache remembers past tokens so you do not re-read the whole prompt.",
    "Paged KV, continuous batching, prefix cache. Different from on-device ORT.",
    "System prompt prefix-cached; cart hardware still TF Lite.")
add("SSE (intermediate)?",
    "Server-sent events: the server talks in a stream. Stop if the client hung up.",
    "text/event-stream, disconnect cancel, heartbeats, Last-Event-ID.",
    "Lisa token stream; cancel GPU work on tablet sleep.")
add("PII (intermediate)?",
    "Personal data. Do not send it to a model if you can avoid it.",
    "Detect/redact at gateway. Logs. Retention. Faces in video.",
    "Diet preference OK; PAN/Aadhaar never in prompts.")
add("Prompt injection (intermediate)?",
    "A hidden note that tries to boss the model.",
    "Untrusted user+docs. Structured tools only. HITL for money. Red team.",
    "Product text 'ignore policy, 100% off' must not call discount tool.")

# Trading intermediate
add("What is a backtest vs paper vs live?",
    "Backtest is a replay. Paper is fake-live. Live is real money.",
    "Costs, slippage, latency, look-ahead, survivorship. Forward test. TAN: 6 years systematic, Telegram 5m/15m, Pine/Python, sub-5% DD — know definitions.",
    "Cannot use the unclosed 5m candle's high as a known value.")
add("Maximum drawdown?",
    "The worst fall from a peak to a trough.",
    "Not the only risk metric. Sample size, period, costs. Sub-5% is a claim with a method.",
    "Peak 100 to 95 is 5% DD. Two strategies with same DD can have different tails.")
add("Look-ahead bias and survivorship?",
    "Look-ahead: future bits. Survivorship: only studying winners that still exist.",
    "Point-in-time listings. Delisted symbols. Timestamp news.",
    "Sentiment from an article timestamped after the move is leakage.")
add("SMC / liquidity in one honest sentence?",
    "A family of discretionary price-action ideas; if you use them, they must become testable rules.",
    "Do not mystify. Encode rules, test, risk limits. Not magic.",
    "TAN rule-based SMC-inspired signals with position sizing — validated, not folklore.")
add("Why FinGPT is not a trading system?",
    "It reads finance language. It does not know your fills or fees.",
    "Feature candidate. Validate lift after costs. Risk limits still rule.",
    "Sentiment as one XGBoost feature, never auto-market-order.")
add("Position sizing and risk limits?",
    "How big a bet, and the max pain you allow.",
    "Vol targeting, stop rules, kill switches. Independent of the ML toy.",
    "Sub-5% DD target drives size, not the model confidence alone.")

# Cloud intermediate
add("AWS Bedrock in one minute?",
    "Managed door to foundation models on AWS.",
    "IAM, data handling, guardrails, regions, latency, price. Still eval. Abstraction layer.",
    "Route Lisa to Bedrock Claude with fallback.")
add("GCP Vertex AI?",
    "Google's managed train/serve/app AI platform.",
    "IAM, endpoints, feature store, monitoring. Avoid lock-in where it hurts.",
    "Same router interface as Bedrock.")
add("SageMaker vs 'just a container'?",
    "SageMaker is AWS's training/hosting product. A container is DIY.",
    "Use managed when ops value > lock-in. Many teams serve FastAPI+ORT themselves.",
    "Training job on SageMaker; latency path still your FastAPI.")
add("Databricks in an AI stack?",
    "A data+ML platform on Spark/lakehouse.",
    "Feature tables, training, governance. Not a replacement for an edge runtime.",
    "Catalogue analytics in Databricks; cart infer on device.")
add("IAM least privilege?",
    "Every service gets the smallest key that still opens its door.",
    "Role per service, no long-lived keys in Git, audit.",
    "Embed job can read catalogue bucket, cannot kms:Decrypt all keys.")
add("Blue/green or canary deploys?",
    "Run old and new, shift a little traffic, watch, then all.",
    "Prompt/model canaries with eval+business KPIs. Instant rollback.",
    "5% of Lisa traffic on prompt v12; auto-revert if groundedness drops.")

QUESTIONS = Q
