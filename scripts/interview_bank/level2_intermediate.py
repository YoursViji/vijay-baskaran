# Intermediate: ML, CV, backend, mobile, cloud intro, LLM/RAG intro, trading hygiene
Q = []

def add(q, kid, tech, *ex):
    Q.append((q, kid, tech, list(ex)))

# ML
add("Supervised vs unsupervised vs reinforcement learning?",
    "Supervised learning is like a teacher handing you the right answers, so the model maps inputs to known labels. Unsupervised learning is grouping similar things without those labels, the way you might sort a messy pantry by how items look. Reinforcement learning is trial and error with a score after each action, more like practicing a game than copying a worksheet.",
    "Supervised learning needs labelled examples such as detection boxes or sentiment tags, and that is the default for checkout vision because a wrong SKU has a clear right answer. Unsupervised methods such as clustering and embedding models are useful for exploration, retrieval, and pretraining, but you still judge them with a supervised or human eval. Reinforcement learning trains an agent with rewards, and it is expensive and unstable for checkout or payment flows, so you should prefer supervised models plus rules plus evals before you ever reward a live agent. In an interview, say which data you have, which error is costly, and why you would not RL a payment agent first.",
    "YOLO on cart cameras is supervised detection, while recipe retrieval uses embeddings judged with labelled queries. Do not put a reinforcement-learning agent on a live payment path until a supervised plus rules stack is already beating a baseline.")
add("Train / validation / test split? Why not peek at test?",
    "Train is practice, validation is the dress rehearsal, and test is the real exam you sit once. If you keep peeking at the exam while you study, the score stops meaning you can do new work. You hide the test set so you cannot secretly memorize it.",
    "Fit parameters only on train. Use validation to choose models, thresholds, and hyperparameters. Report the test set once at the end, and if you retune after seeing test you have burned it. For time-series and trading labels you must split chronologically so the future cannot leak into the past, and when tuning is heavy you use nested cross-validation so the inner loop never sees the outer holdout. An honest split is part of the claim, not a formality.",
    "If you shuffle trading labels at random, tomorrow's close sneaks into today's features and the backtest lies. For store vision, hold out a whole store or a night-shift camera that the training set never saw, then quote that number.")
add("Overfitting vs underfitting? Regularization?",
    "Overfitting is memorizing the homework so the model looks perfect at home and fails on a new aisle. Underfitting is using a model that is too simple to notice the real pattern. Regularization is a penalty that says do not be fancier than the data can support.",
    "You diagnose with learning curves: a large train-versus-val gap is high variance; both errors high is high bias. Regularization includes L2 and L1 weights, dropout, early stopping, data augmentation, and simply using a smaller model. Talk about the actual gap and the failure slice rather than reciting a list of tricks. For detection, a 99 percent train mAP with a collapse on night-shift cameras is overfitting to daytime lighting, not a reason to add more layers.",
    "A detector with 99 percent train mAP and about 40 percent on night-shift cameras is overfit to daytime. Regularize with night-aisle data, photometric augmentation, and early stopping, then re-check the night slice before you ship.")
add("Bias vs variance?",
    "Bias is always missing the dartboard in the same direction, like a model that never sees small SKUs. Variance is scattered shots that change wildly when you draw a new sample. You want to know which error you actually have before you add data or add capacity.",
    "High bias usually means the model cannot represent the pattern, so you add features or capacity after you have confirmed the labels are sound. High variance means the model is too sensitive to the training draw, so you want more data, stronger regularization, or a simpler hypothesis. Error decomposition is a diagnostic you run on slices, not a slogan you recite. A linear model on SKU images underfits; a huge net on two hundred labels overfits.",
    "A linear classifier on SKU photos underfits because the decision boundary is too stiff. A huge network trained on only a few hundred labelled bottles overfits and will not survive a new store's lighting.")
add("Precision, recall, F1, accuracy, ROC-AUC, PR-AUC?",
    "Accuracy can lie when 99 percent of frames have no product, because a model that always says empty still looks clever. Precision asks, of the alarms you raised, how many were true. Recall asks, of the true items, how many you actually found.",
    "Start from a confusion matrix and the cost of each error, not from a single headline metric. For imbalanced detection you read the precision-recall curve and an F-beta that matches the business cost, because ROC-AUC can look flattering when negatives dominate. Thresholds should come from the cost of a false charge versus a missed item, and you should quote per-class numbers for rare SKUs. F1 is a handy summary only after you have said which error hurts more.",
    "A false-positive SKU at checkout is a precision problem, and a missed item is a recall problem. We set the detector threshold from those two costs, not from the nicest mAP slide.")
add("What is a loss function? Cross-entropy vs MSE?",
    "A loss function is a score of how wrong the model is on a batch, and training tries to shrink that score. Cross-entropy is the usual score for classification. Mean squared error is the usual score when you predict a number.",
    "Use cross-entropy for class probabilities, MSE or MAE for regression, and a composite of box, class, and objectness losses for detectors such as YOLO. The loss you optimize is not the business metric you ship on, so you must track checkout-error rate or groundedness beside the training curve. If the loss falls while the store metric stalls, you are optimizing the wrong proxy. Say that out loud in an interview so you do not sound like you train only to minimize a notebook plot.",
    "We optimize a detection loss in PyTorch, but we ship on checkout-error rate, not only mAP. A pretty loss curve that still charges the wrong oil bottle is not a win.")
add("Gradient descent, learning rate, batch size?",
    "Gradient descent takes steps downhill on the loss surface. The learning rate is how large each step is. The batch size is how many examples you look at before you take a step.",
    "SGD and Adam are the common optimizers. A learning rate that is too large diverges and a rate that is too small crawls, and large batches usually need a scaled learning rate rather than a copied one. Mixed precision can speed the same step on GPU without changing the algorithm. When you fine-tune with LoRA you use a small learning rate on the adapter so you do not blow up the frozen base.",
    "Fine-tune a LoRA adapter with a small learning rate and leave the base weights frozen. If you copy a full-model learning rate onto that adapter you can wreck a model that was already useful.")
add("Backpropagation in one minute?",
    "The model makes a guess, the loss says how wrong it was, and backpropagation sends that error backward so each layer knows how to change. You do not have to hand-write the derivatives. You do have to notice when the backward pass has gone insane.",
    "Backprop is the chain rule run through the computation graph, which autograd in PyTorch does for you. Vanishing and exploding gradients show up as a dead or NaN loss, and residuals, careful initialization, and gradient clipping are the usual treatments. You will not hand-derive YOLO backprop in an interview, but you must know that a NaN loss means the graph, the inputs, the learning rate, or mixed precision is broken. Debugging the backward pass is part of owning a training job.",
    "You do not hand-derive YOLO backpropagation. You do need to know that a NaN loss on a cart-camera fine-tune means stop, inspect inputs and learning rate, and do not export that checkpoint.")
add("What is a neural network? MLP vs CNN vs transformer?",
    "A neural network is stacked layers that turn numbers into a useful prediction. An MLP is fully connected layers that see everything at once. A CNN looks at local image patches, and a transformer uses attention so distant tokens can talk.",
    "Inductive bias is the prior you bake in: CNNs assume grid locality, transformers assume that pairwise attention is worth the cost, and modern detectors such as RT-DETR mix both. MLPs are still the right default for small tabular nets, but they waste parameters on images. For a cart camera you want a CNN or transformer detector; for text RAG you want a transformer language model plus a separate embedding model. Choose the family from the data shape and the latency budget, not from fashion.",
    "The ezyCart camera path is a CNN or transformer detector such as YOLO or RT-DETR. Lisa's recipe RAG uses a transformer LLM plus an embedding model, not an MLP over raw pixels.")
add("Embeddings for non-text (images)?",
    "An image embedding turns a photo into a point on a map so similar photos sit near each other. You can search with that map. You should not bill a shopper from a nearest neighbor alone.",
    "Contrastive training such as CLIP and metric-learning losses produce image vectors you can index. Visual search and shelf similarity are good uses; checkout charging is not, unless you also have a calibrated classifier or detector and a confidence threshold. Domain shift still applies, so a studio product shot may not sit next to a glare-filled cart frame. Version the embedding model the same way you version text embeddings, because a silent upgrade reshuffles the map.",
    "You can find similar products from a shelf photo with an image embedding index. You must not bill from embedding nearest-neighbor alone without a detector, a threshold, and a human-auditable SKU decision.")
add("Data leakage?",
    "Leakage is letting the exam answers into the homework, so the model looks brilliant for a fake reason. It often hides in a timestamp, a customer id, or a scaler that saw the test set. The score then collapses the first day you go live.",
    "Classic leaks include the target sitting inside a feature, future timestamps, the same customer on both sides of a split, and a scaler or encoder fit on train plus test. You audit features by asking whether this number would have been knowable at prediction time. For trading, tomorrow's close in today's feature is leakage. For vision, putting frames from the same video in train and test is a milder cousin of the same bug.",
    "Using tomorrow's close as a feature for today's trading signal is leakage. Fitting StandardScaler on train plus test is leakage too, and both make a notebook look smarter than production.")
add("Cross-validation vs walk-forward?",
    "Cross-validation rotates folds so every slice gets a turn as the exam. Walk-forward slides a window through time so you always train on the past and test on the later days. Random folds are the wrong exam when time matters.",
    "Random K-fold leaks time because a later day can train a model that is then scored on an earlier day. Trading, demand, and any labelled stream with drift need walk-forward evaluation, often with an embargo or purge gap so nearby labels cannot leak. Nested walk-forward is how you tune without peeking. In an interview, name the unit you split on, such as day, store, or customer, not just the number of folds.",
    "TAN indicators are judged with walk-forward splits, not a shuffled five-fold. A 5-fold shuffle would let future bars tutor the past and inflate the story.")
add("Class imbalance? How to handle?",
    "If only one in a hundred frames has a rare SKU, the model can ignore that SKU and still look accurate. Accuracy then hides the miss. You have to count the rare class on purpose.",
    "Handle imbalance with more rare labels first, then class weights, resampling, focal loss, and threshold tuning on a validation slice that still has the rare class. Always report per-class recall, not only micro averages. Collecting more bananas will not teach a rare oil SKU. For checkout, a missed rare item is often more expensive than another common false negative, so the threshold is a cost decision.",
    "Rare SKUs at ezyCart checkout need extra labelled boxes, not just more bananas. We track per-class recall for those SKUs and refuse to ship on overall accuracy alone.")
add("Feature scaling? Normalization vs standardization?",
    "Scaling puts features on a similar yardstick so one loud column does not shout over the others. Normalization usually squeezes values into a range. Standardization centers them and divides by spread.",
    "Fit the scaler on train only and persist it with the model, or you have leakage and train-serving skew. Trees such as XGBoost care less about scale; neural nets and linear models care more. Heavy-tailed features often want a quantile transform rather than a naive z-score. Leave one-hot columns as zeros and ones; do not z-score them into nonsense.",
    "For a tabular promo model, scale the numeric features with a train-only scaler and leave one-hot flags as zero or one. Dump that scaler inside the sklearn pipeline so serving cannot forget it.")
add("XGBoost / gradient boosting vs random forest vs linear model?",
    "A linear model is a straight rule you can read. A random forest is many trees voting. Gradient boosting is trees that take turns correcting the last tree's mistakes.",
    "Start tabular work with a linear baseline, then try XGBoost when you need interactions and non-linearities. Random forests are strong and less fussy about scale, but boosting usually wins on well-tuned tabular leaderboards. Neural nets earn their keep when you have huge data or mixed modalities such as images plus text, not when you have a few thousand promo rows. In an interview, say what you would ship first and what would have to beat it.",
    "For who buys which promo, ship an XGBoost baseline before you reach for an LLM classifier. If the boosted trees already rank well, the language model has to beat that number, not just sound smarter.")
add("What is sklearn Pipeline and why?",
    "A Pipeline is a recipe that packages preprocessing and the model so you cannot forget a step at serving time. It fits on train folds only. You save the whole object, not a loose scaler in one file and a model in another.",
    "Put imputation, scaling, and encoding inside the pipeline so cross-validation cannot leak, then joblib-dump the fitted pipeline as the unit you deploy. The alternative is a notebook that scaled on all rows and a production job that scaled differently. Pipelines also make it obvious which columns the model expects. That discipline matters more than the brand of the estimator.",
    "Merchant forecasting can be one pipeline of imputer, scaler, then XGBoost. Serving loads that single object so the live features take the same path the validation fold took.")
add("Calibration of probabilities?",
    "A 70 percent score should be right about 70 percent of the time if you want to treat it as a probability. Raw model scores are often more like ranks than chances. Calibration is the repair job that checks that claim.",
    "You inspect reliability diagrams and, when needed, fit Platt scaling or isotonic regression on a held-out set. Detection confidence from YOLO is not automatically a probability, and a 0.9 box score is not a 90 percent chance until you measure it on store data. Downstream systems that charge, abstain, or page a human need calibrated scores. Recalibrate when the camera, the store, or the class mix shifts.",
    "Do not treat a YOLO 0.9 as a 90 percent chance without calibration on store cameras, and if the night-shift curve is off, gate checkout on a store-specific threshold.")
add("What is batch vs online vs mini-batch learning?",
    "Batch learning looks at all the data before it takes a step. Online learning looks at one example at a time. Mini-batch is the usual middle path that trains on a small group each step.",
    "Most production computer vision is mini-batch training, offline or batch evaluation, and online inference per frame. True online learning in production is rare because you need drift detection, label delay handling, and a rollback. Periodic retrain on newly labelled frames is the practical pattern. Say which of those three you are doing, because interviewers use the words loosely.",
    "We retrain nightly on newly labelled cart frames, which is periodic mini-batch learning, not true online learning. Inference still runs per camera frame with a frozen exported model.")
add("Train/serving skew?",
    "Skew is when the model trained on clean tables but production feeds it messy live data. The notebook metric then has nothing to do with the camera. You fix it by making train and serve share the same feature code.",
    "Use the same preprocess path, log the served features so you can replay them, and put schema checks at the boundary. Resolution, color format, normalization, and letterbox settings are common vision skews. For tabular models, a different missing-value fill or timezone is enough to wreck a score. If you cannot replay a production request through the training preprocess, you do not actually know why the model failed.",
    "Training used RGB images at 640 pixels while the device sent NV12 at 320 pixels, and mAP collapsed. Matching the preprocess, including color convert and letterbox, restored the number.")
add("What is a baseline and why start there?",
    "A baseline is a dumb simple method you must beat before you are allowed to ship something clever. If you cannot beat it, the clever thing is not earning its complexity. Interviewers want to hear what you compared against.",
    "Useful baselines include majority class, last-value forecast, BM25-only retrieval, and a keyword FAQ. You freeze the eval set, measure the baseline, then only keep the new system if groundedness, latency, or error rate actually moves. Complexity that does not beat the baseline is a hobby. This is also how you defend RAG or an LLM classifier against a cheaper lookup.",
    "Measure a BM25-only shopping FAQ against full recipe RAG on the same labelled questions. If groundedness does not lift, do not ship the extra retrieval stack.")
add("PyTorch: tensor, autograd, nn.Module, DataLoader?",
    "A tensor is a grid of numbers the GPU can chew. Autograd tracks how those numbers should change when the loss moves. An nn.Module is the model, and a DataLoader feeds it batches.",
    "You put tensors on cpu or cuda, wrap training in a Module so parameters are registered, and use a DataLoader for shuffled batched input. For inference you want eval mode and no_grad or inference_mode so dropout, batch-norm, and autograd behave. Automatic mixed precision is a training-speed tool, not a substitute for a correct forward. Export to ONNX with a dummy tensor that matches production shape, or the runtime will surprise you.",
    "Export YOLO to ONNX with a dummy tensor of the production image size. If you export at 640 and the cart sends 320, you have built train-serving skew into the file.")
add("eval() vs no_grad() vs inference_mode()?",
    "eval() changes layers such as dropout and batch-norm so they behave as they do at test time. no_grad() stops tracking gradients so you do not waste memory. inference_mode() is a stricter PyTorch inference context that also blocks view-tracking surprises.",
    "You usually want both eval() and a no-grad context at serve time in PyTorch. Forgetting eval() leaves dropout on and makes checkout detections flicker. no_grad() alone does not switch batch-norm to running stats. An ONNX Runtime session is inherently inference, so this pair is about the PyTorch prototype you use before export.",
    "If a PyTorch prototype forgets eval(), dropout stays on and cart boxes jitter frame to frame. The ONNX Runtime session we ship is inherently inference, but the prototype that produced that file must have been in eval mode.")
add("ONNX export pitfalls?",
    "Not every PyTorch operator exists in ONNX, so export can succeed and still be wrong. Dynamic shapes and non-maximum suppression are the usual pain. You must check numerical parity on a golden image, not only that the file was written.",
    "Pin the opset, simplify the graph when you can, and test box or logit parity against PyTorch before you hand the file to TensorRT or TF Lite. Custom NMS plugins are a frequent TensorRT break. Keep a golden clip or image in CI so a later export cannot silently drift. Dynamic batch and dynamic spatial size are features you enable on purpose, not defaults you assume.",
    "A custom NMS plugin broke TensorRT on the kiosk path. We compared boxes on a fixture clip against PyTorch and only then accepted the engine.")
add("JAX: grad, jit, vmap in one line each?",
    "grad takes derivatives of a Python function. jit compiles that function so later calls run as compiled XLA. vmap runs the same function across a batch without you writing the batch loop.",
    "JAX is functional and XLA-backed, which is a different habit from PyTorch's imperative modules and autograd tapes. You choose it when the team and the serving stack already live there, not because the three words sound smart. For cart vision a PyTorch-native detector with an ONNX export is the boring path that ships. Rewriting YOLO in JAX for fashion is a schedule risk.",
    "If the team is PyTorch-native for computer vision, do not rewrite YOLO in JAX to look modern. Export the PyTorch model to ONNX and spend the time on store eval.")
add("TensorFlow vs PyTorch vs JAX — how do you choose?",
    "Think of them as three workshops. You pick the workshop that already has the model, the deploy path, and the people who can debug it at 2 a.m. Switching later is possible if you export, but it is never free.",
    "PyTorch currently owns most detection research and our YOLO path. TensorFlow still matters when TF Lite on Android is the constraint. JAX matters when you want XLA and a functional stack. The reversible choice is to train where the team is strong and export ONNX when the operator set allows it, then pick TensorRT or TF Lite from the device. Do not start from a framework war; start from the runtime you must hit.",
    "Detection trains in PyTorch, exports to ONNX, and runs TF Lite on the Android cart. That path is a choice about devices and people, not a claim that one framework is universally better.")
add("What is transfer learning?",
    "Transfer learning starts from a model that already saw many pictures or words, then teaches it your smaller dataset. You are borrowing a head start. You still have to check that the new domain did not break the borrowed features.",
    "The usual recipe is freeze the backbone, train a new head, then unfreeze lightly with a small learning rate. The domain gap matters: a supermarket cart is not COCO, and a recipe question is not Wikipedia. If the gap is large you need more labelled store data, not only a fancier pretrained checkpoint. Transfer learning is how we fine-tune YOLO on store SKUs rather than training from scratch.",
    "Fine-tune YOLO on labelled ezyCart SKUs rather than training a detector from random weights. Freeze first, then unfreeze the backbone gently once the head is stable.")
add("What is data augmentation for images? Risks?",
    "Augmentation makes extra training pictures by flipping, cropping, or changing lighting so the model sees more variety. You only do this on the training set. If you overdo it you can destroy the very clues the model needs.",
    "Photometric augments such as brightness and mild color jitter help with store lighting; geometric augments such as scale and translation help with camera pose. Do not flip text or OCR, do not recolor SKUs until oil and sauce look interchangeable, and do not pretend augmentation replaces real night-aisle captures. Apply augmentation only on train, and keep a clean validation set that looks like production. Targeted real data for glare and occlusion beats cartoonish transforms.",
    "Do not color-jitter so hard that SKU colors become unrecognizable. Keep real night-aisle frames in the set, because no amount of synthetic brightness will fully replace them.")
add("Label noise and how it shows up?",
    "Wrong boxes teach the model wrong habits, the way a misspelled flashcard teaches the wrong word. The loss can still fall. Production then disputes the same SKU the annotators already confused.",
    "You find label noise in per-class confusion, in annotator disagreement, and in a model that confidently repeats a systematic misbox. Treatments include consensus labelling, QA sampling, and losses that are less eager to overfit a wrong box, but the first fix is the labels. A high mAP on noisy labels is not a store win. Checkout disputes are often cheaper to prevent in the labelling tool than in a later model tweak.",
    "If annotators misbox oil as sauce, the detector will cause checkout disputes on those bottles. Fix the labels and the guidelines first, then retrain, rather than stacking more augmentations on the same mistake.")
add("mAP, IoU, NMS for detection?",
    "IoU is how much two boxes overlap. NMS throws away extra boxes that are sitting on the same object. mAP summarizes precision across classes and overlap thresholds so you can compare detectors.",
    "People quote mAP at IoU 0.5 or a range up to 0.75, and those protocols are not interchangeable. Soft-NMS and transformer detectors such as RT-DETR change how duplicates are suppressed, and RT-DETR aims to avoid classic NMS in the core. High mAP can still fail on glare and occlusion, so you also need a checkout-oriented metric such as wrong-charge rate. Two boxes on one bottle should collapse to one after NMS; if they do not, you will double count.",
    "Two boxes on one bottle should become one after NMS, and we report mAP at 0.5 together with a checkout-oriented error rate because a pretty mAP can still charge the shopper twice.")
add("Classification vs detection vs segmentation vs tracking vs OCR?",
    "Classification says what is in the picture. Detection says what and where with a box. Segmentation paints the pixels, tracking keeps the same object over time, and OCR reads the text.",
    "Checkout vision is usually detection plus tracking so a banana is not counted in every frame as a new item. Segmentation is heavier and useful when you need a mask, such as spill or hand-over-item cases. OCR is for shelf labels, price tags, and packed text, not for recognizing a bottle by its shape. Pick the task from the decision you must make, not from the fanciest head you can attach.",
    "Use OCR for shelf labels and detection for items in the cart camera. Add tracking on the tray so the same banana is not billed thirty times as the shopper holds it still.")

# CV / spatial intermediate
add("What is computer vision in production?",
    "Production vision is cameras plus models plus hardware plus monitoring, not a notebook demo that looked good on one clip. You have to say what happens when confidence is low. You also have to keep labelling new failures.",
    "Define the task, the metric, the lighting and occlusion domain, the latency budget, the privacy rule, and the fallback when the model abstains. Then build a dataset flywheel so production errors become labels. ezyCart self-checkout vision plus kiosk is this loop, not a single YOLO checkpoint. Fail closed on low confidence so a confused frame does not invent a SKU. Hardware thermal limits and model updates are part of the same design.",
    "ezyCart self-checkout vision plus the kiosk must fail closed on low confidence. A pretty demo clip is not production until lighting slices, latency, and a human fallback are specified.")
add("YOLO family (v8/v10/v11) — what to say?",
    "YOLO is a family of fast one-shot detectors that look at the image once and predict boxes. Bigger versions are usually more accurate and slower. You pick a size the same way you pick an engine for a trolley, not from a blog's COCO chart.",
    "Choose nano or small for a cart NPU and a larger variant for a back-office GPU, then benchmark on your own video, not on COCO screenshots. Talk about license, export path to ONNX or TF Lite, and how NMS is handled in the version you picked. v8, v10, and v11 differ in architecture details, but the interview is about device budget, eval set, and operations. Keep one eval set when you swap family members so the comparison is fair.",
    "On the cart NPU we try nano or small YOLO; on a back-office GPU we can afford a larger weight. Both are scored on the same store clips so a COCO blog post cannot pick the winner.")
add("What is RT-DETR?",
    "RT-DETR is a real-time detection transformer. It is still a detector that outputs boxes and classes, just with different guts than YOLO. You compare it on your device, not on a paper's headline.",
    "It uses a set-prediction style and typically avoids classic NMS in the core, which is the talking point interviewers expect. You still compare mAP, small-object recall, milliseconds, and memory on the same image size and precision as YOLO. Transformer detectors can be kinder to crowded shelves and harsher on a tiny NPU. Bake them off with identical preprocessing so you are not comparing two different letterboxes.",
    "Bake off YOLO versus RT-DETR on aisle clips with identical image size and precision. Keep the winner only if store mAP and sub-100ms latency both hold on the target device.")
add("OpenCV's role if you have YOLO?",
    "OpenCV is the Swiss Army knife around the network: resize, undistort, draw, and classic vision. YOLO does not replace those chores. You still need honest pixels before the detector sees them.",
    "Run camera calibration, undistort, color convert, and letterbox in OpenCV or an equivalent, then feed the tensor to ONNX or TF Lite. Do not rewrite undistort in PyTorch on a device just to look neural. Postprocess drawing and simple rules also live here. The network is one stage in a pipeline whose other stages are still computer vision.",
    "Undistort the cart camera with OpenCV, then run the ONNX detector. If you skip undistort, every downstream box is in a bent geometry even when YOLO is right.")
add("Camera calibration, distortion, extrinsics?",
    "Lenses bend pictures, especially at the edges of a cart camera. Calibration measures that bend so geometry is honest. Extrinsics say how the camera sits relative to the robot, the IMU, or the store.",
    "Intrinsics describe focal length and distortion inside one camera. Extrinsics describe pose between cameras, or between a camera and an IMU, which visual-inertial odometry needs. Bad calibration becomes SLAM drift, wrong aisle distances, and product-finder paths that miss the bay. Time sync belongs in the same conversation, because a beautiful extrinsics matrix with a 40 millisecond IMU lag still drifts.",
    "Kimera-VIO needs camera-IMU calibration and clock sync. If those are sloppy, indoor navigation drift is a calibration problem long before it is a model problem.")
add("What is SLAM?",
    "SLAM means you build a map while you also figure out where you are. It is simultaneous localization and mapping, not a single neural net. It fails in boring ways such as blank walls and moving people.",
    "A typical stack has a front end that tracks features, a back end that optimizes poses, and loop closure that recognizes a place you have seen before. Failure modes include textureless walls, crowds, and lighting changes, so you need an aisle-level error budget and a fallback. Indoor navigation that replaced thousands of Bluetooth beacons and saved over 2 million dollars is still a SLAM-plus-operations story, not a claim that drift vanished. Explain the error and the failure modes in the same breath as the savings.",
    "Indoor navigation replaced thousands of Bluetooth beacons and saved over 2 million dollars. In an interview I still explain aisle-level error, textureless aisles, and what the trolley does when tracking drops.")
add("VIO vs VO vs wheel odometry?",
    "Visual odometry estimates motion from the camera alone. Visual-inertial odometry adds an IMU so blur and fast turns have another vote. Wheel odometry counts wheel turns and will lie when the wheels slip.",
    "These sensors are complementary, and they only fuse well if clocks are synced and IMU biases are estimated. Smooth supermarket tiles are a classic wheel-slip surface, while a camera can go blind in a motion-blurred turn where the IMU still sees acceleration. VIO is the usual fusion for a trolley. Do not quote wheel odometry as ground truth on wet floors.",
    "On smooth store tiles the wheels may slip while the camera blurs in a fast turn. VIO lets the IMU carry the pose through that moment, which is why the trolley uses visual-inertial fusion rather than wheels alone.")
add("Kimera-VIO — what is it and what must you not overclaim?",
    "Kimera-VIO is open-source visual-inertial odometry in the Kimera family. It estimates pose from a camera plus an IMU. It is not a full 'SLAM is solved' claim by itself.",
    "Know the inputs, which may be mono or stereo plus IMU, the pose output, the compute budget, and the assumption that calibration and time sync are good. Validate drift on real store routes with an aisle-level error, not a hallway demo. Loop closure and a store map are extra systems; running VIO is not the same as a complete SLAM product. Do not tell an interviewer that indoor navigation is finished because Kimera-VIO started.",
    "We use Kimera-VIO as the motion estimate that feeds the product-finder path. That is a pose stream, not a claim that store-scale SLAM is a solved research problem.")
add("Spatial AI?",
    "Spatial AI is not only saying this is a chair. It is saying the chair is two meters to the left in a frame the trolley understands. Geometry and localization sit next to perception.",
    "You combine perception, geometry, localization, and sometimes planning, and you keep coordinate frames honest among camera, IMU, map, and store. A SKU in the map frame and a trolley in the map frame let you plan a path between them. If those frames drift, the product finder sends people to the wrong bay. Spatial AI is a systems word; in an interview, name the frames and the error you tolerate.",
    "The product finder puts a SKU in the store map frame and the trolley in that same frame, then plans a path between them. If VIO drift grows, that path is wrong even when the SKU classifier is right.")
add("Edge vs cloud inference for vision?",
    "Edge inference runs on the device in your hand or on the trolley. Cloud inference runs on a faraway GPU. Edge is faster and still works if Wi-Fi dies; cloud can host heavier models.",
    "Choose using privacy, bandwidth, thermal limits, update mechanics, and a fallback when the network or the accelerator fails. A hybrid is common: a tiny on-device model for the live path, and a cloud model for hard cases you can afford to delay. Streaming every cart frame to a hosted LLM or Bedrock is the wrong default because of cost, privacy, and latency. Sub-100ms ONNX or TF Lite on the cart is the live checkout path.",
    "Run ONNX or TF Lite on the cart for sub-100ms detections. Do not stream every camera frame to Bedrock; that blows privacy, bandwidth, and the latency budget.")
add("TensorRT vs TF Lite vs ONNX Runtime?",
    "ONNX is the suitcase you pack the model into. TensorRT is a fast unpacker on NVIDIA. TF Lite is the unpacker you take to phones and many edge chips.",
    "The real differences are operator coverage, quantization tools, and how you profile them on the target device. After every export you run golden tests so a missing op did not silently change boxes. Android carts typically want TF Lite or ONNX Runtime; NVIDIA kiosks can take TensorRT. Pick from the hardware you already have, then verify milliseconds and numerical parity, not from a vendor slide.",
    "The Android cart path uses TF Lite or ONNX Runtime, while an NVIDIA kiosk can use TensorRT, and both must pass the same golden-image box comparison after export.")
add("How do you get sub-100ms vision?",
    "You time every stage, shrink the slowest one, then recheck quality. The resume number must say whether it is end-to-end or model-only. A fast network behind a slow resize is still a slow trolley.",
    "Profile resolution, quantization, batch size of one versus larger batches, CPU affinity, and memcpy. End-to-end latency includes camera, color convert, letterbox, infer, NMS, and tracking, and that is the number a shopper feels. Quantizing or switching YOLO size only helps after you know which stage dominates. Sub-100ms ONNX or TF Lite is a measured pipeline, not a model-card claim.",
    "If resize is 40 milliseconds, infer is 30, and NMS is 5, you fix resize first. That is how a cart pipeline gets under 100 milliseconds without magically shrinking the network.")
add("Tracking IDs across frames?",
    "Tracking gives the same banana the same name as it moves so you do not count it thirty times. Detection alone is forgetful. Checkout needs memory across frames.",
    "ByteTrack and SORT-style trackers combine IoU with optional appearance features, and they must handle occlusion when a hand covers the item. You reset identities when the cart or tray is empty so stale IDs cannot resurrect. Scan-bag-pay flows track objects on the tray, not independent per-frame detections. If tracking breaks, you get double charges even when the detector is fine.",
    "In scan-bag-pay we track objects on the tray rather than treating every frame as a new set of SKUs. A still banana keeps one ID until the tray is empty.")
add("Lighting, glare, occlusion — domain shift?",
    "A model trained at noon can fail at night or under a window reflection. That is domain shift, not a random bug. You measure each lighting world on its own.",
    "Split eval by scenario: store LED, window glare, night aisle, and heavy occlusion. Collect targeted data for the failing slice, use auto-exposure carefully, and gate on confidence when the frame is from a world you do not cover. One blended mAP hides a glare disaster. Production vision lives or dies on those slices.",
    "We report separate metrics for store LED versus window-glare sets rather than one blended mAP. If glare recall drops, we collect that slice instead of training longer on easy noon frames.")
add("Privacy for cameras in a store?",
    "Do not keep faces if you do not need them, and say clearly what you store. A cart camera is not a license to build a face database. Shoppers should be able to hear the retention rule in one sentence.",
    "Minimize: process on device when you can, drop frames that are not needed for the SKU event, blur or avoid storing faces, set retention, and log access. Regulation and retailer policy sit beside the model card. Checkout vision can keep the SKU event without keeping a shopper's face. If a hosted model would see raw video, that is a privacy decision, not only a latency decision.",
    "Checkout vision can drop frames that are not needed for the SKU event and avoid storing faces. That is a product rule, not an afterthought once the detector works.")

# Backend intermediate
add("Why FastAPI for AI services?",
    "FastAPI is a Python API framework with type checks and auto-generated docs, sitting next to the same language as PyTorch and ONNX. That is why AI services like it. It is not automatically the system of record for a whole retailer.",
    "You get Pydantic validation, async handlers, OpenAPI, and dependency injection, which are ideal for vision and RAG orchestration. CPU or GPU inference must be offloaded from the event loop, and you still need timeouts, auth, and tracing. At Retailetics the Python FastAPI services sit beside a Java Spring Boot estate behind stable contracts. Choose FastAPI where the ML libraries live; do not rewrite every business ledger into Python for fashion.",
    "Vision and recipe RAG orchestration run in FastAPI. The broader Java estate stays on Spring Boot, and the two talk through versioned contracts rather than one language winning.")
add("Pydantic / bean validation?",
    "Validation checks the form before you accept it, whether that form is JSON from an LLM or an HTTP body. Garbage in is how checkout invents a negative quantity. You reject at the boundary, not deep in the agent.",
    "Pydantic on FastAPI and bean validation on Spring Boot are the same idea: typed schemas, useful error messages, and versioned contracts. LLM tool JSON is untrusted input and must pass the same validation as a public HTTP body. Invalid payloads fail closed with a 4xx, not with a guessed default that charges a shopper. Schema evolution needs compatibility rules so an old Android app does not crash on a new field.",
    "LLM tool JSON and HTTP bodies both go through Pydantic. A model that emits qty=-1 is rejected at the boundary before add-to-cart can run.")
add("Spring Boot in one minute?",
    "Spring Boot is the Java way to build services with batteries included: web, security, config, and actuators. It is how a large retailer already runs. Python FastAPI does not have to replace it.",
    "You coexist with FastAPI behind stable contracts, and you care about thread pools, backpressure, and observability the same way you would in any production JVM service. IoT WebSocket gateways, auth, and device identity often live here because the Android estate already speaks that stack. Observability actuators and mature ops are the reason it stays. In an interview, describe the boundary, not a holy war between Java and Python.",
    "The IoT WebSocket gateway in Spring Boot talks to the Android app, while FastAPI handles vision and RAG. Duplicate scans must still be idempotent across that boundary.")
add("Microservices vs modular monolith?",
    "Microservices are many small programs talking over the network. A modular monolith is one program with clear internal walls. You split only when a boundary pays rent in scaling or ownership.",
    "Every extra service buys you independent deploys and a bill of network failure, distributed data, and versioning. Start modular in one repo with hard module boundaries, then extract when a workload such as vision inference scales differently or a team needs a separate lifecycle. Do not split add-to-cart into a dozen services. Do split GPU inference if its autoscaling and failure modes would poison the checkout API.",
    "Do not split add-to-cart into twelve services. Do split vision inference when it needs its own GPU pool, timeouts, and deploy cadence from the REST catalogue API.")
add("How do WebSockets stay reliable for IoT?",
    "You keep the call up, number the messages, retry without doubling the work, and notice when the other side has died. A trolley that reconnects must not charge twice. Heartbeats are how you learn the cable is dead.",
    "Device identity, a versioned schema, timestamps or sequence numbers, heartbeats, backoff, acknowledgements, idempotency keys, and replay on reconnect are the checklist, and each item is a sentence in the design, not a buzzword. Restore state from a source of truth after reconnect rather than trusting the in-memory socket. At-least-once delivery is the default, so consumers must be idempotent. FastAPI and Spring Boot sockets in the ezyCart path have to agree on that contract.",
    "ezyCart devices talk to Android through FastAPI and Spring Boot WebSockets. Duplicate scan events must not double-charge, so every charge carries an idempotency key that survives reconnect.")
add("REST vs WebSocket vs SSE in the trolley stack?",
    "REST is for asking or changing a thing and getting an answer. WebSockets are for live device chatter both ways. Server-sent events are for a one-way token stream to the UI.",
    "Do not multiplex every concern onto one socket unless you have a reason, because backpressure, auth refresh, and retries differ. SKU lookup is a REST call. IMU and scan events are WebSocket messages. Lisa's tokens are SSE so a tablet can render words as they arrive and cancel when the shopper walks away. Mixing those without queues is how you drop IMU samples while an LLM prompt blocks.",
    "SKU lookup stays REST, IMU and scan events stay on WebSockets, and Lisa tokens stream over SSE. That split keeps a slow recipe answer from stalling live device events.")
add("How do you debug a slow API?",
    "Measure first, find the slow station, change one thing, and measure again. Guessing is how you cache the wrong layer. Percentiles tell you who is actually waiting.",
    "Look at p50, p95, and p99, then traces, SQL EXPLAIN, N+1 queries, payload size, and downstream timeouts. Indexes, query rewrites, and caches are different medicines. The Colan work that made responses about 40 percent faster is a backend story only if you can say whether indexing, caching, or a query rewrite moved the needle. Never quote an average alone while the tail is on fire.",
    "When responses got about 40 percent faster in the Colan-era backend work, the honest interview answer is which measurement moved: indexing, caching, or query rewrite. I would put the trace beside that number.")
add("Cache invalidation basics?",
    "A cache is a sticky note of the answer so you do not redo the work. When the truth changes you must throw the note away. That throw is the hard part.",
    "Use TTLs for naturally aging data, explicit purge when a catalogue updates, and stampede protection so a miss does not melt the origin. Never cache ACL-sensitive personalized prices without the shopper or tenant in the key. Semantic caches for RAG need the same discipline plus a content-hash of the retrieved sources. A cache without an invalidation story is a correctness bug with extra latency wins.",
    "Recipe RAG can use a semantic cache keyed by tenant plus basket hash, and it must miss when the catalogue or the policy chunk changes. Personalized member prices never share that key.")
add("Message queues vs request/response?",
    "A queue is a waiting line for work that can happen in a second, not in this HTTP request. Request and response is for the shopper who is still holding the phone. You pick based on whether the caller can wait.",
    "Systems such as Celery, SQS, or Kafka give you at-least-once delivery, so consumers must be idempotent and you need backpressure and poison-message handling. Embedding ten thousand new products belongs on a queue; the HTTP handler only enqueues. Request and response stays for lookups with a tight SLO. Mixing those without a timeout is how a catalogue re-embed blocks checkout.",
    "A POST to re-embed new products only enqueues a Celery job. The HTTP request does not wait for ten thousand vectors, and the worker is idempotent on product id.")
add("Celery / background jobs?",
    "Background jobs do slow homework in the back room so the counter stays fast. They retry when the world is flaky. They must not retry a charge that already succeeded.",
    "You design retries, acknowledgements, poison queues, idempotency keys, and visibility timeouts as if duplicates will happen, because they will. Nightly re-embeds, report generation, and video export belong here. Anything with money needs a stronger exactly-once story than default Celery retries. Observability of queue depth is part of the API's health.",
    "A nightly job re-embeds changed catalogue pages. If it runs twice, the same product id writes the same vector, so the retry cannot create a second truth.")
add("GraphQL when, not when?",
    "GraphQL lets a client ask for exactly the fields it wants. The risk is that the server now does a surprise amount of work. It is not a replacement for a live event stream.",
    "You need query cost analysis, persisted queries, and an N+1 defense, usually DataLoader-style batching. Staff apps that stitch product details from many resources can benefit. Live IMU samples and scan events do not belong on GraphQL subscriptions if you already have a WebSocket schema with backpressure. Treat GraphQL as an API style with a denial-of-service surface, not as a magic bus.",
    "A staff app can load product details through GraphQL. Live IMU from a trolley stays on the existing WebSocket path, not a GraphQL subscription.")
add("Authn vs authz? RBAC vs ABAC?",
    "Authentication is who you are, and authorization is what you may do. RBAC grants power by role, and ABAC grants it by attributes and policies on the request.",
    "You still check per resource, isolate tenants, and give services identities, often with mTLS, rather than trusting a role string in a JWT forever. Shoppers cannot read other carts. Staff roles cannot export PII dumps without audit. ABAC helps when store, shift, and data class matter more than a single role name, but RBAC is the readable default until those rules exist.",
    "A shopper cannot read another cart, and a staff role cannot export a PII dump without an audit trail. That is authorization on a resource, not only a logged-in flag.")
add("Rate limiting and backpressure?",
    "Rate limiting slows noisy clients so one shopper or one bot cannot knock the API over. Backpressure is the same idea inside your own queues. Fairness per tenant matters as much as a global cap.",
    "Token buckets, 429 responses with Retry-After, load shedding, and queue limits are how you survive. An LLM gateway should cap tokens per minute per store so one prompt loop cannot burn the budget. Backpressure on WebSockets means you drop or sample IMU rather than unbounded buffering. Limits without identity just punish a NAT; limits with a tenant key protect the estate.",
    "The LLM gateway limits tokens per minute per store so one bot cannot burn the budget. A 429 with Retry-After is better than an unbounded Bedrock bill.")
add("Health checks vs readiness vs liveness?",
    "A liveness check says restart me if I am dead. A readiness check says do not send traffic yet. They are not the same probe, and mixing them causes restart storms.",
    "Do not make liveness call a GPU or a lock you might already hold, because a hang then becomes a deadlock restart loop. Readiness should wait until the ONNX Runtime session is loaded. Liveness should stay cheap. Kubernetes will do exactly what you asked, including killing a process that was only slow on a cold model load.",
    "The process is ready when the ONNX Runtime session is loaded, not merely when the HTTP port is open. A crash loop is not ready, and a GPU hang must not be the liveness probe.")
add("Docker: image, layer, registry, non-root?",
    "A Docker image is a box with the app and its libraries. Layers cache the build so you do not recopy the world every time. A registry stores those boxes, and you should not run them as root.",
    "Use a small base, pin digests, scan CVEs, run as non-root, keep secrets out of layers, and add a HEALTHCHECK. Multi-stage builds keep compilers out of the runtime image. Distroless or slim runtimes are for FastAPI plus ONNX Runtime. Reproducible tags beat latest.",
    "The FastAPI plus ONNX Runtime image is a multi-stage build with a slim runtime, non-root user, and no Bedrock keys in the layers. We pin the digest that staging already ran.")
add("docker vs VM vs process?",
    "A VM virtualizes hardware, while a container virtualizes the operating-system userland. A process is just a program on the box you already have.",
    "You trade isolation against overhead. Cloud APIs belong in containers because you want a uniform rollout. On-cart inference is often a process or a library inside the Android app, because nested virtualization is wasted weight on a trolley. Do not container-religion a device that only needs a TF Lite interpreter.",
    "Cloud APIs run in containers. On-cart inference is a process or a native library, not a Docker daemon on the trolley.")
add("CI/CD for mobile + backend together?",
    "You need two pipelines that meet at a contract test, because the app and the API ship on different days. The contract is the handshake. Feature flags are how you survive a mismatch.",
    "Android may flow through Bitrise or GitLab while the API has its own tests, and you version the event schema. An app that expects a new event field must not ship before the gateway understands it. Staged rollouts and flags let you pause one side. Mobile plus backend CI is coordination, not one giant job that paints a green check.",
    "If the Android app expects a new WebSocket event schema, it must not roll out before the gateway. Contract tests in both pipelines are the gate, not a Slack promise.")
add("Observability: logs, metrics, traces?",
    "Logs are stories about what happened. Metrics are numbers you can graph. Traces are the path of one request across services, including the LLM and the database.",
    "Use RED or USE as a starting language, watch cardinality so a cart_id label does not explode Prometheus, and attach exemplars from a spike to a trace. One trace id should follow Android through FastAPI, retrieval, the model, and the WebSocket write. Logs without a trace id are a scavenger hunt. LLM calls belong on that trace or you will never explain a slow Lisa answer.",
    "A cart_id and trace_id start on Android and follow the request through RAG and the WebSocket write. That is how you debug a slow recipe without grepping three systems by time.")
add("What is p95 latency and why not only average?",
    "Average hides the slow shoppers. p95 is the wait that 95 percent of requests beat, so 5 percent are worse. Those 5 percent are often the people who complain.",
    "Put SLOs on p95 and p99, not only on the mean. Tails come from garbage collection, cold starts, retrieval, and the language model, and Lisa's time-to-first-token p95 matters more than a pretty mean if 5 percent of shoppers wait eight seconds. Quote which timer you mean: model-only or end-to-end. Averages are how you miss a stall.",
    "Lisa time-to-first-token p95 matters more than the mean if 5 percent of shoppers wait eight seconds. We SLO that tail, not a notebook's average token time.")
add("Connection pooling?",
    "Pooling reuses database connections instead of shaking hands every request. Handshake time adds up under a kiosk burst. A pool that is too large just knocks over the database.",
    "Size the pool against the database max_connections, set timeouts, and hunt leaks because a leaked checkout connection is a production incident. Spring Boot's HikariCP and FastAPI async pools both need burst math for kiosks. A pool of one per request is not a pool. Watch wait time, not only active connections.",
    "Spring Boot Hikari and the FastAPI async pool are sized for a kiosk burst, not for a quiet laptop demo. If pool wait climbs, we have a leak or an undersized database, not a mysterious slow API.")
add("Pagination, filtering, idempotency keys in public APIs?",
    "Public APIs must bound how much you return, how you filter, and how a retry avoids double work. This is the same idea as basic SQL and HTTP, now with SLOs and abuse in mind. A 2 gigabyte GET is not a feature.",
    "Cap page size, prefer cursor pagination for stable snapshots, and require signed idempotency keys with a TTL on creates and payments. Heavy exports become an async job plus a download link. Filters that hit unindexed columns will blow p95. Idempotency is how a flaky mobile network does not double-charge.",
    "A staff audit export is an async job plus a download link, not a 2 gigabyte GET. The create call carries an idempotency key so a retry does not start a second export.")
add("500K users — what do you clarify?",
    "You clarify whether 500 thousand means registered accounts, daily actives, or concurrent sessions. Design to the peak queries per second, not a vanity count. A chat product with a million daily users is a different bottleneck from a retail account database.",
    "Load-test the actual peak, then apply caches, read replicas, and queued writes where they pay. The Colan-era figure of about 500 thousand users with responses about 40 percent faster is a backend story when you quote the measurement window and the workload. One million daily-active chat users would bottleneck GPUs, not the same layer. Never let an interviewer treat those numbers as interchangeable.",
    "Five hundred thousand registered users is not one million daily-active chat users. I would state which of those the Colan 500K figure was, and I would not pretend a GPU chatbot has the same bottleneck.")

# Mobile intermediate
add("Jetpack: Room, Hilt, Navigation, WorkManager, DataStore?",
    "Room is the local database. Hilt injects dependencies. Navigation moves between screens, WorkManager runs deferred work, and DataStore holds small preferences.",
    "These libraries are lifecycle-aware, which is why they beat home-grown singletons on Android. You write migrations for Room, fakes for Hilt in tests, and you treat WorkManager as best-effort deferred work, not as a real-time IMU path. DataStore replaces most SharedPreferences cases with a safer API. Together they are how an ezyCart Android app survives a socket drop without inventing a new architecture every screen.",
    "Cache the last cart locally in Room if the socket drops, then reconcile on reconnect. That is Room plus an idempotent sync, not a reason to skip the gateway.")
add("Kotlin Coroutines + Flow on Android?",
    "Coroutines make async work readable, and Flow is a stream of values over time, often UI state. You cancel work when the screen goes away. That cancellation is the point.",
    "viewModelScope cancels when the ViewModel clears, which is how you avoid leaking a WebSocket collector. StateFlow is state; SharedFlow is events; backpressure still exists if a device floods you. Collect on the right dispatcher so you never parse JSON on the main thread. Device events should flow into a ViewModel and then into Compose, not into a God Activity.",
    "Device events arrive as a Flow, the ViewModel holds StateFlow for the screen, and Compose collects it. If the user leaves checkout, viewModelScope cancellation stops the collector.")
add("What is an ANR and how did you cut 70%?",
    "An ANR is App Not Responding: the main thread was blocked for about five seconds and the user sees a freeze dialog. It feels like the app died. You cut ANRs by getting I/O and heavy work off that thread.",
    "You find them with StrictMode, traces, and the Play ANR dashboard, then you move disk, JSON, and network off the main thread and watch Choreographer frames. The resume claim of about 70 percent fewer ANRs and about 30 percent better performance is only honest if you name the measurement window and the build that changed. Do not parse JSON or hit disk on the main thread in checkout. After the fix you keep watching the same dashboard so the win does not regress.",
    "Do not parse JSON or hit disk on the main thread in checkout. The Colan-era 70 percent ANR drop and 30 percent performance lift are quoted from that before-and-after window, not from a lab anecdote.")
add("Flutter BLoC vs Provider vs setState?",
    "setState is local to a widget. Provider passes values down the tree. BLoC takes events in and pushes state out, which is easier to test without drawing the UI.",
    "Staff apps and TV monitors benefit from predictable, testable state, which is why BLoC often wins over scattering setState. Provider is fine for simple dependencies. You still keep side effects out of widgets. Pick one pattern per app so a TV monitor and a handheld are not two religions.",
    "An Android TV monitor can use a BLoC that subscribes to cart fleet events and maps them to view state. Tests can fire those events without a TV in the room.")
add("Platform channels / FFI in Flutter?",
    "Platform channels and FFI are how Dart talks to native Android or iOS when you need hardware the Flutter plugins do not cover. Keep that bridge small. Errors should come back as typed results, not as mystery strings.",
    "Channels are for scan, pay, and similar device calls; FFI is for tight native libraries. Threading matters because a blocking native call can still jank the UI. Typed error codes beat a boolean. An SDK lite that calls native scan or pay should treat the channel as an untrusted boundary the same way a backend treats HTTP.",
    "An SDK lite may call native scan and pay over a small platform channel. The Dart side validates the result and never assumes the native call succeeded because it did not throw.")
add("iOS interop / KMP at a high level?",
    "Kotlin Multiplatform lets you share some logic across Android and iOS without sharing all of the UI. Flutter shares UI another way. You should not oversell a stack you did not ship deeply.",
    "KMP uses expect and actual to fill in platform gaps. If you have shipped mostly Android and Flutter, say that honestly rather than claiming to be a UIKit specialist. iOS via Flutter or a thin interop layer is a real skill, but it is not the same as owning a large UIKit codebase. Interviewers prefer an accurate boundary to a fake native resume line.",
    "Honest answer: I have shipped Android and Flutter, and iOS through Flutter or interop, and I will not pretend to be a deep UIKit specialist unless that is actually true.")
add("Offline-first mobile?",
    "Offline-first means the app still works in a dead aisle and then syncs when the radio returns. The phone holds a local source of truth. Not every feature can work that way, especially payments.",
    "You queue writes, resolve conflicts, and replay idempotent commands when connectivity is back. Scanning and cart edits can be local; charging a card usually cannot complete without the server and an idempotent retry. Design the conflict rule before you ship the cache. A trolley in a Faraday-cage corner of a store is the test, not the office Wi-Fi.",
    "You can scan locally and keep the cart in Room, but pay requires connectivity and an idempotent retry. Offline-first is not a promise that payments work in a dead zone.")
add("Security on device: keystore, certificate pinning, secrets?",
    "Do not hide API keys in the APK and hope nobody unpacks it. Use the operating-system keystore for secrets the device must hold. Pinning is a maybe, not a default you cargo-cult.",
    "Obfuscation is not security. Attestation can raise the bar for tampered clients. Real secrets such as Bedrock keys stay on the server. Certificate pinning helps against some network attackers and hurts when you rotate certs without a pin update, so you enable it with a break-glass story. The trolley APK should hold tokens that are scoped and rotatable, not cloud credentials.",
    "Bedrock keys never live in the trolley APK. The app talks to our gateway, and the gateway holds cloud credentials in the server environment.")
add("Play/App Store staged rollout?",
    "You ship to 1 percent of users, watch crashes and ANRs, then walk to 100 percent. A store binary is a slow lever. Feature flags are a faster one.",
    "Upload mapping files so crash stacks are readable, watch ANR dashboards, and do not confuse a Play rollout with a model-file update. A vision model can be a feature-flagged download inside an already-shipped app. Flags let you disable a bad detector without waiting for store review. Staged rollout is how you avoid a 100 percent bad morning.",
    "A vision model file update may be a feature-flagged download rather than waiting for a Play release. The binary rollout still goes 1 percent to 100 percent while we watch ANRs.")
add("Deep links and notifications?",
    "A deep link opens a particular screen from a URL. A notification pokes the user and may do the same. Neither should leak personal data in transit or on a lock screen.",
    "Authenticate deep links so a guessed cart URL is not a data breach. Keep PII out of push payloads; a jammed kiosk alert can carry a device id, not a shopper name. Notification taps should land on a screen the role is allowed to see. Treat both as public surfaces even if the app is internal.",
    "Staff can be notified of a jammed kiosk with a device id, not a shopper name. The deep link opens the staff screen only after the same authz check as the rest of the app.")

# LLM / RAG intro (intermediate, full advanced later)
add("What is Generative AI? What is an LLM?",
    "Generative AI creates new content rather than only labelling what already exists. A large language model predicts the next tokens from the context you gave it. That prediction can be useful and it can also be confidently wrong.",
    "Under the hood you have a transformer decoder, a tokenizer, a context window, and a real hallucination risk. Production use adds grounding, evaluation, cost control, and safety, because a next-token model is not a database. Lisa can generate a recipe answer; YOLO cannot, and you should not use an LLM as the only allergen source. Say what is generated versus what is retrieved.",
    "Lisa generates answers; YOLO does not. We never use an LLM as the only allergen source, because a fluent sentence is not a certified ingredients database.")
add("Tokens and context windows?",
    "Tokens are pieces of words, not always whole words. The context window is how much the model can see at once. If you dump the whole store manual into that window you pay a lot and the model still gets lost.",
    "Cost scales with tokens, and a tokenizer mismatch between your counter and the model will silently truncate or inflate bills. RAG should retrieve a handful of chunks, not 100 thousand tokens of catalogue. Basket plus top chunks is the usual packing for Lisa. Long context is not a strategy if retrieval already failed.",
    "We send the basket plus the top few chunks, not the whole store manual. That keeps Lisa inside the window and inside the token budget.")
add("What is a transformer / self-attention (intermediate)?",
    "Self-attention lets each word look at the other words that actually matter for it. That is how 'this' can attach to a SKU mentioned earlier in the cart. Stack enough of those layers and you have a transformer.",
    "Each head has queries, keys, and values, then you add residuals, a feed-forward block, and positional encodings so order is not lost. Encoder-only, decoder-only, and encoder-decoder stacks are different deployment shapes. Multi-head attention is several of those looks in parallel. In an interview, connect the mechanism to a failure such as lost-in-the-middle rather than only drawing Q, K, and V.",
    "An LLM can connect the word this to the SKU mentioned earlier in the cart list because attention can look back across that context. If the cart is huge, that look-back still competes with everything else in the window.")
add("Embeddings and cosine similarity?",
    "An embedding turns meaning into a list of numbers, like a map pin for a sentence or a product. Cosine similarity asks how aligned two of those arrows are. Nearby pins can share a meaning even when the words differ.",
    "Normalize vectors before cosine, use an approximate nearest-neighbor index at scale, and remember out-of-domain queries will still get a nearest neighbor that may be junk. When you upgrade the embedding model you must re-embed the corpus, because mixed versions are not comparable. Version that model in the index metadata. Retrieval quality starts here, before the LLM writes a word.",
    "The query cheap sparkling water should sit near value seltzer even if the words differ. If we upgrade the embedding model, we re-embed the catalogue rather than mixing two maps.")
add("Prompting vs RAG vs fine-tuning (intermediate)?",
    "Prompting is the instructions you give right now. RAG is opening a trusted book and then writing. Fine-tuning is extra practice that actually changes weights.",
    "Facts that change, such as weekly promos, belong in RAG. Style and JSON format often belong in a prompt, or in a small fine-tune if the prompt cannot hold the shape. Fine-tuning does not create a live truth source, and prompting does not either. Combine them on purpose: RAG for SKU facts, prompt for tone, LoRA for a stubborn output schema.",
    "Weekly promos go through RAG, while JSON shape is a prompt or a LoRA if thousands of labelled receipts justify it. Prompting alone does not make a promo true.")
add("Temperature and top-p?",
    "Temperature and top-p control how adventurous decoding is. Low values make the model more steady and repetitive. High values make it more surprising and more willing to wander.",
    "Neither knob guarantees facts, because a fluent wrong answer can still come out at temperature zero. For tool calls and JSON you want temperature near zero so the schema stays stable. RAG answers that must cite a chunk also want a low temperature. Creative copy can run warmer, but checkout extraction should not.",
    "Missing-SKU extraction runs at temperature near zero so the JSON schema stays boring and valid. We do not turn temperature up to make a factual stock answer 'more interesting'.")
add("What is RAG (intermediate)?",
    "Retrieval-augmented generation finds trusted pages first, then writes the answer from them. The model is a speaker, not the filing cabinet. If retrieval misses, the sentence will still sound sure.",
    "The pipeline is ingest, chunk, embed, retrieve, optionally rerank, generate, cite, and abstain when the chunks are silent. You evaluate retrieval and generation separately so you know which half broke. Shopping assistant recipes with LangChain or LlamaIndex are this pattern over catalogue and policy. Citations are how a shopper or a lawyer can see the source.",
    "Lisa's shopping assistant and recipe flow retrieve catalogue and policy chunks, then generate with those rows in context. If the chunk does not list an ingredient, the answer must abstain rather than invent a SKU.")
add("BM25 vs dense vs hybrid (intermediate)?",
    "BM25 matches words. Dense retrieval matches meaning. Hybrid does both and then usually reranks, which is why it is the default when you can afford it.",
    "BM25 wins on SKUs and exact ids such as EZY-1044. Dense wins on paraphrase such as a spicy pasta night. Hybrid with reciprocal rank fusion and a reranker is the practical default, tuned on a labelled query set. Explain a failure mode for each, because none of them is magic on every query.",
    "EZY-1044 should hit BM25. A shopper who types spicy pasta night needs dense retrieval, and hybrid is how Lisa does not make the shopper choose which language to speak.")
add("Chunking and overlap?",
    "Chunking cuts documents into useful pages so retrieval can pick a passage. A little overlap stops a sentence from being torn in half. Bad chunks make even a strong model sound lost.",
    "Prefer structure-aware splits that keep headings with their clauses, use about 10 to 20 percent overlap, and treat tables and code as special rather than naive token windows. A return-policy clause must stay with its heading or RAG will cite the wrong rule. Evaluate with questions that need two parts of the same section. Chunking is a product decision, not a preprocessor default you never revisit.",
    "A return-policy clause stays in the same chunk as its heading. If we split in the middle, Lisa will retrieve a fragment and invent the missing condition.")
add("What is a vector database (intermediate)?",
    "A vector database stores embeddings and finds nearest neighbors, often with metadata filters. It is a search engine for meaning. It is not automatically secure or correctly filtered.",
    "Pinecone, Qdrant, Milvus, Weaviate, pgvector, FAISS, and similar stores differ on ops, filters, and recall, so you benchmark the query you will actually run. Apply ACL and tenant filters in the query, not as an afterthought on the result list. You still need hybrid search and eval. A vector database without metadata filters is how a shopper retrieves a staff-only chunk.",
    "The ACL filter belongs in the vector query so a shopper never retrieves staff stock-audit chunks. Filtering after retrieval is a leak waiting to happen.")
add("Hallucination (intermediate)?",
    "Hallucination is confident nonsense: a fluent answer that is not supported by the world or the documents. You will not drive it to zero. You can make it rarer and make the system abstain.",
    "Ground the model in retrieved chunks, demand citations, abstain when chunks are silent, evaluate faithfulness, keep temperature low for factual tasks, and optionally add a critic. Never promise zero hallucinations. Allergen and price answers are where this matters most. A shopping assistant that invents gluten-free is a safety bug, not a cute LLM quirk.",
    "If the retrieved chunk is silent about gluten, Lisa must not invent a gluten-free claim. Abstain, ask a follow-up, or point the shopper to the pack, rather than sounding sure.")
add("LangChain vs LlamaIndex (intermediate)?",
    "LangChain is Lego for applications and tools. LlamaIndex is a librarian for data and RAG indexes. You can combine them, and you should still keep business logic in your own code.",
    "Indexes and ingestion often sit well in LlamaIndex. Tools, agents, and graphs often sit well in LangChain or LangGraph. Test retrieval and tools with fakes so a demo key is not required to unit-test checkout. Frameworks are not an excuse to bury pricing rules inside a chain class you cannot read.",
    "We can build recipe indexes in LlamaIndex and expose tools through LangChain or LangGraph. The add-to-cart rule still lives in our service code with tests that do not call an LLM.")
add("What is an AI agent vs a chain (intermediate)?",
    "A chain is a fixed recipe of steps. An agent chooses the next allowed step as it goes. Agents fail in more ways, so you start with a chain unless the task truly branches.",
    "Agents need state, tools, budgets, and stop conditions, because a loop that can call tools can also loop until the money is gone. A SKU lookup is a chain. A multi-step recipe that then finds missing items may be an agent, still with a step cap. In an interview, say what the agent is not allowed to do.",
    "SKU lookup is a chain: retrieve, answer, stop. A recipe plus missing-items flow can be an agent that may call get_stock, but it still cannot pay without a human.")
add("ReAct pattern?",
    "ReAct means the model thinks, acts with a tool, looks at the result, and repeats. It is a loop with observations, not a single prompt. You cap the loop so it cannot think forever.",
    "Reasoning plus acting plus observing is useful when the next tool depends on the last result, such as out-of-stock then search-alternatives. Use structured tools rather than free-form side effects, and cap iterations. Log each thought and tool for traces. ReAct without a budget is a cost incident.",
    "A Lisa flow can call get_stock, see out of stock, then search_alternatives. That ReAct loop is capped, and it still cannot apply an invented discount.")
add("Tool calling (intermediate)?",
    "Tool calling is the model filling in a form and your code running the function. The model is not the security boundary. Your validator and authorization checks are.",
    "Define a JSON schema, validate with Pydantic, authorize the caller, execute with timeouts, and return a typed result. Human-in-the-loop belongs on money and irreversible actions. Treat the model output as untrusted the same way you treat a public HTTP body. If the schema is loose, the model will wander into a dangerous argument.",
    "add_to_cart uses a strict schema and Pydantic, and pay requires a human in the loop. The model may propose the tool call; it does not get to charge a card by itself.")
add("MCP (intermediate)?",
    "MCP is a standard plug for tools and context so hosts and servers can talk without a custom glue each time. It is a protocol. It is not automatically safe.",
    "You still need authentication, authorization, validation, and audit on every tool the server exposes. A catalogue MCP server is reasonable. A raw SQL MCP server without a guard is a data breach with extra steps. Treat MCP like any other remote API, because that is what it is.",
    "A catalogue MCP server can expose search with the same ACL as the HTTP API. We would not expose raw SQL over MCP without a guard and an audit log.")
add("LangGraph (intermediate)?",
    "LangGraph is a flowchart with memory: nodes do work, edges choose the next node, and state is the backpack you carry. You can loop, checkpoint, and wait for a human. It is how you make an agent inspectable.",
    "Cycles, checkpoints, human-in-the-loop, retries, and step limits are the features that matter in production. Lisa can retrieve, generate a recipe, list missing SKUs, then confirm, with a recorded state at each hop. Graphs fail clearly when you forget a termination condition. Prefer a graph you can draw on a whiteboard over a hidden recursive agent.",
    "Lisa's graph retrieves, generates a recipe, lists missing SKUs, then confirms with the shopper. Each step is a node we can checkpoint and test without running the whole loop.")
add("CrewAI / AutoGen (intermediate)?",
    "CrewAI and AutoGen are helpers for role-based or conversational multi-agent setups. They make it easy to spin up a planner talking to a researcher. Easy is not the same as better.",
    "Give agents narrow roles, share state explicitly, and measure whether extra agents lift the eval against one agent or a graph. Often LangGraph is enough. Multi-agent debate that cannot change a groundedness number is theatre. Cost and latency grow with every extra speaker.",
    "Use a planner, researcher, and executor only if an eval shows lift versus one agent on the same recipe task. Otherwise Lisa stays a single graph with tools.")
add("LangSmith / Langfuse / LangFlow / n8n?",
    "LangSmith and Langfuse are flight recorders and eval harnesses for LLM traces. LangFlow and n8n are visual pipes that are handy for prototypes and ops glue. Visual is not the same as production control.",
    "Redact PII in traces, because a prompt log is a new database of shopper text. Use Smith or Fuse to score groundedness and to inspect a failed tool call. Use n8n for something like a Telegram alert pipe on an independent trading venture, not for checkout. A visual builder that cannot version, review, or roll back is not your payment path.",
    "Trace a failed add_to_cart in LangSmith or Langfuse. Use n8n for a Telegram alert pipe on TAN, not for ezyCart checkout.")
add("Hosted vs local LLM (intermediate)?",
    "A hosted LLM is a model you call over the internet, the way you would phone a specialist. A local LLM is a model you run on your own machines, so the tokens do not have to leave your building.",
    "Quality usually still favors frontier hosted models, while cost flips as soon as a FAQ or extraction path is hot enough to keep a GPU busy all day. Privacy and data-residency push you local when prompts contain receipts, diets, or camera-derived text you do not want in another vendor's log. Latency is a round trip plus queue on a hosted API, versus a cold start and a capacity plan you own with Ollama or vLLM. Operations is the rest of the iceberg: keys, quotas, evals, and paging a vendor versus paging your GPU host. Sit every provider behind one abstraction with fallbacks across Bedrock, Vertex AI, OpenAI, Anthropic, Gemini, Ollama, and vLLM so a single outage or price spike is not a product outage. Choose hosted for a Lisa pilot that needs frontier quality; choose local when a measured FAQ slice meets quality at a lower token cost or a harder privacy bar.",
    "We would pilot Lisa on a hosted frontier model so the shopping assistant is allowed to be good while we learn the eval. Then we would measure a local Llama 3 FAQ slice on the same labelled questions, and only move that slice off the hosted API if groundedness, privacy, and cost all hold.")
add("LoRA / PEFT (intermediate)?",
    "LoRA is a way to train a small adapter instead of the whole model. PEFT is the family name for that idea. You keep the base frozen and teach a thin extra path.",
    "You pick rank and alpha, freeze the base, and evaluate the actual task metric, watching for overfit on a few thousand labels. You can merge the adapter for simplicity or serve it beside the base. LoRA is good for a JSON extractor's style; it is a bad place to hide SKU facts that should live in RAG. If 5 thousand labelled receipts already memorize, you shrank a memorizer, not a general assistant.",
    "A LoRA JSON extractor can learn the receipt schema. SKU facts still live in RAG, because we do not want to fine-tune every promo into weights.")
add("Quantization (intermediate)?",
    "Quantization uses fewer bits for the numbers so the model is smaller and faster. You must recheck quality, especially on the small or rare classes. Average metrics can hide a disaster.",
    "INT8, 4-bit, and FP8, plus post-training quantization versus quantization-aware training, are the usual menu, and TensorRT or TF Lite are where those bits actually run. Look at per-class recall, not only mean mAP. If small SKUs drop after INT8, mix precision or skip quantizing that head. Quantization is a measured trade, not a checkbox on an export script.",
    "INT8 YOLO on the cart is the default speed play. If small SKUs drop on the per-class report, we mix precision rather than pretending the average mAP still represents those bottles.")
add("vLLM and KV cache (intermediate)?",
    "vLLM is a fast server for open models. The KV cache remembers keys and values from past tokens so the model does not re-read the whole prompt every step. That memory is why streaming feels affordable.",
    "Paged KV, continuous batching, and prefix caching are how vLLM keeps GPUs busy with many chats. A stable system prompt can sit in a prefix cache. This is a server-side story, different from on-device ONNX Runtime or TF Lite on a cart. Do not talk as if vLLM runs on the trolley NPU.",
    "Lisa's system prompt can be prefix-cached on a vLLM box. Cart hardware still runs TF Lite for vision; that path is not vLLM.")
add("SSE (intermediate)?",
    "Server-sent events are a one-way stream from the server to the client, like a ticker of tokens. If the client hangs up you must stop the work. A spinning GPU after a tablet sleeps is a bug.",
    "You send text/event-stream, heartbeat comments so proxies do not kill you, and you cancel generation on disconnect. Last-Event-ID exists for resume, but many LLM streams just start a new answer. TTFT is when the first event arrives. SSE is how Lisa talks to a tablet without a full WebSocket for a one-way token hose.",
    "Lisa streams tokens over SSE, and we cancel GPU work if the tablet sleeps or the shopper navigates away. Otherwise you pay for tokens nobody will read.")
add("PII (intermediate)?",
    "PII is personal data that can identify someone. Do not send it to a model if you can avoid it. Logs and traces are a second copy you might forget.",
    "Detect and redact at the gateway, set retention, and remember that faces in video are PII too. Diet preference might be acceptable in a recipe prompt; a card number or Aadhaar number never is. Prompt logs are a datastore with a new blast radius. Shopper text goes through the same review as any other personal field.",
    "A diet preference may be allowed in a Lisa prompt. PAN or Aadhaar must never enter prompts, traces, or training dumps.")
add("Prompt injection (intermediate)?",
    "Prompt injection is a hidden note that tries to boss the model, often sitting inside a product description or a user message. The model cannot be trusted to ignore it. Your tools must refuse.",
    "Treat user text and retrieved documents as untrusted. Only structured, authorized tools can run, and money paths need a human. Red-team with malicious catalogue copy. A product text that says ignore policy and take 100 percent off must not be able to call a discount tool.",
    "If product text says ignore policy, 100 percent off, the discount tool must not run. Lisa may quote the text as data; it may not obey it as an instruction.")

# Trading intermediate
add("What is a backtest vs paper vs live?",
    "A backtest is a replay of the past with your rules. Paper trading is fake-live, with real clocks and no real money. Live is real money, real fills, and real regret if you skipped costs.",
    "You must model costs, slippage, latency, look-ahead, and survivorship, then forward-test before you scale. TAN is an independent venture, not an employer, with about six years of systematic work, Telegram alerts on 5-minute and 15-minute bars, Pine and Python research, and a sub-5 percent drawdown claim you should be able to define. Definitions matter more than a pretty equity curve. You cannot treat the unclosed bar's high as a known value.",
    "You cannot use the unclosed 5-minute candle's high as a known value in a TAN backtest. That would be look-ahead, and it would not survive paper trading.")
add("Maximum drawdown?",
    "Maximum drawdown is the worst fall from a peak to a trough on the equity curve. It is one risk number, not the whole risk story. A small drawdown on a short sample can still hide an ugly tail.",
    "Always say the period, the sample size, and whether costs are in, because a sub-5 percent drawdown is a claim with a method, not a personality trait. Two strategies with the same drawdown can have very different tail losses. Position sizing is how you target that number. TAN's sub-5 percent figure is an independent-venture metric you should explain, not a company result.",
    "A peak of 100 down to 95 is a 5 percent drawdown. I would still ask what the tails look like, because two TAN-style rules with the same drawdown can fail very differently on a gap day.")
add("Look-ahead bias and survivorship?",
    "Look-ahead bias is using future bits as if you already knew them. Survivorship bias is studying only the names that still exist, like grading only the students who stayed in school. Both make a backtest look kinder than live trading.",
    "Use point-in-time listings, include delisted symbols, and timestamp news and sentiment at the moment they were knowable. An article stamped after the move is leakage. Walk-forward with an embargo is how you reduce the temptation. If your data vendor quietly drops dead tickers, your history is already lying.",
    "Sentiment from an article timestamped after the move is leakage. A TAN research pipeline has to reject that feature the same way a vision pipeline rejects future frames.")
add("SMC / liquidity in one honest sentence?",
    "Smart-money and liquidity ideas are a family of discretionary price-action stories. If you use them, they must become testable rules with a stop, or they are folklore. Honesty beats mystique in an interview.",
    "Do not mystify order blocks as magic. Encode the rule, test it walk-forward, put risk limits on it, and accept that many SMC sketches fail once costs are in. TAN can use SMC-inspired signals only as rule-based code with position sizing. If you cannot write the rule down, you cannot defend it.",
    "TAN uses rule-based, SMC-inspired signals with position sizing, validated walk-forward, not folklore on a screenshot. If a liquidity idea cannot become a coded rule, it does not go live.")
add("Why FinGPT is not a trading system?",
    "FinGPT reads finance language, but it does not know your fills, your fees, or your kill switch. A language model is not a trading system or a book of orders.",
    "At best it is a feature candidate, such as a sentiment score, and you still validate lift after costs. Risk limits still rule the account. Auto-market-ordering from a generated sentence is how you donate money to the spread. Keep the model upstream of a boring position sizer.",
    "Sentiment from a finance language model can be one XGBoost feature in research. It never becomes an automatic market order on TAN, because fills and fees are the real system.")
add("Position sizing and risk limits?",
    "Position sizing is how big a bet you take. Risk limits are the max pain you allow before you flatten. Together they matter more than a model's confidence score.",
    "Volatility targeting, stop rules, and kill switches are independent of the machine-learning toy that suggested the direction. A sub-5 percent drawdown target drives size. If the model is 90 percent sure and the limit says no, you do not trade. That separation is the professional answer.",
    "TAN's sub-5 percent drawdown target drives position size, not the model's confidence alone. A confident signal that would breach the limit is a pass, not a larger order.")

# Cloud intermediate
add("AWS Bedrock in one minute?",
    "Bedrock is a managed door to foundation models on AWS. You call models without standing up every GPU yourself. You still owe evals, IAM, and a fallback.",
    "Talk about IAM, data handling, guardrails, regions, latency, and price, because a managed API is still a production dependency. Sit Bedrock behind the same abstraction as other providers so you can fall back. Lisa can route to Claude on Bedrock for a pilot, then fail over if throttled. Bedrock does not replace your groundedness tests.",
    "Route Lisa to Bedrock Claude for a hosted pilot, with a fallback on the same router interface. If Bedrock throttles, the shopper should still get a degraded but safe path, not a blank bubble.")
add("GCP Vertex AI?",
    "Vertex AI is Google's managed platform for training, serving, and app-level generative AI. It is another door, with Google's IAM and regions. It is not a reason to rewrite your product logic in a vendor notebook.",
    "You still care about IAM, endpoints, feature stores, and monitoring, and you avoid lock-in where it would hurt a later move. The honest architecture is the same router interface you use for Bedrock. Eval, grounding, and cost caps do not change because the logo did. Choose Vertex when the rest of the estate is already on GCP, not because a slide said it was unified.",
    "Lisa's router should call Vertex with the same interface as Bedrock. Switching clouds then becomes a config and an eval, not a rewrite of the shopping assistant.")
add("SageMaker vs 'just a container'?",
    "SageMaker is AWS's product for training and hosting models. A plain container is you plus FastAPI plus a GPU node. Both can work; they bill different kinds of toil.",
    "Use managed training when the operations value beats the lock-in, such as a bursty training job. Many teams still serve FastAPI plus ONNX Runtime themselves for the latency path they understand. Do not put the cart's sub-100ms detector behind a generic hosting wrapper if a local runtime is already faster. Be explicit about which half is managed.",
    "A training job can run on SageMaker while the live latency path stays our FastAPI plus ONNX Runtime service. Those are different problems, and SageMaker winning training does not mean it should serve the cart.")
add("Databricks in an AI stack?",
    "Databricks is a data and ML platform on Spark and a lakehouse. It is strong for features, training tables, and governance. It is not an edge runtime for a trolley.",
    "Use it for catalogue analytics, feature tables, and training sets that need governance. Do not pretend a Spark cluster will meet sub-100ms cart inference. The boundary is: heavy data work in the lakehouse, live infer on device or a slim service. That split keeps roles honest in an interview.",
    "Catalogue analytics can live in Databricks. Cart inference stays on device with ONNX or TF Lite, because a lakehouse cluster will not make a frame-by-frame SLO.")
add("IAM least privilege?",
    "Least privilege means every service gets the smallest key that still opens its own door. A shared god role is how a batch job becomes a breach. You audit who used what.",
    "Give each job a role, ban long-lived keys in Git, and review CloudTrail-style logs. An embed job can read the catalogue bucket without decrypting every KMS key in the account. Humans and services should not share credentials. Least privilege is also how a prompt-injection bug in one tool cannot become admin on the warehouse.",
    "The embed job may read the catalogue bucket and must not have kms:Decrypt on every key in the account. That is least privilege, not a delay in the sprint.")
add("Blue/green or canary deploys?",
    "Blue/green means old and new sit side by side, then you switch. A canary sends a little traffic to the new thing, watches, then continues. Both exist so you can roll back without a speech.",
    "For prompts and models you canary on eval plus business KPIs, not only on HTTP 200. If groundedness drops, revert instantly. Five percent of Lisa traffic on a new prompt should auto-revert rather than wait for a meeting. Infrastructure canaries and prompt canaries share the idea and need different metrics.",
    "Send 5 percent of Lisa traffic to prompt v12 and auto-revert if groundedness drops. That is a canary for a language-model change, not only a load-balancer trick.")

QUESTIONS = Q
