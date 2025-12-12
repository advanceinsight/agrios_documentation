==================
Core Domain Models
==================

This page describes the *core* AgriOS domain models and how they relate to each other.
It’s written for developers who need to understand **where business data lives**, **how it connects**,
and **where to extend** the system safely.

.. contents::
   :local:
   :depth: 2

-----------------------------
1. Domain Model Mental Model
-----------------------------

AgriOS is organized around a few central concepts:

- **Actors**: Farmers, field agents, cooperatives/buyers (depending on configuration)
- **Land units**: Farms/plots (and optional seasonal/crop context)
- **Programs**: Trainings and participation
- **Commerce**: Trade/transactions (contracts, deliveries, volumes, prices)
- **Ingestion**: External survey data (e.g., KoBo) mapped into the above

The system is implemented as **Odoo modules** (``agrios_*``). Ownership generally follows module boundaries:

- ``agrios_farmer`` owns farmer identity and farmer-centric attributes
- ``agrios_plot`` owns plot/farm/land-unit data
- ``agrios_training`` owns training sessions and participation tracking
- ``agrios_trade`` owns trade lifecycle data
- ``agrios_kobo`` owns ingestion and mapping logic

--------------------------------
2. Primary Entities (At a Glance)
--------------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 28 54

   * - Entity
     - Module owner
     - Purpose
   * - Farmer
     - ``agrios_farmer``
     - Identity + profile data for producers; parent object for most workflows
   * - Plot / Farm
     - ``agrios_plot``
     - Land units linked to farmers; optionally spatial metadata/boundaries
   * - Training / Session
     - ``agrios_training``
     - Programs delivered to farmers; sessions/events and their metadata
   * - Participation / Attendance
     - ``agrios_training``
     - Join table linking farmers to trainings (and outcomes)
   * - Trade / Transaction
     - ``agrios_trade``
     - Commercial flows: volumes, pricing, deliveries, counterparties
   * - Survey Sync / Mapping
     - ``agrios_kobo``
     - Ingest external submissions and map them to farmer/plot/training/trade

------------------------------------------------
3. Farmer Model (``agrios_farmer``)
------------------------------------------------

**Role:** The Farmer is the central actor in AgriOS. Most objects ultimately relate to a farmer
either directly (e.g., participation) or indirectly (e.g., trade via deliveries tied to a farmer).

Typical contents (conceptual):
- Core identity: name, unique IDs, contact info
- Program metadata: membership status, group/cooperative affiliation
- Household/demographic attributes (if collected)
- Relationships to plots, trainings, and transactions

Common relationships:
- Farmer → Plot(s) (1..N)
- Farmer → Training Participation(s) (1..N)
- Farmer → Trade records (1..N) (directly or via intermediate objects)

Extension points (recommended):
- Add farmer attributes by **extending** the farmer model in a dedicated module
- Add computed fields for derived attributes (e.g., risk tier, completeness score)
- Avoid embedding ingestion logic here; keep ingestion in ``agrios_kobo``

.. note::
   If your implementation uses ``res.partner`` as the base “person/organization” record,
   document the specific mapping (e.g., “Farmer extends partner” vs “Farmer is separate model”)
   in a short subsection here.

------------------------------------------------
4. Plot / Farm Models (``agrios_plot``)
------------------------------------------------

**Role:** Plots (and optionally farms) represent land units linked to farmers.

Typical contents (conceptual):
- Plot identifiers (internal / external)
- Area and location metadata
- Optional geometry / boundary data
- Crop/season metadata (if modeled)
- Link to farmer owner/manager

Common relationships:
- Plot → Farmer (N..1)
- Plot → Commodity/crop (optional)
- Plot → Survey submissions (indirectly, via ingestion mappings)

Extension points (recommended):
- Add plot attributes (soil type, compliance flags, deforestation risk inputs)
- Add geometry handling in plot module or a dedicated GIS extension module
- Keep trade logic out of plots unless it is purely *plot metadata* used by trade

------------------------------------------------
5. Training Models (``agrios_training``)
------------------------------------------------

**Role:** Training captures capacity building programs, sessions, and farmer participation.

Typical contents (conceptual):
- Training program: name, topic, provider, curriculum references
- Session/event: date, location, facilitator, attendance method
- Participation/attendance: join records linking farmer ↔ session/program
- Outcomes: pass/fail, score, certification, notes

Common relationships:
- Training Program → Session(s) (1..N)
- Session → Participation(s) (1..N)
- Participation → Farmer (N..1)

Extension points (recommended):
- Add new outcomes or scoring logic by extending participation model
- Add reporting views and dashboards in training module (or a reporting module)
- Avoid embedding farmer profile updates inside training logic; prefer explicit actions/workflows

------------------------------------------------
6. Trade / Transaction Models (``agrios_trade``)
------------------------------------------------

**Role:** Trade models the commercial side: buying, selling, deliveries, volumes, pricing,
counterparties, and status transitions.

Typical contents (conceptual):
- Counterparty (buyer/cooperative/trader) references
- Volumes, grades, pricing, and currency
- Delivery/collection events
- Contract or order references (if applicable)
- Lifecycle/state tracking (draft → confirmed → delivered → settled)

Common relationships:
- Transaction/Delivery → Farmer (N..1) (directly or via membership)
- Transaction/Delivery → Plot (optional, if traceability required)
- Transaction/Delivery → Counterparty (N..1)

Extension points (recommended):
- Implement pricing logic as computed fields / service-style methods
- Keep compliance and traceability add-ons in dedicated modules if they grow large
- If integrating with accounting, ensure boundaries between AgriOS trade objects and Odoo accounting are explicit

------------------------------------------------
7. Ingestion & Mapping (``agrios_kobo``)
------------------------------------------------

**Role:** ``agrios_kobo`` handles external data ingestion and mapping—commonly from KoBoToolbox.
This module should be the primary home for:
- authentication/config for data sources
- sync scheduling/orchestration (manual or automated)
- mapping from submission fields → Odoo fields
- validation rules and error handling
- idempotency (avoid duplicate ingestion)

Recommended pattern:
- Keep “raw submission” records (optional) separate from “mapped domain updates”
- Write mapping logic so it can be re-run safely
- Record provenance (source form ID, submission ID, timestamps)

Common targets:
- Farmer updates/creation
- Plot creation/update
- Training participation import
- Trade event import (if used)

------------------------------------------------
8. Relationships & Cardinality Summary
------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Relationship
     - Typical type
     - Notes
   * - Farmer → Plot
     - 1..N
     - A farmer may manage multiple plots; plots usually have one primary farmer
   * - Farmer → Participation
     - 1..N
     - Participation links farmers to training sessions/programs
   * - Training Program → Session
     - 1..N
     - Programs can have multiple sessions/events
   * - Session → Participation
     - 1..N
     - Many farmers can attend a single session
   * - Farmer → Transaction/Delivery
     - 1..N
     - Commercial records often tie to farmer; sometimes also to plot
   * - Plot → Transaction/Delivery
     - 0..N
     - Optional; used when traceability to land unit is required

---------------------------------------------
9. Where Business Logic Should Live (Rules)
---------------------------------------------

- Farmer identity and farmer-centric rules → ``agrios_farmer``
- Plot/land-unit rules → ``agrios_plot``
- Training workflows and attendance → ``agrios_training``
- Pricing/volume/delivery lifecycle → ``agrios_trade``
- External ingestion/mapping/validation → ``agrios_kobo``

Anti-patterns to avoid:
- Putting ingestion parsing inside farmer/plot models
- Duplicating the same field definitions across modules
- Circular dependencies between modules (declare dependencies explicitly)


