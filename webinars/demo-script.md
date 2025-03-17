Start with CSV file
Zendesk Export
Emailed from CEO
Please see exported tickets from Zendesk activity in 2024 I got IT to do for us
Have looked it over and thinking our priorities for 2025 should be:

1. Respond quickly
2. Provide a great experience
3. Support the sales team with identifying opportunities to engage

Please can you look into the data more to help with presenting to the entire customer support team.

Thank you.

CSV file sent from CEO to customer support head.
We will upload/import CSV to sheets
Connect sheet to Looker Studio
Build dashboard, graphs, dive into the dataset
Share an email back to CEO with useful insights


---
Intro:

Thank you          [to whomever is handing it over]

Thanks [name]

Good morning everyone,

I’m Jacob. A Sales Engineer at Brio Technologies.

I work closely with Corey and the Looker team at Google to help companies take full advantage of the Looker platform.

Today I’ll demonstrate discovering insights using Looker from data collected by a customer support team.

With that in mind, let’s get in to the demo.

---
**START**
**GMAIL**
Start in gmail
Gemini side panel
Show unread emails
Open email
At bottom click, Edit with google sheets
---
**MOVE**
**Google Sheets**
Leave summary open in gem side panel (looks good)

---
**MOVE**
**Looker Studio**
Looker Studio dev account
Create data source
Google Connectors (24)
Partner Connectors (1169)

Rename top left: 2024 Zendesk Export
File upload (connect to CSV)
Connect to Google Sheets
Check for fresh data (every 15 minutes) - if records were added
Show data preview - all fields

---
**-> Create Report**
Title 2024 Customer Support Analysis
Use pages
- Home

**Average First Response Time by Month**

1. Sharp decrease in Feb & March, indicates improvement in support efficiency in early Q1
2. Spikes in July-August - possible causes, higher ticket volume, staff shortages, process inefficiencies (req. further investigation)
3. Fluctuations in Q3/4 - Rising towards December, could be linked to seasonal demand, holidays, ops challenges

**Resolution Time by Issue Type**

- No Issue Type categorized in dataset
Dimension: 
Issue Type using a formula:

`CASE 
  WHEN REGEXP_MATCH(User, "(?i).*login.*|.*access denied.*|.*authentication.*") THEN "Login Issues"
  WHEN REGEXP_MATCH(User, "(?i).*api.*|.*integration.*|.*webhook.*") THEN "API Issues"
  WHEN REGEXP_MATCH(User, "(?i).*error.*|.*crash.*|.*bug.*|.*failure.*") THEN "Software Bugs"
  WHEN REGEXP_MATCH(User, "(?i).*billing.*|.*invoice.*|.*payment.*|.*refund.*") THEN "Billing Issues"
  WHEN REGEXP_MATCH(User, "(?i).*feature request.*|.*enhancement.*|.*upgrade.*") THEN "Feature Requests"
  ELSE "Other Issues"
END`

API issues are taking the longest to resolve, can look into API documementation, or send follow ups to customers struggling to use the API, get feedback to improve the product/this part of the process and reduce the burden on the customer support team.

Add date range control to drill down into issues that took the most time during the start of the year, where first response time is slower...

January - lots of login issues, is this linked to forced password reset or 2FA changes?

**Positive Support Experiences by Contact**
Can look at users who have satisfaction scores of 5
Can search for all sat scores for a specific contact.
Possibly able to identify good contacts to refer to our sales team for follow ups.

Example:
Control
Search by contact name:
All tickets for
Michael Smith
Enjoys working with us but didn't have a great experience with Visionary
Worth reaching out or investigating more to understand why, we need to keep this customer happy

**Support Tickets by Product**
Pie Chart
Most issues with Visionary product
Can quickly identify Product to focus on e.g.
Clearer documentation
Software updates
Help product, support team to focus
and reduce issues in 2025











Share
Schedule report - support ticket volume by customer
Set it up to stay updated (data is refreshed every 15 minutes), with support ticket volume by customer - first thing every Monday morning 8am. 
Send now to test it out.
Show email report.

Customize email subject line: 
Support Ticket Volume by Customer
MSG. 
Monitor support ticket volume by customer, to help escalate investigations for priority customers with the most issues.





