# Frequently Asked Questions (FAQ)

Find answers to common questions about the system.

## About AgriOS

- **What is AgriOS?** AgriOS is an open-source, subscription-free Enterprise Resource Planning (ERP) system for African agri-SMEs and cooperatives. Built on the Odoo Community platform, it integrates business management and traceability tools to help organisations improve operational efficiency, become more eligible for financing, and formalise their role in global value chains. The goal is to provide a "plug-and-play" tool that doesn't require deep technical expertise to set up.

- **What technology is AgriOS built on?**
It's built on Odoo Community, a proven, open-source ERP platform. This ensures the system is scalable and robust and avoids vendor lock-in. It also integrates with specialised third-party tools like the Kobo Toolbox for offline data collection.

## Cost & Business Model
- **Is AgriOS really free? What are the potential costs?** Yes, the standard version of AgriOS is and will always be subscription-free. The business model is designed as a digital public good. The only potential costs for users would be: Hosting (after an initial 1-2 year period, estimated at $10-$20/month), Customisation (if you require non-standard features), and Internal Staff (time dedicated to manage the system).
- **How does the project sustain itself financially if the software is free?** The financial sustainability is built on a two-pronged model: Grants and Foundational Support (approx. 50% from governments/foundations supporting digital public goods) and Commercial Contracts (50% from larger stakeholders paying for services like feature development and training).

## Features & Functionality
- **Deciding on New Features:** We build for the community, not just individual organisations. With limited resources, we consider: Will it require customisation for each user? What is the general demand? How much time/effort will it take to develop?
- **What are the key features of AgriOS?** Key modules include: Farmer and Farm Management (profiling, mapping, contracts), Core Business Operations (sales, CRM, purchasing, invoicing, inventory, HR), Data Collection (Kobo Toolbox integration), and Traceability and Compliance.
- **Does AgriOS work offline?** Yes, it is designed for the African context. It integrates with tools like the Kobo Toolbox for offline data collection. Data syncs automatically once a connection is established.
- **Can I integrate payment systems like mobile money (M-Pesa)?** Direct integration is complex and requires tailoring. It is technically possible but not included by default; it requires a commercial arrangement or donor support.
- **Can the system track complex value chains, including upstream and downstream activities?** Yes, but we cannot adapt for every manufacturing case.
- **Is there a module for tracking physical assets like cooler boxes?** There is one in the Odoo Community, but we do not plan to integrate it for now. We will decide based on interest among Early Adopters.
- **Can the system facilitate direct communication with farmers via SMS?** This requires customisation and is not included for Early Adopters currently. It is technically feasible on a commercial basis.
- **Does the platform support specific payment schedules, like weekly payments based on supply?** Yes, there are payment schedules. (Note: It is unclear what ‘based on supply’ specifically refers to in this context).

## Offtake & Procurement
- **Is it possible to bulk upload offtake products?** Yes, you can bulk upload using an Excel or CSV file, ensuring data formats match the templates.
- **When will the offsetting feature be available?** The feature is nearly finished and will be available when the Agri-OS implementation starts.
- **Can you upload bulk payments if you pay farmers in cash?** Yes, using the "import record" function with a formatted Excel or CSV file.
- **How does the system work for a dairy business (daily milk purchases with input deductions)?** This uses the offsetting feature. When creating a bill for milk, the system shows outstanding invoices for inputs. You can select invoices to deduct, and the system calculates the net amount owed. This supports recurring deductions.
- **Can field supervisors be treated as warehouses for stock?** Yes, that is the most logical approach if you do not have physical warehouses.
- **Can we link farmer training lists with subsequent purchase records?** Yes, it is linked through the farmer who attended the training and purchased the product.

## Financial Management & Credit
- **Does the system support instalment payments for inputs given to farmers?** Yes. You can create custom "payment terms" that automatically split an invoice into multiple instalments with due dates.
- **Can the system send automatic payment reminders via text message?** Technically yes, but SMS functionality is not currently available.
- **Can a credit limit be set for each farmer?** Yes. You can set a maximum open balance to block transactions or issue warnings if the limit is exceeded.
- **What currencies are available?** All formal currencies.
- **Can I charge one farmer in USD and another in kwacha?** Yes.
- **Can I store inventory in different currencies?** No. It is all stored in one.
- **Can we link the platform to our MPESA till data?** We can import the records, but triggering payments via AgriOS is not available for now. Bank reconciliation should be possible, but is not yet confirmed.

## Inventory Management
- **Can the system track inventory movement between a head office and different branches?** Yes. You can create an "internal transfer" to update stock levels at both locations automatically.
- **How can you segregate certified products from non-certified ones?** The recommended method is to create two different product types (e.g., "Fairtrade Certified Cocoa" and "Standard Cocoa") and assign the correct type to each farmer.
- **Can the system assign batch IDs for perishable goods like fish?** Yes, we have traceability and expiration dates (e.g., 3 days after receipt).
- **Can we capture batch production dates and get expiry alerts?** Yes.
- **What is the best way to handle returned stock, track expiry, and record stock destroyed?** The Inventory module.

## User Management & Access Rights
- **How many sub-accounts can a company have, and can farmers be grouped?** You can have unlimited users. Farmers can be assigned to specific salespersons/extension agents, and access rights can be configured so agents only see their assigned farmers.
- **Can a salesperson create their profile and add farmers?** This is flexible. You can grant specific permissions to create new farmers, edit assigned farmers, or just view records.
- **Can a third-party, like an accounting firm, be given access?** Yes, you can create a user account for them with specific permissions.

## Implementation & Support
- **What are the benefits of being an early adopter?** Benefits include In-Person Training (flights/accommodation covered), Dedicated Implementation Support (remote support for rollout), and Influence on Development (feedback shapes the tool).
- **What is expected from an early adopter?** Committing Time and Resources, Sharing anonymised organisational data for research, and Providing Feedback.
- **Do we provide any additional training for the rest of the team?** We are happy to add team members to the mailing list.
- **Can I customise AgriOS for my specific business needs?** The standard version is for the broad community. However, as it is open-source, you can develop custom features with your own team or hire an external Odoo service provider.

## Data & Commercial Use
- **Who owns my data? Is it secure?** You own 100% of your data. AgriOS requires temporary access for setup/analysis but not long-term. Data is stored securely with mainstream hosting providers.
- **Can I use AgriOS to make money for my own business?** Yes. You are free to Offer Services (implementation/training), White-Label the Product, or Develop Custom Features for clients. There is no financial obligation to the AgriOS team for this.

- 
