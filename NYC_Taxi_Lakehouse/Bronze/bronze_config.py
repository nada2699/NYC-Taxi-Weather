CATALOG = "nyc_taxi_project"
SCHEMA = "bronze"
VOLUME = "src_files"

BASE_PATH = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}"



INGESTION_CONFIG={
    "tlc_taxi_lookup":{
        "source":"tlc",
        "path": f"{BASE_PATH}/taxi_zone_lookup.csv",
        "file_type": "csv",
        "table":f"{CATALOG}.{SCHEMA}.tlc_taxi_lkp"        
    },
    "yello_tripdata":{
        "source":"tlc",
        "path": f"{BASE_PATH}/yellow_tripdata_2025-01.parquet",
        "file_type": "parquet",
        "table":f"{CATALOG}.{SCHEMA}.yellow_tripdata_202501"
    },
    "weather":{
        "source":"meteo_api",
        "path":f"{BASE_PATH}/open_meteo/parquet",
        "table":f"{CATALOG}.{SCHEMA}.weather_bronze",
        "state_table": f"{CATALOG}.{SCHEMA}.weather_ingestion_state"
    }

}


LOAD_CONFIG= {
        "raw_path":f"{BASE_PATH}/open_meteo/raw",
        "parquet_path":f"{BASE_PATH}/open_meteo/parquet"
    }

