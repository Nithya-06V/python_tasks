def create_device_config(device_id,**kwargs):
    allowed=["baud_rate","parity","timeout_ms","debug"]
    config={"device_id":device_id}
    for k,v in kwargs.items():
        if k not in allowed:
            raise ValueError("Unsupported key: "+k)
        config[k]=v
    return config
print(create_device_config("D01",baud_rate=115200,parity="N",timeout_ms=500))