# Basic / fresher: Python, OOP, DS, HTTP, SQL, Git, Linux, Java/Kotlin intro
Q = []  # (question, kid, tech, [examples])

def add(q, kid, tech, *ex):
    Q.append((q, kid, tech, list(ex)))

# Python
add("What is Python and why is it used in AI?",
    "Python is a readable language with lots of ready-made tools for data and models.",
    "Dynamic language with NumPy, Pandas, PyTorch, FastAPI. Fast to experiment; profile before optimizing. GIL matters for CPU threads; use multiprocessing or native extensions for heavy compute.",
    "AI services at Retailetics sit in Python FastAPI; training/export also in Python.",
    "A notebook prototype is not production until it has tests, types, and packaging.")
add("What is the difference between a list, tuple, set, and dict?",
    "List is a line of items you can change. Tuple is a locked line. Set is a bag of unique stickers. Dict is a labeled locker.",
    "list: ordered, mutable, O(1) append. tuple: immutable, hashable if contents are. set: unique, O(1) avg lookup. dict: key→value hash map. Choose by mutability, uniqueness, and lookup needs.",
    "Cache SKUs in a set for O(1) membership. Cart lines are a list of dicts {sku, qty}.",
    "Dedup device event_ids with a set so the same scan is not charged twice.")
add("What is a list comprehension?",
    "A short way to build a list from another list with a rule.",
    "[f(x) for x in xs if pred(x)] is eager. Generator ( ) is lazy. Nested comps hurt readability — prefer a loop if nested.",
    "skus = [line['sku'] for line in cart if line['qty'] > 0]")
add("What are *args and **kwargs?",
    "Extra unnamed toys go in *args. Extra named toys go in **kwargs.",
    "*args is a tuple of extra positional args; **kwargs a dict of extra keywords. Useful for wrappers, decorators, and forwarding to FastAPI/Pydantic.",
    "A logging decorator wraps any tool function without rewriting its signature.")
add("What is a decorator?",
    "A wrapper that adds behavior around a function without rewriting it.",
    "Syntactic sugar for f = deco(f). Common: @app.get, retries, auth, timing. Closures capture state. functools.wraps preserves metadata.",
    "Time a FastAPI inference handler with a decorator that logs p95-relevant duration.")
add("What is a generator? What is yield?",
    "A generator gives you items one at a time instead of building the whole pile.",
    "yield suspends the frame. Generators are iterators, memory-light, good for streaming tokens or reading large files. Send/throw exist but keep it simple.",
    "Stream SSE tokens with a generator that yields each LLM chunk then stops on disconnect.")
add("Mutable vs immutable types?",
    "Immutable means you cannot change the box; you make a new one. Mutable you can poke.",
    "Immutable: int, str, tuple, frozenset. Mutable: list, dict, set. Mutable default args are a classic bug (def f(x=[])). Hashable keys must be immutable.",
    "Never use {} as a default cache in a function — it is shared across calls.")
add("What is the GIL?",
    "Python's lock so only one thread runs Python bytecode at a time.",
    "I/O-bound work can still use threads. CPU-bound Python should use multiprocessing, C extensions, or native inference (ONNX/TensorRT) off the GIL.",
    "TF Lite/ONNX inference releases into native code; the GIL is not the cart's bottleneck — the NPU/CPU is.")
add("== vs is? shallow vs deep copy?",
    "== asks 'same value?'. is asks 'same object in memory?'. Shallow copy shares inner boxes; deep copy clones them.",
    "is compares identity. copy.copy vs copy.deepcopy. Nested dicts in agent state need deepcopy if you checkpoint.",
    "LangGraph state copies: mutating a nested list without copy can leak into the previous checkpoint.")
add("What are exceptions and context managers?",
    "try/except is a safety net. with is a helper that always tidies up, like closing a file.",
    "Use specific exceptions. with open, with lock, contextlib.contextmanager. Never swallow Exception silently in payment/checkout paths.",
    "WebSocket send: catch disconnect, cancel the LLM job, do not retry a charge.")
add("What is virtualenv / venv / pip / requirements vs lock files?",
    "A venv is a private toy box of libraries so projects do not fight.",
    "Pin versions (requirements.txt or poetry.lock/uv.lock). Reproducible Docker images. Never pip install unpinned in production.",
    "Cart service image pins FastAPI, Pydantic, onnxruntime — same versions in staging and prod.")
add("What is typing in Python? Optional, list[str], Protocol?",
    "Type hints are labels that help humans and tools catch mistakes before runtime.",
    "PEP 484. Pydantic uses types at the API boundary. mypy/pyright in CI. Optional[X] = X | None. Prefer list[str] over List[str] in 3.9+.",
    "add_to_cart(sku: str, qty: int) — Pydantic rejects qty=-1 before the agent proceeds.")
add("sync vs async Python? async/await?",
    "async is for waiting on the network without blocking the whole restaurant.",
    "asyncio event loop. FastAPI async def for I/O. Do not run CPU inference inside async without a threadpool — it stalls the loop.",
    "async WebSocket fan-in from devices; run ONNX infer in a worker pool.")
add("What is a module vs package? __init__.py? PYTHONPATH?",
    "A module is one file. A package is a folder of modules.",
    "Imports, circular import pitfalls, explicit relative imports. Keep API surface small.",
    "Split retrieval, agents, and serving packages so tests can mock tools.")

# OOP
add("What is OOP? Class vs object?",
    "A class is the cookie cutter. An object is a cookie.",
    "Encapsulation, abstraction, inheritance, polymorphism. Prefer composition over deep inheritance in services.",
    "A Detector base with YOLODetector and RTDETRDetector sharing a preprocess interface.")
add("What are the four pillars of OOP?",
    "Hide guts (encapsulation), show a simple face (abstraction), reuse a parent (inheritance), same action different types (polymorphism).",
    "Interviewers want examples, not slogans. SOLID: SRP, OCP, LSP, ISP, DIP — apply lightly, not as religion.",
    "PaymentGateway interface with NFC and card implementations — same charge() call.")
add("Overloading vs overriding? Abstract class vs interface?",
    "Overriding replaces a parent's method. Overloading is same name different args (Java). Python uses default args / *args instead.",
    "ABC/Protocol in Python; interface in Java/Kotlin. Abstract = cannot construct, must implement.",
    "Kotlin CheckoutUseCase overrides execute(); Java cannot override a static method as polymorphism.")
add("What is composition vs inheritance?",
    "Inheritance is 'is-a'. Composition is 'has-a'. Prefer has-a when you just need a helper.",
    "Deep hierarchies break. Inject a Retriever into an Agent rather than Agent extends Retriever.",
    "Lisa has a retriever, a tool box, and a tracer — it is not a subclass of LlamaIndex.")
add("What is encapsulation and why private fields?",
    "Keep the messy bits inside so callers cannot break invariants.",
    "Python _convension vs real privacy in Java/Kotlin. Validate in constructors.",
    "Cart total is computed from lines; callers should not set total=0 by hand.")

# Data structures & complexity
add("What is Big-O? Best / average / worst case?",
    "A guess of how work grows when the pile of data grows.",
    "O(1), O(log n), O(n), O(n log n), O(n²). State assumptions. Amortized vs worst. Memory also matters.",
    "Rerank 50 chunks with a cross-encoder is O(k) model calls — do not rerank 10M docs.")
add("Array vs linked list vs hash map vs tree vs heap?",
    "Array is a row of seats. Linked list is a chain. Hash map is lockers. Tree is a family tree. Heap is a priority line.",
    "Arrays: cache-friendly. Hash maps: expected O(1). Trees/heaps: ordered / priority. Know when each fails (hash collisions, unbalanced trees).",
    "Event_id → processed boolean is a hash set. Next-soonest retry is a heap.")
add("Stack vs queue vs deque? BFS vs DFS?",
    "Stack is last-in first-out (plates). Queue is first-in first-out (ticket line).",
    "DFS uses stack/recursion; BFS queue. LangGraph cycles need a visited/step budget like BFS/DFS on graphs.",
    "Agent loop detection is a visited set of (node, tool-signature).")
add("What is a graph? Directed vs undirected?",
    "Dots (nodes) and arrows (edges). Directed arrows have a direction.",
    "LangGraph is a directed graph with state. DAGs have no cycles; agents often need bounded cycles.",
    "Planner → retriever → tool → answer, with a loop edge capped at N.")
add("Binary search? When does it work?",
    "Guess the middle of a sorted list, throw away half, repeat.",
    "O(log n) on random-access sorted data. Off-by-one bugs are common. Interpolation search is a variant.",
    "Not for unsorted SKU lists — use a hash index instead.")
add("Recursion vs iteration? What is a stack overflow?",
    "Recursion is a function calling itself. Too deep and the call stack explodes.",
    "Tail recursion is not optimized in Python. Prefer iteration for deep trees; explicit stack.",
    "Do not recurse unbounded on a tool-calling agent — use a step counter.")
add("What is hashing? Collisions?",
    "A blender that turns a key into a locker number. Two keys can land in the same locker.",
    "Load factor, chaining vs open addressing, hashCode/equals contract in Java. Security: hash flooding.",
    "SKU strings hashed into a dict. Bad hashCode in Java breaks HashMap.")

# HTTP / REST
add("What is HTTP? Methods GET POST PUT PATCH DELETE?",
    "HTTP is how browsers and apps talk to servers. GET reads. POST creates. PUT replaces. PATCH nips. DELETE removes.",
    "Safe/idempotent: GET should not change state. PUT/DELETE idempotent. POST often not. Status codes: 2xx success, 4xx client, 5xx server.",
    "GET /products/{sku}. POST /cart/items. Do not GET to charge a card.")
add("What is REST?",
    "A style of API: resources with URLs, HTTP verbs, and stateless calls.",
    "Resource-oriented, HATEOAS rarely fully used. Versioning, pagination, error bodies. Contrast GraphQL (client picks fields) and RPC.",
    "Product catalogue REST; live cart telemetry is WebSocket, not REST polling.")
add("What are HTTP status codes 200, 201, 204, 400, 401, 403, 404, 409, 429, 500, 503?",
    "200 OK, 201 created, 400 you sent junk, 401 who are you, 403 you may not, 404 missing, 429 slow down, 500 we broke, 503 busy.",
    "401 unauthenticated vs 403 unauthorized. 409 conflict/idempotency. 429 rate limit. 502/504 gateway. Do not return 200 with an error payload for tools.",
    "add_to_cart of an unknown SKU: 404. Duplicate event id: 200/204 with the original result (idempotent).")
add("What is idempotency?",
    "Doing the same request twice should not double the side effect.",
    "Idempotency keys for payments and device events. PUT is idempotent; POST needs a key. Exactly-once is hard; at-least-once + idempotent handler is the usual design.",
    "Scan event_id already processed → ignore. Payment key reused → return original receipt.")
add("Headers, cookies, CORS, TLS?",
    "Headers are sticky notes on the request. TLS is the encrypted tunnel. CORS is the browser's guest list.",
    "Authorization: Bearer. Content-Type. CORS is a browser rule, not API security. TLS everywhere. Cookies: HttpOnly, Secure, SameSite.",
    "Mobile app uses bearer tokens; do not put secrets in query strings.")
add("What is JSON? JSON vs XML vs protobuf?",
    "JSON is nested labeled boxes of text, numbers, lists. XML is older tagged text. Protobuf is compact binary.",
    "JSON for public APIs; protobuf/Avro for high-QPS internal events. Schema evolution matters.",
    "LLM tool calls are JSON. IoT high-rate telemetry might be protobuf on the wire.")
add("Query params vs path vs body?",
    "Path is which thing. Query is filters. Body is the payload.",
    "Do not put PII in query logs. GET has no body in practice. Pagination: cursor > offset for large catalogues.",
    "GET /products?q=pasta. POST /assist with the basket JSON in the body.")
add("REST vs GraphQL vs gRPC vs WebSockets vs SSE?",
    "REST is ask/answer. GraphQL is pick-your-fields. gRPC is fast binary RPC. WebSockets are a phone call. SSE is a one-way radio.",
    "Choose by chat vs events vs CRUD. LLM tokens: SSE. Device telemetry: WebSocket. Catalogue: REST/GraphQL.",
    "Lisa streams SSE; trolley sensors use WebSockets into FastAPI/Spring Boot.")

# SQL
add("What is SQL? Primary key vs foreign key?",
    "SQL talks to tables. A primary key uniquely names a row. A foreign key points at another table's key.",
    "Normalization vs denormalization. Constraints enforce integrity that app code will forget.",
    "orders.id PK. orders.customer_id FK. Do not orphan cart lines.")
add("INNER vs LEFT vs RIGHT vs FULL join?",
    "INNER is only matches. LEFT keeps all left rows even without a match.",
    "NULLs in outer joins. Accidental INNER drop of unmatched products is a common bug in analytics.",
    "LEFT JOIN products to inventory so missing stock still shows the SKU.")
add("WHERE vs HAVING? GROUP BY?",
    "WHERE filters rows before grouping. HAVING filters after aggregates.",
    "SELECT sku, SUM(qty) FROM lines GROUP BY sku HAVING SUM(qty)>10. Index columns used in WHERE.",
    "Top SKUs sold per day for a merchant dashboard.")
add("What is an index? Clustered vs secondary? When does it hurt?",
    "An index is the book's back index — faster find, slower writes, extra storage.",
    "B-tree vs hash vs GIN (pgvector). Composite order matters. Use EXPLAIN ANALYZE. Too many indexes slow checkouts.",
    "INDEX on orders(customer_id, created_at). EXPLAIN before claiming a 40% API speedup.")
add("What is a transaction? ACID?",
    "A transaction is a bundle that all happens or none happens. ACID: Atomic, Consistent, Isolated, Durable.",
    "Isolation levels: read committed vs repeatable read vs serializable. Deadlocks. Saga for distributed checkout.",
    "Charge + emit receipt in one transaction; do not charge if insert fails.")
add("Normalization (1NF, 2NF, 3NF) vs denormalization?",
    "Normalization reduces duplicate facts. Denormalization copies facts for speed.",
    "OLTP vs OLAP. Event sourcing as an alternative. Know update anomalies.",
    "Catalogue name denormalized onto a receipt line so historical receipts do not change when the SKU is renamed.")
add("SQL injection and how to prevent it?",
    "Never glue user text into SQL like tape. Use parameters.",
    "Prepared statements, ORMs, least-privilege DB users. MCP/SQL tools are dangerous without allowlists.",
    "sku = request; execute('... WHERE sku=%s', [sku]) — never f-strings.")
add("NULL behavior in SQL? Three-valued logic?",
    "NULL means unknown. NULL = NULL is not true.",
    "IS NULL. COALESCE. Aggregates skip NULLs. Unique indexes and multiple NULLs depend on the engine.",
    "missing gluten_free flag is NULL, not false — Lisa must not claim 'not gluten-free'.")
add("OFFSET pagination vs keyset/cursor?",
    "OFFSET skips rows (gets slow). Cursor remembers the last id and continues.",
    "Large catalogues: keyset on (created_at, id). OFFSET 100000 is a full scan.",
    "Product admin list uses cursor pagination, not page=5000.")
add("What is N+1 query problem?",
    "You fetch a list, then one extra query per item. That is a thousand tiny trips.",
    "Eager load/join or IN (...) batch. ORMs hide this. Trace SQL in staging.",
    "Loading 50 cart lines then 50 product queries — join or batch instead.")

# Git
add("What is Git? commit, branch, merge, rebase?",
    "Git is a time machine for code. A commit is a snapshot. A branch is an alternate timeline.",
    "Merge creates a merge commit; rebase replays. Never rebase public shared history casually. PR reviews.",
    "Feature branch cursor/interview-guide-a8c9 merged to main, then gh-pages publish.")
add("git clone, status, add, commit, push, pull, fetch?",
    "clone copies. status looks. add stages. commit saves. push shares. pull fetches+merges.",
    "fetch vs pull. Origin vs upstream. Detached HEAD. .gitignore.",
    "Do not commit .env or model secrets. Pin PDFs that are meant to be public.")
add("merge conflict? how to resolve?",
    "Two people edited the same lines. You pick the combined truth.",
    "Open the markers, test, commit. Prefer smaller PRs to reduce conflicts.",
    "Two prompt files edited — keep both eval cases, do not drop tests.")
add("What is a pull request / code review?",
    "A request for teammates to read your change before it lands.",
    "Describe why, risk, test plan. Review for correctness, security, not nits only.",
    "Prompt change PRs must attach eval before/after scores.")
add("HEAD, stash, tag, cherry-pick?",
    "HEAD is where you are. stash pockets dirty files. tag names a version. cherry-pick copies one commit.",
    "Tags for releases (model-prompt-v12). Cherry-pick hotfixes carefully.",
    "Tag last-known-good prompt for rollback.")
add("force push risks?",
    "force push rewrites shared history and can erase teammates' work.",
    "Use --force-with-lease if you must. Protect main.",
    "Never force-push main/gh-pages of a public site without checking.")

# Linux / OS / networking extras
add("What is a process vs thread?",
    "A process is a program. Threads are workers inside it sharing memory.",
    "Isolation vs shared-memory races. GIL. Containers isolate processes.",
    "One FastAPI process, threadpool for ONNX; separate process for vLLM.")
add("stdin, stdout, stderr, exit codes?",
    "stdin in, stdout out, stderr complaints. Exit 0 means OK.",
    "CI fails on non-zero. Log structured JSON to stdout in K8s.",
    "Eval job exits 1 if groundedness drops — that blocks deploy.")
add("What is DNS, IP, port, TCP vs UDP?",
    "IP is the building address. Port is the apartment. TCP is a reliable call. UDP is a postcard.",
    "TLS on TCP. WebSockets upgrade HTTP. UDP for some realtime but not checkout.",
    "Cart app connects wss:// to the IoT gateway on 443.")
add("What is a deadlock? Race condition?",
    "Deadlock: two waiters each hold what the other needs. Race: winner depends on luck of timing.",
    "Locks, lock ordering, immutable messages, actor/queue models. Reproduce with stress tests.",
    "Two services updating the same cart line without optimistic versioning.")

# Java / Kotlin / Android fresher
add("Java vs Kotlin for Android?",
    "Kotlin is the modern Android language: less boilerplate, null-safety.",
    "Null safety, coroutines, data classes, interop with Java. Jetpack Compose is Kotlin-first. Java still appears in older modules.",
    "ezyCart Android app: Kotlin + existing Java libraries.")
add("What is null safety in Kotlin?",
    "String? might be missing. String cannot. The compiler nags you to check.",
    "?. ?: !! (avoid !!). Java interop platform types. Prevents a class of NPEs.",
    "sku: String not String? on add_to_cart.")
add("What is an Activity / Fragment / ViewModel?",
    "Activity is a screen. Fragment a piece of screen. ViewModel keeps data when the screen rotates.",
    "MVVM: UI observes ViewModel; ViewModel talks to repositories. SavedStateHandle.",
    "Cart screen ViewModel holds line items; rotation does not empty the cart.")
add("What is Jetpack Compose vs XML views?",
    "Compose describes UI as functions of state. XML was nested layout files.",
    "Recomposition, remember, unidirectional data flow. Interop with views exists.",
    "Staff Flutter app is another declarative UI; Android cart may use Compose.")
add("What is Flutter / Dart? Widget tree?",
    "Flutter paints its own UI on iOS and Android from one Dart codebase.",
    "Immutable widgets, setState/BLoC/Provider, platform channels. Good for staff tools; native may still win for tight hardware.",
    "Flutter staff/TV monitor and Flutter SDK lite for small vendors.")
add("What is an APK / Play release / ProGuard?",
    "APK is the install package. Play is the store. ProGuard/R8 shrinks and obfuscates.",
    "Signing, versionCode, staged rollout, mapping files for crash deobfuscation. CI with Jenkins/GitLab/Bitrise.",
    "Colan CI/CD cut ANR 70% and lifted performance 30% — know how you measured ANR.")
add("HTTP on mobile: Retrofit/OkHttp vs Ktor?",
    "Libraries that call REST from the phone.",
    "Interceptors for auth, retries, logging (no PII). Timeouts. Certificate pinning when needed.",
    "Android ezyCart calls backend; WebSocket client for live IoT.")
add("What is MVVM vs MVP vs MVC?",
    "Ways to split UI from logic so screens do not become god objects.",
    "MVVM + LiveData/Flow on Android; BLoC on Flutter. Test ViewModels without the UI.",
    "CartViewModel unit tests do not need an emulator.")
add("Coroutines / Flow vs RxJava vs callbacks?",
    "Coroutines are Kotlin's readable async. Flow is a stream of values.",
    "structured concurrency, cancellation, Dispatchers.IO vs Main. Prefer structured concurrency over callback hell.",
    "Collect device events on IO, update UI on Main.")
add("What is SOLID in one sentence each?",
    "Single job, open to extension, don't break subclasses, small interfaces, depend on abstractions.",
    "Use as a smell detector, not a checklist to gold-plate a trolley app.",
    "A 2000-line Activity violates SRP — split scanning, pay, and ads.")

# Misc fresher
add("What is JSON Schema / OpenAPI?",
    "A contract that says what fields exist and their types. OpenAPI documents REST APIs.",
    "FastAPI generates OpenAPI from Pydantic. Breaks are versioned. Clients stub from the spec.",
    "Tool JSON schemas for agents are the same idea as OpenAPI for humans.")
add("What is CI vs CD?",
    "CI is auto-test on every change. CD is auto-release when tests pass.",
    "Unit, lint, security scan, evals, image build, staging, prod with rollback.",
    "Prompt change blocked if eval groundedness drops.")
add("Unit vs integration vs e2e tests?",
    "Unit is one function. Integration is several pieces. e2e is the whole user journey.",
    "Test pyramid. Mock LLMs in unit tests; contract-test tools; a few e2e cart flows.",
    "Unit-test Pydantic tool args. Integration-test retriever+rerank with a fixture index.")
add("What is a race in checkout if two scans arrive?",
    "Two events at once can double-count if you are not careful.",
    "Per-cart lock or serial queue + idempotent event ids. Optimistic versioning on cart row.",
    "Same barcode twice: qty+=1 once per unique event_id.")
add("How do you read a stack trace?",
    "Start at the bottom cause, then the frames that led there.",
    "Caused by vs traceback. Map obfuscated Android stacks with mapping.txt.",
    "ANR traces point at main-thread IO — move work off main.")
add("What is UTF-8?",
    "A way to store every language's characters as bytes.",
    "Do not confuse character length with byte length. JSON default UTF-8.",
    "Tamil recipe names must round-trip in the assistant.")
add("Environment variables vs config files vs secret managers?",
    "Config is settings. Secrets are passwords. Do not commit secrets.",
    "12-factor. Kubernetes secrets / vault. Rotate. Different env per stage.",
    "Bedrock keys never in the Android app; they live on the server.")
add("What is pagination, filtering, sorting in APIs?",
    "Do not send the whole catalogue. Send a page, with filters and order.",
    "Stable sort keys, max page size, total vs cursor. Reject unbounded queries.",
    "Staff stock-audit lists aisles page by page.")
add("What is a 12-factor app (name a few)?",
    "A set of habits: config in env, stateless processes, logs as streams, etc.",
    "You need not recite all 12; show you build scalable services.",
    "Cart API is stateless; session in Redis/DB; logs to stdout.")
add("GET caching and Cache-Control / ETag?",
    "Browsers and CDNs can reuse a GET if you allow it.",
    "ETag/If-None-Match. Authorization headers often bypass shared caches. Do not cache personalized prices.",
    "Public product images cached; membership price never.")
add("What is a JWT? Risks?",
    "A signed blob saying who you are. Anyone with the blob looks like you until it expires.",
    "exp, iss, aud. Store securely on mobile. Revocation is hard — short TTL + refresh. Never put in localStorage on web if XSS.",
    "Staff app JWT cannot call shopper-only routes (403).")
add("Hash vs encryption vs encoding?",
    "Hash is one-way blender. Encryption is a lock with a key. Encoding is changing shape (Base64), not secret.",
    "Passwords: salted hash (bcrypt/argon2). PII at rest: encrypt. Base64 is not encryption.",
    "Do not Base64 a PAN and call it 'encrypted' in an LLM prompt.")
add("What is stdout logging vs a debugger?",
    "Logs tell the story later. A debugger is live stepping.",
    "Structured logs with request_id. Debug locally; traces in prod (LangSmith for LLM).",
    "Correlate cart_id across Android, WebSocket, and RAG spans.")

QUESTIONS = Q
