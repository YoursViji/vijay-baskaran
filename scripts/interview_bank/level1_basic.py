# Basic / fresher: Python, OOP, DS, HTTP, SQL, Git, Linux, Java/Kotlin intro
Q = []  # (question, kid, tech, [examples])

def add(q, kid, tech, *ex):
    Q.append((q, kid, tech, list(ex)))

# Python
add("What is Python and why is it used in AI?",
    "Python is a readable programming language that looks close to plain English, which is why beginners can learn it quickly. It is used in AI because the main libraries for data, training, and serving already live there, so you can try an idea without switching languages. You still have to measure later, because a notebook that feels fast is not automatically a production service.",
    "Python is a dynamically typed language with a huge ecosystem around NumPy, Pandas, PyTorch, and FastAPI, which is why it became the default for AI work. The trade-off is that pure Python is slower than compiled languages on CPU-bound loops, and the GIL means only one thread runs Python bytecode at a time. In production I prototype in Python, keep serving in Python when I/O or native extensions do the heavy work, and I profile before I rewrite a hot path. At Retailetics the AI services sit in FastAPI, while ONNX and TF Lite take vision off the interpreter so we stay under 100ms.",
    "At Retailetics I serve Lisa and the trolley inference APIs from Python FastAPI, and training plus ONNX export stay in Python as well.",
    "A notebook prototype is not production until it has tests, type checks, pinned dependencies, and a packaging path into a container.")
add("What is the difference between a list, tuple, set, and dict?",
    "A list is an ordered row of items that you can change, like cart lines you keep appending. A tuple is an ordered row that you lock after you create it, which is useful for fixed records. A set is a bag of unique values, so duplicates disappear. A dict is a labeled locker: you look up a value by a key instead of scanning the whole row.",
    "A list is ordered and mutable with amortized O(1) append. A tuple is immutable, and it is hashable only if every item inside is hashable, which is why tuples can be dict keys and lists cannot. A set stores unique items with average O(1) membership. A dict is a hash map from key to value and is the default structure for JSON-shaped data. I choose among them by whether I need order, uniqueness, mutability, or keyed lookup, and I do not use a list scan when a set or dict would be O(1).",
    "On ezyCart I cache known SKUs in a set for O(1) membership checks, and each cart is a list of dicts with sku and qty.",
    "I also put device event_ids into a set so the same scan cannot be charged twice if the trolley retries.")
add("What is a list comprehension?",
    "A list comprehension is a compact way to build a new list by walking another collection and applying a rule. You read it as 'make this value for each item if the condition is true.' It is great for short transforms and messy when you nest several of them.",
    "The form [f(x) for x in xs if pred(x)] is eager, so it builds the whole list in memory at once. A generator expression in parentheses is lazy and yields items as you iterate, which is the better default for large streams. Nested comprehensions often hide bugs, so I switch to a plain loop when the logic has more than one filter or a side effect. In production I use comprehensions for small mappings at the API boundary and generators when I stream tokens or file rows.",
    "When Lisa reads a cart I collect SKUs with skus = [line['sku'] for line in cart if line['qty'] > 0], which drops empty lines in one readable pass.")
add("What are *args and **kwargs?",
    "Sometimes a function should accept extra arguments without listing every name in advance. Extra unnamed values land in *args as a tuple, and extra named values land in **kwargs as a dict. That is how wrappers can forward whatever the inner function needs.",
    "*args is a tuple of leftover positional arguments and **kwargs is a dict of leftover keyword arguments. They are the standard way to write decorators, logging wrappers, and thin adapters that forward into FastAPI or Pydantic without copying every parameter. The trade-off is that a sloppy signature hides mistakes until runtime, so I still type the public API and only use *args/**kwargs at the edges. In production I keep the HTTP contract explicit and use forwarding inside helpers that should not care about every field.",
    "A timing decorator around a Lisa tool function uses *args and **kwargs so I can wrap any handler without rewriting its signature.")
add("What is a decorator?",
    "A decorator is a wrapper that adds behavior around a function without copying the function body. You write @retry above a function and Python hands that function to the wrapper. It is a clean way to add timing, auth, or logging in one place.",
    "A decorator is syntactic sugar for f = deco(f), and functools.wraps should copy the original name and docstring so traces stay readable. Common production uses are FastAPI route registration, retries, auth checks, and timing. Closures let the decorator hold state such as a counter or a circuit breaker. The trade-off is magic: too many stacked decorators make call stacks hard to follow, so I keep them thin and test the wrapped behavior. In production I decorate inference handlers to log duration that I can roll into p95, not to hide business logic.",
    "I time FastAPI inference handlers with a decorator that records duration so we can watch whether ONNX stays under 100ms.")
add("What is a generator? What is yield?",
    "A generator is a function that hands you items one at a time instead of building a giant list first. The yield keyword pauses the function, remembers where it was, and continues on the next request. That is how you stream a long answer without filling memory.",
    "yield suspends the stack frame and turns the function into an iterator, so memory stays proportional to one chunk rather than the whole result. Generators are the right shape for streaming LLM tokens, reading large files, and paging database rows. send and throw exist, but I keep generators simple and treat disconnect as a StopIteration path. The trade-off versus a list is that you can walk a generator only once unless you rebuild it. In production Lisa streams SSE from a generator that yields each token and stops when the client disconnects.",
    "Lisa streams SSE tokens with a generator that yields each LLM chunk and then stops cleanly on disconnect so we do not keep paying for unused tokens.")
add("Mutable vs immutable types?",
    "An immutable value cannot be changed in place, so any edit creates a new object, like a new string. A mutable value can be poked, like appending to a list or updating a dict. Mixing them carelessly is how shared default arguments surprise you later.",
    "Immutable types include int, str, tuple, and frozenset. Mutable types include list, dict, and set. Hashable dict keys must be immutable, which is why a list cannot be a key. Mutable default arguments such as def f(x=[]) are a classic bug because the empty list is created once and shared across calls. In production I treat request bodies as immutable after validation and I deepcopy nested agent state when I checkpoint, so a later mutation cannot leak into the previous snapshot.",
    "I never use a mutable dict as a default cache argument in a function, because that cache would be shared across every caller by accident.")
add("What is the GIL?",
    "The GIL is Python's Global Interpreter Lock, a lock that lets only one thread run Python bytecode at a time. Think of it as a single microphone in a meeting: many people can wait, but only one talks Python at once. Waiting on the network can still overlap, which is why threads help I/O even with the GIL.",
    "The Global Interpreter Lock serializes Python bytecode, so CPU-bound Python threads do not get true multi-core speedup. I/O-bound work still benefits from threads because a thread releases the GIL while it waits on sockets or disk. For heavy CPU I use multiprocessing, a process pool, or native extensions such as ONNX Runtime and TF Lite, which release the GIL while they run compiled kernels. In production on ezyCart I do not fight the GIL for vision: inference runs in native ONNX or TF Lite under 100ms, and FastAPI uses async plus a worker pool so the event loop is not stuck in Python loops.",
    "TF Lite and ONNX inference drop into native code, so the GIL is not the cart's bottleneck. The NPU or CPU kernel is.")
add("== vs is? shallow vs deep copy?",
    "== asks whether two values look the same, while is asks whether they are the exact same object in memory. A shallow copy makes a new outer box but still shares the inner boxes. A deep copy clones the nested boxes too, which is what you want before you mutate a snapshot.",
    "is compares identity and == compares equality, so two equal strings may or may not be the same object. copy.copy is shallow and copy.deepcopy walks nested containers. The trade-off is cost: deepcopy is safer for nested dicts and lists, but it is slower, so I do not clone huge tensors by accident. In production, agent or cart state that will be checkpointed needs a deep copy of nested lists, otherwise a later mutation leaks into the previous snapshot.",
    "When we snapshot Lisa or LangGraph-style state, mutating a nested list without a deep copy can leak changes into the previous checkpoint and make retries lie.")
add("What are exceptions and context managers?",
    "try and except are a safety net for errors you can handle, such as a missing file or a closed socket. A context manager, used with with, always tidies up at the end, like closing a file even if you crash. Together they keep cleanup from depending on every path remembering to close things.",
    "I catch specific exceptions and let unexpected ones bubble so we get a real failure instead of a silent wrong charge. with open, with lock, and contextlib.contextmanager guarantee release of files, mutexes, and HTTP clients. Swallowing bare Exception in a checkout path is a production incident waiting to happen. In production a WebSocket disconnect is an expected exception: we cancel the LLM job and we never retry a payment from that path.",
    "On the trolley WebSocket, if the client disconnects I catch it, cancel the in-flight Lisa job, and I do not retry a charge that may already have been sent.")
add("What is virtualenv / venv / pip / requirements vs lock files?",
    "A venv is a private library folder so one project's packages do not fight with another project's packages. pip installs into that folder, and a requirements file lists what you need. A lock file goes further and pins the exact versions that were tested.",
    "Virtualenv or venv isolates dependencies, pip installs them, and a requirements.txt is a human list while poetry.lock or uv.lock is a fully resolved graph. The trade-off is convenience versus reproducibility: unpinned installs drift, and that drift shows up as 'works on my laptop' outages. In production I pin every runtime package in the Docker image and I install the same lock in staging and prod. I never pip install an unpinned package onto a live cart service.",
    "The cart service image pins FastAPI, Pydantic, and onnxruntime so staging and production run the same versions we tested.")
add("What is typing in Python? Optional, list[str], Protocol?",
    "Type hints are labels that tell humans and tools what a function expects, such as a string SKU or a list of names. They do not run the program by themselves, but checkers can catch many mistakes before you ship. Optional means a value may also be missing, which is None in Python.",
    "PEP 484 type hints are the contract I put on public functions, and Pydantic enforces those types at the API boundary. mypy or pyright in CI catches drift that unit tests miss. Optional[X] is X | None, list[str] is preferred over List[str] on Python 3.9+, and Protocol describes a structural interface without forcing inheritance. The trade-off is a little annotation cost for a lot of safety. In production add_to_cart(sku: str, qty: int) is rejected by Pydantic if qty is negative before the agent proceeds.",
    "Lisa's add_to_cart(sku: str, qty: int) uses Pydantic so qty=-1 never reaches the cart service.")
add("sync vs async Python? async/await?",
    "Synchronous code waits for one thing to finish before it starts the next, like a cashier who serves one customer at a time. Async lets the same worker start other waiting work, such as network calls, without blocking the whole restaurant. You write async def and await the slow I/O.",
    "asyncio runs an event loop, and FastAPI async def is the right shape for I/O such as database calls and WebSockets. The trade-off is that CPU work inside async def stalls every other connection on that loop. In production I keep request handlers async, and I run ONNX inference in a thread or process pool so a 30ms native call cannot freeze token streaming. Mixing blocking libraries into async without a pool is a classic p95 killer.",
    "ezyCart fans device WebSockets in async FastAPI, and ONNX inference runs in a worker pool so the event loop stays free.")
add("What is a module vs package? __init__.py? PYTHONPATH?",
    "A module is one Python file you can import. A package is a folder of modules, often with an __init__.py that marks it as a package. PYTHONPATH tells Python where to look for those folders if they are not already installed.",
    "Imports should be explicit, packages should expose a small public surface, and circular imports are a design smell that I break by moving shared types into a thin module. __init__.py can re-export, but I keep it light so importing a package is not expensive. PYTHONPATH hacks work locally and fail in Docker, so production images install the package with pip. In the Lisa stack I split retrieval, agents, and serving into packages so tests can mock tools without importing the whole service.",
    "I keep retrieval, agent tools, and FastAPI serving in separate packages so tests can mock a retriever without booting the full Lisa service.")

# OOP
add("What is OOP? Class vs object?",
    "Object-oriented programming means you group data and the actions on that data into a class, which is the cookie cutter. An object is one cookie made from that cutter, with its own values. You talk to the object through methods instead of scattering the same logic across files.",
    "A class defines fields and methods; an object is a runtime instance. Encapsulation, abstraction, inheritance, and polymorphism are the usual pillars, but in services I prefer composition over deep inheritance because long hierarchies become brittle. The trade-off is that OOP can hide control flow if you over-abstract, so I keep class trees shallow and interfaces small. In production a Detector base with YOLODetector and RTDETRDetector sharing preprocess is enough polymorphism; I do not build a six-level vision framework.",
    "On ezyCart a Detector base class lets YOLODetector and RTDETRDetector share the same preprocess and postprocess interface while swapping the model file.")
add("What are the four pillars of OOP?",
    "Encapsulation hides the messy internals so callers cannot break the rules. Abstraction shows a simple face, like charge() instead of every card-network detail. Inheritance reuses a parent, and polymorphism means the same action can behave differently for different types.",
    "Interviewers want examples, not slogans, so I walk through encapsulation, abstraction, inheritance, and polymorphism on a real interface. SOLID is a useful smell detector (single responsibility, open for extension, Liskov, small interfaces, depend on abstractions) but it is not a religion to gold-plate a trolley app. The trade-off of inheritance-heavy designs is fragility when a subclass needs only one method. In production I put a PaymentGateway interface in front of NFC and card implementations so checkout calls the same charge() method.",
    "Checkout talks to a PaymentGateway interface with NFC and card implementations, so the same charge() call works for both without the UI knowing the vendor.")
add("Overloading vs overriding? Abstract class vs interface?",
    "Overriding means a child class replaces a parent method with its own version. Overloading means the same name with different arguments, which Java supports and Python usually handles with default arguments or *args. An abstract class or interface is a contract you cannot construct until someone fills in the missing methods.",
    "Java and Kotlin distinguish overloading from overriding; Python does not overload by signature in the Java sense and uses defaults, *args, or singledispatch instead. Abstract classes in Python are ABC types, and Protocol is a structural interface. Abstract means you cannot construct it and subclasses must implement the required methods. The trade-off is rigidity versus a clear contract. In production I define a CheckoutUseCase with execute() that Kotlin can override, and I never pretend a static Java method is polymorphic.",
    "Kotlin CheckoutUseCase overrides execute() for each payment rail, and I do not treat a Java static helper as a polymorphic override.")
add("What is composition vs inheritance?",
    "Inheritance says a child is a kind of parent, like a YOLO detector is a detector. Composition says an object has a helper, like Lisa has a retriever. When you only need a helper, has-a is usually safer than is-a.",
    "Deep inheritance trees break when a subclass needs only part of the parent. Composition injects collaborators, which is easier to test and swap. The trade-off is a few more constructor arguments in exchange for a shallower, more honest design. In production I inject a Retriever into Lisa rather than making the agent a subclass of LlamaIndex, and I inject tracers and tool boxes the same way.",
    "Lisa has a retriever, a tool box, and a tracer as composed parts. It is not a subclass of LlamaIndex.")
add("What is encapsulation and why private fields?",
    "Encapsulation means the messy bits stay inside the object so callers cannot break the rules. Private fields are the walls that stop someone from setting a cart total to zero by hand. Callers use methods that keep the data consistent.",
    "Python uses a _prefix convention and name mangling for __, while Java and Kotlin can enforce real privacy. I validate in constructors and keep derived fields computed, not stored as writable public state. The trade-off is a little more API surface for a lot fewer invariant bugs. In production the cart total is computed from lines, and callers cannot set total=0 because that would desync checkout from what was scanned.",
    "ezyCart computes cart total from line items, so a caller cannot set total=0 by hand and skip a scanned SKU.")

# Data structures & complexity
add("What is Big-O? Best / average / worst case?",
    "Big-O is a way to guess how much work grows when the pile of data grows, ignoring constant factors. Best case is the lucky path, average is typical, and worst case is the painful path you must still survive. Memory growth matters too, not only time.",
    "Common classes are O(1), O(log n), O(n), O(n log n), and O(n²), and I state whether I mean time or memory and which case. Amortized O(1) append is not the same as worst-case O(n) when a list resizes. The trade-off of a fancy structure is often memory or implementation risk. In production I will rerank fifty recipe chunks with a cross-encoder, but I will not pretend that is fine for ten million documents, because that is O(k) model calls with a huge k.",
    "Lisa reranks about fifty retrieved recipe chunks, which is a bounded O(k) model cost. I would never rerank the whole catalogue.")
add("Array vs linked list vs hash map vs tree vs heap?",
    "An array is a row of seats with fast index access. A linked list is a chain that is cheap to splice but slow to jump into the middle. A hash map is lockers with labels, a tree is a family tree that stays ordered, and a heap is a priority line that always exposes the next most urgent item.",
    "Arrays and Python lists are cache-friendly for scans and index access. Hash maps give expected O(1) lookup and fail under bad hash functions or huge load factors. Trees and heaps give ordered or priority operations at O(log n), and unbalanced trees degrade. In production event_id membership is a hash set, and the next-soonest retry is a heap, because those match the access pattern instead of forcing everything into a list.",
    "Processed scan event_ids live in a hash set, and the next retry time for a failed IoT message lives on a heap so we always pop the soonest job.")
add("Stack vs queue vs deque? BFS vs DFS?",
    "A stack is last-in first-out, like a pile of plates. A queue is first-in first-out, like a ticket line. A deque lets you add or remove from both ends, which is handy when you need both behaviors.",
    "DFS walks with a stack or recursion and goes deep first. BFS walks with a queue and explores neighbors before grandchildren. Agent graphs need a visited set and a step budget the same way graph search does, or a tool loop never ends. In production I treat Lisa's agent loop like a bounded graph walk: a visited set of node plus tool signature, and a max-step cap, rather than unbounded recursion.",
    "Lisa's loop detection is a visited set of (node, tool-signature) plus a step budget, which is the same idea as not revisiting nodes in BFS or DFS.")
add("What is a graph? Directed vs undirected?",
    "A graph is a set of dots called nodes and the links between them called edges. In a directed graph each link has an arrow, so A to B is not the same as B to A. An undirected graph is a two-way street.",
    "LangGraph-style agents are directed graphs with state on the nodes, and a DAG has no cycles. Agents often need a bounded cycle, such as retrieve then tool then answer then retrieve again, which is fine only with a cap. The trade-off of adding edges is more power and more ways to loop forever. In production Lisa is planner to retriever to tool to answer, with a loop edge capped at N steps.",
    "The Lisa graph is planner, retriever, tool, then answer, with a loop edge that is hard-capped so a bad tool result cannot spin forever.")
add("Binary search? When does it work?",
    "Binary search guesses the middle of a sorted list, throws away the half that cannot contain the answer, and repeats. It is fast because each step halves the remaining work. It only works when the data is sorted and you can jump to an index.",
    "Binary search is O(log n) on random-access sorted data, and off-by-one errors in the low/high window are the usual bugs. It does not help an unsorted SKU list; that needs a hash index. Interpolation search is a variant when values are uniformly distributed, but I rarely need it. In production catalogues I index by SKU hash rather than binary-searching an unsorted Python list.",
    "I do not binary-search unsorted SKU lists on the trolley. I use a hash index so lookup stays O(1) as the catalogue grows.")
add("Recursion vs iteration? What is a stack overflow?",
    "Recursion is a function calling itself until a base case stops it. Iteration is a loop that you control with a counter or a stack you own. If recursion goes too deep, the call stack overflows and the program crashes.",
    "Python does not optimize tail recursion, so a deep recursive walk will hit sys.getrecursionlimit. I prefer iteration or an explicit stack for deep trees and for any agent loop. The trade-off of recursion is prettier code versus a hidden depth bomb. In production I never recurse unbounded on tool calling; Lisa has a step counter that stops the graph.",
    "A tool-calling agent that recurses on every tool result will overflow or burn tokens. Lisa uses a step counter and an explicit graph instead.")
add("What is hashing? Collisions?",
    "Hashing is a blender that turns a key into a locker number so you can jump there instead of scanning. Two different keys can land in the same locker, and that is a collision. A good map still works; it just chains or probes to separate those keys.",
    "Hash maps depend on a load factor and a collision strategy such as chaining or open addressing. In Java the hashCode and equals contract must stay consistent or HashMap silently breaks. Hash flooding is a security issue if untrusted keys can force many collisions. In production SKU strings hash into a dict, and I do not implement my own hash table unless I have a measured reason.",
    "Cart SKUs are hashed into a dict for lookup. A broken hashCode in a Java service would turn that map into a linked list and show up as checkout latency.")

# HTTP / REST
add("What is HTTP? Methods GET POST PUT PATCH DELETE?",
    "HTTP is the request and response language browsers and apps use to talk to servers. GET reads, POST creates, PUT replaces the whole resource, PATCH changes a piece, and DELETE removes it. You should not use GET for something that charges a card, because GET is supposed to be a safe read.",
    "GET should be safe and not change server state. PUT and DELETE are idempotent; POST often is not unless you add an idempotency key. Status classes are 2xx success, 4xx client fault, and 5xx server fault. In production the catalogue is GET /products/{sku} and add-to-cart is POST /cart/items, and I refuse designs that charge a card on GET because crawlers and retries would double-bill.",
    "ezyCart uses GET /products/{sku} for the catalogue and POST /cart/items for scans. We never charge a card on a GET.")
add("What is REST?",
    "REST is a style for APIs where you name resources with URLs, use HTTP verbs, and keep each call stateless. The server does not remember your previous click in hidden session magic; you send what it needs each time. It is a good fit for catalogues and a poor fit for a live video-like cart stream.",
    "Resource-oriented HTTP with JSON is what most teams mean by REST, and full HATEOAS is rare. You still need versioning, pagination, and typed error bodies. GraphQL lets the client pick fields, and RPC hides resources behind procedures. In production the product catalogue is REST, while live cart telemetry is a WebSocket, because polling REST would waste battery and add latency.",
    "The ezyCart catalogue is a REST resource API. Live trolley telemetry uses WebSockets into FastAPI and Spring Boot instead of REST polling.")
add("What are HTTP status codes 200, 201, 204, 400, 401, 403, 404, 409, 429, 500, 503?",
    "200 means OK, 201 means created, and 204 means success with no body. 400 means the client sent junk, 401 asks who you are, 403 says you may not, 404 means missing, 409 is a conflict, and 429 asks you to slow down. 500 means we broke, and 503 means the service is overloaded or down for a bit.",
    "401 is unauthenticated and 403 is authenticated but not allowed, and mixing them confuses clients and security reviews. 409 is the conflict or idempotency collision, 429 is rate limit, and 502 or 504 point at a gateway. Tools and agents should not get HTTP 200 with an error payload, because they will treat it as success. In production an unknown SKU is 404, a duplicate event id returns the original result with 200 or 204, and a Bedrock outage surfaces as 503 with a fallback path.",
    "add_to_cart of an unknown SKU returns 404. A duplicate scan event_id returns 200 or 204 with the original result so retries stay idempotent.")
add("What is idempotency?",
    "Idempotency means doing the same request twice does not double the side effect. If the trolley retries a scan, you should still add the item once. Payments need an idempotency key for the same reason.",
    "PUT is naturally idempotent; POST needs an idempotency key if it creates a charge or a cart line. Exactly-once delivery is hard across networks, so the usual design is at-least-once delivery plus an idempotent handler keyed by event_id. The trade-off is extra storage of processed keys versus duplicate charges. In production a scan event_id that we already processed is ignored, and a reused payment key returns the original receipt.",
    "If the same barcode scan arrives twice with one event_id, we process it once. A reused payment idempotency key returns the original receipt instead of charging again.")
add("Headers, cookies, CORS, TLS?",
    "Headers are sticky notes on the request, such as who you are and what format you speak. TLS is the encrypted tunnel so those notes are not readable on the wire. CORS is the browser's guest list for which websites may call your API, and cookies are small bits of state the browser stores.",
    "Authorization Bearer tokens, Content-Type, and correlation ids belong in headers. CORS is a browser rule, not an API security control, so a mobile app or server can still call you. TLS should be everywhere, and cookies that hold sessions need HttpOnly, Secure, and SameSite. In production the Android ezyCart app uses bearer tokens, secrets never go in query strings, and Lisa does not put Bedrock keys on the phone.",
    "The ezyCart mobile app sends bearer tokens in headers. We never put secrets or member identifiers in query strings that will be logged.")
add("What is JSON? JSON vs XML vs protobuf?",
    "JSON is nested labeled boxes of text, numbers, lists, and true or false, and it is the common language of web APIs. XML is older tagged text that is more verbose. Protobuf is compact binary with a schema, which is better when you send many small messages per second.",
    "JSON is the right default for public APIs and LLM tool calls because humans and models can read it. Protobuf or Avro is better for high-QPS internal telemetry where schema evolution and bytes matter. The trade-off is debuggability versus size and strict schemas. In production Lisa tools speak JSON, and I would consider protobuf only for high-rate IoT if JSON encoding showed up in profiles.",
    "Lisa tool calls are JSON. High-rate trolley telemetry could move to protobuf on the wire if JSON encoding ever became the measured bottleneck.")
add("Query params vs path vs body?",
    "The path says which thing you mean, such as /products/EZY-1044. Query parameters are filters and options, such as search text or page size. The body carries the payload of a write, such as a basket JSON.",
    "GET should not rely on a body, PII should not sit in query strings because they leak into logs and referrers, and pagination should prefer a cursor over a huge offset. Path params identify a resource; query params filter it. In production search is GET /products?q=pasta and Lisa assist is POST /assist with the basket in the body so we do not log the whole cart on a query string.",
    "Catalogue search is GET /products?q=pasta. Lisa assist is POST /assist with the basket JSON in the body so cart contents are not pasted into access logs.")
add("REST vs GraphQL vs gRPC vs WebSockets vs SSE?",
    "REST is ask and answer on resources. GraphQL lets the client pick fields. gRPC is fast binary RPC, WebSockets are a two-way phone call, and SSE is a one-way radio from server to client. You pick the one that matches the traffic shape, not the one that sounds newest.",
    "CRUD catalogues fit REST or GraphQL. Chat token streams fit SSE. Device telemetry and live cart state fit WebSockets. gRPC is strong inside a service mesh and awkward in a browser. In production Lisa streams tokens over SSE, trolley sensors use WebSockets into FastAPI and Spring Boot, and the product catalogue stays REST.",
    "Lisa streams answers over SSE. Trolley sensors use WebSockets into FastAPI and Spring Boot so scans are not polled over REST.")

# SQL
add("What is SQL? Primary key vs foreign key?",
    "SQL is the language you use to talk to tables in a database. A primary key uniquely names a row, like an order id. A foreign key points at another table's key, like an order pointing at a customer, so you cannot leave orphan rows as easily.",
    "Constraints belong in the database because application code will forget them under a bug or a race. Normalization reduces duplicate facts; denormalization copies them for read speed. In production orders.id is the primary key, orders.customer_id is a foreign key, and cart lines cannot exist without a cart because that would orphan scanned items at checkout.",
    "orders.id is a primary key and orders.customer_id is a foreign key. Cart lines are not allowed to exist without a parent cart, so we do not orphan scans.")
add("INNER vs LEFT vs RIGHT vs FULL join?",
    "An INNER join keeps only rows that match on both sides. A LEFT join keeps every left row even when the right side has no match, filling gaps with NULL. RIGHT is the mirror, and FULL keeps unmatched rows from both sides.",
    "The common analytics bug is an accidental INNER join that drops products with no inventory row, which then looks like missing SKUs. NULLs from outer joins must be handled or aggregates lie. I default to LEFT when the left side is the entity I must still show. In production I LEFT JOIN products to inventory so a missing stock row still shows the SKU on a staff list.",
    "Staff inventory views LEFT JOIN products to stock so a SKU with no stock row still appears, instead of silently disappearing from an INNER join.")
add("WHERE vs HAVING? GROUP BY?",
    "WHERE filters individual rows before you group them. GROUP BY folds rows that share a key into one bucket, and HAVING filters those buckets after you aggregate. That is why you cannot put SUM in WHERE the same way you put it in HAVING.",
    "A typical query is SELECT sku, SUM(qty) FROM lines GROUP BY sku HAVING SUM(qty) > 10, and columns in WHERE should be indexed if the table is large. Mixing WHERE and HAVING incorrectly is a fresher bug that produces empty dashboards. In production merchant dashboards group sales by SKU and day in SQL, not in Python loops after downloading the whole table.",
    "A merchant dashboard for top SKUs sold per day is a GROUP BY sku, day query with HAVING on the summed quantity, not a Python loop over every line.")
add("What is an index? Clustered vs secondary? When does it hurt?",
    "An index is like the back of a book: it makes finding a value faster, but you pay extra storage and slower writes. A clustered index is the order the rows are stored; a secondary index is an extra lookup structure. Too many indexes make every checkout write update many trees.",
    "B-trees are the default, hash indexes help equality, and GIN or pgvector help arrays and embeddings. Composite index column order must match the query. EXPLAIN ANALYZE is how I prove an index helps, because guessing is how you slow writes. In production I index orders(customer_id, created_at) and I would not claim a 40% backend speedup without an EXPLAIN, which is the same discipline we used when Colan backends got about 40% faster.",
    "I add INDEX on orders(customer_id, created_at) and run EXPLAIN ANALYZE before claiming a speedup. At Colan we measured about 40% faster backends the same way, not by adding indexes blindly.")
add("What is a transaction? ACID?",
    "A transaction is a bundle of steps that all happen or none happen, like charge and write the receipt together. ACID means Atomic, Consistent, Isolated, and Durable. If the insert fails, the charge should not stay behind.",
    "Isolation levels range from read committed to repeatable read to serializable, and each trades throughput for fewer anomalies. Deadlocks happen when two transactions grab locks in opposite orders. Distributed checkout often needs a saga because you cannot have one ACID transaction across a bank and your database. In production I charge and emit a receipt in one database transaction where I can, and I never keep a charge if the receipt insert fails.",
    "Checkout writes the receipt in the same transaction as marking the cart paid. If the insert fails, we do not keep a dangling charge record.")
add("Normalization (1NF, 2NF, 3NF) vs denormalization?",
    "Normalization stores each fact once so you do not update it in five places. First, second, and third normal form are steps that remove repeating groups and facts that depend on the wrong key. Denormalization copies a fact on purpose for faster reads, such as a product name printed on a receipt.",
    "OLTP systems stay closer to 3NF so updates stay consistent. OLAP and receipts often denormalize because history must not change when a SKU is renamed tomorrow. Event sourcing is another way to keep history without wide mutable rows. In production the catalogue is normalized, and a receipt line stores the name as it was at purchase so historical receipts stay stable.",
    "We denormalize the catalogue name onto a receipt line so a later SKU rename cannot rewrite yesterday's shopper receipt.")
add("SQL injection and how to prevent it?",
    "SQL injection happens when you glue user text into a query like tape, and the user types a command instead of a name. The fix is to use parameters so the database treats input as data, never as code. You also give the database user as few powers as it needs.",
    "Prepared statements, bound parameters, and ORMs that escape correctly are the baseline. Least-privilege database users limit the blast radius. LLM or MCP SQL tools are dangerous without allowlists because the model can be tricked into writing a DROP. In production sku comes from the request and we execute with a bound parameter, never an f-string.",
    "The cart lookup is execute('... WHERE sku=%s', [sku]). I never build that WHERE clause with an f-string from request text.")
add("NULL behavior in SQL? Three-valued logic?",
    "NULL means unknown, not zero and not false. In SQL, NULL = NULL is not true, because two unknowns are not known to be equal. You check IS NULL, and you use COALESCE when you need a fallback value.",
    "Three-valued logic is true, false, and unknown, so WHERE gluten_free = FALSE will not return NULL rows. Aggregates skip NULLs, which can hide missing data. Unique indexes treating multiple NULLs as distinct depends on the engine. In production a missing gluten_free flag stays NULL, and Lisa must not say the item is not gluten-free.",
    "If gluten_free is NULL on a product, Lisa must not claim the item is not gluten-free. Unknown is not the same as false.")
add("OFFSET pagination vs keyset/cursor?",
    "OFFSET pagination skips the first N rows and then reads a page, which gets slower as N grows because the database still walks those rows. Cursor or keyset pagination remembers the last id or timestamp and continues from there. For a huge catalogue, the cursor stays fast.",
    "OFFSET 100000 is often a full scan plus skip, which is why admin pages die at high page numbers. Keyset on (created_at, id) is stable if the sort is unique. The trade-off is that you cannot jump to page 500 as easily. In production the product admin list uses cursor pagination, not page=5000.",
    "The product admin list pages with a cursor on (created_at, id). We do not offer page=5000 with OFFSET because that would scan tens of thousands of rows.")
add("What is N+1 query problem?",
    "N+1 means you fetch a list of N items and then run one extra query per item. Fifty cart lines become fifty extra product lookups, which is a thousand tiny trips if the cart is large. The fix is to join or to batch with IN.",
    "ORMs hide N+1 because lazy relations look like field access. I eager-load, join, or batch ids, and I trace SQL in staging so a new relation does not ship a surprise. The trade-off of a join is a wider row versus dozens of round trips. In production loading fifty cart lines then fifty product queries is a bug; we join or batch instead.",
    "Loading fifty ezyCart lines and then fifty product queries is the N+1 I watch for. We join products in one query or batch SKUs with IN.")

# Git
add("What is Git? commit, branch, merge, rebase?",
    "Git is a time machine for code that stores snapshots called commits. A branch is an alternate timeline where you try a feature without breaking the main line. Merge combines timelines, and rebase replays your commits on top of a newer base.",
    "A commit is a snapshot with a message, a branch is a pointer, merge creates a merge commit, and rebase rewrites your local commits onto another tip. I never rebase public shared history casually because it forces teammates to recover. Pull requests are the review gate. In production work I use a feature branch, merge to main after review, and I do not rewrite main.",
    "I land interview-guide work on a feature branch, merge to main after review, and then publish. I do not rebase shared main to make the history look linear.")
add("git clone, status, add, commit, push, pull, fetch?",
    "clone copies a repository, status shows what changed, and add stages files for the next snapshot. commit saves that snapshot locally, push shares it, fetch downloads without merging, and pull fetches and integrates. Those seven commands are most of daily Git.",
    "fetch updates remote refs without touching your working tree; pull is fetch plus merge or rebase. origin is your copy's default remote, and detached HEAD means you are not on a branch. .gitignore keeps build junk and secrets out. In production I never commit .env files or model secrets, and I only pin public artifacts that are meant to be public.",
    "I never commit .env files, API keys, or model weights. Public PDFs that are meant to ship with the site are pinned on purpose.")
add("merge conflict? how to resolve?",
    "A merge conflict means two people edited the same lines and Git will not guess. You open the markers, keep the combined truth, run tests, and then commit the resolution. Smaller pull requests make this rare.",
    "Conflicts are resolved in the working tree, not by force-pushing away someone else's work. I prefer smaller PRs and frequent merges from main to reduce conflict size. After resolving I run the relevant tests because a naive keep-both can duplicate or drop logic. In production if two prompt files conflict, I keep both eval cases rather than dropping tests to make Git happy.",
    "If two prompt files conflict, I keep both eval cases and re-run the tests. I do not delete a test file just to clear conflict markers.")
add("What is a pull request / code review?",
    "A pull request is a request for teammates to read your change before it lands on the main branch. Review is for correctness, security, and missing tests, not only for nits. You describe why you changed it, what could break, and how you tested.",
    "A good PR states the why, the risk, and the test plan. Reviewers should look for behavioral bugs and security issues first. Nitpicking style without a linter wastes time. In production a prompt change should attach eval before-and-after scores so we do not ship a quieter but less grounded Lisa.",
    "Prompt-change pull requests for Lisa must attach eval scores before and after so a fluent regression cannot hide behind a green unit test.")
add("HEAD, stash, tag, cherry-pick?",
    "HEAD is the commit you are standing on. stash pockets dirty files so you can switch branches, a tag names a version, and cherry-pick copies one commit onto another branch. Tags are how you mark a release you might need to roll back to.",
    "Tags should be immutable release names such as a prompt or model version. Cherry-pick is for hotfixes and is easy to duplicate if you later merge the original branch. stash is local and easy to lose, so I do not stash production fixes overnight. In production I tag a last-known-good prompt so we can roll Lisa back without hunting through the log.",
    "I tag the last-known-good Lisa prompt so a bad eval on main can roll back to a named version instead of a remembered hash.")
add("force push risks?",
    "A force push rewrites the shared history and can erase a teammate's commit that you never pulled. It is how people lose work on a branch everyone is using. If you must rewrite a private branch, force-with-lease is the safer form.",
    "git push --force overwrites the remote tip. --force-with-lease still fails if someone else pushed, which is the minimum bar. Protected main should forbid force pushes. In production I never force-push main or a public site branch without checking, because that can drop a release or a teammate's fix.",
    "I never force-push main or the public site branch without checking who else pushed. A lease still beats a blind force.")

# Linux / OS / networking extras
add("What is a process vs thread?",
    "A process is a running program with its own memory. Threads are workers inside that process that share memory, which is why they can race. Isolation is easier between processes; sharing is cheaper between threads.",
    "Processes isolate crashes and memory; threads share an address space and need locks or immutability. Python's GIL further limits CPU threads, so CPU-heavy work often wants processes anyway. Containers isolate processes, not magic. In production one FastAPI process owns the HTTP loop, a thread pool runs ONNX, and a separate process would host something like vLLM if we served a local LLM.",
    "ezyCart serving is one FastAPI process with a thread pool for ONNX. A local LLM would sit in a separate process rather than on the API loop.")
add("stdin, stdout, stderr, exit codes?",
    "stdin is input, stdout is normal output, and stderr is the complaint channel. An exit code of zero means success, and any other number means failure to whoever started the program. Continuous integration treats a non-zero exit as a red build.",
    "In Kubernetes I log structured JSON to stdout and keep stderr for true process errors. CI fails the job on non-zero, so eval scripts must exit 1 when quality drops. Mixing human logs and machine metrics on unstructured stdout makes scraping painful. In production an eval job that sees groundedness drop exits 1 and that blocks deploy.",
    "If Lisa's groundedness eval drops, the job exits 1 so CI cannot promote that prompt. A zero exit would ship a regression.")
add("What is DNS, IP, port, TCP vs UDP?",
    "An IP address is the building, and a port is the apartment inside it. DNS is the phone book that turns a name into that address. TCP is a reliable phone call that retries lost packets, and UDP is a postcard that might get lost.",
    "TLS usually sits on TCP. WebSockets start as HTTP and then upgrade. UDP is fine for some realtime media and a bad idea for checkout because lost packets would mean lost money. In production the cart app connects with wss to the IoT gateway on port 443 so stores do not open odd ports.",
    "The ezyCart app connects with wss to the IoT gateway on port 443. Checkout never rides UDP because a dropped packet is not acceptable.")
add("What is a deadlock? Race condition?",
    "A deadlock is two waiters each holding what the other needs, so both freeze. A race is when the winner depends on lucky timing, such as two scans updating quantity at once. Both show up when shared state is updated without a clear owner.",
    "Fixes include lock ordering, timeouts, immutable messages, and putting updates on a single-threaded queue per cart. Optimistic versioning on a row detects lost updates without holding long locks. I reproduce with stress tests, not with hope. In production two services must not update the same cart line without a version column or a per-cart serial queue.",
    "If two services update the same cart line without optimistic versioning, a late retry can wipe a scan. We serialize per cart or version the row.")

# Java / Kotlin / Android fresher
add("Java vs Kotlin for Android?",
    "Kotlin is the modern language for Android: less boilerplate, null-safety, and coroutines. Java still appears in older modules and libraries, and Kotlin can call it. For a new Android screen I would write Kotlin unless the surrounding code is a Java island.",
    "Kotlin's null safety, data classes, and coroutines cut a class of crashes and callback nests that Java Android code accumulated. Jetpack Compose is Kotlin-first. Interop with Java is real, so a mixed module is normal. In production the ezyCart Android app is Kotlin talking to existing Java libraries rather than a rewrite for its own sake.",
    "The ezyCart Android app is Kotlin and still links existing Java libraries, which is the interop story I would give in an interview.")
add("What is null safety in Kotlin?",
    "In Kotlin, String cannot be missing, and String? might be missing. The compiler nags you to check before you dereference. That nags away a whole class of null-pointer crashes.",
    "Safe calls ?., Elvis ?:, and explicit checks are the tools; !! is an escape hatch I avoid because it reintroduces NPEs. Java interop types are platform types and need care at the boundary. The trade-off is a little more annotation for far fewer production crashes. In production add_to_cart takes sku: String, not String?, so a missing SKU fails at compile or at the API boundary.",
    "add_to_cart uses sku: String rather than String?, so a missing SKU cannot silently become a null crash on the trolley client.")
add("What is an Activity / Fragment / ViewModel?",
    "An Activity is a screen, a Fragment is a reusable piece of a screen, and a ViewModel holds the data that should survive rotation. If you put the cart only in the Activity, turning the phone empties it. The ViewModel outlives the view.",
    "MVVM means the UI observes a ViewModel, and the ViewModel talks to repositories, not to Android views. SavedStateHandle covers process death beyond rotation. The trade-off of stuffing logic in an Activity is untestable screens. In production the cart screen ViewModel holds line items so rotation does not empty the trolley UI.",
    "The ezyCart cart screen ViewModel holds line items. Rotating the phone does not empty the cart because the list is not stored only in the Activity.")
add("What is Jetpack Compose vs XML views?",
    "Jetpack Compose describes UI as functions of state, so you say what the screen should look like for this cart. XML views were nested layout files that you mutated by hand. Compose redraws from state instead of hunting findViewById.",
    "Recomposition, remember, and unidirectional data flow are the Compose model, and interop with old views exists for mixed screens. XML is still in older apps and is not wrong, just more mutation-heavy. In production I would use Compose for new Android cart UI, and I would not rewrite a stable XML checkout only for fashion.",
    "Staff tools also use Flutter, which is another declarative UI. New Android cart screens can use Compose without forcing a rewrite of a stable XML checkout.")
add("What is Flutter / Dart? Widget tree?",
    "Flutter is a toolkit that paints its own UI on iOS and Android from one Dart codebase. You build a tree of widgets, which are descriptions of UI, and Flutter draws them. That is why one staff app can run on a phone and on a TV.",
    "Widgets are immutable descriptions; state lives in State objects, BLoC, or Provider. Platform channels reach native APIs when you need hardware. Flutter is excellent for staff tools; native Kotlin may still win for the tightest camera and NFC paths. In production we ship a Flutter staff and TV monitor and a Flutter SDK lite for small vendors, while the trolley client stays closer to native where hardware is hot.",
    "We use a Flutter staff and TV monitor plus a Flutter SDK lite for small vendors, while the hardware-heavy trolley path stays native where it must.")
add("What is an APK / Play release / ProGuard?",
    "An APK is the install package you put on a phone. Google Play is the store that ships it, with version codes and staged rollouts. ProGuard or R8 shrinks and obfuscates the code so the package is smaller and stack traces need a mapping file.",
    "Signing, versionCode, staged rollout, and mapping files for crash deobfuscation are part of a real release, not an afterthought. CI with Jenkins, GitLab, or Bitrise should build, test, and upload. The trade-off of obfuscation is smaller APKs versus harder crash reading if you lose mappings. At Colan from 2012 to 2021 we used that pipeline discipline to cut ANR about 70% and lift performance about 30% for around 500K users, and I always say how we measured ANR rather than waving at a number.",
    "At Colan, CI and release hygiene helped cut ANR about 70% and lift performance about 30% for around 500K users. I treat mapping files as part of the release, because an obfuscated crash without them is a black box.")
add("HTTP on mobile: Retrofit/OkHttp vs Ktor?",
    "Retrofit and OkHttp are the usual Android pair for calling REST, and Ktor is another HTTP client that fits Kotlin Multiplatform. They all send HTTP; the difference is interceptors, coroutines, and sharing code. You still need timeouts and you still must not log personal data.",
    "OkHttp interceptors handle auth, retries, and logging, and I strip PII from those logs. Timeouts and backoff belong in the client, not only in the UI. Certificate pinning is for high-threat apps and has operational cost when certs rotate. In production ezyCart Android calls the backend with this stack and keeps a WebSocket client for live IoT, not a polling loop.",
    "The ezyCart Android app calls REST for catalogue and cart, and it holds a WebSocket client for live IoT scans instead of polling.")
add("What is MVVM vs MVP vs MVC?",
    "These are ways to split the screen from the rules so one file does not become a god object. MVC puts a controller in the middle, MVP uses a presenter that talks to a view interface, and MVVM lets the view observe a ViewModel. On Android, MVVM with Flow is the common modern choice.",
    "MVVM plus LiveData or Flow keeps Android UI as a renderer of state. MVP is more explicit and more boilerplate. MVC Activities became god objects historically. I test ViewModels without an emulator. In production CartViewModel unit tests cover scan and total logic without spinning a device.",
    "CartViewModel unit tests cover adding a line and totaling the cart without an emulator. That is the point of MVVM on ezyCart.")
add("Coroutines / Flow vs RxJava vs callbacks?",
    "Coroutines are Kotlin's readable way to write async code that still looks like a sequence. Flow is a stream of values over time, like a live list of scans. Callbacks nest, and RxJava is a powerful older stream library that many apps still have.",
    "Structured concurrency means a scope owns child jobs and cancels them together, which callbacks do not give you for free. I use Dispatchers.IO for disk and network and Main for UI updates. RxJava is fine in legacy modules; I do not mix three async styles in one screen. In production I collect device events on IO and update the cart UI on Main.",
    "Device scan events are collected on Dispatchers.IO and the cart UI updates on Main. Cancellation of the screen scope stops the collector.")
add("What is SOLID in one sentence each?",
    "Single responsibility means one job per class. Open-closed means you extend without editing a stable core. Liskov means a subclass must not break the parent's promises, interface segregation means small interfaces, and dependency inversion means you depend on abstractions. Together they are a smell detector, not a trophy wall.",
    "I use SOLID as a review language, not as a checklist to gold-plate a trolley app. A 2000-line Activity violates single responsibility because scanning, pay, and ads are three jobs. The trade-off of over-applying SOLID is a forest of one-method types. In production I split those jobs into separate types and I keep the payment interface small.",
    "A 2000-line Activity that scans, pays, and shows ads violates single responsibility. On ezyCart those jobs are split so a checkout bug does not live inside the camera loop.")

# Misc fresher
add("What is JSON Schema / OpenAPI?",
    "JSON Schema is a contract that says which fields exist and what types they have. OpenAPI uses that idea to document a REST API so humans and machines agree. If the contract says qty is a positive integer, a client can fail before it calls you.",
    "FastAPI generates OpenAPI from Pydantic models, so the docs and the validation stay in one place. Breaking field changes need a version, not a silent rename. Generated clients stub from the spec. Agent tool JSON schemas are the same idea as OpenAPI, just aimed at models. In production Lisa tools have JSON schemas, and humans get OpenAPI for the HTTP API.",
    "Lisa tool arguments use JSON Schema the same way the FastAPI cart API publishes OpenAPI for human clients. Both are contracts, not suggestions.")
add("What is CI vs CD?",
    "Continuous integration means every change is built and tested automatically. Continuous delivery or deployment means a green build can be released, sometimes all the way to production. Together they stop 'it worked on my machine' from becoming the release process.",
    "A serious pipeline runs unit tests, lint, security scans, evals for AI, image builds, and a staging gate with rollback. CI without CD still helps; CD without tests is a faster way to ship bugs. In production a Lisa prompt change is blocked if eval groundedness drops, which is the AI equivalent of a red unit test.",
    "A prompt change that drops Lisa groundedness fails CI and does not deploy. That is CD gated on evals, not only on compile.")
add("Unit vs integration vs e2e tests?",
    "A unit test checks one function with fakes around it. An integration test checks several real pieces together, such as a retriever and an index. An end-to-end test walks a user journey, which is powerful and slow, so you only keep a few.",
    "The test pyramid says many unit tests, fewer integration tests, and a handful of e2e paths. I mock LLMs in unit tests, contract-test tools against schemas, and keep a few real cart flows. In production I unit-test Pydantic tool args and integration-test retriever plus rerank against a fixture index, rather than calling a live model from every PR.",
    "I unit-test Pydantic tool arguments and integration-test retriever plus rerank with a fixture index. A full trolley e2e is reserved for a few smoke paths.")
add("What is a race in checkout if two scans arrive?",
    "If two scans hit the cart at once, both might read qty as 1 and both write qty as 2, and you lose an item, or both might add and you double-count. A race means the result depends on timing. Checkout needs a single owner for that cart's updates.",
    "The production pattern is a per-cart lock or a serial queue plus idempotent event ids, often with an optimistic version on the cart row. At-least-once IoT delivery makes this mandatory, not optional. I would rather serialize one cart than corrupt a bill. In production the same barcode twice still increments once per unique event_id.",
    "If the same barcode arrives twice, quantity increases once per unique event_id. A second copy of that event is ignored instead of double-charging.")
add("How do you read a stack trace?",
    "You start at the root cause, often at the bottom or in a Caused by line, and then you walk the frames that led there. Each frame is a file and line that was on the stack. On Android, obfuscated names need a mapping file before they mean anything.",
    "Python shows the latest call at the bottom; Java often has Caused by chains. I never guess from the first line of a huge Android ANR dump. Mapping.txt from R8 turns obfuscated frames back into class names. In production ANR traces that sit on main-thread I/O tell me to move that work off main, which is the same class of fix behind Colan's ANR drop.",
    "ANR traces that show disk or network on the main thread mean I move that work off main. That is the reading skill behind cutting ANR, not a mystery Play Console number.")
add("What is UTF-8?",
    "UTF-8 is a way to store every language's characters as one or more bytes. English letters take one byte, and many other scripts take more. Character length is not the same as byte length, which matters when you slice strings.",
    "JSON defaults to UTF-8, and mixing Latin-1 with UTF-8 is how recipe names turn into garbage. I never truncate a string by raw bytes in the middle of a character. In production Tamil recipe names in Lisa must round-trip through the API, the index, and the phone UI without mojibake.",
    "Tamil recipe names in Lisa must round-trip through JSON, the retriever, and the client. If we sliced by bytes we would break characters.")
add("Environment variables vs config files vs secret managers?",
    "Config is settings such as log level or feature flags. Secrets are passwords and API keys, and they must not be committed next to config. Environment variables are the usual way to inject both, but a secret manager is where the passwords should live.",
    "Twelve-factor config lives in the environment, Kubernetes secrets or a vault hold credentials, and each stage has its own values. Rotation matters as much as storage. In production Bedrock keys never sit in the Android app; they live on the server and come from a secret manager into the FastAPI process.",
    "Bedrock keys never ship in the ezyCart Android app. They live in a server-side secret manager and are injected into FastAPI as environment values.")
add("What is pagination, filtering, sorting in APIs?",
    "You do not send the whole catalogue in one response. You send a page, you let the client filter, and you sort with a stable key. Unbounded queries are how a staff screen takes down the database.",
    "Stable sort keys, a max page size, and cursor pagination are the production defaults. I reject unbounded sort-plus-filter combinations that cannot use an index. Total counts are expensive; I do not compute them if the UI does not need them. In production staff stock-audit lists aisles page by page.",
    "Staff stock-audit lists aisles page by page with a max page size. We reject a request that asks for the whole store's SKUs in one shot.")
add("What is a 12-factor app (name a few)?",
    "Twelve-factor is a set of habits for services: store config in the environment, keep processes stateless, treat logs as streams, and scale by adding processes. You do not have to recite all twelve in an interview. You should show that you build services that can restart and scale without sticky memory.",
    "I name config in env, stateless processes, backing services as attached resources, and logs to stdout, then I stop reciting. Sticky in-memory sessions fail when you add a replica. In production the cart API is stateless, session or cart state lives in Redis or the database, and logs go to stdout for the cluster to collect.",
    "The cart API processes are stateless. Cart session state lives in Redis or the database, and logs go to stdout rather than a local file.")
add("GET caching and Cache-Control / ETag?",
    "Browsers and CDNs can reuse a GET response if you say they may. Cache-Control sets how long, and an ETag is a fingerprint so the client can ask whether the copy is still good. Personalized prices must not sit in a shared cache.",
    "If-None-Match with ETags saves bytes on unchanged catalogues. Authorization headers usually mean the response is private. Caching a member price on a CDN would leak discounts across shoppers. In production public product images are cached and membership prices are never cached shared.",
    "Public product images are cached at the CDN. A membership price is never stored in a shared GET cache because the next shopper could see the wrong number.")
add("What is a JWT? Risks?",
    "A JWT is a signed blob that says who you are and what you may do until it expires. Anyone who steals that blob looks like you for the rest of its lifetime. That is why it must be short-lived and stored carefully on a phone.",
    "I check exp, iss, and aud, keep access tokens short, and use refresh tokens with rotation. Revocation of a JWT is hard, which is the main trade-off versus a server session. I never put JWTs in web localStorage if XSS is in play. In production a staff-app JWT cannot call shopper-only routes and gets 403.",
    "A staff-app JWT is rejected with 403 on shopper-only routes. Stealing that token still must not grant checkout-as-shopper.")
add("Hash vs encryption vs encoding?",
    "Hashing is a one-way blender: you cannot get the original password back. Encryption is a lock with a key, so you can unlock later. Encoding such as Base64 only changes shape and is not secret, even if it looks messy.",
    "Passwords should be salted hashes such as bcrypt or argon2, PII at rest should be encrypted, and Base64 in an LLM prompt is still plaintext to the model. Mixing these words in an interview is a red flag. In production I would never Base64 a card PAN and call it encrypted in a Lisa prompt.",
    "I do not Base64 a card PAN and call it encrypted inside an LLM prompt. Encoding is not a security control on ezyCart or Lisa.")
add("What is stdout logging vs a debugger?",
    "A debugger lets you step live through code on your machine. Logs tell the story later in production when you cannot attach a debugger. You want structured logs with a request id so you can follow one cart across services.",
    "I debug locally with a debugger and I rely on structured logs and traces in production. For LLM paths that means a tracer such as LangSmith or an equivalent, not print statements. A request_id or cart_id must follow the shopper from Android through the WebSocket into RAG spans. In production I correlate cart_id across those systems instead of SSHing into a pod to attach pdb.",
    "I correlate cart_id across the Android client, the WebSocket, and Lisa RAG spans. That is how I debug a wrong recipe in production without attaching a debugger.")

QUESTIONS = Q
