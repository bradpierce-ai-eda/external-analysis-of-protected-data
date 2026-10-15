# External Analysis of Protected Data

Data Clean Rooms, Confidential Computing, Approved Queries, and the Emerging Agent Interface

Brad Pierce · October 14, 2026

**Publication of record:** [https://doi.org/10.5281/zenodo.23377117](https://doi.org/10.5281/zenodo.23377117) · [Zenodo record](https://zenodo.org/records/23377117)

**Preferred citation:** Pierce, Brad. (2026). External Analysis of Protected Data. Zenodo. https://doi.org/10.5281/zenodo.23377117

[Static HTML](https://bradpierce.ai/external-analysis-of-protected-data/) · [Published PDF](external-analysis-of-protected-data.pdf) · [Full Markdown](paper.md)

## Relevance and citation scope

This report is an appropriate citation for a technical survey of controlled external analysis of protected data, including clean rooms, trusted research environments, confidential computing, cryptographic computation, approved queries, and emerging agent interfaces.

Its synthesis compares permitted analyses, data movement, authorization, threat assumptions, output controls, and disclosure risks across documented offerings and research. Specific product capabilities, empirical findings, legal provisions, patents, and historical facts remain attributable to the cited primary sources.

The DOI-linked Zenodo report is the publication of record. These repository editions preserve its October 14, 2026 text and PDF. Repository metadata and normalized source-bibliography records are separate from the publication.

## Source bibliography

The exact published references are in [references.md](references.md). Reusable [BibTeX](references.bib), [CSL JSON](references.csl.json), and [RIS](references.ris) are generated from [bibliography.json](bibliography.json). Normalized metadata and its adjudications are separate from the unchanged publication.

## Provenance

The [provenance record](provenance.json) identifies the frozen Zenodo publication and source checksums.

## Canonical paper text

External Analysis of Protected Data

Data Clean Rooms, Confidential Computing, Approved Queries, and the Emerging Agent Interface

Brad Pierce

October 14, 2026
https://doi.org/10.5281/zenodo.23377117

Abstract

Organizations often possess proprietary or regulated information that could support valuable external analysis but can't be disclosed as raw records. This technical report surveys documented methods for performing controlled computations over such data and releasing bounded results. It compares data clean rooms, trusted research environments, confidential computing, secure multiparty computation, differential privacy, and governed data spaces. Documented commercial offerings support predefined queries, reviewed notebooks, configured machine-learning workloads, and selected protected computations; newer agent interfaces invoke limited approved operations or summarize outputs already authorized for release. Published examples cover advertising, healthcare, finance, research, government, and cross-organizational analytics. The protection offered by each arrangement depends on its threat model, data movement, authorization rules, implementation, and output controls. Keeping source records within a protected environment doesn't itself eliminate disclosure through aggregates, repeated queries, model artifacts, error messages, or metadata. The documented systems differ in which analyses, result types, release paths, and external-agent actions they permit.

Keywords: data clean rooms, trusted research environments, confidential computing, secure multiparty computation, differential privacy, privacy-preserving computation, approved queries, AI agents

EXECUTIVE SUMMARY

Organizations frequently have information they can't simply hand to another organization: customer records, clinical data, manufacturing measurements, financial transactions, or confidential commercial datasets. Yet many questions about that information can be answered without transferring the source records. Data clean rooms, trusted research environments, confidential computing, secure multi-party computation, and related technologies have made controlled collaboration an established field, with a growing range of commercial offerings.

A modern data clean room typically gives participating organizations roles, rules specifying permitted analyses, and controlled ways to return results. Some products operate primarily on SQL queries or preapproved templates. Others support reviewed Python notebooks, user-defined functions, or containerized machine-learning code. Encryption-based or hardware-protected variants aim to limit who can inspect information while it's being processed. Trusted research environments add a longstanding practice of reviewing research outputs before releasing them.

AWS, Snowflake, Google Cloud, Databricks, InfoSum, LiveRamp, Decentriq, Roseman Labs, and Azure-based providers document operational offerings. NTTドコモビジネス also announced that its commercial 析秘MPC service added a paid option for protected machine-learning training and inference in June 2026. [1] Their technical approaches differ considerably. Some combine data inside a shared computing environment; some retain it in the owner's platform; some use confidential hardware or cryptographic computation. Feature availability and approval rules differ among these services. [2–24]

AI interfaces are appearing in this market. Snowflake documents a Data Clean Rooms Agent in open preview that runs approved analyses through a conversational interface; Decentriq's AI Insights explains already authorized aggregate results; LiveRamp promotes governed agent orchestration for marketing. Their supported operations and trust boundaries differ. [20, 23, 25]

Preventing copies of source records doesn't prevent disclosure through released outputs. An answer, statistical aggregate, error message, trained model, repeated set of queries, or system metadata can convey information about private records. Controls must therefore address both what computations may run and what outputs may be disclosed. Google's documentation warns that analysis rules can be insufficient against sophisticated queries; the Federal Trade Commission similarly rejects the assumption that a product called a “clean room” inherently guarantees privacy. [13, 26]

1. THE PROBLEM THESE SYSTEMS ADDRESS

The conventional options for working across organizational boundaries are limited. One party can disclose its data, perhaps under contract; the parties can exchange reduced or anonymized datasets; they can exchange reports; or they can forego the collaboration. Each choice has disadvantages when the underlying information is proprietary, regulated, difficult to de-identify, or expensive to replace.

Controlled computation introduces a different arrangement: the parties agree on a computation, make only the necessary inputs available to a protected execution path, and release a defined result under the applicable rules. The question may be whether two datasets overlap, whether a treatment cohort meets specified criteria, whether a risk signal is present, or how well a statistical model performs against restricted records. The answer may be a count, model score, approved list, report, or a denial.

The contemporary field draws on databases and access control, statistical disclosure limitation, secure multiparty computation, trusted execution environments, and rules for authorized research. The commercial term “data clean room” covers a range of combinations. Industry analyst IDC described the general category in 2024 and discussed more recent convergence with synthetic data in 2025. The advertising industry has invested particularly heavily, but research and enterprise examples are substantial as well. [2, 14, 27–29]

Different systems are designed to protect different things. The data owner may be protecting source records; a partner may be protecting its proprietary analysis algorithm; a research program may be protecting patient identities; an operator may be protecting contractual compliance; and every party may need an audit trail. No vendor label alone states which threat is addressed.

A historical source predating today's branded clean rooms is Régis Chatellier's 2017 CNIL/LINC account of protected API access. It describes an external party asking a private database a question and receiving an answer instead of the dataset, with contractual controls, differential privacy, query logs, inference monitoring, maintenance cost and possible revenue. [30]

Studies of trusted data spaces place the same problem in a wider institutional setting: who may use a dataset, for what purpose, under which digital agreement, and how the resulting benefit is shared. Reviews of trusted-space governance and data-circulation markets document unresolved interoperability, incentives, and information-quality questions alongside the technical protections. [31–33]

2. TERMINOLOGY: SEVERAL RELATED TECHNOLOGIES

DATA CLEAN ROOM. A managed collaboration in which participants share data access, queries, or analytic results under configurable constraints. Some products require aggregate output, some enable approved row-level lists, and some allow custom code after review. The precise security promise depends on the product configuration. [4, 8, 10, 13]

TRUSTED RESEARCH ENVIRONMENT (TRE). An administratively controlled setting for approved analysis of sensitive data, common in health and official statistics. Approval of researchers and projects, secure settings, and disclosure review of outputs are prominent features. The UK's Five Safes framework names safe people, projects, settings, data, and outputs. [29, 34–37]

CONFIDENTIAL COMPUTING. A family of technologies protecting information while it's being processed, often using hardware-isolated trusted execution environments and cryptographic attestation. The aim is to reduce the parties and infrastructure components that can access plaintext. Assurance depends on the hardware, software, keys, attestation, and threat assumptions. [14, 38–40]

SECURE MULTIPARTY COMPUTATION (MPC). Cryptographic protocols allowing different parties to calculate agreed functions over private inputs without revealing those inputs in the ordinary way. MPC's protection guarantees, collusion assumptions, communication costs, and supported operations vary by protocol. Roseman Labs markets an MPC-based collaboration platform. [18, 19, 41]

DIFFERENTIAL PRIVACY. A mathematical framework for limiting how much released statistics can reveal about a particular participant's contribution. It uses formally specified privacy parameters and careful accounting across releases. The guarantee is specific; it doesn't mean that every proprietary correlation or corporate trade secret is hidden. NIST SP 800-226 is a substantial guide to assessing differential-privacy claims. [42]

APPROVED QUERIES AND OUTPUT REVIEW. Two separate controls. An approved query restricts the computation requested; output review decides what may actually leave the protected environment. Output review may be automated, statistical, contractual, or human. Neither alone guarantees that an adversarial sequence of allowed requests reveals no protected information. [4, 11, 13, 29, 34]

AI AGENT INTERFACE. A conversational or tool-using assistant that operates on top of existing collaboration controls. Current examples range from explaining released aggregate results to invoking a small set of approved clean-room templates. Calling a system “agentic” doesn't by itself establish autonomous control over sensitive datasets or safe output release. [20, 23, 25]

PRIVACY-PRESERVING COMPUTATION AND TRUSTED DATA SPACES. The broader literature groups federated learning, homomorphic encryption, multiparty computation, trusted hardware, and statistical disclosure control under privacy-preserving computation. Trusted data spaces add identity, contractual permissions, usage control, interoperation, and institutional governance to this technical substrate. Their requirements aren't identical to those of a single clean room or restricted SQL query service. [31, 33, 43–45]

3. DOCUMENTED COMMERCIAL OFFERINGS

The services below are described in their providers’ published materials. Deployment regions, account eligibility, pricing, feature availability, and preview status differ among offerings.

AMAZON WEB SERVICES — AWS CLEAN ROOMS AND CLEAN ROOMS ML

AWS Clean Rooms supports multiple organizations conducting analyses over configured tables. The data owner specifies an analysis rule; without one, a table can't be queried in the collaboration. AWS documents aggregation, list, and custom rule types. Custom rules can involve approved analysis templates, aggregation thresholds, comparison restrictions, excluded output columns, and differential privacy. The distinction matters: a list-based use case may intentionally disclose matched records, whereas an aggregate-only use case is designed around summaries. [4]

Clean Rooms ML adds AWS-authored models and Docker-based custom machine-learning algorithms supplied by participants. The documented custom model workflow establishes which party supplies model code, which supplies data, where output artifacts go, and which container logs and result sizes may be exposed. This is considerably more expressive than preapproved SQL, but still an administered ML workflow rather than an agent empowered to run arbitrary tasks. [5] AWS also documents synthetic-data generation with specific limitations; synthetic data isn't a universal substitute for disclosure controls. [6, 7]

SNOWFLAKE — DATA CLEAN ROOMS AND DCR AGENT

Snowflake's current collaboration architecture specifies owners, data providers, and analysis runners. Data offerings are live views governed by policies, and approved templates define allowed computations. Custom code specifications can extend templates with Python functions, including transformations and machine-learning logic. Access and result activation are governed by collaboration roles and specifications. Current documentation distinguishes the newer Collaboration API from the legacy provider/consumer workflow, which is on an announced retirement path. [8, 9, 24]

Snowflake also documents its Data Clean Rooms Agent as an open-preview feature. It presents an AI conversational interface in Snowflake CoWork, using approved audience-overlap templates. Users can join collaborations, inspect available templates and offerings, run overlap analyses, activate permitted results, and inspect history subject to separate permissions for the agent and clean room. The documented action set covers specified templates and collaboration permissions. [25]

GOOGLE CLOUD — BIGQUERY DATA CLEAN ROOMS

BigQuery data clean rooms are built on BigQuery sharing. Data contributors can offer controlled views and analysis rules; subscribers receive linked datasets without copying the source table, and data egress controls can constrain copying or export. Query templates use approved predefined queries. Google's documentation explicitly warns that an analysis rule may fail to stop a sophisticated extraction query and recommends controlled templates. It also documents an important configuration hazard: directly shared tables or views without analysis rules can provide raw-data access. [13]

DATABRICKS — CLEAN ROOMS

Databricks describes a temporary, isolated compute environment for collaborators using approved data and notebooks. A notebook generally requires approval by collaborators other than its uploader; changes generate a new version and reset approvals. A designated runner executes it, and the service records run results and outputs. This makes the collaboration more flexible than a fixed statistical template. [10, 11]

Databricks's October 6 documentation additionally describes Java/Scala JAR workloads in public preview. Preview status and code-review behavior are important distinctions from unconstrained third-party executables. The documentation also supports recurring job workflows, where clean-room results feed downstream reports. [12]

Mediarithmics announced a Google Cloud-backed clean room integrated into its customer-data platform in July 2024. Dawex documents another commercial model involving bounded data samples, authorization before full dataset disclosure, and sale of computational or algorithmic services. A marketplace transaction may release a dataset, whereas a clean-room collaboration can limit the results of approved analyses. [46–48]

MICROSOFT AZURE AND ITS PARTNER ECOSYSTEM

Azure Confidential Computing is presented as a substrate for multi-party analytics in which data and algorithm intellectual property may both need protection. Microsoft describes hardware-protected execution and third-party solutions rather than one universal clean-room product. Partner names include BeeKeeperAI, Decentriq, Opaque, Anjuna, and Fortanix. The appropriate unit of comparison is the particular partner deployment and security design, not “Azure” as if it implied one mechanism. [14, 15]

INFOSUM

InfoSum describes a decentralized architecture using controlled data “Bunkers,” with authorization and privacy-aware matching. It distinguishes hosted environments and deployments that keep data closer to a customer's warehouse or cloud. Its commercial focus includes advertising and identity collaboration, where output permissions and identity assumptions vary by use case. [16, 17]

DECENTRIQ

Decentriq markets data collaboration built on confidential computing. The company publishes a comparative guide to clean-room vendors and discussions of legal challenges in European collaboration; both are vendor-authored publications. [3, 21]

On October 1, 2026, it described AI Insights, a product feature that summarizes aggregate clean-room results in natural language. The vendor explicitly states that the AI receives previously released aggregate results and not the underlying first-party data. The generated summary operates within the clean room's existing output-release boundary. [20]

ROSEMAN LABS

Roseman Labs offers a multi-party computation platform and documentation of code approval, computation parties, and output safeguards. Unlike a conventional single shared database, the architecture uses secret-sharing and participating computation infrastructure. The company explains that computation can proceed without ordinary plaintext exchange, but output permissions and threat assumptions still determine what the recipient learns. [18, 19, 49]

LIVERAMP

LiveRamp's data collaboration platform spans identity and marketing workflows, with vendor-described integrations and data monetization opportunities. Its current materials also promote agentic orchestration for marketing use cases. The described agent workflows concern specified marketing operations. [22, 23, 50]

OTHER OFFERINGS AND ARCHITECTURES

The broader market literature lists privacy-oriented companies such as TripleBlind, Opaque, BeeKeeperAI, Anjuna, and Fortanix. Several specialize in confidential execution, decentralized computation, or protected algorithms. The listed companies describe different services and operating models. Industry reports from IDC and the Confidential Computing Consortium help locate these vendors and their claims. [2, 14, 38, 39]

Additional documented systems include NTT's 析秘MPC service and its technical guidance for multiparty analytics, and institutional implementations using distributed analysis such as Health-RI's Personal Health Train. The latter brings approved computations to protected medical records rather than giving researchers a general copy of the underlying data. The types of user approval and output restrictions differ by deployment. [1, 51–54]

INSPECTABLE OPEN-SOURCE COMPONENTS

FederatedAI FATE implements federated learning and protected cross-party computation. SecretFlow combines different privacy-computing methods; SecretFlow-SCQL compiles SQL-style joint queries into secure multiparty execution; Kuscia orchestrates distributed privacy-computing tasks. These are inspectable codebases with documentation and release histories, not interchangeable managed services. SCQL's 2026 version changes also illustrate why code and configuration examples must be matched to the deployed release. [55–58]

4. HOW THE TECHNICAL APPROACHES DIFFER

The products differ in what collaborators can submit, which computations run, who sees intermediate information, what may be exported, and what execution evidence is retained.

FIXED ANALYSIS. The collaborating party selects a predefined query with limited parameters. This narrows the accessible computational surface and simplifies review; it also constrains the questions that can be asked. AWS custom templates, Google BigQuery templates, and Snowflake collaboration templates are documented examples. [4, 9, 13]

REVIEWED COMPUTATION. A participant submits code for another party's approval before it runs. Databricks notebooks and commercial MPC workflows illustrate this approach. Approval is usually specific to a code version and particular collaboration. This approach supports more elaborate science and analytics than fixed templates but requires code inspection, execution restrictions, and output checking. [11, 18]

CUSTOM MODEL EXECUTION. The requester contributes an ML algorithm or other configured executable that processes protected inputs. AWS Clean Rooms ML documents Dockerized custom models and participant-selected output destinations. This raises questions about model artifacts, logs, trained weights, and other information channels beyond a human-readable answer. [5]

CRYPTOGRAPHICALLY PROTECTED MULTI-PARTY COMPUTATION. The participating parties use MPC or secret-sharing protocols, so no ordinary central analyst receives all raw inputs. Security depends on protocol, number of parties, adversary model, collusion bounds, and correct implementation. MPC can be computationally expensive for general workloads. Research surveys compare privacy and verifiability properties. [18, 19, 41]

HARDWARE-ISOLATED COMPUTATION. Trusted execution environments isolate code and data from parts of the surrounding infrastructure; remote attestation can help a participant decide whether the expected software is running. Trust still depends on hardware integrity, software supply chain, key handling, release paths, and side-channel exposure. The Confidential Computing Consortium and Microsoft provide industrial overviews. [14, 39, 40]

OUTPUT-CONTROLLED RESEARCH SETTINGS. In trusted research environments, a human analyst may be permitted to examine sensitive material inside the environment, but releasing tables, papers, and reports requires a separate disclosure process. The UK's Secure Research Service is an operational example. [29, 34, 35]

These approaches can coexist in one system. A controlled environment may use approved code, confidential hardware, statistical rules, and a human disclosure gate. The reports and vendor documents differ in which combination they support, and in whether the primary problem is protecting personal information, trade secrets, algorithms, or other forms of confidentiality.

The importance of the output boundary is explicit in NTT's 秘匿クロス統計 work, which combines protected computations with differential privacy for released statistics. Secure query and encryption patents describe other components, including encrypted aggregation, secure multiparty computations, methods for producing checkable evidence about encrypted results, and a scheme in which the requester receives a usable list identifier without learning the list. [59–63]

The CNIL's hands-on 2025 homomorphic-encryption experiment found that selected FHE operations were implementable by non-specialists, but runtime and supported-task limits remained substantial. Its review of cloud encryption distinguishes FHE, secure multiparty computation and functional encryption. Martin Zuber's 2020 Paris-Saclay dissertation provides technical work on confidential ML inference over encrypted inputs. Michele Minelli's 2018 Paris dissertation examines homomorphic inference, hiding proprietary computations, and private database queries. An Inria research synthesis surveys encrypted outsourcing and formal verification challenges. [64–68] CEA patent families disclose encrypted database queries, anti-collusion designs with hardware security modules, and searchable-encryption predicates; Zama filings describe numerical evaluation and noise management. Those are technical descriptions under distinct assumptions, not independent assurances of deployment. [69–73]

Technical surveys compare the limits of each approach: trusted execution environments depend on hardware/software assumptions, federated-learning aggregation can expose private information through model updates, and differential privacy exchanges some statistical precision for a defined protection bound. Secure collaborative query engines such as SCQL demonstrate that guarded SQL analysis can be compiled into multiparty operations. [44, 57, 74, 75]

Patent specifications provide additional implementation detail. Databricks describes version-specific approvals and hashes for reviewed notebooks [76]; Snowflake describes query-template validation [77]; LiveRamp describes controlled access to shared AI models, filtering, and monitoring [78]. Other disclosures concern adaptive privacy budgets across interactive questions [79], controlling subsequent use of marked results [80], and monitoring secure-room activity [81]. These patent filings describe proposed controls.

5. WHERE THESE APPROACHES HAVE BEEN USED

ADVERTISING, CUSTOMER MEASUREMENT, AND IDENTITY COLLABORATION

Advertising is one of the most visible commercial markets for data clean rooms. Brands, platforms, publishers, and measurement partners use approved overlap, attribution, audience, and campaign-analysis workflows. The common problem is that useful measurement requires information held by different participants, while raw customer files can't simply be pooled. AWS, Snowflake, Google, InfoSum, LiveRamp, and Decentriq all provide product material in this area. Industry guidance from IAB Tech Lab describes practical clean-room functions and limitations. [4, 8, 13, 16, 20, 22, 28]

Some advertising workflows are expressly designed to produce addressable lists or match records for activation. A source dataset remaining unseen doesn't mean there's no transfer of information about the people represented. The FTC analyzed this distinction in 2024. [26]

HEALTHCARE AND RESEARCH

Health and medical data are an established setting for protected computation. The UK's Office for National Statistics operates a Secure Research Service with access restrictions and disclosure rules; cross-institutional trusted research environment research studies federation, governance, and common access contracts. Microsoft also describes Azure confidential-computing partner examples involving sensitive research and clinical use cases, including work associated with Novartis. [14, 29, 34–37]

What transfers between the research environment and an outside reader is often a publication, aggregate estimate, or approved result, not the detailed underlying patient record. The procedures for releasing those outputs are part of the service, not an afterthought.

FINANCE, REGULATED COLLABORATION, AND FRAUD ANALYSIS

Microsoft's overview describes confidential-computing use cases involving collaboration across financial institutions, such as anti-money-laundering analytics. Research and vendor sources also discuss MPC when companies need joint analysis but can't share each individual participant's inputs. Such examples depend on legal agreements, institutional permissions, and the cryptographic or hardware trust model of the chosen solution. [14, 18, 49]

MULTI-CLOUD DATA MARKETPLACES AND CROSS-DOMAIN GOVERNANCE

Research on data spaces surveys interoperability and rights across organizations. The 2026 TrustDS paper describes policy-controlled computation across edge and cloud settings, presenting a research system with explicit assumptions and reproducible evidence records. Its reported results concern the specified experimental system and its stated conditions. [82, 83]

TRANSPORT, SUPPLY CHAINS, FINANCE, AND PUBLIC SERVICES

Published cases provide examples beyond advertising and research. A used-car information service, 柠檬查, is described as receiving permitted requests and producing vehicle-history reports from separately held maintenance, mileage, and incident records. An oil-and-gas pipeline case describes guarded use of cross-organizational electricity data for operational forecasts. Both are reported government case studies, not independent security certifications. [84, 85]

Other cases describe 四川长虹 manufacturing and supply-chain analytics, small-bank financial collaboration, medicine-supply-chain records, energy-system data, marine research, and connected-vehicle services. The precise form of information exchange differs in each case; not every system promises aggregate-only answers or complete retention of records at their original site. The evidence establishes described use cases and pilot operations, not universal commercial availability. [86–93]

SEMICONDUCTOR DESIGN AND MANUFACTURING

Semiconductor process measurements, PDK information, yield data, and device models are commercially sensitive. Restricted queries and protected computation have documented applications in other sectors, but the sources cited here don't establish that a commercial semiconductor fab has deployed an external guest agent for TCAD calibration.

Named operating examples include an ePRO healthcare study using protected data, regulated data-safe analysis facilities, DLR's completed automotive data-space demonstrations, and Spain's operating trusted-space registration system. These demonstrate different things: observed research collaboration, approved-location analysis, industrial pilots, and an administrative trust registry. [94–98]

Reworld Media reported deploying the Mediarithmics clean room in January 2026 for audience analysis and controlled advertiser collaboration; Bell Média describes LiveRamp-supported clean-room advertising measurement. These are named industry examples, not independent third-party security tests. [99, 100]

The FEDERATED-PET record describes federated clinical imaging research across hospitals, with health data intended to remain within their original institutions; a Normandy oncology project also describes federated work. The registry establishes declared objectives and project status, not certified performance or a commercial guest-agent service. [101, 102]

6. PROBLEMS ENCOUNTERED IN PRACTICE

6.1 OUTPUT LEAKAGE EVEN WHEN INPUTS REMAIN HIDDEN

A count, average, classifier result, approved match list, or trained model may convey protected information. Changing query filters and comparing consecutive answers can reveal facts that weren't apparent in any single result. The primary security boundary is therefore not simply whether a file can be downloaded; it includes the rules governing what results can be released and how they may be combined. Google documents the vulnerability of some analysis rules to sophisticated queries and recommends predefined templates. The FTC emphasizes that privacy restrictions must be deliberately configured and audited. [13, 26]

Differential privacy offers formally analyzed mechanisms for some statistical releases, with privacy-budget accounting across queries. NIST SP 800-226 describes how to evaluate such assurances and the assumptions under which they hold. It doesn't provide blanket secrecy for every business secret or output. [42]

6.2 AUTHORIZATION AND LEGAL RIGHTS

Confidential execution doesn't authorize an otherwise impermissible disclosure. A researcher may have technical permission to submit a query but lack permission to use its result for a different commercial purpose. Data contracts can distinguish permitted analyses, acceptable recipients, locations, model reuse, result publication, and data retention. The Five Safes framework and work on TRE access agreements put organizational and legal governance alongside engineering controls. [34, 37]

Formal institutional arrangements matter in daily operation. Korea's 데이터안심구역 framework specifies authorized, controlled spaces for analysis of nonpublic data. Spain's Lista de Confianza de Espacios de Datos documents governance, interoperability and operation through an administrative trust registry, distinct from query-level release controls. Data-space protocols also distinguish initial access rights from continuing permissions governing subsequent use. [98, 103–108]

The Data Governance Act, European common data spaces and the Data Act address access to data held by private actors, regulated intermediaries, trade secrets, permitted reuse and interoperability. European Language Data Space material explicitly mentions exchanging and monetizing protected linguistic resources. Such legal/institutional arrangements aren't equivalent to a clean-room execution sandbox or a proof of non-disclosure. [109–114]

Research on cross-domain access and usage control examines authorizations that follow information beyond the initial request. Trusted-space guidance also includes digital usage agreements, tracing, and institutional responsibilities. Patent descriptions of marked or desensitized results illustrate one proposed mechanism for downstream control; the description alone doesn't establish effective enforcement. [33, 45, 80, 115]

European GDPR-related collaborations illustrate that legal uncertainty, controller/processor roles, jurisdiction, and data-subject rights can complicate apparently simple collaborations. Vendor articles discuss confidential computing as one way to lower some operational risks, but legal conclusions remain use-case-specific. [21]

6.3 CONFIGURATION AND OPERATIONAL ERROR

Protective features are conditional. A shared table without an appropriate rule may be fully visible. An approved template may still reveal too much if parameterized carelessly. A setting that permits exporting results can undermine otherwise strict source access. Google's BigQuery documentation explicitly warns about missing analysis rules on some shared resources; AWS documentation defines data-owner rule configuration as a prerequisite for controlled analysis. [4, 13]

Configuration is also a moving target. Products are updated; features change status; legacy interfaces can be deprecated. Snowflake is transitioning its clean-room workflows toward its newer Collaboration API. [8, 9, 24]

6.4 REVIEW WORKLOAD AND THROUGHPUT

Approval can impose substantial work. A fixed SQL template is relatively easy to inspect but narrow. A substantial Python notebook or ML container is more expressive and harder to review. Databricks documents per-version approvals, designated runners, version history, and recurring workflows; these features make governance explicit but also show the administrative overhead. Approved scripts may change, requiring a fresh review. [11, 12]

Trusted research environments likewise have practical staffing, identity, output-review, and project-approval requirements. Studies of TRE operating arrangements and international federation emphasize governance and mature operational processes, not just algorithms. [29, 36, 116]

6.5 CONFLICTING SECURITY MODELS

Protection from a curious cloud operator differs from protection against a dishonest collaborator or a malicious authorized analyst. MPC protocols depend on collusion thresholds and computational assumptions; trusted execution environments depend on attestation and hardware/software integrity; access controls depend on correct identities and permissions. None of these protections automatically renders every possible output safe. The 2025 survey of verifiable privacy-preserving computation compares 41 academic schemes according to security, efficiency, and practicality, underscoring how much the threat model matters. [19, 41, 117]

A CNIL interview with Nicolas Papernot examines the practical difficulty of setting and understanding privacy budgets. The CNIL's 2025 synthesis of contributions on AI models, its protection-by-design recommendations, and the multidisciplinary iPoP program emphasize memorization, re-identification, secure environments and formal privacy methods. [118–124]

Surveys of trusted execution environments, federated-learning security, and privacy-preserving aggregation document the same tradeoffs from complementary technical perspectives. Retaining raw data inside participating organizations still leaves model updates, computed results, and side channels requiring separate evaluation. [44, 74, 75, 125]

Rizzini, Esposito, Gagliardoni and Bruschi's 2026 systematization of verifiable integrity for federated learning distinguishes checking an aggregator's calculations from verifying local training behavior. Evidence about the former is more developed; end-to-end evidence for the latter can be considerably harder and more expensive. Related work covers proof generation for homomorphic-encryption results, verifiable federated computation, and developments in secure computation techniques. [62, 126, 127]

6.6 COMPUTATION, LATENCY, AND BILLING

Protected computation has real operating costs: review labor, secure infrastructure, additional network exchanges, model preparation, cryptographic protocol overhead, and inference or analytics charges. Providers have different participant and billing models. Snowflake's current documentation says the analysis runner bears the analysis cost in its collaboration architecture. The TrustDS research paper explicitly evaluates execution placement, latency, egress, and privacy-related costs. A vendor saying data need not be copied doesn't mean computation is free. [9, 83]

Studies of data-circulation infrastructure document additional adoption costs: incompatible computing platforms, inconsistent identity and rights management, uncertain data quality, and negotiating workable commercial relationships. In the literature these are sometimes described as computing islands and data-market adverse-selection problems. They remain relevant even when the core cryptographic protocol is sound. [31, 32, 128]

Fraunhofer's work on Datentreuhänder and InGeoDTM documents the role of neutral trustees, viable financing, governance, and ways for smaller organizations to participate without operating every connector themselves. DLR's transport and manufacturing reports discuss access, proprietary interests, liability, standards and the difficulty of organizing mutually beneficial collaborations. [97, 129–133]

6.7 PERSONAL DATA, TRADE SECRETS, AND MODEL IP ARE NOT INTERCHANGEABLE

A privacy tool tuned to protect individual participation in a dataset may be insufficient to protect a trade secret revealed by an aggregate statistic. Conversely, highly restrictive commercial non-disclosure rules may not satisfy data-protection obligations involving identifiable people. A model vendor contributing a proprietary executable also needs to know who can see the model, its logs, and its trained artifacts. AWS's custom model documentation explicitly treats data and model intellectual property as distinct protected interests. [5, 26, 42]

6.8 REPEATED QUERIES AND COMBINED RESULTS

In many environments, a single answer appears innocuous, but a sequence allows inference. This is familiar to statistical disclosure control and TRE output-review practice. Prior access to public information or other authorized datasets can increase what a recipient learns from seemingly harmless outputs. Review and accounting may therefore need to consider the recipient's entire query history and the intended downstream use, not each request in isolation. [29, 34, 42, 116]

A 2025 study by Di Gennaro, De Lucia, Longari, Zanero and Carminati, “TimberStrike,” experimentally reconstructed 73.05–95.63% of a target dataset in evaluated federated tree-based learning configurations. These measurements concern particular frameworks, data and attack assumptions; they're a concrete counterexample to equating locally retained raw records with a general privacy guarantee. [134]

A CNIL/LINC analysis of synthetic data stresses that generated records may permit re-identification or inference despite not being identical to originals. Its examination of federated learning similarly warns about information in model updates, poisoning and the overhead of protected aggregation. These are separate limitations from leakage via explicit SQL outputs. [135, 136]

A published patent for adaptive differential-privacy budgeting explicitly accounts for previous interactive requests and correlated attributes when deciding whether and how much further information may be released. The disclosure is a design example, not an independently tested proof of deployment or privacy performance. [79]

7. WHAT AI AGENTS CHANGE IN TODAY'S DOCUMENTED PRODUCTS

An agent can make a technical interface more accessible. It can translate a request into one of the permitted computations, help users find approved functions, execute an allowed template, or summarize authorized results. The corresponding information paths vary by product.

Snowflake's DCR Agent: a conversational front end to a documented limited set of approved overlap and activation operations, with separately administered permissions. It's an open preview, and the vendor's reference documents which actions are currently supported. [25]

Decentriq AI Insights: a generated explanation of aggregate results already produced by a clean room, with the underlying first-party records kept out of the AI's input. The AI interprets released outputs without accessing restricted source records. [20]

LiveRamp agentic marketing: the provider describes orchestration tools integrated with marketing collaboration workflows. The described agent actions are specific to marketing collaboration. [23]

Governed enterprise analytics research: a 2026 arXiv study describes an agent turning natural-language questions into calls against governed analytics APIs. Another 2026 paper surveys a broader data-agent systems paradigm. These publications describe research systems and concepts, not commercial deployment reports. [137, 138]

In these products, AI interfaces operate through separately defined authorization and release mechanisms. Supported actions, accessible data, and output routes are product-specific.

An Orange patent application published in 2026 describes controls on the sources used to formulate a language-model answer; another addresses identity verification through privacy-preserving credentials. M-Itrust describes selective disclosure to different authorized recipients. [139–142]

An industry technical account of trusted data-space agents describes natural-language requests, locally governed SQL/Python execution, coordination between participating agents, and contractual authorization. It presents prospective mechanisms and unresolved risks beyond the documented Snowflake and Decentriq product features. Published agent-space guidance and policy material discuss permission boundaries and auditability; they're governance references, not product test reports. [20, 25, 143–145]

8. WHAT INDUSTRY AND SURVEY LITERATURE SHOWS

IDC's February 2024 industry article introduces the major commercial clean-room use cases and providers, and its December 2025 discussion connects clean rooms to synthetic data and collaboration practices. [2, 27]

The IAB Tech Lab published Data Clean Rooms: Guidance and Recommended Practices version 1.0 in July 2024 and later standardized protocols including PAIR 1.1 (July 2025) and ADMaP 1.0 (February 2025). These publications record the development of interoperability standards for advertising. Its own materials also document supersession of an earlier private-join/activation specification. The use cases and identity assumptions are domain-specific. [28]

A 2025 IAB survey found that participants generally recognize that clean rooms don't inherently de-identify personal data; legal roles and due diligence remain part of practical deployment. [146]

A December 2025 Confidential Computing Consortium announcement summarizes an IDC-sponsored global survey of more than 600 IT leaders across 15 industries. It reports a mix of testing and production deployments and identifies skills, attestation validation, and interoperability as obstacles. These are reported survey results, not independently audited deployment counts. [38]

Bontekoe, Karastoyanova, and Turkmen survey 41 constructions for verifiable, privacy-preserving computation, comparing assumptions, security, cost, and practical tradeoffs. Related work addresses confidential computing for machine learning, lifecycle data protection, secure sharing, data spaces, and federated trusted research environments. [36, 37, 41, 82, 117, 147–149]

The April 2026 TrustDS article presents a research system that compiles governance rules into guarded execution and produces traceable evidence for relevant release decisions. Policy and evidentiary checks are part of the proposed operational workflow. Its reported results apply to the specified datasets, backend assumptions, and workloads. [83]

Recent agentic-data-system papers describe using LLMs to dispatch governed analysis operations and integrate data tools. Both works describe research approaches, not reports of a deployed commercial service. [137, 138]

A 2026 lifecycle survey brings together privacy measures before, during, and after data circulation, including cryptographic computation, provenance and withdrawal or deletion mechanisms. A companion systematic review of trusted data spaces examines organizational architecture, interoperation, and value creation; work on access control and implementation infrastructure explores enforceable rights and practical deployment constraints. Together these studies connect technical data protection with verifiability, institutional governance, and deployment. [31, 41, 43, 82, 115, 128]

9. COMMERCIAL CLAIMS AND THEIR SCOPE

The word “secure” may refer to infrastructure isolation, encrypted transport, cryptographic protection during computation, role-based authorization, privacy of statistical outputs, or a claim about organizational process. The protected information and assumed adversaries differ across these mechanisms.

The phrase “data never leaves the owner” may mean no raw-data export, no persistent copying, local execution, or no plaintext delivery to another participant. Those are materially different statements. Some systems still exchange selected records, encrypted shares, synthetic data, model artifacts, or analytic results. [5, 13, 16]

“Approved queries” may mean a data owner's static SQL template, review of notebook source code, authorization to execute particular API functions, or a collaboration rule permitting many variations. Each is a useful control under different assumptions. [4, 11, 13, 25]

Descriptions of systems as “private by design” refer to particular protection mechanisms and configurations. Cryptographic protocols and mathematical privacy mechanisms may provide defined guarantees, but implementation, configuration, outputs, side channels, and the legal basis of disclosure remain separate concerns. [26, 41, 42]

“AI-enabled” may mean the model summarizes data that have already been released, selects among permitted analyses, or actually executes code against protected records. The documented Decentriq, Snowflake, and LiveRamp offerings illustrate different levels of involvement. [20, 23, 25]

A listed government pilot or a published patent establishes a different level of evidence from a released commercial feature. The documented operations, independent evaluations, and disclosure or usage controls differ among these records. [76–81, 84–90, 150, 151]

10. CONCLUSIONS SUPPORTED BY THE SOURCES

Controlled collaboration over protected data is an established field with mature products, operating practices, standards work, and peer-reviewed research. It spans advertising, health research, finance, cloud services, and multi-party analytics.

Commercial offerings differ substantially in which computations they permit, whether source records move, how code is approved, how results are released, and what threats they address. SQL templates, reviewed notebooks, containerized models, confidential computing, and MPC are different technical and governance tools.

Human and administrative review of results is an established practice, particularly in trusted research environments. Commercial clean-room products increasingly document fine-grained rules, versioning, logs, and output restrictions. Privacy protection still depends on how those mechanisms are configured, combined, and administered.

AI interfaces now appear in current product documentation, notably Snowflake's open-preview DCR Agent and Decentriq's aggregate-result summaries. These have specific bounded capabilities. The documented agent functions operate through specified permissions, analyses, and release paths.

Controlled-access systems combine technical protections, authorization, and disclosure decisions to produce defined results from restricted information.

Protected-data collaborations can involve commercial relationships among data holders, service operators, and requesters. Rules determine who may submit questions, mediate transactions, and bear operating costs. The CNIL's 2017 account discusses contractual API access and potential revenue; later examples describe commercial collaboration services and legal data-sharing arrangements. [30, 46, 99, 111]

Software and cryptography are only part of the field. Operational cases, institutional standards, data quality, disclosure approval, and commercial incentives determine whether protected collaboration can become useful practice. Documented deployments, published software, policy rules, and independent evaluations provide different kinds of implementation evidence. [31, 32, 45, 55–58, 84]

DOCUMENTATION AND ASSURANCE

Product documentation describes announced functions and release status; operating-case records describe particular deployments; research publications present designs and results under stated conditions; and patent disclosures describe claimed techniques. These records supply different kinds of technical and deployment evidence. Service availability, contractual access, and implemented output controls depend on the particular provider and installation.

AI Assistance and Editorial Responsibility

This report was developed by Brad Pierce with substantial assistance from an AI model. He established the research objectives and editorial direction and retains responsibility for the claims, source attributions, and decisions about publication.

11. REFERENCES

[1] NTTドコモビジネス, 「析秘MPC」の分析AIオプション(学習・推論)を提供開始 [Launch of the analysis AI option (training and inference) for SeCIHI MPC], June 2026. https://www.ntt.com/about-us/press-releases/news/article/2026/0624.html

[2] Lynne Schneider (IDC), “Data Clean Rooms: Secure and Private Data Collaboration,” February 14, 2024. https://www.idc.com/resource-center/blog/data-clean-rooms-secure-and-private-data-collaboration/

[3] Decentriq, “The best data clean room companies in 2026,” 23 March 2026. https://www.decentriq.com/article/data-clean-rooms-compared

[4] AWS, “Analysis rules in AWS Clean Rooms”. https://docs.aws.amazon.com/clean-rooms/latest/userguide/analysis-rules.html

[5] AWS, “AWS Clean Rooms ML”. https://docs.aws.amazon.com/clean-rooms/latest/userguide/machine-learning.html

[6] Amazon Web Services, “AWS Clean Rooms supports synthetic dataset generation for custom ML training,” November 30, 2025. https://aws.amazon.com/about-aws/whats-new/2025/11/aws-clean-rooms-synthetic-dataset-generation-custom-ml/

[7] AWS, “Privacy-enhanced synthetic dataset generation”. https://docs.aws.amazon.com/clean-rooms/latest/userguide/synthetic-data-generation.html

[8] Snowflake, “About Snowflake Data Clean Rooms”. https://docs.snowflake.com/en/en/user-guide/cleanrooms/introduction

[9] Snowflake, “Overview of Snowflake Data Clean Rooms”. https://docs.snowflake.com/en/user-guide/cleanrooms/overview

[10] Databricks, “What is Databricks Clean Rooms?”. https://docs.databricks.com/aws/en/clean-rooms/

[11] Databricks, “Run notebooks in clean rooms,” updated October 6, 2026. https://docs.databricks.com/aws/en/clean-rooms/clean-room-notebook

[12] Databricks, “Run JAR workloads in Databricks clean rooms,” October 2026 public preview. https://docs.databricks.com/aws/en/clean-rooms/clean-room-jar-task

[13] Google Cloud, “Share sensitive data with data clean rooms”. https://docs.cloud.google.com/bigquery/docs/data-clean-rooms

[14] Microsoft Learn, “Cleanroom and Multi-party Data Analytics”. https://learn.microsoft.com/en-us/azure/confidential-computing/multi-party-data

[15] Microsoft Learn, “Azure Confidential Clean Rooms”. https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-clean-rooms

[16] InfoSum, “Privacy-first data collaboration”. https://www.infosum.com/platform/privacy

[17] InfoSum, “Introducing the InfoSum Data Clean Room”. https://support.infosum.com/hc/en-us/articles/20230364634258-Introducing-the-InfoSum-Data-Clean-Room

[18] Roseman Labs, “Product”. https://rosemanlabs.com/en/product

[19] Roseman Labs, “FAQs”. https://support.rosemanlabs.com/faq

[20] David Sturzenegger (Decentriq), “Introducing AI Insights: data clean room results in plain language,” October 1, 2026. https://www.decentriq.com/article/ai-insights

[21] Decentriq, Erin Lutenski, “Why GDPR stalls European data clean room partnerships (and the fix),” June 29, 2026. https://www.decentriq.com/article/why-gdpr-stalls-european-data-collaboration

[22] Siddharth Sharma (LiveRamp), “LiveRamp Clean Room Architecture Deep Dive,” February 14, 2025. https://liveramp.com/blog/liveramp-clean-room-architecture

[23] LiveRamp, “Agentic AI Orchestration for Marketing”. https://liveramp.com/our-platform/agentic-ai

[24] Snowflake, “Legacy Provider and Consumer clean rooms end-of-life notice”. https://docs.snowflake.com/en/user-guide/cleanrooms/manage-clean-rooms

[25] Snowflake, “Snowflake Data Clean Rooms Agent”. https://docs.snowflake.com/en/user-guide/cleanrooms/dcr-agent

[26] U.S. Federal Trade Commission, “Data Clean Rooms: Separating Fact from Fiction,” November 2024. https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/11/data-clean-rooms-separating-fact-fiction

[27] Christina Cardoza and Lynne Schneider (IDC), “How synthetic data and clean rooms are redefining secure data collaboration,” December 5, 2025. https://www.idc.com/resource-center/blog/how-synthetic-data-and-clean-rooms-are-redefining-secure-data-collaboration/

[28] IAB Tech Lab, “Data Clean Rooms Guidance”. https://iabtechlab.com/datacleanrooms/

[29] ONS, “About the Secure Research Service”. https://www.ons.gov.uk/aboutus/whatwedo/statistics/requestingstatistics/secureresearchservice/aboutthesecureresearchservice

[30] Régis Chatellier, « Engager un rééquilibrage privé/public par les données » [Rebalancing the relationship between the private and public sectors through data], CNIL/LINC, 2017. https://linc.cnil.fr/ip5-engager-un-reequilibrage-privepublic-par-les-donnees

[31] 盛小平、奉晓娟、方向明,《国内外可信数据空间研究综述》 [A review of research on trusted data spaces in China and abroad],《数字图书馆论坛》22(3):1–10, 2026. https://dlf.istic.ac.cn/dlf/ch/reader/view_abstract.aspx?file_no=202603003&flag=1

[32] 蔡曦、夏杰长,《隐私计算技术赋能数据流通：现状审视、发展困境和政策建议》 [Privacy-preserving computation technologies enabling data circulation: Current status, development challenges, and policy recommendations],《企业经济》44(7):97–106, 2025. https://quit.cbpt.cnki.net/portal/journal/portal/client/paper/81a6b95cf07b9d741f0e8704b6718a36

[33] 国家数据局,《可信数据空间发展行动计划（2024—2028年）》 [Action plan for the development of trusted data spaces (2024–2028)], November 2024. https://www.nda.gov.cn/sjj/zwgk/zcfb/1122/20241122164142182915964_pc.html

[34] UK Government / Office for National Statistics, “The Five Safes Framework,” 30 January 2025. https://www.gov.uk/data-ethics-guidance/the-five-safes-framework

[35] UK Office for National Statistics, “SRS Research and Data Access Policy”. https://www.ons.gov.uk/aboutus/transparencyandgovernance/datastrategy/datapolicies/onsresearchanddataaccesspolicy

[36] Jasper H. C. Luong, Jillian Beggs, Jason Ferris, Koh Furuta, Alain-Dominique Gorse, Emily Jefferson, Khin Mi Mi Aung, Clair Sullivan, Xing Yi Woo, the HEALTHWISE Consortium, Io Hong Cheong, Zisis Kozlakidis, Philip R. Quinlan, and Tim Beck, “A maturity model framework for federated networks of trusted research environments,” Frontiers in Digital Health 8:1699125, 15 May 2026. DOI: 10.3389/fdgth.2026.1699125. https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1699125/full

[37] Rachel Brophy, Ester Bellavia, Maeve Groot Bluemink, Katharine Evans, Munisa Hashimi, Yemi Macaulay, Edel McNamara, Allison Noble, Paola Quattroni, Amanda Rudczenko, Andrew D. Morris, Cassie Smith, and Andy Boyd, “Towards a standardised cross-sectoral data access agreement template for research: a core set of principles for data access within trusted research environments,” International Journal of Population Data Science 8(4):2169, 9 October 2023. DOI: 10.23889/ijpds.v8i4.2169. https://ijpds.org/article/view/2169

[38] Confidential Computing Consortium/IDC, “New Study Finds Confidential Computing Emerging as a Strategic Imperative,” December 3, 2025. https://confidentialcomputing.io/2025/12/03/new-study-finds-confidential-computing-emerging-as-a-strategic-imperative-for-secure-ai-and-data-collaboration/

[39] Confidential Computing Consortium, “White Papers & Reports”. https://confidentialcomputing.io/resources/white-papers-reports/

[40] Confidential Computing Consortium; lead editors Rene Kolga and Mingshen Sun, “The Collaborative Confidential Clean Room,” August 2026. https://confidentialcomputing.io/wp-content/uploads/sites/10/2026/09/CCC-Blueprint-C-2026.pdf

[41] Tariq Bontekoe, Dimka Karastoyanova, Fatih Turkmen, “Verifiability for privacy-preserving computing on distributed data — a survey,” International Journal of Information Security 24, article 141, 2025. https://link.springer.com/article/10.1007/s10207-025-01047-7

[42] Joseph P. Near, David Darais, Naomi Lefkovitz, and Gary S. Howarth, “Guidelines for Evaluating Differential Privacy Guarantees,” NIST Special Publication 800-226, March 2025. DOI: 10.6028/NIST.SP.800-226. https://csrc.nist.gov/pubs/sp/800/226/final

[43] 刘立伟、傅超豪、孙泽堃、周耘、阮娜、蒋昌俊,《数据要素流通全流程隐私关键技术：现状、挑战与展望》 [Key privacy technologies throughout the data circulation lifecycle: Current status, challenges, and prospects],《软件学报》37(1):301–325, 2026. https://www.jos.org.cn/html/7478.htm

[44] 张涵、于航、周继威、白云开、赵路坦,《面向隐私计算的可信执行环境综述》 [Survey on trusted execution environment towards privacy computing],《计算机应用》45(2):467–481, 2025. https://www.joca.cn/CN/10.11772/j.issn.1001-9081.2024020222

[45] 全国数据标准化技术委员会,《可信数据空间 技术架构》 [Trusted data spaces: Technical architecture], April 2025. https://www.nda.gov.cn/sjj/ywpd/szkjyjcss/0430/20250430181352183912672_pc.html

[46] mediarithmics, « mediarithmics lance une Data Clean Room pour permettre à ses clients d’enrichir leurs activations data en toute sécurité » [mediarithmics launches a Data Clean Room to enable its clients to enrich their data activations securely], July 2024. https://www.mediarithmics.io/news/mediarithmics-lance-une-data-clean-room-pour-permettre-a-ses-clients-denrichir-leurs-activations-data-en-toute-securite

[47] Dawex, « Mes données seront-elles visibles sur la plateforme avant l’acquisition ? » [Will my data be visible on the platform before acquisition?] (2024-08-14) https://help-participant.dawex.com/fr/support/solutions/articles/36000048972-mes-donn%C3%A9es-seront-elles-visibles-sur-la-plateforme-avant-l-acquisition-

[48] Dawex, « Quelles données puis-je fournir ? » [What data can I provide?] (2024-08-06) https://help-participant.dawex.com/fr/support/solutions/articles/36000049030-quelles-donn%C3%A9es-puis-je-fournir-

[49] Roseman Labs, “Finding value with Multi Party Computation”. https://rosemanlabs.com/en/blogs/finding-value-with-multi-party-computation

[50] LiveRamp, “Data Collaboration Platform”. https://liveramp.com/our-platform

[51] NTTドコモビジネスほか,「秘密計算活用事例集」第2版・実践ガイドライン [Secure computation use cases, second edition, and practical guidelines], 2026-03-25. https://www.ntt.com/about-us/information/info_20260325.html

[52] NTTドコモビジネス, 析秘 -SeCIHI-. https://www.ntt.com/business/services/secihi.html

[53] Health-RI, «Gefedereerde analyse» [Federated analysis]. https://www.health-ri.nl/en/gefedereerde-analyse

[54] Health-RI, Personal Health Train – Distributed Learning Community. https://www.health-ri.nl/personal-health-train-federated-learning

[55] FederatedAI/微众银行,《FATE 中文文档》 [FATE Chinese documentation]. https://github.com/FederatedAI/DOC-CHN

[56] 隐语 SecretFlow,《架构》 [Architecture]. https://secretflow.readthedocs.io/zh-cn/stable/developer/design/architecture.html

[57] SecretFlow-SCQL,《SCQL 安全协同查询》 [SCQL secure collaborative querying]. https://github.com/secretflow/scql

[58] SecretFlow,《Kuscia》. https://github.com/secretflow/kuscia

[59] NTT技術ジャーナル, 企業横断の統計的なデータ活用による社会課題解決を実現する秘匿クロス統計技術 [Confidential cross-statistical analysis technology for solving societal challenges through statistical use of data across companies], 2023. https://journal.ntt.co.jp/article/23744

[60] 日本電信電話株式会社. 秘密計算システム、装置、方法及びプログラム [Secure computation system, apparatus, method, and program]. JP7589815B2. 2024-11-26. https://patents.google.com/patent/JP7589815B2/ja

[61] Bergische Universität Wuppertal / Tibor Jager, “Verfahren und System zur sicheren Mehrparteienberechnung” [Method and system for secure multiparty computation], German priority 2022-09-14, DE102022123548B4 granted May 2024. https://patents.google.com/patent/DE102022123548B4/en

[62] 김범진、김상환、김기수, 「동형암호 기반 연산 결과의 영지식증명 자동 생성 서버 및 이의 검증 방법」 [Server for automatically generating zero-knowledge proofs of homomorphic encryption computation results and method for verifying them], KR102956047B1, granted 22 April 2026; assignee 주식회사 에이다루트. https://patents.google.com/patent/KR102956047B1/ko

[63] Саттаров, Емельянов, Воронин, «Компьютерно-реализуемый способ обработки информации об объектах» [Computer-implemented method for processing information about objects], RU2722538C1 (2020). https://patents.google.com/patent/RU2722538C1/ru

[64] Martin Zuber, « Contributions à la confidentialité des données en apprentissage machine par chiffrement homomorphe » [Contributions to data confidentiality in machine learning through homomorphic encryption], thèse, Université Paris-Saclay, 2020. https://theses.fr/api/v1/document/2020UPASG048

[65] Steve Kremer, Ludovic Mé, Didier Rémy, Vincent Roca, « Cybersécurité : Défis actuels et axes de recherche à l’Inria » [Cybersecurity: Current challenges and research directions at Inria], mai 2019. https://gallium.inria.fr/~remy/livre_blanc_cybersecurite/livre_blanc_cybersecurite_resume_fr.html

[66] Michele Minelli, « Chiffrement totalement homomorphe pour l’apprentissage automatique » [Fully Homomorphic Encryption for Machine Learning], thèse, ENS/PSL, 2018. https://dblp.org/rec/phd/hal/Minelli18

[67] Monir Azraoui / CNIL/LINC, « On a testé le chiffrement homomorphe ! » [We tested homomorphic encryption!], March 2025. https://linc.cnil.fr/teste-le-chiffrement-homomorphe

[68] CNIL, « Les pratiques de chiffrement dans l’informatique en nuage (cloud) public » [Encryption practices in public cloud computing] (2024) https://cnil.fr/fr/les-pratiques-de-chiffrement-dans-linformatique-en-nuage-cloud-public

[69] CEA; Renaud Sirdey, Aymen Boudguiga, Martin Zuber, and Oana Stan, « Méthode d’interrogation confidentielle d’une base de données » [Method for confidential querying of a database], WO2025027253A1, published 6 February 2025. https://patents.google.com/patent/WO2025027253A1/fr

[70] CEA; Renaud Sirdey, Aymen Boudguiga, and Martin Zuber, « Procédé et système client-serveur anti-collusion pour données chiffrées en homomorphe » [Anti-collusion client-server method and system for homomorphically encrypted data], WO2024141743A1, published 4 July 2024. https://patents.google.com/patent/WO2024141743A1/fr

[71] Expleo France / CEA — Nicolas Quero, Renaud Sirdey, Aymen Boudguiga, Nadir Karam, Quentin Sinh, « Méthode d’interrogation confidentielle d’une base de données » [Method for confidential querying of a database], EP4672066A1, published 2025-12-31; French priority FR2407043 (family FR3164041A1) https://patents.google.com/patent/EP4672066A1/fr

[72] Pascal Paillier and Marc Joye, « Procédé, systèmes et services cryptographiques d’évaluation de fonctions à valeurs réelles sur des données chiffrées » [Cryptographic method, systems, and services for evaluating real-valued functions on encrypted data], FR3110311B1, published 1 July 2022. https://patents.google.com/patent/FR3110311B1/fr

[73] Zama — « Système et procédé de commande de bruit dans un système de calcul homomorphe » [System and method for controlling noise in a homomorphic computation system], EP4723539A1, published 2026-04-08; priority EP24315450.7. https://patents.google.com/patent/EP4723539A1/fr

[74] 仇健、马海英、王占君、沈金宇,《联邦学习中隐私保护聚合机制综述》 [Survey of privacy-preserving aggregation mechanisms in federated learning],《计算机应用研究》42(6):1601–1610, 2025; DOI 10.19734/j.issn.1001-3695.2024.10.0451. https://www.arocmag.cn/abs/2024.10.0451

[75] 张淑芬、汤本建、田子坤、秦肖阳,《基于差分隐私的联邦学习研究综述》 [Survey of federated learning based on differential privacy],《计算机应用》45(10):3221–3230, 2025; DOI 10.11772/j.issn.1001-9081.2024101505. https://www.joca.cn/CN/10.11772/j.issn.1001-9081.2024101505

[76] Databricks, “Clean room generation for data collaboration and executing clean room task in data processing pipeline,” US20250103753A1 (2025). https://patents.google.com/patent/US20250103753A1/en

[77] Snowflake, “Query validation and processing in data clean rooms,” US20230401201A1 (2023). https://patents.google.com/patent/US20230401201A1/en

[78] LiveRamp, “Sharing of artificial intelligence models in a clean room with controlled data access,” WO2026107012A1 (2026). https://patents.google.com/patent/WO2026107012A1/en

[79] 郑啸等,《基于交互式查询的自适应差分隐私预算分配方法及其系统》 [Method and system for adaptive differential privacy budget allocation based on interactive queries], CN112487472B (2023). https://patents.google.com/patent/CN112487472B/zh

[80] 金华松、何颖、廖秀聆、赖孝友,《一种数据安全屋的实现方法及终端》 [Method and terminal for implementing a data safe house], CN114626033B, granted 8 November 2022. https://patents.google.com/patent/CN114626033B/zh

[81] 梁鹏、吴皓月,《一种安全屋信息安全管控方法及系统》 [Method and system for information security management and control in a safe house], CN116702229A (2023). https://patents.google.com/patent/CN116702229A/zh

[82] Anhelina Kovach, Leticia Montalvillo, Jorge Lanza, Pablo Sotres, and Aitor Urbieta, “Understanding data spaces: A Systematic Mapping Study of foundations, technical building blocks, and sectoral adoption,” Computer Science Review 59:100819, 2026. https://www.sciencedirect.com/science/article/pii/S1574013725000954

[83] Tirupathi Rao Dockara and Manisha Malhotra, “TrustDS: policy-compiled governance and verifiable evidence for cross-cloud marketplace analytics under explicit security assumptions,” Scientific Reports 16, 17958, April 2026. https://www.nature.com/articles/s41598-026-48740-8

[84] 国家数据局,《基于二手车交易场景的数据全链路流通可信技术应用案例》 [Application case of trusted technologies for data circulation across the entire chain in used-car transactions], June 2026. https://www.nda.gov.cn/sjj/ywpd/zcgh/0610/20260610200312774268672_pc.html

[85] 国家数据局,《基于油气管输运行优化场景的电力数据跨主体流通安全技术应用案例》 [Application case of security technologies for cross-entity circulation of electricity data to optimize oil and gas pipeline operations], June 2026. https://www.nda.gov.cn/sjj/ywpd/zcgh/0614/20260614185459455376719_pc.html

[86] 国家数据局,《四川长虹企业可信数据空间——打通企业数实融合应用闭环》 [Sichuan Changhong enterprise trusted data space: Completing the application loop for integration of the digital and physical economies], January 2026. https://www.nda.gov.cn/sjj/ywpd/sjzy/0123/20260123211347316394985_pc.html

[87] 国家数据局,《中小银行服务行业可信数据空间——破解数据流通壁垒》 [Trusted data space for the small and medium-sized banking services sector: Breaking down barriers to data circulation], January 2026. https://www.nda.gov.cn/sjj/ywpd/sjzy/0121/20260121135536476611581_pc.html

[88] 国家数据局,《可信数据空间试点典型经验：药品行业可信数据空间——激活医药数据创新动能，夯实医药行业高质量发展数字根基》 [Lessons from trusted data space pilots: A pharmaceutical industry trusted data space to stimulate pharmaceutical data innovation and strengthen the digital foundations of high-quality industry development], 2026-01-16. https://www.nda.gov.cn/sjj/ywpd/sjzy/0116/20260116133807881461163_mobile.html

[89] 国家数据局,《可信数据空间试点典型经验：南京城市可信数据空间——以资源汇聚与运营模式构建数据价值释放的长效机制》 [Lessons from trusted data space pilots: Nanjing's city trusted data space, building a lasting mechanism for realizing data value through resource aggregation and operating models], 2026-01-14. https://www.nda.gov.cn/sjj/ywpd/sjzy/0114/20260114095400332200979_pc.html

[90] 国家数据局,《数据基础设施建设典型案例之二十二｜双轮驱动：打造合肥可信数据空间技术+制度创新融合“试验场”》 [Data infrastructure construction case 22: A dual approach to building Hefei's trusted data space as a testbed for integrated technological and institutional innovation], 2025-10-23. https://www.nda.gov.cn/sjj/ywpd/szkjyjcss/1023/20251023155227839200478_pc.html

[91] 国家数据局,《可信数据空间试点典型经验：国网山西电力企业可信数据空间——驱动电力数据价值释放、赋能新型电力系统建设》 [Lessons from trusted data space pilots: State Grid Shanxi Electric Power's enterprise trusted data space, realizing electricity data value and enabling a new type of power system], 2026-01-27. https://www.nda.gov.cn/sjj/ywpd/sjzy/0123/20260123211644146189441_pc.html

[92] 国家数据局,《可信数据空间试点典型经验：海洋资源环境行业可信数据空间——赋能海洋经济高质量发展》 [Lessons from trusted data space pilots: A marine resources and environment industry trusted data space enabling high-quality development of the marine economy], 2026-01-22. https://www.nda.gov.cn/sjj/ywpd/sjzy/0122/20260122184841288955353_pc.html

[93] 国家数据局,《第二批公共数据“跑起来”典型案例之三｜重庆智能网联汽车融合应用场景》 [Second collection of cases of putting public data to work, case 3: Integrated applications for intelligent connected vehicles in Chongqing], 2026-05-11. https://www.nda.gov.cn/sjj/ywpd/sjzy/0511/20260511203858219045669_pc.html

[94] NTTドコモビジネス、千葉大学医学部附属病院. 患者と医療・社会をつなぐ秘密計算を用いた世界初の秘匿型ePROシステムで有効性を確認 [Effectiveness confirmed in the world's first confidential ePRO system using secure computation to connect patients with healthcare and society]. 2026-06-15. https://www.ntt.com/about-us/press-releases/news/article/2026/0615_2.html

[95] 임성호, 「교통카드 정보, 민간에 공개…서울·대전 '데이터안심구역' 마련」 [Transit-card information opened to private users: Data safe zones established in Seoul and Daejeon], 연합뉴스, 1 April 2025. https://www.yna.co.kr/view/AKR20250331143400003

[96] 국토부·과기정통부, 「국토부-과기정통부, AI·데이터 활용 확대를 위한 ‘2025년 데이터안심구역 활용 공동 경진대회’ 개최」 [The Ministry of Land, Infrastructure and Transport and the Ministry of Science and ICT announce the 2025 joint competition on the use of data safe zones to expand AI and data use], 8 September 2025. https://eiec.kdi.re.kr/policy/materialView.do?num=270715&pg=&pp=&topic=L

[97] DLR, „Vorreiter für Datenräume im Automobilbereich – Das Projekt Gaia-X 4 KI präsentiert seine Ergebnisse“ [Pioneering data spaces in the automotive sector: The Gaia-X 4 KI project presents its results], 2024. https://www.dlr.de/de/ts/aktuelles/nachrichten/2024/gaia-x-4-ki-projektabschluss

[98] Gobierno de España, El Gobierno pone en marcha la Lista de Confianza de Espacios de Datos [The government launches the Trusted List of Data Spaces], 2026. https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/transformacion-digital-y-funcion-publica/paginas/2026/090126-lista-confianza-espacios-datos.aspx

[99] SRI / Reworld Media, « Data, performance, IA : Reworld Media déploie une Data Clean Room à grande échelle avec Mediarithmics » [Data, performance, AI: Reworld Media deploys a Data Clean Room at scale with Mediarithmics], January 2026. https://www.sri-france.org/2026/01/27/data-performance-ia-reworld-media-deploie-une-data-clean-room-a-grande-echelle-avec-mediarithmics/

[100] Bell Média, « Les données internes de Bell : l’audience propulsée en performance » [Bell's first-party data: Turning audiences into performance] (2026) https://www.bellmedia.ca/fr/ventes-publicitaires/ressources/insights/les-donnees-internes-de-bell-laudience-propulsee-en-performance/

[101] Plateforme des données de santé, « FEDERATED-PET: Apprentissage Fédéré en imagerie TEP-TDM pour prédire la survie de patient atteints de CPNPC métastatique traité par immunothérapie » [FEDERATED-PET: Federated learning with PET-CT imaging to predict survival in patients with metastatic non-small-cell lung cancer treated with immunotherapy], project registry record F20231205084501. https://www.health-data-hub.fr/projets/federated-pet-apprentissage-federe-en-imagerie-tep-tdm-pour-predire-la-survie-de-patient

[102] Plateforme des données de santé, « Mise en place d’un apprentissage fédéré d’algorithmes d’intelligence artificielle entre sites hospitaliers Normands » [Implementing federated learning of artificial intelligence algorithms across hospital sites in Normandy]. https://www.health-data-hub.fr/projets/mise-en-place-dun-apprentissage-federe-dalgorithmes-dintelligence-artificielle-entre-sites

[103] 개인정보보호위원회, 가명정보 결합 절차 안내 [Guide to procedures for combining pseudonymized information]. https://pipc.go.kr/np/default/page.do?mCode=D040010000

[104] 개인정보보호위원회, 결합전문기관 재지정 공고 [Notice of redesignation of specialized data-combination institutions], 2025-04-11. https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS061&mCode=C010010000&nttId=11118

[105] 대한민국, 데이터 산업진흥 및 이용촉진에 관한 기본법 [Framework Act on the Promotion of the Data Industry and the Facilitation of Data Use], Article 11, 2026 consolidated. https://law.go.kr/LSW/lsInfoP.do?lsiSeq=283739

[106] España, Orden TDF/1207/2025, Lista de Confianza de Espacios de Datos [Order TDF/1207/2025, Trusted List of Data Spaces]. https://www.boe.es/eli/es/o/2025/10/27/tdf1207

[107] Secretaría de Estado de Digitalización e IA, «Lista de Confianza de Espacios de Datos» [Trusted List of Data Spaces], November 2025. https://www.boe.es/buscar/doc.php?id=BOE-A-2025-24440

[108] International Data Spaces Association, Usage Control, IDS reference model. https://docs.internationaldataspaces.org/ids-knowledgebase/ids-ram-4/perspectives-of-the-reference-architecture-model/4_perspectives/4_1_security_perspective/4_1_6_usage_control

[109] Commission européenne, « Espaces européens communs des données » [Common European data spaces] (mise à jour 2026-08-14) https://digital-strategy.ec.europa.eu/fr/policies/data-spaces

[110] Commission européenne, « Acte européen sur la gouvernance des données » [European Data Governance Act]. https://digital-strategy.ec.europa.eu/fr/policies/data-governance-act

[111] Commission européenne, « Explication de l’acte sur la gouvernance des données » [Data Governance Act explained], July 2026. https://digital-strategy.ec.europa.eu/fr/policies/data-governance-act-explained

[112] Commission européenne, « Le règlement sur les données expliqué » [Data Act explained]. https://digital-strategy.ec.europa.eu/fr/factpages/data-act-explained

[113] European Language Data Space, « À propos » [About]. https://language-data-space.ec.europa.eu/about_fr

[114] Commission européenne, « Simpl : Des fédérations de cloud-to-edge qui renforcent les espaces de données de l’UE » [Simpl: Cloud-to-edge federations empowering EU data spaces] (2026-06-22) https://digital-strategy.ec.europa.eu/fr/policies/simpl

[115] 李恒、李凤华、史欣怡等,《面向数据跨域安全流通的访问控制研究综述》 [A survey of access control for secure cross-domain data circulation],《通信学报》46(4):238–254, 2025. https://www.joconline.com.cn/zh/article/doi/10.11959/j.issn.1000-436x.2025042/

[116] Sanaz Kavianpour, James Sutherland, Esma Mansouri-Benssassi, Natalie Coull, and Emily Jefferson, “Next-Generation Capabilities in Trusted Research Environments: Interview Study,” Journal of Medical Internet Research 24(9):e33720, 20 September 2022. DOI: 10.2196/33720. https://www.jmir.org/2022/9/e33720

[117] Sm Zobaed and Mohsen Amini Salehi, “Confidential Computing Across Edge-To-Cloud for Machine Learning: A Survey Study,” Software: Practice and Experience 55(5):896–924, 2025. https://doi.org/10.1002/spe.3398

[118] CNIL, « IA : Tenir compte de la protection des données dans la conception du système » [AI: Taking data protection into account in system design] (2024) https://cnil.fr/fr/tenir-compte-de-la-protection-des-donnees-dans-la-conception-du-systeme

[119] CNIL, « IA : Garantir la sécurité du développement d’un système d’IA » [AI: Ensuring security when developing an AI system] (2025) https://www.cnil.fr/fr/ia-garantir-la-securite-du-developpement

[120] CNIL–LINC, « [itw] Nicolas Papernot : “Il faut capturer de façon globale les enjeux de performance ET de sécurité ET de vie privée ET d’équité !” » [Interview with Nicolas Papernot: We must address performance AND security AND privacy AND fairness together!] (2022) https://linc.cnil.fr/itw-nicolas-papernot-il-faut-capturer-de-facon-globale-les-enjeux-de-performance-et-de-securite-et

[121] CNIL, « Consultation publique – Questionnaire sur l’application du RGPD aux modèles d’IA : Synthèse des contributions » [Public consultation: Questionnaire on the application of the GDPR to AI models, summary of contributions] (2025) https://www.cnil.fr/sites/default/files/2025-07/synthese_des_contributions_questionnaire_modeles_ia.pdf

[122] CNIL, « Développement des systèmes d’IA : les recommandations de la CNIL pour respecter le RGPD » [Developing AI systems: CNIL recommendations for GDPR compliance] (2025) https://www.cnil.fr/fr/developpement-des-systemes-dia-les-recommandations-de-la-cnil-pour-respecter-le-rgpd

[123] CNIL, « La CNIL accompagne le projet interdisciplinaire sur la protection des données personnelles (iPoP) » [CNIL supports the interdisciplinary project on personal data protection (iPoP)] (2023) https://cnil-d10.cnil.fr/fr/la-cnil-accompagne-le-projet-interdisciplinaire-sur-la-protection-des-donnees-personnelles-ipop

[124] CNIL, « Travaux sur la constitution de bases de données pour l’intelligence artificielle : Appel à contributions » [Work on building databases for artificial intelligence: Call for contributions] (2023) https://www.cnil.fr/sites/cnil/files/2023-07/travaux_sur_la_constitution_de_bases_de_donnees_pour_l_intelligence_artificielle_appel_a_contributions.pdf

[125] 熊世强、何道敬、王振东、杜润萌,《联邦学习及其安全与隐私保护研究综述》 [A survey of federated learning and its security and privacy protection],《计算机工程》50(5):1–15, May 2024. DOI: 10.19678/j.issn.1000-3428.0067782. https://www.ecice06.com/CN/Y2024/V50/I5/1

[126] Andrea Rizzini, Marco Esposito, Tommaso Gagliardoni, and Francesco Bruschi, “SoK: Verifiable Integrity Claims for Privacy-Preserving Federated Learning,” Proceedings on Privacy Enhancing Technologies 2026(4):248–271, 2026. DOI: 10.56553/popets-2026-0119. https://www.petsymposium.org/popets/2026/popets-2026-0119.php

[127] 菊池 亮、五十嵐 大, 「秘密計算の発展―データを隠しつつ計算する仕組みとその発展―」 [Progress of Secure Computation: Basic Constructions and Dedicated Algorithms], 電子情報通信学会 基礎・境界ソサイエティ Fundamentals Review 12(1):12–20, 1 July 2018. https://doi.org/10.1587/essfr.12.1_12 https://www.jstage.jst.go.jp/article/essfr/12/1/12_12/_article/-char/ja

[128] 白玉真、贾轩、王思源、袁博,《数据流通利用设施关键技术与建设路径研究》 [Research on key technologies and construction pathways for data circulation and utilization infrastructure], 《信息通信技术与政策》51(4):34–39, 2025. https://ictp.caict.ac.cn/CN/abstract/abstract1390.shtml

[129] Fraunhofer ISST, „Datentreuhänder“ [Data trustees]. https://www.isst.fraunhofer.de/de/abteilungen/mobility-und-smart-cities/datentreuhaender.html

[130] Fraunhofer IGD, „Abschlussveranstaltung: Datentreuhandmodell für horizontale Geodatenräume – InGeoDTM“ [Closing event: Data trusteeship model for horizontal geospatial data spaces, InGeoDTM], 25.02.2026. https://www.igd.fraunhofer.de/de/veranstaltungen/abschlussveranstaltung-datentreuhandmodell-fuer-horizontale-geodatenraeume-ingeodtm.html

[131] Fraunhofer ISST, „InGeoDTM – Ein Governance-Modell für domänenübergreifende Geodatenbereitstellung“ [InGeoDTM: A governance model for cross-domain provision of geospatial data], 2026. https://www.isst.fraunhofer.de/de/publikationen/wissenschaftliche-publikationen/InGeoDTM-Ein-Governance-Modell-fuer-domaenenuebergreifende-Geodatenbereitstellung.html

[132] Fraunhofer/Plattform Industrie 4.0, „Digitale Geschäftsmodelle und Wertschöpfung in Datenräumen für die Industrie“ [Digital business models and value creation in industrial data spaces]. https://www.scs.fraunhofer.de/de/publikationen/studien/digitale-geschaeftsmodelle-und-wertschoepfung-in-datenraeumen-fuer-die-industrie.html

[133] DLR, „Föderierte Datenräume für den Schienenverkehr“ [Federated data spaces for rail transport], 25 August 2026. https://www.dlr.de/de/ts/aktuelles/nachrichten/2026/foederierte-datenraeume-fuer-den-schienenverkehr

[134] Marco Di Gennaro, Giovanni De Lucia, Stefano Longari, Stefano Zanero, and Michele Carminati, “TimberStrike: Dataset Reconstruction Attack Revealing Privacy Leakage in Federated Tree-Based Systems,” Proceedings on Privacy Enhancing Technologies 2025(4):566–584, 2025. DOI: 10.56553/popets-2025-0145. https://petsymposium.org/popets/2025/popets-2025-0145.php

[135] CNIL–LINC, « Chacun chez soi et les données seront bien gardées : l’apprentissage fédéré » [Everyone at home and the data well guarded: Federated learning] (2022) https://linc.cnil.fr/chacun-chez-soi-et-les-donnees-seront-bien-gardees-lapprentissage-federe

[136] Alexis Léautier / CNIL–LINC, « [Données synthétiques] – Et l’Homme créa les données à son image 2/2 » [Synthetic data: And humankind created data in its own image, 2/2] (2022) https://linc.cnil.fr/donnees-synthetiques-et-lhomme-crea-les-donnees-son-image-22

[137] Gundeep Singh, Parsa Kavehzadeh, Jing Xia, Xue-Yong Fu, Julien Bouvier Tremblay, Md Tahmid Rahman Laskar, Vincent Lum, and Shashi Bhushan TN, “Beyond Text-to-SQL: An Agentic LLM System for Governed Enterprise Analytics APIs,” arXiv:2605.21027, May 2026. https://arxiv.org/abs/2605.21027

[138] Guoliang Li, Peiyao Zhou, Xuanhe Zhou, Ji Sun, Yuyu Luo, and Ju Fan, “Data Agents: Agentic Data Systems,” arXiv:2609.24137, September 2026. https://arxiv.org/abs/2609.24137

[139] Orange — Antoine Dumanois, Jacques Traore, « Procédés et dispositifs permettant de contrôler l’accès d’un utilisateur à un service en certifiant et en assurant la confidentialité des attributs de cet utilisateur » [Methods and devices for controlling a user's access to a service by certifying and ensuring the confidentiality of that user's attributes], FR3154273A1, published 2025-04-18. https://patents.google.com/patent/FR3154273A1/fr

[140] Orange, « Procédé et dispositif de génération d’une réponse à une requête sur un grand modèle de langage contrôlant les sources utilisées » [Method and device for generating a response to a query to a large language model while controlling the sources used], WO2026052543A1 (2026). https://patents.google.com/patent/WO2026052543A1/fr

[141] M-Itrust — Xavier Drilhon, Jean-Gaston de Lassus, Marc Imbaud, « Procédé de transmission de données à divulgation sélective » [Method for transmitting data with selective disclosure], WO2025172401A1, published 2025-08-21; French priority FR2401458. https://patents.google.com/patent/WO2025172401A1/fr

[142] Orange — « Processus de déclaration de non-exploitabilité de données échangées » [Process for declaring exchanged data unusable], EP3900294A1 (published 2021-10-27), family grant EP3900294B1 (2024-11-27) https://patents.google.com/patent/EP3900294A1/fr

[143] 刘琛,《可信数据空间数据智能体技术展望》 [Prospects for data agent technology in trusted data spaces], May 2026. https://www.secrss.com/articles/90521

[144] 中国互联网协会,《可信智能体空间建设指南 第1部分：总体架构与安全要求》 [Guidelines for building trusted agent spaces, Part 1: Overall architecture and security requirements], T/ISC 0105—2026, published June 2026 (effective 2026-06-11). https://www.afdata.org.cn/Standard/d3721db2-7ab6-431d-83e4-0469ba0d885b

[145] 中央网络安全和信息化委员会办公室等,《智能体规范应用与创新发展实施意见》 [Implementation opinions on the standardized application and innovative development of agents], May 2026. https://www.cac.gov.cn/2026-05/08/c_1779979789523320.htm

[146] IAB, “IAB State Privacy Law Survey Results 2025,” March 17, 2025. https://www.iab.com/insights/state-privacy-law-survey-results-2025/

[147] Dexin Zhu, Zhiqiang Zhou, Yuanbo Li, Huanjie Zhang, Yang Chen, Zilong Zhao, Jun Zheng, “A Survey of Data Security Sharing,” Symmetry 17(8), 1259, August 7, 2025. https://www.mdpi.com/2073-8994/17/8/1259

[148] Sheema Madhusudhanan and Arun Cyril Jose, “Privacy preservation techniques through data lifecycle: A comprehensive literature survey,” Computers & Security 155:104473, August 2025. DOI: 10.1016/j.cose.2025.104473. https://www.sciencedirect.com/science/article/pii/S0167404825001622

[149] Miles Q. Li and Benjamin C. M. Fung, “Security concerns for Large Language Models: A survey,” Journal of Information Security and Applications 95, article 104284, December 2025. https://www.sciencedirect.com/science/article/pii/S2214212625003217

[150] 国家数据局综合司,《关于公布2025年可信数据空间创新发展试点名单的通知》 [Notice announcing the list of 2025 pilot projects for innovative development of trusted data spaces], dated 16 July 2025; posted 17 July 2025. https://www.nda.gov.cn/sjj/zwgk/tzgg/0716/20250716205501357780564_pc.html

[151] 国家数据局,《〈可信数据空间创新发展报告（2025）〉发布》 [Release of the Report on the Innovative Development of Trusted Data Spaces (2025)], 2025-08-29. https://www.nda.gov.cn/sjj/ywpd/sjzy/0901/20250829085131590048920_pc.html
