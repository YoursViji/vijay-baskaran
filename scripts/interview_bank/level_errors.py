# AI / LLM / RAG / serving error codes — full-sentence meanings and interview actions
Q = []


def add(q, kid, tech, *ex):
    Q.append((q, kid, tech, list(ex)))


add(
    "What does HTTP 400 mean on an LLM or RAG API, and what do you do?",
    "HTTP 400 means the client sent a request the server cannot understand, such as a malformed JSON body or a missing required field. It is the caller's homework, not a GPU failure. In an interview I say I fix the payload and I do not retry 400 in a loop, because the same bad body will fail forever.",
    "A 400 Bad Request on a FastAPI RAG or agent endpoint usually means Pydantic or the HTTP layer rejected the shape of the request before a model was even called. I log the validation errors, return a typed problem body, and treat the case as a client bug in traces so on-call does not page GPUs. I never map a 400 to a silent empty answer, because Lisa would then look as if she had no catalogue. In production I add contract tests so Android and the agent tools cannot ship a field rename that produces a wall of 400s. Retrying 400 is a cost bomb, not resilience. The interview story is: classify the error, fail closed, teach the client.",
    "If add_to_cart arrives without a sku, FastAPI returns 400 with a field error, the agent tells the shopper the barcode was empty, and we do not call Bedrock at all.",
)
add(
    "What does HTTP 401 mean, and how is it different from 403?",
    "HTTP 401 means the server does not know who you are, usually a missing or expired token. HTTP 403 means the server knows who you are and still will not let you do that thing. Shoppers hear both as 'access denied', but the fix is different: refresh login versus stop asking for someone else's cart.",
    "401 Unauthorized is unauthenticated: no Bearer token, a bad JWT, or an expired credential. 403 Forbidden is authenticated but not allowed: wrong tenant, wrong role, or an ACL miss on a RAG collection. I never collapse them into one 'auth error' in an LLM gateway, because a shopper with an expired token needs a refresh, while a shopper querying staff stock-audit chunks needs a hard deny. In traces I tag 401 as client-session and 403 as authorization so security reviews can see permission probes. On mobile the ezyCart app refreshes on 401 and does not retry 403. Interviewers want that distinction out loud, not a shrug.",
    "A staff JWT that tries a shopper-only Lisa route should come back 403, while a tablet with an expired token should come back 401 and refresh, never as a hallucinated 'I cannot find that product'.",
)
add(
    "What does HTTP 403 mean for RAG and tools?",
    "HTTP 403 means you are signed in and still not allowed. In RAG it often means the retriever would have returned a document the caller must not see. The safe move is deny, log, and abstain, not to let the model paraphrase the forbidden page.",
    "Authorization belongs in the retriever and in the tool allowlist, not only in a later prompt instruction. If a shopper's query would retrieve staff-only stock-audit chunks, I filter by ACL at search time and return 403 or an empty authorized set, then Lisa abstains. A 403 on a money tool such as discount or pay is a feature, not an outage. I audit 403 spikes because they can be either a client bug or a probing attacker. MCP and LangChain tools do not become safe because they returned a friendly sentence. The interview action is: show the ACL filter, the deny, and the audit log.",
    "Lisa must not quote a staff stock-audit chunk to a shopper; the retriever filters it, the API can surface 403 to a misconfigured client, and the model says it does not have that information.",
)
add(
    "What does HTTP 404 mean on model, index, or SKU routes?",
    "HTTP 404 means the thing you named is not there: a SKU, a collection, a prompt id, or a model deployment. It is not a permission error and it is not a GPU outage. I tell the user the resource is missing and I do not invent a substitute as if it existed.",
    "On a catalogue API, 404 is an unknown SKU. On a model gateway, 404 or a vendor model_not_found means the deployment name is wrong or the vendor retired the id. On a vector store, a missing collection should be 404 or a typed index-not-found, not a 500. I fail closed for checkout SKUs and I abstain in Lisa rather than guess. I alert when 404 rates jump after a deploy, because that is often a renamed index alias or a client still on an old path. Interviewers want you to separate 'not found' from 'forbidden' and from 'the model crashed'.",
    "GET /products/EZY-1044 returning 404 means that SKU is not in the live catalogue, so Lisa must not add it; a missing vector collection after a bad alias swap is the same class of error at RAG scale.",
)
add(
    "What does HTTP 409 mean in carts, payments, and idempotent LLM tools?",
    "HTTP 409 means your change collided with the current state, such as two devices updating the same cart version. It is a conflict, not a validation typo. The interview move is to retry with the new version or return the original idempotent result, not to double-charge.",
    "409 Conflict is how I surface optimistic-concurrency failures and some idempotency clashes. For payments and add_to_cart I prefer storing an idempotency key and returning the original receipt on replay, which can be 200, while a true version clash is 409. Agent tools must use the same keys so a retried tool call after a 502 does not add pasta sauce twice. I never treat 409 as retry-with-the-same-body forever without reading the new state. In ezyCart, two scan events with different ids are not a 409; two writers on one cart row are. That distinction is what a senior answer sounds like.",
    "If the tablet retries add_to_cart with the same event id, we return the original line instead of a 409 storm; if two writers race the cart version, we return 409 and the client reloads state.",
)
add(
    "What does HTTP 422 mean, and how does it show up in LLM tool calls?",
    "HTTP 422 means the JSON was readable but semantically invalid, such as qty of minus one or a SKU that fails a schema. FastAPI and Pydantic use it for validation that is deeper than 'this is not JSON'. I do not send that body to the model; I tell the agent the field is wrong.",
    "422 Unprocessable Entity is the contract for schema-valid JSON that still fails business validation. Pydantic field validators on FastAPI and on tool arguments should return 422 with a pointer to the field. For LLM structured output I validate the model JSON the same way: one repair attempt, then fail closed. Mapping a 422 into a 200 with an error string inside the body is how tools start hallucinating success. In interviews I say 400 versus 422 is less important than 'do not call the LLM, do not retry blindly, show the field'. Money tools use extra=forbid so extra keys cannot sneak a discount.",
    "If Lisa emits add_to_cart with qty=-1, Pydantic raises a validation error, we return 422 to the tool layer, and the graph asks the shopper to confirm a positive quantity instead of hitting the cart service.",
)
add(
    "What does HTTP 429 mean for OpenAI, Anthropic, Bedrock, and your own gateway?",
    "HTTP 429 means slow down: you hit a rate limit or a quota window. Retrying immediately makes it worse. I back off, honor Retry-After if present, shed load to cache or a smaller model, and I never hide 429 as a generic 500.",
    "429 Too Many Requests is the honest signal for tokens-per-minute, requests-per-minute, or a per-tenant quota I set on the Lisa gateway. Vendor APIs and our own gateway should both emit 429 rather than queue until the shopper's tablet looks frozen. I use jittered exponential backoff, a max attempt count, and a fallback route: semantic cache, extractive FAQ, or a local vLLM Llama 3 slice. I meter 429s per tenant so one viral recipe loop cannot starve the store. In an interview I separate rate_limit from insufficient_quota: one is a window, the other is billing. Both can surface as 429 depending on the vendor, so I read the error code inside the body, not only the HTTP status.",
    "If Bedrock throttles Lisa, the gateway returns 429 with Retry-After, retries twice with jitter, then answers a FAQ from cache or a local vLLM model instead of hanging the tablet.",
)
add(
    "What does HTTP 500 mean on an AI service, and what should you not do?",
    "HTTP 500 means the server hit an unexpected failure, such as an unhandled exception in FastAPI. It is our bug until proven otherwise. I do not return 500 for validation, and I do not retry 500 on a non-idempotent charge without a key.",
    "500 Internal Server Error should be rare, typed in logs, and tied to a trace id the on-call can open in LangSmith or OpenTelemetry. I distinguish 500 from 502/503/504, which often mean a dependency or overload rather than a crash in our process. I never convert a content_filter or a Pydantic miss into a 500, because that trains clients to retry unsafe or invalid work. For LLM backends I wrap vendor errors into a stable envelope: retryable versus not, plus the vendor code. Checkout paths fail closed. The interview answer is the taxonomy, the trace, and the rollback, not 'restart the pod'.",
    "An unhandled None in a reranker is a 500 with a trace id; a bad Lisa prompt that the model refuses is not a 500, and we do not restart GPU nodes to hide an application bug.",
)
add(
    "What does HTTP 503 mean, and how do you use it for GPU backpressure?",
    "HTTP 503 means the service is temporarily unavailable, often overloaded or not ready. It is a polite closed sign, not a mystery crash. Clients should retry with backoff or take a degraded path, and load balancers should stop sending traffic until readiness returns.",
    "503 Service Unavailable is how I shed load when the vLLM queue, the ONNX pool, or a dependency is past SLO. Readiness probes should fail so Kubernetes or the gateway stops new traffic, while liveness stays up unless the process is actually wedged. I pair 503 with Retry-After and a degraded mode: cache-only FAQ, skip the reranker, or route to a smaller model. Returning 200 with an empty completion is worse, because the shopper thinks Lisa answered. GPU OOM can become 503 after we catch it, rather than a crashing tight loop. Interviewers want backpressure, not heroic infinite queues.",
    "If the vLLM queue would blow Lisa p95, we return 503, serve cached FAQs, and keep ezyCart scanning on the WebSocket path so checkout does not wait on a GPU.",
)
add(
    "What do HTTP 502 and 504 mean in front of an LLM or vector database?",
    "HTTP 502 means a proxy got a bad answer from upstream. HTTP 504 means the proxy waited too long. Both often sit in front of vLLM, Bedrock, or a vector DB. I treat them as dependency failures, retry only if the tool is idempotent, and I cut the prompt or the k so the next call can finish.",
    "502 Bad Gateway and 504 Gateway Timeout are typical when API Gateway, nginx, or a mesh in front of FastAPI cannot complete a long prefill. I set timeouts deliberately: shorter than the gateway, longer than p95 TTFT, and I stream SSE so a long generation is not one blocking HTTP call. I do not raise the gateway timeout to five minutes as a strategy; I shrink context, use prefix cache, or split tools. Vector search that hangs should time out with a 504-class error and a BM25 fallback. The interview action is timeout budgets and fallbacks, not a bigger number in nginx.",
    "A long RAG prefill that dies at the mesh is a 504; Lisa should then retry a shorter context or fall back to BM25 plus a smaller model, not wait on a second full 10-million-document search.",
)
add(
    "What is insufficient_quota, and how do you talk about it in an interview?",
    "insufficient_quota means the vendor will not run the request because the account is out of credits or over a hard billing cap. It is not a bad prompt. I fail the request, page billing or the platform owner, and I switch to a fallback model or a local vLLM path if the product must stay up.",
    "OpenAI-style insufficient_quota and similar Bedrock or Anthropic billing errors are capacity of money, not capacity of GPUs. I surface them as a typed non-retryable error distinct from 429 rate limits, because retrying a dead quota only burns latency. Dashboards should show quota remaining, not only HTTP codes. For Lisa I keep a documented fallback: another vendor behind the same router, or a local Llama 3 FAQ slice. I do not hide quota death as a generic 500, and I do not invent a cost savings figure in the interview. The senior move is prepaid alerts, per-tenant caps, and a kill switch before the bill becomes a surprise.",
    "If the hosted pilot for Lisa hits insufficient_quota, the router fails that path, serves FAQ from local Llama 3 or cache, and pages the owner rather than looping the same OpenAI call.",
)
add(
    "What is context_length_exceeded, and what do you do?",
    "context_length_exceeded means the prompt plus the completion budget is larger than the model's window. The model never saw the end of your RAG dump. I cut history, cut chunks, or map-reduce the documents, and I do not raise max_tokens to 'see if it fits'.",
    "This error is a design smell: we stuffed system prompt, chat history, and fifty retrieved chunks into one window. Fixes are rerank-to-five, lost-in-the-middle packing, hierarchical summarize, a larger-window model only when eval says it helps, and a hard cap in the gateway. Tokenizer mismatch can cause a surprise here if we counted characters or counted with the wrong tokenizer. I fail the request with a typed error the agent can handle: shrink and retry once, then abstain. I never silently truncate the middle of a legal clause. Interviewers want the packing strategy, not 'we switched to a 128k model' as the only plan.",
    "Lisa recipe RAG that stuffs forty chunks will hit context_length_exceeded; we rerank to five, keep the clause with its heading, and retry once before abstaining.",
)
add(
    "What is a rate_limit error versus a 429 you emit yourself?",
    "A vendor rate_limit error means their window is full. A 429 you emit yourself means your gateway is protecting tenants and GPUs. Both mean wait, but the lever is different: change the vendor plan versus shed your own traffic.",
    "I parse the vendor body for rate_limit_exceeded, retry-after, and which dimension failed: RPM, TPM, or concurrent connections. I do not blindly retry Bedrock, OpenAI, and Anthropic on the same policy, because their windows differ. Internally I still return 429 to Android and to agent tools so they share one client policy. I keep a token bucket per store so one merchant cannot consume the vendor quota for everyone. In interviews I mention jitter, max retries, and a degraded model. I do not claim we 'never hit rate limits' if we run a public shopping assistant.",
    "When OpenAI returns rate_limit_exceeded, Lisa's gateway waits on Retry-After, then may route the FAQ slice to vLLM, while the trolley WebSocket scan path is unaffected.",
)
add(
    "What does content_filter or a safety/content policy error mean?",
    "A content_filter error means the vendor or your guardrail refused the input or the output as unsafe. It is a successful safety decision, not a crashed model. I show a safe refusal to the shopper and I log enough to debug without storing the raw harmful text longer than policy allows.",
    "OpenAI content_filter, Anthropic refusals, Bedrock Guardrails, and our own classifiers can all block self-harm, scams, or medical overreach. I do not retry a filtered call with a jailbreak 'ignore the policy' rewrite. I distinguish input filter from output filter, because a retrieved product page that tries prompt injection should be dropped before generate. Allergen questions that the RAG cannot ground should abstain even if the filter would have allowed a guess. Metrics should count filter hits separately from 500s so leadership does not treat safety as downtime. The interview action is layered guardrails plus a human policy, not turning the filter off to raise answer rate.",
    "If a retrieved HTML comment tries to force a 100 percent discount, the injection defense and a content policy layer must block the tool, and Lisa refuses instead of calling a discount API.",
)
add(
    "What does model_not_found mean, and how do you prevent it in production?",
    "model_not_found means the name you called does not exist, was renamed, or was retired by the vendor. It is a configuration error. I pin model ids in one router, eval a successor before cutover, and I never scatter raw 'gpt-x' strings across forty services.",
    "Vendors deprecate models on a calendar. A Principal-level answer is an abstraction: Lisa asks the router for 'recipe-mid' or 'complaint-frontier', not for a hardcoded snapshot in the Android app. When a model id 404s, the router fails over to the last-evaled fallback and pages. CI should fail if a configured id is not in the allowlist. I do not discover deprecation in production on a Saturday. Edge vision uses versioned ONNX files with the same idea: yolo-store-v17, not 'whatever was on disk'. Interviewers are listening for deprecation drills, not for memorized model names.",
    "If a hosted frontier id is retired, Lisa's router serves the previously evaled successor or a local Llama 3 FAQ path, and we do not leave a raw vendor id in the trolley APK.",
)
add(
    "What is an LLM timeout, and how is it different from TTFT slowness?",
    "A timeout means you stopped waiting; the call may still be burning GPU on the other side unless you cancelled. Slowness is a high time-to-first-token that still succeeds. I set timeouts, cancel on SSE disconnect, and I measure TTFT p95 separately from total time.",
    "Client timeouts, gateway timeouts, and vendor timeouts are three clocks that must nest. If the tablet gives up and we do not cancel, we pay for unused tokens. FastAPI StreamingResponse for Lisa must abort the vendor request on disconnect. I classify timeouts as retryable only when the operation is idempotent and we did not already stream tokens the user might have seen. Prefill-heavy RAG is the usual root cause, so I shrink context before I extend the timeout. Interviewers want cancellation, not a 120-second nginx number. Sub-100ms is a vision SLO on device; chat TTFT is a different budget and I never mix the two numbers.",
    "If the shopper locks the tablet, we cancel the Lisa generation so Bedrock or vLLM does not keep decoding into the void, which is a timeout-and-cancel story rather than a 500.",
)
add(
    "What is invalid_request_error on OpenAI-style APIs?",
    "invalid_request_error means the vendor rejected the arguments: a bad parameter, an unsupported combination, or a schema the model endpoint does not accept. It is usually not transient. I fix the client contract and I do not retry the same JSON.",
    "This family covers unknown parameters, negative max_tokens, mixing tools with an incompatible response format, and asking a model for a feature it does not have. I keep a compatibility matrix in the router: which deployment supports tools, JSON mode, or vision. Mapping invalid_request_error to 400 or 422 on our public API is correct; mapping it to 500 is a lie. Agent graphs should treat it as a developer bug and fail the CI fixture. I mention it in interviews to show I read vendor error types instead of retrying everything. Logs include the parameter name, not the full prompt if it contains PII.",
    "If a Lisa tool path asks a local Llama 3 deployment for a response_format it does not support, the router returns a typed invalid request and we fall back to Pydantic-validated plain JSON instead of spinning.",
)
add(
    "How do authentication_error and permission_error differ on vendor LLM APIs?",
    "authentication_error means the key is missing, wrong, or revoked. permission_error means the key is valid and still not allowed to use that model or that operation. One is 'who are you', the other is 'this key cannot use GPT-class X'.",
    "I keep vendor keys in a secret manager, not in the Android APK and not in LangSmith payloads. A rotated key that 401s should page, because every Lisa call will fail. A permission_error on a newly enabled model often means IAM or a project allowlist, which is the Bedrock and Vertex equivalent of 403. Least privilege still applies: the embed job role cannot invoke the frontier chat model. In interviews I connect this to IAM least privilege and to the 401 versus 403 HTTP story so it sounds like one mental model. I do not paste keys into the whiteboard.",
    "The FastAPI Lisa service role can invoke the chat model, the nightly embed job cannot, and a revoked key is an authentication failure that pages on-call rather than a shopper-facing hallucination.",
)
add(
    "What is Anthropic overloaded_error or HTTP 529, and what do you do?",
    "overloaded_error or a 529-style overloaded response means the vendor is too busy, not that your JSON is wrong. It is retryable with backoff, and it is a reason to have a second provider. I do not treat it as a prompt quality problem.",
    "Anthropic has used overloaded_error when the fleet is saturated. The operational response is the same as a 503: jittered retry, then failover to Bedrock, Vertex, OpenAI, or vLLM behind the same abstraction. I keep this distinct from content refusals so eval dashboards do not punish prompts for vendor weather. Capacity planning still matters: if we depend on one vendor without a fallback, overloaded_error is an outage. Interviewers want multi-provider routing here, which matches the hosted-versus-local story on Lisa. I do not claim we never see overload.",
    "If Anthropic is overloaded during a recipe spike, Lisa's router retries once, then serves the same evaled path on Bedrock or a local Llama 3 FAQ slice.",
)
add(
    "What vector database errors must you name in an interview?",
    "The usual vector DB failures are a missing collection, a dimension mismatch, a bad metadata filter, and a timeout on the query. They look like 404, 400, or 503 at the HTTP layer. I never let them become a confident wrong answer from the LLM.",
    "Index or collection not found means the alias swap failed or the client is on the wrong environment. Dimension mismatch means the query embedding was produced by a different model than the index, which is a broken deploy. Filter syntax or type errors mean an ACL or tenant field is wrong, and I fail closed rather than search without the filter. Timeouts and memory errors mean shard sizing and HNSW parameters, plus a BM25 fallback. I version embedding models in metadata and dual-run indexes during upgrades so 10 million documents are not silently incomparable. The interview action is typed errors, BM25 fallback, and alias rollback, not 'restart Pinecone'.",
    "If we upgrade the embedding model and forget to re-index, query vectors have the wrong width, the vector DB errors, and Lisa must fall back to BM25 instead of answering from a random nearest neighbor.",
)
add(
    "What is an embedding dimension mismatch, and why is it a deploy bug?",
    "A dimension mismatch means you asked a 384-wide index to store or search a 1024-wide vector. The database should reject it. It always means two embedding models are in play without a migration.",
    "I pin the embedding model id next to the index name, and I refuse to mix them. Onboarding a new model on 10 million documents is a shadow index, dual retrieve, recall compare, then alias swap, with rollback to the previous generation. Serving a query with the old tokenizer or the new model against the old index is a silent quality disaster if the DB were to coerce sizes, so I want a hard error. FastAPI should catch it as 500/503 only after we classify it as a config incident. Interviewers use this to see whether you have operated RAG or only demoed it.",
    "A Lisa catalogue-v2 shadow index uses the new embedding width; live traffic stays on catalogue-v1 until recall matches, so shoppers never query across mismatched dimensions.",
)
add(
    "What GPU OOM errors mean on vLLM, PyTorch, or ONNX, and what do you do?",
    "GPU out of memory means the card ran out of VRAM: the batch, the KV cache, or the model weights did not fit. It is not a wrong answer from the model. I reduce batch, quantize, cap context, or move the job, and I return 503 rather than crash-loop the replica.",
    "CUDA OOM on vLLM is often KV cache growth from long RAG prompts and high concurrency, which is why paged attention and prefix cache exist. PyTorch training OOM is a different story: batch size, gradient checkpointing, or a LoRA rank that is too wide. On-device TF Lite and ONNX on the cart are CPU or NPU memory problems, not data-center CUDA, and I do not mix those numbers with the sub-100ms vision SLO. I catch OOM, shed load, and keep a smaller model warm. I never retry the same huge context on the same GPU and hope. The interview answer names prefill versus decode memory, then the lever you turn.",
    "If Lisa's vLLM replica OOMs on a stuffed RAG prompt, we cap chunks, return 503 to new sessions, and keep ONNX vision on the trolley running, because that path is not on the same GPU.",
)
add(
    "What is a tokenizer mismatch, and how does it show up?",
    "A tokenizer mismatch means you counted or split text with a different tokenizer than the model uses. Your 'this fits in 8k' estimate is a lie, and RAG chunks may be too big or oddly cut. I tokenize with the model's tokenizer, not with whitespace or a generic GPT guess.",
    "Context_length_exceeded, surprise bills, and broken truncation all follow from counting characters or using tiktoken for a Llama model. Chunkers must use the same tokenizer as the embedding or chat model they feed, or at least a conservative upper bound. Fine-tunes and LoRA jobs must train with the right tokenizer files; serving with a different vocab is a silent quality bug. In interviews I say we unit-test token counts on fixtures, including Tamil and Malay product names, because UTF-8 character length is not token length. I do not treat tokenizer files as optional extras in the Docker image.",
    "A Tamil recipe name that looks short in characters can consume many tokens; Lisa's chunker uses the model tokenizer so we do not blow the window or bill a surprise completion.",
)
add(
    "How do Pydantic ValidationError and 422 protect agent tools?",
    "Pydantic raises ValidationError when types or constraints fail. FastAPI turns that into HTTP 422. For agents, the same validation wraps tool arguments so the model cannot pass a string where an int belongs. I treat the model as an untrusted client.",
    "Tool JSON is not trusted input. I define a schema, parse with Pydantic, reject extras on money tools, and return a typed error the graph can turn into a user question. One repair generation is enough; then I fail closed. This is the same discipline as public HTTP APIs on FastAPI. LangChain or MCP tools that skip validation are how prompt injection becomes a side effect. In interviews I connect 422, structured output, and HITL for pay. I do not 'ask the model to be careful' as the control.",
    "add_to_cart requires sku as a string and qty as a positive int; if the LLM emits qty as the word 'two', validation fails, we ask the shopper to confirm, and we never hit the cart service with a guess.",
)
add(
    "What SSE and client-disconnect errors should you handle?",
    "If the client hangs up, the server should stop generating. An SSE disconnect is not a 500; it is a cancelled job. I cancel the vendor call so we do not pay for tokens nobody will read.",
    "Server-sent events use text/event-stream. FastAPI must notice a disconnected tablet, cancel the asyncio task, and end the vLLM or Bedrock stream. Heartbeats keep proxies from killing an idle-looking stream during a slow tool call. Last-Event-ID is optional replay, not a substitute for idempotent tools. Mixing WebSockets for IoT with SSE for Lisa tokens is intentional: different backpressure. Interviewers want disconnect cancellation as a cost and correctness control. I do not buffer the entire answer then flush, because that throws away TTFT.",
    "When the ezyCart tablet sleeps mid-sentence, Lisa's SSE handler cancels the GPU work; the cart WebSocket for scans stays up independently.",
)
add(
    "What does a 401 or 403 from a vector DB or object store mean during ingest?",
    "It means the embed job's credentials cannot read the bucket or write the index. It is IAM, not a chunking algorithm failure. I stop the job, fix the role, and I do not mark the index live.",
    "Nightly re-embed of a catalogue should fail closed if S3 or GCS returns 403, otherwise you swap an alias onto a half-written index. Least privilege still holds: the job can read the catalogue bucket and write one index prefix, not decrypt every KMS key. I surface this as a pipeline failure in CI or Airflow, not as Lisa 500s the next morning. Interviewers connect this to IAM least privilege and to RAG delete/update correctness. I would rather have yesterday's complete index than today's empty one.",
    "If the embed role loses s3:GetObject, the job errors, catalogue-live keeps pointing at yesterday's build, and shoppers still retrieve last known promos instead of a blank index.",
)
add(
    "When should you retry an AI error, and when must you not?",
    "Retry 429, 503, 502, timeouts, and vendor overload with jitter and a cap. Do not retry 400, 401, 403, 404, 422, insufficient_quota, invalid_request, or content_filter. Never retry a non-idempotent pay tool without the same idempotency key.",
    "I classify errors in one gateway table: retryable, user-fixable, and incident. Bounded exponential backoff with jitter honors Retry-After. After the budget I degrade: cache, BM25, smaller model, or abstain. 409 needs a reload of state, not a blind replay of the old body. Agent loops that retry a typed empty SKU are a bug, not resilience. This is the same pattern I use on ezyCart WebSocket scans: at-least-once delivery plus idempotent handlers. In interviews I would rather hear this taxonomy than a list of status codes without actions.",
    "Lisa retries a 503 from vLLM twice, never retries a 422 from add_to_cart, and retries add_to_cart after a 502 only with the same event key so pasta sauce cannot appear twice.",
)
add(
    "How do you present this error taxonomy to a hiring manager who is not an SRE?",
    "I say: four buckets. The caller sent a bad form, the caller is not allowed, the brain or GPU is busy, or we have a real bug. Each bucket has a shopper-visible sentence and an engineer action. I do not dump twenty acronyms unless they ask.",
    "Bad form is 400 and 422 and invalid_request: tell the user what field failed. Not allowed is 401, 403, permission_error, and content_filter: refresh login, deny, or refuse safely. Busy is 429, 503, overloaded, OOM after catch, and timeouts: wait, fallback, cancel. Real bug is 500, dimension mismatch, tokenizer/config incidents: trace, rollback, page. I draw that on the whiteboard next to Lisa and the trolley scan path so they see checkout does not share fate with chat. This is how I would talk as Principal AI without turning the interview into a status-code recitation.",
    "I would say: if Lisa cannot answer, the shopper still scans; 429 means wait or use a cached FAQ; 403 means we will not read staff documents; 500 means we have a bug and a trace id, not a creative model.",
)

QUESTIONS = Q
