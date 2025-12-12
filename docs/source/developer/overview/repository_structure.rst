==============================================
Repository Structure
==============================================

This document explains how the AgriOS codebase is organised, how responsibilities are split across modules, and how developers should reason about where new logic belongs.

Its goal is to help new contributors quickly answer:

* "Where should I put this code?"
* "How do these modules relate to each other?"

1. High-Level Structure
-----------------------

AgriOS is implemented as a set of custom Odoo Community modules, each responsible for a specific domain concept in agricultural operations.

At the top level, the repository looks like this:

.. code-block:: text

    AgriOS/
    ├── agrios_farmer/
    ├── agrios_plot/
    ├── agrios_trade/
    ├── agrios_training/
    ├── agrios_kobo/
    ├── agrios_theme/
    ├── agrios_demo/
    ├── LICENSE
    ├── eslint.config.cjs
    └── ...

Each ``agrios_*`` directory is a self-contained Odoo module with its own:

* Data models
* Views
* Security rules
* Business logic
* Dependencies

AgriOS intentionally avoids a monolithic "core" module. Instead, it uses domain-driven modularity.

2. Design Philosophy
--------------------

AgriOS follows a few core structural principles:

2.1 Domain-Centric Modules
~~~~~~~~~~~~~~~~~~~~~~~~~~
Each module corresponds to a real-world agricultural domain (farmer, plot, trade, training), not a technical concern.

2.2 Thin Coupling, Explicit Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Modules depend on each other only where the business logic truly overlaps, and dependencies are explicitly declared in ``__manifest__.py``.

2.3 Extend, Don't Fork
~~~~~~~~~~~~~~~~~~~~~~
AgriOS expects downstream users to:

* Extend models
* Add fields
* Override views

...rather than modifying core modules directly.

3. Module-by-Module Responsibilities
------------------------------------

3.1 agrios_farmer
~~~~~~~~~~~~~~~~~
**Primary responsibility:** Farmer entities and identity.

This module defines:

* Farmer profiles
* Demographic and identification data
* Core relationships to plots, trainings, and transactions

**Owns:**

* Farmer model definitions
* Farmer-specific views and forms
* Farmer-level permissions

**Does NOT own:**

* Plot geometry
* Trade or pricing logic
* Survey ingestion

3.2 agrios_plot
~~~~~~~~~~~~~~~
**Primary responsibility:** Farms, plots, and land units.

This module defines:

* Plots and farms
* Spatial or boundary-related metadata
* Crop or season associations (if present)

**Owns:**

* Plot data models
* Plot ↔ farmer relationships
* Plot-level attributes

**Does NOT own:**

* Farmer identity logic
* Trade or transaction logic
* External GIS integrations (unless explicitly scoped)

3.3 agrios_trade
~~~~~~~~~~~~~~~~
**Primary responsibility:** Commercial transactions and trade flows.

This module defines:

* Sales, deliveries, or aggregation logic
* Volumes, pricing, and buyer relationships
* Trade-related lifecycle states

**Owns:**

* Trade and transaction models
* Trade workflows
* Buyer-facing logic

**Does NOT own:**

* Farmer demographics
* Plot boundaries
* Training data

3.4 agrios_training
~~~~~~~~~~~~~~~~~~~
**Primary responsibility:** Capacity building and training programmes.

This module defines:

* Training programmes
* Participation and attendance
* Outcomes or certifications

**Owns:**

* Training models
* Training session workflows
* Farmer participation tracking

**Does NOT own:**

* Farmer core identity
* Trade outcomes
* Survey ingestion

3.5 agrios_kobo
~~~~~~~~~~~~~~~
**Primary responsibility:** External data ingestion from KoBoToolbox (or similar).

This module defines:

* Data import/sync logic
* Field mapping between surveys and AgriOS models
* Validation and error handling

**Owns:**

* Survey ingestion logic
* Mapping layers
* Sync orchestration

**Does NOT own:**

* Core farmer or plot schemas
* Business rules unrelated to ingestion

3.6 agrios_theme
~~~~~~~~~~~~~~~~
**Primary responsibility:** UI styling and branding.

This module defines:

* Visual theming
* UI assets
* Frontend customisation

**Owns:**

* CSS / JS assets
* Layout overrides

**Does NOT own:**

* Business logic
* Data models

3.7 agrios_demo
~~~~~~~~~~~~~~~
**Primary responsibility:** Demonstration and sample data.

This module defines:

* Demo records
* Example workflows
* Sandbox data for testing or onboarding

**Owns:**

* Demo XML/CSV data
* Example configurations

**Does NOT own:**

* Core production logic

4. Cross-Module Dependencies
----------------------------

Typical dependency direction:

.. code-block:: text

    agrios_farmer
          ↑
    agrios_plot    ↑
    agrios_trade
          ↑
    agrios_training

*Note: ``agrios_kobo`` may depend on any module it imports data into.*

Dependency Rules
~~~~~~~~~~~~~~~~
1. Dependencies must be declared explicitly in ``__manifest__.py``.
2. Circular dependencies should be avoided.
3. If two modules depend heavily on each other, reconsider responsibility boundaries.

5. Where to Put New Code (Rules of Thumb)
-----------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Feature Type
     - Where It Belongs
   * - New farmer attribute
     - ``agrios_farmer``
   * - Plot geometry logic
     - ``agrios_plot``
   * - Survey mapping
     - ``agrios_kobo``
   * - Training attendance
     - ``agrios_training``
   * - Pricing rules
     - ``agrios_trade``
   * - Styling changes
     - ``agrios_theme``

If logic spans multiple domains:

1. Put the core logic in the module that owns the domain.
2. Extend or hook from other modules.

6. Extending Existing Modules
-----------------------------

AgriOS expects extension via:

* Odoo model inheritance
* View extension (XML)
* Additional modules layered on top

**Avoid:**

* Editing core module code unless necessary.
* Hard-coding country- or programme-specific logic into base modules.

7. Common Anti-Patterns to Avoid
--------------------------------

❌ Putting trade logic in ``agrios_farmer``
❌ Embedding survey parsing directly into farmer models
❌ Creating "misc" or "utils" dumping grounds
❌ Circular module dependencies

8. Summary
----------

AgriOS is intentionally modular, explicit, and domain-driven.

If you:

* Respect module boundaries
* Declare dependencies clearly
* Extend instead of overwrite

You will be able to scale the platform cleanly across:

* Countries
* Commodities
* Programmes
* Partners