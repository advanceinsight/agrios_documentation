=============================
Model & Field Naming Conventions
=============================

This page defines the naming conventions used across AgriOS for:

- Odoo models (technical names)
- Python classes and files
- fields and relations
- XML IDs (views, actions, menus, security)
- module naming and dependencies

The goal is to make the codebase **consistent, searchable, and upgrade-safe** as it grows
across countries, commodities, and partners.

.. contents::
   :local:
   :depth: 2

--------------------------
1. Modules
--------------------------

1.1 Module naming
~~~~~~~~~~~~~~~~~

AgriOS modules should use the prefix:

- ``agrios_<domain>`` for core domain modules
- ``agrios_<integration>`` for integrations (e.g., KoBo)
- ``agrios_<country>_<topic>`` for localization/country modules
- ``agrios_<partner>_<topic>`` for partner/program modules

Examples:

- ``agrios_farmer``
- ``agrios_plot``
- ``agrios_trade``
- ``agrios_training``
- ``agrios_kobo``
- ``agrios_theme``
- ``agrios_demo``
- ``agrios_gh_localization`` (Ghana localization)
- ``agrios_partnerx_reports`` (partner-specific reporting)

Avoid:
- vague names like ``agrios_utils`` unless it is truly shared and stable
- creating a dumping-ground module for unrelated features

1.2 Dependency hygiene
~~~~~~~~~~~~~~~~~~~~~~

- Keep dependencies **minimal and explicit** in ``__manifest__.py``.
- Avoid circular dependencies.
- If you need shared primitives, prefer a clearly scoped base module (e.g., ``agrios_core``)
  *only if* there is truly shared functionality across domains.

--------------------------
2. Model Technical Names
--------------------------

2.1 Model naming format
~~~~~~~~~~~~~~~~~~~~~~~

Odoo model technical names should be:

- all lowercase
- dot-separated
- namespaced under ``agrios``

Recommended format:

- ``agrios.<domain>.<entity>`` for non-core
- or ``agrios.<entity>`` for the most central objects

Examples:

- ``agrios.farmer``
- ``agrios.plot``
- ``agrios.trade.transaction``
- ``agrios.training.program``
- ``agrios.training.session``
- ``agrios.training.participation``
- ``agrios.kobo.mapping``
- ``agrios.kobo.submission``

Avoid:
- generic names that collide with Odoo core (e.g., ``farmer`` alone)
- renaming models after they’re in production (migration cost is high)

2.2 Use consistent entity nouns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose one noun per concept and stick to it:

- use ``plot`` consistently (avoid mixing ``field``, ``farmplot``, etc.)
- use ``participation`` consistently (avoid mixing ``attendance`` + ``participation`` for same join-table)

If there is a real distinction (e.g., session attendance vs program enrollment), document it and encode it in names.

--------------------------
3. Python Classes & Files
--------------------------

3.1 Python model classes
~~~~~~~~~~~~~~~~~~~~~~~~

Python class names should be:

- PascalCase
- descriptive, matching the entity

Examples:

- ``AgriOSFarmer``
- ``AgriOSPlot``
- ``AgriOSTrainingProgram``

If inheriting an existing model:

- use a meaningful class name (avoid ``X(models.Model): _inherit="..."`` with ambiguous class names)

3.2 File layout
~~~~~~~~~~~~~~~

Prefer one file per domain entity, or coherent grouping:

.. code-block:: text

   models/
   ├── farmer.py
   ├── plot.py
   ├── training_program.py
   ├── training_session.py
   └── training_participation.py

Avoid:
- huge ``models.py`` files containing many unrelated models
- mixing ingestion mapping logic with domain models

--------------------------
4. Field Naming Conventions
--------------------------

4.1 Field names
~~~~~~~~~~~~~~~

Field names should be:

- snake_case
- descriptive and stable
- not overly abbreviated

Examples:
- ``id_number``
- ``phone``
- ``area_ha``
- ``gps_lat``, ``gps_lng`` (if using point coordinates)
- ``submission_id`` (for provenance)
- ``source_system``

Avoid:
- ambiguous abbreviations (e.g., ``nm``, ``qty``) unless already universal in the domain
- units-less numeric fields (always encode units when relevant)

4.2 Units and measurement fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a field is a measurement, encode the unit in the name:

- ``area_ha`` (hectares)
- ``weight_kg`` (kilograms)
- ``distance_km``

If you store both value and unit, be explicit:

- ``area_value`` and ``area_uom`` (uom = unit of measure)
- but prefer standardizing units where possible

4.3 Relational fields
~~~~~~~~~~~~~~~~~~~~~

Many2one fields should be singular nouns ending in ``_id``:

- ``farmer_id``
- ``plot_id``
- ``program_id``

One2many and many2many fields should be plural nouns:

- ``plot_ids``
- ``participation_ids``
- ``tag_ids``

If a one2many field points to the “line” concept, use ``_line_ids``:

- ``delivery_line_ids``
- ``transaction_line_ids``

4.4 Computed fields
~~~~~~~~~~~~~~~~~~~

Computed fields should read like derived facts:

- ``completeness_score``
- ``total_volume_kg``
- ``is_compliant``

Store computed fields only when:
- performance requires it, or
- you need a historical snapshot

Document if a computed field is stored and why.

--------------------------
5. XML IDs (Views, Menus, Actions, Security)
--------------------------

5.1 General format
~~~~~~~~~~~~~~~~~~

XML IDs should follow:

``<module>.<type>_<entity>_<purpose>``

Examples:

- ``agrios_farmer.view_farmer_form``
- ``agrios_farmer.view_farmer_tree``
- ``agrios_farmer.action_farmer_list``
- ``agrios_farmer.menu_farmer_root``

Use consistent ``type`` prefixes:

- ``view_...`` for views
- ``action_...`` for actions
- ``menu_...`` for menus
- ``group_...`` for groups
- ``rule_...`` for record rules
- ``seq_...`` for sequences
- ``report_...`` for reports

Avoid:
- random or auto-generated IDs
- renaming XML IDs after releases (breaks references)

5.2 View inheritance IDs
~~~~~~~~~~~~~~~~~~~~~~~~

For inherited views:

- suffix with ``_inherit_<extension>``

Example:

- ``agrios_farmer.view_farmer_form_inherit_myext``

Ensure inherited view IDs are unique and clearly tied to your extension module.

--------------------------
6. Menus and UI Organization
--------------------------

- Keep menus aligned with domain modules.
- Avoid scattering menus across unrelated modules.
- If adding program/country menus, group them under a clearly named parent.

Examples:
- ``AgriOS / Farmers``
- ``AgriOS / Plots``
- ``AgriOS / Training``
- ``AgriOS / Trade``
- ``AgriOS / Integrations / KoBo``

--------------------------
7. Security Naming
--------------------------

7.1 Groups
~~~~~~~~~~

Group XML IDs:

- ``agrios_<module>.group_<role>``

Examples:
- ``agrios_trade.group_trade_manager``
- ``agrios_training.group_training_user``

7.2 ACL CSV conventions
~~~~~~~~~~~~~~~~~~~~~~~

In ``ir.model.access.csv``, keep IDs readable and aligned:

- ``access_<model>_<role>``

Example:
- ``access_agrios_farmer_user``

Record rules:
- ``rule_<model>_<scope>`` (e.g., own_records, coop_records, all_records)

--------------------------
8. Database Stability & Renames
--------------------------

Renaming model technical names, field names, or XML IDs is expensive and risky.

Rules:
- Treat model/field names as **public API** once released.
- If a rename is unavoidable, document it and provide a migration plan.
- Prefer adding new fields and deprecating old ones over renaming in-place.

--------------------------
9. Examples (Quick Reference)
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Item
     - Good
     - Why
   * - Many2one to farmer
     - ``farmer_id``
     - Standard Odoo convention; easy searchability
   * - Plot area
     - ``area_ha``
     - Unit encoded in name
   * - Ingest provenance
     - ``source_form_id``, ``submission_id``
     - Enables idempotency + debugging
   * - Inherited view id
     - ``view_farmer_form_inherit_myext``
     - Signals purpose and origin


