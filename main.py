from datetime import datetime
from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   

    # Using Dataflow Services
    service = build('dataflow', 'v1b3')

    # Specify Project Name
    project = "crm-sales-opportunities"

    #Fetch current date to identify correct file with suffix '_{current_date}'
    current_date = datetime.now().strftime("%Y%m%d")

    # Dataflow template for loading CSV to BQ
    template_path = "gs://dataflow-templates-us-central1/latest/GCS_CSV_to_BigQuery"
  
    template_body = {
    "jobName": "bq-load-test",  # Provide a unique name for the job
    "parameters": {
        "inputFilePattern": f"gs://pdks_staging/sales_pipeline_{current_date}.csv",
        "schemaJSONPath": "gs://pdks_staging/metadata/bq_schema.json",
        "outputTable": "crm-sales-opportunities:crm_sales_staging.sales_pipeline",
        "bigQueryLoadingTemporaryDirectory": "gs://pdks_staging/temp/",
        "badRecordsOutputTable": "crm-sales-opportunities:crm_sales_staging.sales_pipeline_error_recs",
        "containsHeaders": "false",
        "delimiter": ",",
        "csvFormat": "Default",
        "csvFileEncoding": "UTF-8"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
