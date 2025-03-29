import logging
import azure.functions as func
import gzip

def main(myblob: func.InputStream, outputblob: func.Out[bytes]):
    logging.info(f"🚀 بدء معالجة الملف: {myblob.name} (الحجم: {myblob.length} بايت)")

    try:
        # قراءة المفحص
        raw_data = myblob.read()
        logging.info(f"📦 تم قراءة {len(raw_data)} بايت من {myblob.name}")

        # ضغط الملف
        compressed_data = gzip.compress(raw_data)
        logging.info(f"🗜️ تم ضغط الملف إلى {len(compressed_data)} بايت")

        # الحفظ في الإخراج
        outputblob.set(compressed_data)
        logging.info(f"✅ تم حفظ الملف المضغوط في output/{myblob.name}.gz")

    except Exception as e:
        logging.error(f"❌ فشل المعالجة: {str(e)}", exc_info=True)  # تسجيل التفاصيل الكاملة للخطأ