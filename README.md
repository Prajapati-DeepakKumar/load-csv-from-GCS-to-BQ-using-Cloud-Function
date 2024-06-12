# load-csv-from-GCS-to-BQ-using-Cloud-Function
This repository demonstrates the automation of data transfer from Google Cloud Storage to BigQuery using Cloud Functions.
The filename to be read from the storage bucket has the name format 'filename_(current_date).csv'.
This method calls the existing dataflow template "gs://dataflow-templates-us-central1/latest/GCS_CSV_to_BigQuery" to transfer data.
