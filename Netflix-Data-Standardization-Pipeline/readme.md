# Netflix Data Standardization Pipeline

## Project Overview
This project demonstrates a SQL Server-based data engineering pipeline to ingest, profile, clean, and analyze Netflix catalog data.

The raw dataset was loaded into SQL Server and transformed into an analytics-ready clean layer by standardizing dates and decomposing mixed-format duration fields into structured attributes.

---

## Business Objective
The goal was to convert raw Netflix content metadata into a clean dataset that can support business questions such as:

- How many Movies vs TV Shows are available?
- How has content growth changed over time?
- What is the average movie runtime?
- How many seasons do TV shows typically have?

---

## Architecture

End-to-end data pipeline transforming raw Netflix catalog data into analytics-ready insights using a layered architecture.

<img width="1999" height="846" alt="image" src="https://github.com/user-attachments/assets/928ce99f-3305-4130-b3b9-47d799346cb3" />



