User FAQ
========

Find answers to common questions about the system.

About AgriOS
------------

**What is AgriOS?**
   AgriOS is an open-source, subscription-free Enterprise Resource Planning (ERP) system for African agri-SMEs and cooperatives. Built on the Odoo Community platform, it integrates business management and traceability tools to help organisations improve operational efficiency, become more eligible for financing, and formalise their role in global value chains. The goal is to provide a "plug-and-play" tool that doesn't require deep technical expertise to set up.

**What technology is AgriOS built on?**
   It's built on Odoo Community, a proven, open-source ERP platform. This ensures the system is scalable and robust and avoids vendor lock-in. It also integrates with specialised third-party tools like the Kobo Toolbox for offline data collection.

**Is AgriOS Open Source?**
   AgriOS is fully open-source. It uses two well-known, widely trusted licenses:
   Odoo Community runs under the LGPL-v3 license. All AgriOS modules are released under the MPL-2.0 license. What this means in practice is simple:

   AgriOS is free to use, free to modify, and free to build on. Any improvements made to our modules must remain open, but organisations are free to create their own add-ons, integrations, and commercial services around AgriOS without restriction.

   This approach protects the openness of the AgriOS core while giving users, partners, and developers complete freedom to innovate. It ensures AgriOS remains a true digital public good—owned by the community, adaptable to local needs, and never locked behind a vendor.

Cost & Business Model
---------------------

**Is AgriOS really free? What are the potential costs?**
   Yes, the standard version of AgriOS is and will always be subscription-free. The business model is designed as a digital public good. Non subscription costs may include hosting (though we're covering those costs for now), customisation (if you need it) and the cost of your own staff to manage the setup and maintenance.

**How does the project sustain itself financially if the software is free?**
   The financial sustainability is built on a two-pronged model: Grants and Foundational Support (approx. 50% from governments/foundations supporting digital public goods) and Commercial Contracts (50% from larger stakeholders paying for services like feature development and training).

Features & Functionality
------------------------

**Deciding on New Features:**
   We build for the community, not just individual organisations. With limited resources, we consider: Will it require customisation for each user? What is the general demand? How much time/effort will it take to develop?

**What are the key features of AgriOS?**
   Key modules include: Farmer and Farm Management (profiling, mapping, contracts), Core Business Operations (sales, CRM, purchasing, invoicing, inventory, accounting), Data Collection (Kobo Toolbox integration), and Traceability and Compliance.

**Does AgriOS work offline?**
   No AgriOS does not work offline. However, AgriOS can be integrated with tools like Kobo Toolbox for offline data collection.

**Can I integrate payment systems like mobile money (M-Pesa)?**
   Direct integration is complex and requires tailoring. It is technically possible but not included by default; it requires a commercial arrangement or donor support.

**Can the system track complex value chains, including upstream and downstream activities?**
   Yes, but we cannot adapt for every manufacturing case.

**Can the system facilitate direct communication with farmers via SMS?**
   This requires customisation and is not currently included. It is technically feasible on a commercial basis.

**Does the platform support specific payment schedules, like weekly payments based on supply?**
   Yes, there are payment schedules. calendar

Offtake & Procurement
---------------------

**Is it possible to bulk upload offtake products?**
   Yes, you can bulk upload using an Excel or CSV file, ensuring data formats match the templates.

**Can you upload bulk payments if you pay farmers in cash?**
   Yes, using the "import record" function with a formatted Excel or CSV file.

**How does the system work for a dairy business (daily milk purchases with input deductions)?**
   This uses the offsetting feature. When creating a bill for milk, the system shows outstanding invoices for inputs. You can select invoices to deduct, and the system calculates the net amount owed. This supports recurring deductions.

**Can field supervisors be treated as warehouses for stock?**
   Yes, that is the most logical approach if you do not have physical warehouses.

**Can we link farmer training lists with subsequent purchase records?**
   Yes, it is linked through the farmer who attended the training and purchased the product.

Financial Management & Credit
-----------------------------

**Does the system support instalment payments for inputs given to farmers?**
   Yes. You can create custom "payment terms" that automatically split an invoice into multiple instalments with due dates.

**Can the system send automatic payment reminders via text message?**
   Technically yes, but SMS functionality is not currently available.

**Can a credit limit be set for each farmer?**
   Yes. You can set a maximum open balance to block transactions or issue warnings if the limit is exceeded.

**What currencies are available?**
   All formal currencies.

**Can I charge one farmer in USD and another in kwacha?**
   Yes.

**Can I store inventory in different currencies?**
   No. It is all stored in one.

**Can we link the platform to our MPESA till data?**
   We can import the records, but triggering payments via AgriOS is not available for now. Bank reconciliation should be possible, but is not yet confirmed.

Inventory Management
--------------------

**Can the system track inventory movement between a head office and different branches?**
   Yes. You can create an "internal transfer" to update stock levels at both locations automatically.

**How can you segregate certified products from non-certified ones?**
   The recommended method is to create two different product types (e.g., "Fairtrade Certified Cocoa" and "Standard Cocoa") and assign the correct type to each farmer.

**Can the system assign batch IDs for perishable goods like fish?**
   Yes, we have traceability and expiration dates (e.g., 3 days after receipt).

**Can we capture batch production dates and get expiry alerts?**
   Yes.

**What is the best way to handle returned stock, track expiry, and record stock destroyed?**
   The Inventory module.

User Management & Access Rights
-------------------------------

**How many sub-accounts can a company have, and can farmers be grouped?**
   You can have unlimited users. Farmers can be assigned to specific salespersons/extension agents, and access rights can be configured so agents only see their assigned farmers.

**Can a salesperson create their profile and add farmers?**
   This is flexible. You can grant specific permissions to create new farmers, edit assigned farmers, or just view records.

**Can a third-party, like an accounting firm, be given access?**
   Yes, you can create a user account for them with specific permissions.

Implementation & Support
------------------------

**What support are you offering to individual users?**
   None. We'll run webinars where users can get feedback from our technical specialists.

Data & Commercial Use
---------------------

**Who owns my data? Is it secure?**
   You own 100% of your data. AgriOS requires temporary access for setup/analysis but not long-term. Data is stored securely with mainstream hosting providers.

**Do I need to host with you?**
   We're very happy for you to host by yourself though be sure to check for regular updates so you benefit from our upgrades.

**Can I use AgriOS to make money for my own business?**
   Yes. You are free to Offer Services (implementation/training), White-Label the Product, or Develop Custom Features for clients. There is no financial obligation to the AgriOS team for this.

General & Vision
----------------

**What is "SaaM" and how does it relate to AgriOS?**
   "SaaM" stands for "Software as a Mentor." It reflects our philosophy that AgriOS isn't just a tool for recording data; it functions as a form of embedded Technical Assistance. By enforcing standardised workflows, the software effectively "teaches" and instils best practices in financial management, governance, and supply chain oversight.

**Why do you use the term "System of Systems"?**
   AgriOS is designed as a "System of Systems" because it integrates heavy-duty ERP capabilities (like invoicing and inventory) with field-level data tools (like plot geolocation and farmer profiles) and connects with external specialized tools (like Kobo Toolbox or future integrations with AgStack and FAO's WHISP).

Compliance & Regulations (EUDR & ISO)
--------------------------------------

**How does AgriOS specifically help with EUDR compliance?**
   We estimate that the AgriOS functionality covers 80% of upsteam EUDR compliance obligations but it is not yet packaged into a single  Compliance Suite. This is on our road map to helps users address Article 9 (deforestation-free proof), Article 10 (geolocation), and Article 11 (risk mitigation): store verifiable evidence of legal land use and FPIC, perform automated deforestation checks against the 2020 cut-off date, and generate machine-readable data packages for buyers.

**Is AgriOS ISO 18716 certified?**
   No, ISO 18716 is a *guidance* standard, not a certification. However, AgriOS is designed to be an "ISO Enabler." We are enhancing core modules to operationalise the standard (e.g., adding by-law tracking to the Farmer module and KPI tracking to Project Management) and building a specific "ISO 18716 Alignment Module" to report on adherence to these best practices. We're not there yet, though.

Technical Architecture & Integrations
-------------------------------------

**What is the AgStack Asset Registry integration?**
   We plan to integrate with AgStack to create a unique, permanent, and anonymous "public geoID" for every plot of land. This ensures an immutable link between the physical asset and its digital record, which is crucial for long-term traceability and financing.

**How does the system handle "Light Accounting" vs. Standard Accounting?**
   AgriOS provides "light accounting" integrated into operations (invoicing, payments, offsetting inputs against milk/crops). For complex, statutory accounting, it allows data to be exported or integrated with standard accounting packages, but its primary focus is on operational financial flows relevant to the value chain.

**Can I use Kobo Toolbox with AgriOS?**
   Yes. AgriOS integrates with Kobo Toolbox to facilitate robust offline data collection in the field. This allows for surveys and primary data gathering without an internet connection, which then syncs with the main ERP.

Opportunities for Service Providers
-----------------------------------

**I am a local IT firm. Do I need to pay to become a service provider?**
   No. You do not pay us. You can use the open-source code to build a business offering implementation, training, and support to local agri-SMEs. You keep 100% of the revenue you generate. We only ask that code improvements be contributed back to the master repository.

**Will there be an official certification for service providers?**
   Yes, in the future. We propose a model where a limited number of providers can be formally trained and certified. This would give them enhanced credibility, leads from our website, and direct technical support in exchange for a revenue-sharing agreement.
