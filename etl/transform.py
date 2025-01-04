# menambahkan data ke dalam cloud yang sudah dilakukan prediksi

# mengunggah gambar ke dalam sufy storage 
import boto3
from botocore.exceptions import NoCredentialsError

# Konfigurasi kredensial dan endpoint Sufy
ACCESS_KEY = 'dTcqqo_dfll4oK0KG39THbbSPjWcmjChZWMEeVxA'
SECRET_KEY = 'vXzdVaJ1OXGcbhPNntXZxYQP_0_IF0kqQvSKRb38'
ENDPOINT_URL = 'https://mos.ap-southeast-3.sufybkt.com'

# Inisialisasi klien S3
s3 = boto3.client('s3',
                  aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY,
                  endpoint_url=ENDPOINT_URL)

def transform_data(label, data):
    # Nama bucket dan file yang akan diunggah
    bucket_name = 'grayscaleimage'
    file_name = data
    object_name = label

    
    try:
        # Unggah file ke Sufy Cloud Storage
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"Gambar {object_name} berhasil diunggah ke bucket {bucket_name}.")
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except NoCredentialsError:
        print("Kredensial tidak tersedia.")
