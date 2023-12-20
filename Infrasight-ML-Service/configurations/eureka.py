import os
import py_eureka_client.eureka_client as eureka_client

EUREKA_HOST = os.environ.get("EUREKA_HOST", default="localhost")
EUREKA_PORT = int(os.environ.get("EUREKA_PORT", default=8010))
HOST = os.environ.get("HOST", default="0.0.0.0")
PORT = int(os.environ.get("PORT", default=8000))

def register():
    eureka_client.init(eureka_server=f"http://{EUREKA_HOST}:{EUREKA_PORT}/eureka",
                       app_name="Infrasight-ML-Service",
                       instance_host=HOST,
                       instance_port=PORT)
