==========================
Roles & Responsibilities
==========================

This guide explains the **core operational roles involved in using AgriOS**,
what each role is responsible for, and how responsibilities should be
distributed to ensure **data quality, accountability, and trust**.

It is intended for **implementers and program owners** who are setting up
AgriOS for real-world use.

AgriOS is designed to support multiple stakeholders across the agricultural
ecosystem, but *not all stakeholders are system users*.
Clear role definition is essential for successful deployment.

.. contents::
   :local:
   :depth: 2

----------------------------------
1. Why Roles Matter in AgriOS
----------------------------------

AgriOS is a **single source of truth ERP and traceability system**.
This means:

- data entered once is reused everywhere
- errors propagate if roles are unclear
- trust depends on governance, not just software

Poor role design is one of the most common causes of failed ERP deployments.

AgriOS deliberately separates:
- **data entry**
- **data approval**
- **data use**
- **system governance**

:contentReference[oaicite:0]{index=0}

----------------------------------
2. Overview of Core Roles
----------------------------------

AgriOS distinguishes between **operational roles** (people who use the system)
and **ecosystem stakeholders** (people who benefit from the data).

Core operational roles:

- System Administrator
- Program Manager
- Field Agent
- Trade Operator
- Analyst / Reporting User

Other stakeholders (farmers, buyers, lenders, governments) are
*not direct system users*, but are affected by how these roles perform.

----------------------------------
3. System Administrator
----------------------------------

**Primary responsibility:** System integrity and configuration.

Typical profile:
- IT staff
- implementation partner
- local service provider

Responsibilities:
- initial system setup
- user creation and role assignment
- module installation
- configuration decisions (IDs, workflows, permissions)
- upgrades and backups

What this role should NOT do:
- enter operational data regularly
- override business rules for convenience
- act as a substitute for program management

Key principle:
> Administrators enable the system — they do not run the program.

----------------------------------
4. Program Manager
----------------------------------

**Primary responsibility:** Data quality and operational governance.

Typical profile:
- cooperative manager
- SME operations lead
- NGO program lead

Responsibilities:
- defining workflows (what gets recorded, when)
- approving or reviewing records
- archiving incorrect or obsolete data
- monitoring completeness and coverage
- ensuring staff follow agreed processes

Program Managers are **accountable for the credibility of the data**.

What this role should NOT do:
- bulk data entry
- technical configuration changes
- manual data manipulation outside the system

Key principle:
> If the data is questioned by a buyer or lender, the Program Manager owns the explanation.

----------------------------------
5. Field Agent
----------------------------------

**Primary responsibility:** Primary data collection.

Typical profile:
- extension officer
- enumerator
- cooperative field staff

Responsibilities:
- registering farmers
- registering plots
- recording training participation
- capturing field-level observations
- correcting errors through approved processes

What this role should NOT do:
- delete records
- edit historical trade data
- approve their own work
- bypass validation rules

Field Agents are the **front line of data quality**.

Key principle:
> Field Agents capture facts — they do not decide policy.

----------------------------------
6. Trade Operator
----------------------------------

**Primary responsibility:** Commercial record accuracy.

Typical profile:
- procurement officer
- warehouse manager
- buying clerk

Responsibilities:
- creating draft trades or purchase records
- recording deliveries and quantities
- confirming trades when conditions are met
- ensuring trade states reflect reality

What this role should NOT do:
- change farmer or plot data
- alter settled trades
- override pricing rules without approval

Trade Operators work with **high-risk, high-sensitivity data**.

Key principle:
> Trade data must be auditable, not convenient.

----------------------------------
7. Analyst / Reporting User
----------------------------------

**Primary responsibility:** Interpretation, not creation, of data.

Typical profile:
- M&E staff
- finance staff
- donor reporting staff
- compliance teams

Responsibilities:
- running reports
- exporting data
- interpreting trends
- answering stakeholder questions

What this role should NOT do:
- modify source records
- “fix” data by editing reports
- create parallel spreadsheets as system replacements

Key principle:
> Reports explain the system — they do not correct it.

----------------------------------
8. Farmers (Important Clarification)
----------------------------------

Farmers are **not system users** in AgriOS.

They are:
- data subjects
- value chain participants
- beneficiaries

Their data:
- must be accurate
- must be explainable
- must be handled responsibly

Any errors affecting farmers are the responsibility of:
- Field Agents (entry)
- Program Managers (oversight)

:contentReference[oaicite:1]{index=1}

----------------------------------
9. External Stakeholders (Read-Only)
----------------------------------

The following stakeholders may consume AgriOS outputs but do not operate the system:

- commercial buyers
- lenders and investors
- governments
- auditors
- certification bodies

They rely on:
- role separation
- audit trails
- consistent processes

AgriOS is designed to generate **investor-grade and compliance-ready data**
*only if roles are respected*.

----------------------------------
10. Common Role Assignment Mistakes
----------------------------------

Avoid these patterns:

- one person holding all roles
- administrators entering business data
- field agents approving their own records
- analysts “fixing” data in Excel
- unclear accountability for errors

Most data failures are **organizational, not technical**.

----------------------------------
11. Recommended Minimum Setup
----------------------------------

For small deployments:

- 1 System Administrator (part-time)
- 1 Program Manager
- 2+ Field Agents
- 1 Trade Operator
- 1 Analyst (can be the Program Manager)

Roles may overlap — responsibilities must not.

----------------------------------
12. Summary
----------------------------------

AgriOS works best when:

- roles are explicit
- authority is separated
- accountability is clear
- convenience does not override governance

Good role design is the foundation for:
- trusted data
- access to finance
- regulatory compliance
- scalable growth

