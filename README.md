# p-reporter-task

## 1. Modulo 3 State Machine
This directory ([src](src)) contains a python implementation of a state machine for calculating the value of a binary integer modulo 3. The state machine is designed to process binary input strings and determine the remainder when the binary number is divided by 3. 
This implementation uses the general purpose Deterministic Finite Automation (DFA) to implement this solution without having to convert string to int type.
The following key components are contained in the [integer_state_fsm.py](src/integer_state_fsm.py), [modulo_three_fsm.py](src/modulo_three_fsm.py) and [main.py](src/main.py) file:
1. **IntegerStateMachine Class**: This is a generic class used to implement a DFA. It is initialized with a set of states, input values, an initial state, a set of final states, and a transition function that defines how the machine moves between states based on input value. It has a method `process_input` that takes a binary string as input and processes it character by character, transitioning between states according to the transition function.
2. **ModThreeStateMachine**: This class inherits from IntegerStateMachine and is specifically designed to calculate the modulo 3 of a binary integer. It defines the states (representing remainders `0, 1, and 2`), input values (`0 and 1`), initial state (`0`), final states (`0, 1, 2`), and the transition function based on the rules of binary arithmetic modulo 3.
3. **Main Function**: The main function creates an instance of ModThreeStateMachine and processes a sample binary input string (`"1101"`). It prints the final state of the machine, which represents the modulo 3 value of the binary integer.

### Why a Deterministic Finite Automaton (DFA)?
There are 2 choices when implementing a state machine: DFA and NFA (Nondeterministic Finite Automaton) See [Introduction of Finite Automata](https://www.geeksforgeeks.org/theory-of-computation/introduction-of-finite-automata/).
I chose DFA because it is the most natural model to solve this problem. In DFA, for each state and input symbol, there is exactly one transition to a next state. This property makes DFA easier to implement and understand, especially for problems like calculating modulo values where the transitions are deterministic and straightforward. Thus using NFA would add unnecessary complexity to the implementation without providing any additional benefits for this specific problem.

### How to Run the Code
To run the code, ensure you have Python installed on your system. You can execute the script by running the following command in your terminal:
```bash
python -m src.main 1101
```

## 2. Data Architecture for a restaurant exercise
This repository contains the data architecture for a restaurant exercise, including the necessary tables to create and populate the database tables.
The architecture is designed to handle various aspects of restaurant management, including item menu items, sales, store/franchise, and fact tables.

In designing this architecture, I made use of the Star Schema model with sales fact table and dimensions, which is a common approach for organizing data in a data warehouse. This model allows for efficient querying and analysis of large datasets, making it well-suited for the restaurant exercise.
Looking at the issue from a high level, the data architecture includes the following components:
- **Dimensional Tables**: These tables store the dimensions of the data, such as menu items, stores/franchises, store menu, item, category, sales and time. They provide context for the fact tables and are used for filtering and grouping data in queries.
- **Fact Table**: This central table store the quantitative data related to restaurant operations, such as time, store, item and/or category. This table is denormalized and allows for OLAP operations They contain foreign keys that reference the dimensional tables, allowing for efficient querying and analysis of the data.

Below is a diagram illustrating the data architecture for the restaurant exercise:
![Data Architecture Diagram](data_architecture/Data%20Architect%201.png)
link to open dbdiagram.io: https://dbdiagram.io/d/Data-Architect-p-reporter-task-68f82ad12e68d21b419bf502

In modelling this data architecture, we considered various factors such as data volume, query performance, and ease of maintenance. We also ensured that the architecture is flexible enough to accommodate future changes and additions to the data model.
### Table Descriptions
1. **DimStores**: This table contains information about the stores or franchises of the restaurant, including store ID, store name, location, date it was opened.
2. **DimTime**: This table contains information about the time dimension, including week start date, day of the week, month, quarter, and year.
3. **DimItems**: This table contains information about the menu items, including item ID, item name, category, price.
4. **FactSales**: This table contains information about the sales transactions, including store ID, item ID, quantity sold
5. **Other Supporting Tables**: These tables include Category, StoreMenu and Sales, which provide additional context and information for the dimensional tables.

This schema provides a solid foundation for managing and analyzing restaurant data, and can be extended or modified as needed to meet the specific requirements of the exercise.

### Ingestion pipeline and Technologies Used
An assumption is made that we will be using the AWS ecosystem for building the ingestion pipeline. The following technologies will be used:
- **AWS Kinesis**: This service will be used to collect and process real-time data streams from various sources, such as point-of-sale systems, online orders, and customer feedback.
- **AWS S3**: This service will be used to store the raw data collected from Kinesis streams in a scalable and cost-effective manner OR .
- **AWS Redshift**: This service can be used instead of AWS S3 to store and analyze the processed data in a data warehouse environment from Kinesis, allowing for efficient querying and reporting. This is because redshift supports fast SQL queries, large fact tables, star schema and now supports streaming data ingestion.
- **AWS Glue or Lambda Functions**: This service will be used to perform ETL (Extract, Transform, Load) operations on the data stored in S3 or Redshift, transforming it into a format suitable for analysis and loading it into the dimensional and fact tables.

### Questions for Clarification
To ensure a successful implementation of the data architecture and ingestion pipeline, the following questions need to be clarified:
1. What is the estimated volume of data to be ingested and processed on a daily
2. How frequently is the data updated or changed?
3. What are the data formats and sources for the data to be ingested?
4. How do the franchise/store submit their sales data? Is it through a centralized system or individual systems? Is it via file uploads, APIs, or other methods?
5. What is the granularity of the report required to be generated? Is it daily, weekly, monthly, or quarterly?

### Assumptions
1. I assumed each franchise has a unique store id and uses a common item_id for the same menu item across all franchises.
2. I assumed that the sales data is collected at the item level, meaning that each sale transaction is recorded for each individual menu item sold.
3. I assumed that all franchises/stores follow a standardized menu structure, with consistent item and categories across all locations.

