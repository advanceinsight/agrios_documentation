==========================
Implementation Guide
==========================

This guide explains **how to set up AgriOS for a real-world deployment**.
It is written for **system owners, program managers, and implementers**
who are responsible for making AgriOS work in practice: not just technically,
but operationally and organizationally.

This guide should be read **before any large-scale data entry begins**.

----------------------------------
1. Purpose of This Guide
----------------------------------

AgriOS is flexible by design.  
That flexibility is powerful (and dangerous) if early decisions are unclear.

This guide helps you to:

- Make correct setup decisions
- avoid irreversible mistakes
- align software behavior with program reality
- ensure data can be trusted by buyers, lenders, and regulators

AgriOS does not enforce “one right way”. **There are choices to be made.**

----------------------------------
2. Who This Guide Is For
----------------------------------

You should read this guide if you are:

- a Program Manager
- an NGO or cooperative lead
- a government or donor project owner
- an implementation partner
- a system administrator supporting a program

If you are a Field Agent or daily system user,
see the **User Guides** instead.

----------------------------------
3. Pre-Implementation Checklist
----------------------------------

Before configuring AgriOS, answer these questions **offline** with stakeholders.

3.1 Organizational Scope
~~~~~~~~~~~~~~~~~~~~~~~~

Decide:

- Is this one program or multiple programs?
- One cooperative or multiple cooperatives?
- One country or multiple countries?

Why this matters:
- affects security rules
- affects reporting
- affects long-term scalability

Rule of thumb:
> If data should never be mixed, it should be separated from day one.

----------------------------------
3.2 Farmer Identity Strategy
----------------------------------

Decide **how farmers will be uniquely identified**.

Common options:
- national ID
- cooperative ID
- program-issued ID
- combination of fields

Key rules:
- choose ONE primary identifier
- make it stable
- do not reuse identifiers

Bad decisions here are extremely hard to fix later.

----------------------------------
3.3 Plot Granularity
----------------------------------

Decide what a “plot” means in your program:

- every physical field?
- one plot per crop?
- one plot per farm?
- non-spatial logical units?

AgriOS supports all of these — but reporting and compliance depend on consistency.

Rule of thumb:
> Define plots at the level you expect to make decisions about land.

----------------------------------
3.4 Training Tracking Depth
----------------------------------

Decide how much detail you will track:

- only attendance?
- session-level participation?
- outcomes or certifications?

More detail:
- increases reporting power
- increases operational burden

Start simple. You can extend later.

----------------------------------
3.5 Trade Workflow Strictness
----------------------------------

Decide:

- who can create trades?
- when are trades confirmed?
- who can settle or cancel?
- are partial deliveries allowed?

AgriOS trade states exist to **protect financial truth**.
Do not weaken them for convenience.

----------------------------------
4. Data Ingestion Strategy
----------------------------------

AgriOS supports multiple data entry approaches.

4.1 Manual Entry
~~~~~~~~~~~~~~~~

Best for:
- small programs
- high-touch onboarding
- low technical capacity contexts

Risks:
- slower
- more human error
- harder to scale

----------------------------------
4.2 Survey-Based Ingestion (e.g. KoBo)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Best for:
- large-scale onboarding
- distributed field teams
- standardized data collection

Requirements:
- clear form design
- mapping validation
- ingestion oversight

Important:
> Surveys collect data. They do not define truth.
AgriOS does.

----------------------------------
4.3 Mixed Approach
~~~~~~~~~~~~~~~~~~

Common and valid:
- surveys for onboarding
- manual corrections and reviews

Ensure:
- reprocessing rules are understood
- errors are reviewed, not ignored

----------------------------------
5. Data Governance & Quality
----------------------------------

AgriOS cannot guarantee data quality by itself.

You must define:

- who reviews new records
- how errors are corrected
- when data becomes “trusted”
- what happens to obsolete records

Recommended pattern:
- Field Agents enter data
- Program Managers review
- Archiving instead of deletion

----------------------------------
6. Security & Access Setup
----------------------------------

Use roles deliberately.

Minimum guidance:
- Administrators configure, not operate
- Field Agents cannot approve their own data
- Trade Operators cannot alter farmer identity
- Analysts cannot modify source records

Do not:
- share accounts
- give everyone full access
- rely on trust alone

----------------------------------
7. Reporting Readiness
----------------------------------

Before sharing reports externally, ensure:

- roles are respected
- draft vs confirmed data is understood
- reporting definitions are documented
- everyone agrees what numbers mean

Never surprise partners with unexplained numbers.

----------------------------------
8. Pilot Before Full Rollout
----------------------------------

Strongly recommended:

- start with a pilot group
- test workflows end-to-end
- review reports with real data
- fix process issues before scaling

Most failures happen during **first scale**, not first setup.

----------------------------------
9. Change Management
----------------------------------

Expect:
- resistance
- confusion
- workarounds

Mitigations:
- train by role
- explain *why* rules exist
- tighten rules gradually
- document decisions

AgriOS succeeds when people trust the system,
not when they fear it.

----------------------------------
10. Common Implementation Mistakes
----------------------------------

Avoid:

- starting data entry before decisions are made
- importing bad data “to fix later”
- giving admins operational responsibilities
- bypassing workflows for speed
- letting spreadsheets replace the system

----------------------------------
11. When to Revisit Setup Decisions
----------------------------------

Revisit decisions when:

- program scope changes
- new compliance requirements appear
- scale increases significantly
- new stakeholders rely on the data

Document changes and communicate them.

----------------------------------
12. Summary
----------------------------------

A successful AgriOS implementation depends on:

- deliberate setup
- clear roles
- disciplined governance
- patience during rollout

The software is flexible.
Your responsibility is to use that flexibility wisely.

