## DE-ZoomCamp > Module #2 > HomeWork

### Question 1

What is count of records for the 2024 Yellow Taxi Data?

#### Answer: [20,332,093]
<img width="809" height="236" alt="image" src="https://github.com/user-attachments/assets/be0f9718-b183-4f0b-af26-c6a201dea3cd" />



---

### Question 2. 

What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

#### Answer: [0 MB for the External Table and 155.12 MB for the Materialized Table]
<img width="768" height="334" alt="image" src="https://github.com/user-attachments/assets/aa2d6efc-29c7-43f3-9187-47a04fe29f69" />
<img width="775" height="346" alt="image" src="https://github.com/user-attachments/assets/957aba85-694c-4369-be6f-d71336022d8c" />


---

### Question 3. 

Why are the estimated number of Bytes different?

#### Answer: [BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.]


---

### Question 4. 

How many records have a fare_amount of 0?

#### Answer: [8,333]
<img width="754" height="346" alt="image" src="https://github.com/user-attachments/assets/591e84a9-cf8c-4ed0-96f6-06d8552fca28" />



---

### Question 5. 

What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy)

#### Answer: [Partition by tpep_dropoff_datetime and Cluster on VendorID]
<img width="845" height="367" alt="image" src="https://github.com/user-attachments/assets/ead911b0-050d-4819-963f-683c08d4c44c" />

<img width="587" height="446" alt="image" src="https://github.com/user-attachments/assets/9fb8fa99-7211-41e7-80d4-3d042be9881b" />


---

### Question 6. 

Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive). Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values?


#### Answer: [310.24 MB for non-partitioned table and 26.84 MB for the partitioned table]
<img width="717" height="251" alt="image" src="https://github.com/user-attachments/assets/6b4dec1e-5ef0-446c-a9a3-fae76c82642f" />
<img width="757" height="267" alt="image" src="https://github.com/user-attachments/assets/b292142b-4249-439e-9da6-49906bed8f33" />


---

### Question 7. 

Where is the data stored in the External Table you created?

#### Answer: [GCP Bucket]
<img width="802" height="448" alt="image" src="https://github.com/user-attachments/assets/3b2b8cd4-37b2-46cf-8d31-70c67f2df7f2" />


---

### Question 8. 

It is best practice in Big Query to always cluster your data:

#### Answer: 

---

### Question 9. 

Write a `SELECT count(*)` query FROM the materialized table you created. How many bytes does it estimate will be read? Why? 

#### Answer: 



