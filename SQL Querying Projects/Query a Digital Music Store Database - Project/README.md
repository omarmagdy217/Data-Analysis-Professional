## Digital Music Store Database Querying
![chinook_erd](https://user-images.githubusercontent.com/36456356/231261373-29f7f1d4-9d84-4716-9180-4c804537bcca.png)
**SQLite** is used to browse the `chinook.db` database with the **ERD** diagram shown above and apply the queries in the `queries.txt` file to answer the following questions:
- How many Tracks does each Artist have?
- What are the most popular Genres?
- Which Countries have Most Rock Music Listeners?
- What Albums include Tracks with length above AVG?

Data retrieved from these queries is then exported to **CSV** format and opened in **Excel** to generate summary visualizations reported in the `report.pdf` with some analysis statements.

---
`sub_queries.txt` file includes more complex sub-queries to answer question like:
- Who is the customer with highest spend amount on top artist's albums?
- Which country having the maximum genre purchases?
