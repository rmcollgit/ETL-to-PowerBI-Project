# PowerBI-Project
This repository contains a complete end-to-end data project that transforms raw sales data into a clean, insightful Power BI dashboard. The dataset is sourced from Kaggle’s Superstore dataset, which includes detailed information on customer orders, products, delivery times, and geographical locations across the United States.

The project follows a clear pipeline: data is extracted, cleaned using Python and Pandas, exported to CSV, and then visualised using Power BI. It is designed to be fully reproducible on your local machine.

<img width="954" height="202" alt="image" src="https://github.com/user-attachments/assets/b859ad0c-5dea-4e04-8f3a-e5663e4daca7" />

## The dataset

Customer information: name, region, and ID

Product data: category, sub-category, and product names

Sales performance: sales value (count of sales was calculated to infer sales volume)

Delivery details: order and ship dates and ship mode (delivery time was calculated)

Geography: US cities, states, and postal codes


## How to run on your machine

1. Clone the repository
2. Run the files in the Python folder, in the order; get_data.py, create_df.py, cleaning_data.py
3. Open the dashboard in the PowerBI folder
4. Ensure that the dashboard has access to the CSV from python then transform, close and apply.

## Interacting with the dashboard

This dashboard has been designed to be fully interactive, here's how to navigate and filter the data:

Location slicer:
- On the side of each page there is a dropdown list of US states, just select the ones that you are interested in to filter all visuals.
- To reset press select/deselect all.

Year slicer:
- On the side of each page you can slide across years or manually enter a year to filter all visuals.

Other filters:
- You can click on the data in any visual or table to filter others.
- For example if you are only interested in furniture sales, just click on that section of the category visualisation.

Page navigation:
- Buttons on the side of each page allow you to easily switch between pages.
- Just click the button whilst pressing Ctrl to move page.

## Contributing
Contributions are welcome, if you'd like to suggest a feature, fix a bug, or improve the dashboard:

1. Fork the repository

2. Create a new branch: git checkout -b feature/your-feature-name

3. Make your changes and commit: git commit -m "Add feature"

4. Push to your fork: git push origin feature/your-feature-name

5. Open a pull request
