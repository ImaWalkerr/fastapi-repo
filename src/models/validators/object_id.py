from bson.objectid import ObjectId


def object_id_to_string(v) -> str:
    if isinstance(v, ObjectId):
        return str(v)
    return v
