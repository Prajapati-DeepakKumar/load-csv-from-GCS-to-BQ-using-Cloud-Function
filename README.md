# load-csv-from-GCS-to-BQ-using-Cloud-Function
This repository demonstrates the automation of data transfer from Google Cloud Storage to BigQuery using Cloud Functions.

The filename to be read from the storage bucket has the name format '_filename_yyyymmdd.csv_'.

This method calls the existing dataflow template "_gs://dataflow-templates-us-central1/latest/GCS_CSV_to_BigQuery_" to transfer data.

Use the Event type "*On (finalizing/creating) file in the selected bucket*" as trigger while creating the cloud function to automate data load after each successfull upload of the file into the specified bucket.
