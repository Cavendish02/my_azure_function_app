import azure.functions as func
import logging

app = func.FunctionApp()

@app.function_name(name="ProcessBlobFunction")
@app.blob_trigger(arg_name="myblob", path="samples-workitems/{name}", connection="AzureWebJobsStorage")
def ProcessBlobFunction(myblob: func.InputStream):
    logging.info(f"Processing blob: {myblob.name}")
