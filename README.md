# Globox A/B Test Project

### This project was completed for the Masterschool Data Analysis program as a Mastery project.

## Project Overview
The A/B test was conducted on the mobile website, showing a banner highlighting key products in the food and drink category. The control group saw the original site and the test group saw the banner. The users were randomly assigned to the test or control group.

The data was stored in a PostgreSQL database. The first step in the process was to explore the data in SQL. There were 3 tables, `users`, `groups`, and `activity`. The `users` table was a list of all the users by ID with their country code and gender. The `groups` table contained information around what group they were in, the date they joined the test (visited the page), and the type of device (Android or iOS). Finally, the `activity` table contained purchase activity with the date of the purchase, the device used, and the amount spent in USD.

## Process

After exploring the data I found the test was over 12 days and there were approximately 49,000 users in the test. I also found there were 643 users with no country data, 294 with no device data, and 6855 with no gender data. In both cases I decided to replace the Null value with 'Unknown' or 'U'. To extract the data from the database I used the following query:
```
SELECT
	u.id AS user_id,
	COALESCE(u.country, 'Unknown') as country,
	COALESCE(u.gender, 'U') AS gender,
	COALESCE(g.device, 'U') AS device,
	g.group AS test_group,
	g.join_dt AS join_date,
CASE WHEN a.spent > 0 THEN 'Yes' ELSE 'No' END AS converted,
ROUND(COALESCE(SUM(a.spent), 0)::numeric, 2) AS total_spent
FROM
	users u
LEFT JOIN
	groups g ON u.id = g.uid
LEFT JOIN
	activity a ON u.id = a.uid
GROUP BY
	u.id,
	country,
	gender,
	g.device,
	g.group,
	g.join_dt,
	converted;
```
Then used the export to CSV tool in Beekeeper Studio to get the data in a format to be used in Excel.
I used Excel to preform statistical analysis to determine if there was a statastically signifigant difference between the control (A) and test (B) groups for Conversion Rate and Average Amount Spent. Details on this can be found in the .xlsx file and the report. I also calculated the 95% confidence intervals.

To see if the test groups were ideal I used a Notable.io notebook to identify the ideal sample size, the Python code is in this repo.

Once the statistical analysis was complete I used Tableau Public to create various charts to show trends in the data and to complete a Novelty test to ensure any chances were not due to the newness of the banner.

Finally, I compiled a written report and PowerPoint Presentation.