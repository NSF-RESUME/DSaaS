# TODO: Move it to a different folder so its easily sharable

import dill
import codecs
from osprey.server.lib.error import ServiceError, SERIALIZE_ERR, DESERIALIZE_ERR

"""

    This module helps serializing, and deserializing functions for creating modifiers/verifiers in the client side


    They can be pickled, and sent as part of the request body

"""


def serialize(obj) -> str:
    try:
        return codecs.encode(dill.dumps(obj), "base64").decode()
    except Exception:
        raise ServiceError(SERIALIZE_ERR, "Cannot serialize the function")

def deserialize(obj: str):
    try:
        return dill.loads(codecs.decode(obj.encode(), "base64"))
    except Exception:
        raise ServiceError(DESERIALIZE_ERR, "Cannot deserialize the function")