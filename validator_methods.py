def set_attributes(obj, **kwargs):
    for key, value in kwargs.items():
        if key in obj.allowed_keys:
            setattr(obj, key, value)