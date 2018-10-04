# Byte Data Insights  

Overview
---
This repository contains files for a short assignment analyzing Byte Foods items purchased data and a tool to further extend these insights.

There are 3 folders in this project:
- [assets](https://github.com/tlapinsk/byte-data-insights/tree/master/assets)
- [data](https://github.com/tlapinsk/byte-data-insights/tree/master/data)
- [notebooks](https://github.com/tlapinsk/byte-data-insights/tree/master/notebooks)

The assets folder holds any images needed for the project.

The data folder holds holds the items purchased data and "fake" product data used to exemplify how a second table could improve the quality of the original insights.

The notebooks folder includes iPython notebooks, where I have curated my insights and written a small set of functions to process CSV files into a Postgres database.

This README file serves as a project write-up, details my thought process, and also includes potential improvements for a Production setting. 

The Assignment
---
The goals of this project:
* Show off your experience with data processing and engineering
* The speed of finding meaning in a new data set
* Code and methodology quality 
* Dealing with a limited set of details and the decision-making process

Tasks:
* Generate at least 3 actionable insights on the data
* Build a tool that can take in additional data as it becomes available and improve quality of the insights from above

### Dependencies  
* Python
* Postgres
* Jupyter Notebook
* matplotlib
* numpy
* pandas
* plotly
* psycopg2
* sqlalchemy

## Notebook Details  

### `Insights.ipynb`  

`Insights.ipynb` generates a few basic insights from the `items_purchased.csv`. There are more than three insights generated in the file - with the three most important shown below:

**Top 10 Selling Products**  
In the Insights file, I have generated the ~300 top selling products. To make this more concise, I have shortened it to 10 for the write-up. I'm curious what Product 4061 is.

| product_id | count |   
|------------|-------|
|    4061    | 68369 | 
|    4202    | 32361 |  
|    4793    | 27828 | 
|    2360    | 26496 | 
|    4207    | 24443 | 
|    4203    | 22463 | 
|    4319    | 21524 | 
|    2941    | 20630 | 
|    3815    | 19084 | 
|    2603    | 32361 | 

**Repeat Customers**  
Are customers repeat customers?

Yes, they are repeat customers. It seems like the top 10 (shown below) may all be corporate accounts. Within the top 100 though, it seems like a fair assessement that people do come back to purchase repetitively.

|                      card_hash                          | count |   
|---------------------------------------------------------|-------|
|    pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidl...    | 24467 | 
|    sZcYIySlDHP+sxK0GF8ZUSMYqFnoLQrbtLmsPGt+NT+ukG...    | 1688  |  
|    y4u3ViaqERLVpLdauGsClhX1v4DdxsZ2yr86TYYd7FVTzn...    | 1444  | 
|    V+trkgPKWB3Ah4u2Wq05EEPaicgnC7f6Mp+Kazbl1QZS2Z...    | 791   | 
|    RT09yBDAn5SvTjwiN5Qv5MQYPI2dUGrN6pVeHimAfvLuRE...    | 787   | 
|    3jThs4CWlxmW2ttPDkxsOlaHvMr2DZE8d44SOs13JdYKcC...    | 745   | 
|    bNakfBB3xWoCn8MZy03wMW069LsLsYF9wdKc+6uB30CmKn...    | 698   | 
|    mvqlnyiysM3Gim5u1S7fbs8TwR9Ivv9WsxJcg6nHDmSKip...    | 686   | 
|    nJqefwWsi08TlTzFhaHI84Gl6N7B0l7AR+u3lTgrjGa7gh...    | 680   | 
|    MKK69j+bCHjQBuFvoWBdh3KdpzMvs2Q//4ckTaw0uyGI22...    | 648   |

If so, do they buy the same products time and again? Yes, as seen the top 10 products sell very frequently.

|                   card_hash                       | product_id | count |
|---------------------------------------------------|------------|-------|
| pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidl...	|    4061    |  1677 |
| pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidl...	|    4793    |  807  |
| pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidl...	|    2941    |  635  |
| pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidl...	|    4202    |  551  |
| pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidl...	|    2350    |  543  |
| mvqlnyiysM3Gim5u1S7fbs8TwR9Ivv9WsxJcg6nHDmSKip...	|    5465    |  531  |
| pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidl...	|    2360    |  525  |
| pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidl...	|    4207    |  500  |
| pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidl...	|    4319    |  475  |
| pxWdKu6voFceSKpehBo0XZ6EJF5N0UDXWvnd/EbM46cidl...	|    4349    |  451  |

**Time of Day**  
What time of day do customers typically purchase items? Looks like stocking the machines with popular evening snacks/foods is important.

|   time_of_day   |   count  |
|-----------------|----------|
|   Evening       |  613779  |
|   Afternoon     |  274805  |
|   Morning       |  226988  |

**Most Lucrative Kiosks**  
As a small bonus, I am including notes about the most lucrative kiosks.

I believe the most lucrative kiosks would serve as great case studies for what makes a successful Byte Foods Kiosk. Potential insights include:
* Creating company personas (or profiles) so you can identify high potential clients
* Combining this with top selling products to optimize performance across kiosks

| kiosk_id |  count  |
|----------|---------|
|   750    |  12295  |
|   589    |  11533  |
|   680    |  11119  |
|   303    |  10190  |
|   831    |  9468   |
|   956    |  9307   |
|   423    |  9120   |
|   830    |  9060   |
|   58	   |  8941   |
|   955    |  8265   |

### `Data Feeder.ipynb`  
The Data Feeder notebook serves as a small introduction for loading a database (Postgres in this case) with data from `items_purchased.csv` and `product_info.csv`. 

Two important notes must be made about the data loading mechanism.
1. One script is built to create a table for the first time
2. The second is built to load data incrementally (e.g. feed the data) as it is generated. It will add it to the `purchases` or `product_info` table depending on the CSV provided

Note: The second script utilizes a `copy_from` method instead of inserting the data. This is the recommended solution for loading data from a CSV file into Postgres using psycopg2.

**Table Design**  
Example of potential design around the `items_purchased` table. This exemplifies a highly extensible model and shows great potential for further data analysis.

![alt text](https://github.com/tlapinsk/byte-data-insights/blob/master/assets/Table%20Design.png "Table Design Diagram")

**Key Takeaways**  
Below are some key takeaways from this portion of the assignment:

- As more data is added to the `purchases` table, we will be able to see trends over time. For example, how do things fluctuate month to month? Does seasonality make a difference in purchasing behavior?
- The `product_info` table serves as a very small example of extensibility from the `purchases` table. If we were to setup a data warehouse, I would imagine there being a whole range of tables that extended insights from the `purchases` table. The design diagram and tables with dotted outlines (see above) help illustrate this
- The tool does not feel complete. As this is a small assignment, there is a lot of room for improvement. See the **Potential Improvements** section for more details
- The chart generated at the end of the notebook is a small taste of what could be a larger dashboard. This would allow business users to track KPIs and the like. See below for the chart since it seems that GitHub did not load it properly.

![alt text](https://github.com/tlapinsk/byte-data-insights/blob/master/assets/Extending%20Insights%20Example.png "Extending Data Insights Example")

## Running the Notebooks  

### `Insights.ipynb`  
Details for running the notebook below:

At the command prompt

    git clone https://github.com/tlapinsk/byte-data-insights.git
    cd byte-data-insights
    cd data
    tar -xvzf items_purchased.tar.xz
    cd ..
    jupyter notebook

Open `Insights.ipynb` in your browser. You should be able to Run All cells and generate the insights.

### `Data Feeder.ipynb`  
Details for running the notebook below:

Please ensure you have Postgres running locally with a database named `postgres` loaded.

Assuming you have already cloned the repository, unzipped the `items_purchased.tar.xz`, and have Jupyter Notebook running.

Open `Data Feeder.ipynb` and replace your Postgres username and password where necessary (one in each cell).

You should then be able to Run All cells and monitor Postgres to see the tables being created / updated.

As a note, the incremental load will dump the same data twice into each table since there is no new data provided. It is merely an example of how to load data incrementally.

## Potential Improvements  
The insights and tool provided are small examples, that by no means would be run in Production. They are helpful in providing examples of how I would load these CSVs into a database (assuming the CSVs lives locally on my computer).

**Insights Improvements**  
- Create front end web interface and dashboard for users
- Explore Plotly or other similar tools to analyze data
- Explore further insights from a larger Datawarehouse setting

**Data Feeder Improvements**  
In a Production setting I would propose the following improvements:
- Run an S3 bucket to host CSV files
- Upon new CSV files being dumped into S3, fire AWS Lambda function to feed CSV file into Postgres (or any other database)
- OR, assuming APIs endpoints are built, tap into these APIs on regular intervals
- OR, assuming other databases host Sales data, create ETL Mappings to load data into a Datewarehouse / Data Lake incrementally