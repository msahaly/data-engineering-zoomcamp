## DE-ZoomCamp > Module #1 > HomeWork

### Question 1. Understanding Docker images

Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

What's the version of pip in the image?

#### Answer: pip 23.3
<img width="643" height="169" alt="image" src="https://github.com/user-attachments/assets/1487efa6-738c-40be-a14b-ae1cfb362101" />


---

### Question 2. Understanding Docker networking and docker-compose

Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

#### Answer: db:5432


---

### Question 3. Counting short trips

For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?

#### Answer: 8007
```sql
  SELECT 
  	count(*) as tips_count 
  FROM 
  	green_taxi_data 
  WHERE
  	lpep_pickup_datetime >= '2025-11-01' and lpep_pickup_datetime < '2025-12-01' AND 
  	trip_distance <= 1
```
<img width="1059" height="511" alt="image" src="https://github.com/user-attachments/assets/cdecbcc1-31ce-49c6-82b8-fe6d87875505" />


---

### Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).

#### Answer: 2025-11-14
```sql
  SELECT 
  	lpep_pickup_datetime, trip_distance 
  FROM 
  	green_taxi_data 
  WHERE
  	trip_distance < 100
  ORDER BY trip_distance DESC
  LIMIT 1
```
<img width="911" height="494" alt="image" src="https://github.com/user-attachments/assets/b91904d2-58b0-4475-b9ee-0a92d193d9b7" />



---

### Question 5. Biggest pickup zone

Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

#### Answer: East Harlem North
```sql
  SELECT 
  	COUNT(t.*) as total_amount, z."Zone"
  FROM 
  	green_taxi_data as t INNER JOIN
  	pickup_zones as z
  	ON t."PULocationID" = z."LocationID"
  WHERE
  	t.lpep_pickup_datetime >= '2025-11-18 00:00:00' AND 
  	t.lpep_pickup_datetime < '2025-11-19 00:00:00'
  GROUP BY z."Zone"
  ORDER BY total_amount DESC
  LIMIT 1
```
<img width="836" height="622" alt="image" src="https://github.com/user-attachments/assets/5ac44521-8172-4544-9717-6dd3a736ee90" />


---

### Question 6. Largest tip

For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

Note: it's tip , not trip. We need the name of the zone, not the ID.

#### Answer: Yorkville West
```sql
  SELECT 
  	t.lpep_pickup_datetime,
  	t.lpep_dropoff_datetime,
  	t."PULocationID",
  	t."DOLocationID",
  	t.tip_amount,
  	z."Zone" as pickupZone,
  	zo."Zone" as dropOffZone
  FROM 
  	green_taxi_data as t INNER JOIN
  	pickup_zones as z
  	ON t."PULocationID" = z."LocationID" AND 
  	z."Zone" = 'East Harlem North' AND 
  	t.lpep_pickup_datetime >= '2025-11-01 00:00:00' AND 
  	t.lpep_pickup_datetime < '2025-12-01 00:00:00'
  	INNER JOIN pickup_zones as zo
  	ON t."DOLocationID" = zo."LocationID"
  
  -- GROUP BY z."Zone"
  ORDER BY t.tip_amount DESC
  LIMIT 1
```
<img width="1278" height="733" alt="image" src="https://github.com/user-attachments/assets/70ccd6c9-a8e6-44be-8ec5-0ffac0ae3da6" />


---

### Question 7. Terraform Workflow

Which of the following sequences, respectively, describes the workflow for:

Downloading the provider plugins and setting up backend,
Generating proposed changes and auto-executing the plan
Remove all resources managed by terraform`

#### Answer: terraform init, terraform apply -auto-approve, terraform destroy

