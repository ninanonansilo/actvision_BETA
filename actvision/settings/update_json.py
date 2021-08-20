import json
from datetime import datetime
import pytz
import re
from google.cloud import storage
import os
import time

user_id = "10000000ce62qqqq"


def time_now(): # 파일이름 저장할 때 사용할 목적의 시간함수
    now = datetime.utcnow()
    UTC = pytz.timezone('UTC')
    now_utc = now.replace(tzinfo=UTC)
    KST = pytz.timezone('Asia/Seoul')
    now_kst = now_utc.astimezone(KST)
    return now_kst

def time_now_local():  # 타임테이블에서 사용할 목적의 시간함수
    now_time = time.time()
    return now_time

def save_file(setting):  # 파일 이름을 현재 시간으로 저장
    now = datetime.utcnow()
    UTC = pytz.timezone('UTC')
    now_utc = now.replace(tzinfo=UTC)
    KST = pytz.timezone('Asia/Seoul')
    now_kst = now_utc.astimezone(KST)
    print("-----------------")
    print(setting)
    with open(user_id +"/send", 'w', encoding='UTF-8-sig') as make_file:
        #json.dump(setting, make_file, indent='\t')
        make_file.write(json.dumps(setting, ensure_ascii=False, indent='\t'))
    return 0



def file_path(user_name): #디렉토리에서 가장 뒤에 파일 이름 로드
    file_list = os.listdir(user_name)
    return str(file_list[-1])

def list_blobs(bucket_name): # 버킷 -> JSON/READALL 안에 가장 최신파일의 이름을 반환
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs("ynu-mcl-act")
    list_blob = []
    i = 0
    except_str = str(user_id + "/JSON/READALL/")  # 제외시킬 문자열
    for blob in blobs:
        if blob.name.startswith(except_str):
            i += 1
            blob.name = blob.name.replace(except_str, '')
            list_blob.append(blob.name)
    print(list_blob)
    if list_blob == []: # 기존 READALL에 읽을 파일이 없다면 생성해서 올림
        init_setting = setting_json()
        now_kst = time_now()  # 현재시간 받아옴
        init_setting["Time"] = [now_kst.strftime("%Y"), now_kst.strftime("%m"), now_kst.strftime("%d"),
                          now_kst.strftime("%H"), now_kst.strftime("%M"), now_kst.strftime("%S")]
        save_file(init_setting)
        UPLOAD("ynu-mcl-act", user_id + "/send", user_id + "/JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
        print("READALL에서 읽을 파일이 없습니다. 새로 생성합니다")
        return now_kst.strftime("%Y%m%d%H%M%S")
    return list_blob[-1]


def read_json():  # 임시파일에 있는 tmep를 json으로 읽어와 반환
    with open(user_id + '/temp', 'r',encoding="utf-8-sig") as f:
        json_data = json.load(f)
    return json_data


def setting_json():  # 초기에 JSON 만듬
    setting = dict()

    setting["Pattern"] = "-1"

    Brightness_Control = dict()
    Brightness_Control["Mode"] = "0"
    Brightness_Control["Brightness"] = "20"
    Brightness_Control["CDS_Value"] = "0"
    Brightness_Control["Auto_Brightness"] = ["1", "10"]
    Brightness_Control["Auto_CDS"] = ["0", "0"]
    setting["Brightness_Control"] = Brightness_Control

    Power = dict()
    Power["Manual_ONOFF"] = "0"
    Power["Mode"] = "0"
    Power["Auto_ON"] = ["0", "0"]
    Power["Auto_OFF"] = ["0", "0"]
    setting["Power_Control"] = Power

    setting["Time"] = ["2021", "7", "21", "13", "42"," 3"]

    return setting

def value_of_request_body(bytes):
    string = bytes.decode('UTF-8-sig')
    numbers = re.sub(r'[^0-9]', '', string)

    return numbers

def value_of_request_body_list(bytes):
    string = bytes.decode('UTF-8-sig')
    w = string.split('&')
    for i in range(len(w)):
        w[i] = re.sub(r'[^0-9]', '', w[i])
    return w

def request_body_list_text(bytes):
    string = bytes.decode('UTF-8-sig')
    w = string.split('&')
    for i in range(len(w)):
        if i == 0:
            w[i] = w[i][11:]
        elif i == 8:
            w[i] = w[i][13:]
        elif i == 9:
            w[i] = w[i][15:]
        else:
            w[i] = re.sub(r'[^0-9]', '', w[i])
    return w

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'act_key.json'
storage_client = storage.Client()
def UPLOAD(bucket_name, source_file_name, destination_blob_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print("PI {} ---> GCP {} COMPLETE".format(source_file_name , destination_blob_name))

def DOWNLOAD(bucket_name, source_blob_name,destination_file_name):
    #set_bucket_public_iam(bucket_name)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    #print("GCP {} ---> PI {} COMPLETE".format(source_blob_name , destination_file_name))


def set_bucket_public_iam(bucket_name):
    """Set a public IAM Policy to bucket"""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    policy = bucket.get_iam_policy(requested_policy_version=3)
    policy.bindings.append(
        {"role": "roles/storage.objectViewer", "members": {"allUsers"}}
    )

    bucket.set_iam_policy(policy)

    print("Bucket {} is now publicly readable".format(bucket.name))


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            f = open("temp", 'w', encoding="UTF-8-sig")
            f.close()
    except :
        pass

def createDirectory_blank(directory):  # 비어있는 디렉토리 만들기 (추후 삭제)
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except :
        pass



def copy_blob(
    bucket_name, blob_name, destination_bucket_name, destination_blob_name
):
    """Copies a blob from one bucket to another with a new name."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    # destination_bucket_name = "destination-bucket-name"
    # destination_blob_name = "destination-object-name"

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )

    print(
        "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )

def delete_blob(bucket_name, blob_name):  # 객체 삭제하는 소스
    """Deletes a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    print("Blob {} deleted.".format(blob_name))

