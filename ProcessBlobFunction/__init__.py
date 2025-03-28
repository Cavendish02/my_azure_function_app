import logging
import azure.functions as func
import gzip

def main(myblob: func.InputStream, outputblob: func.Out[bytes]):
    """Azure Function to compress an uploaded file using gzip and store it in the output container."""
    
    logging.info(f"🚀 Processing file: {myblob.name} ({myblob.length} bytes)")

    try:
        # قراءة محتوى الملف وضغطه
        compressed_data = gzip.compress(myblob.read())

        # تخزين البيانات المضغوطة في `outputblob`
        outputblob.set(compressed_data)

        logging.info(f"✅ File '{myblob.name}' compressed successfully! Saved as '{myblob.name}.gz'.")

    except Exception as e:
        logging.error(f"❌ ERROR processing '{myblob.name}': {str(e)}")
