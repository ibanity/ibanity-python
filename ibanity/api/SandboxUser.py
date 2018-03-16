from collections import namedtuple


def get_list(client, params):
    uri = client.api_schema["sandbox"]["users"].replace("{sandboxUserId}", "")
    response = client.get(uri, params, None)
    return list(
        map(
            lambda user:
            __create_user_named_tuple__(user), response["data"]
        )
    )


def create(client, attributes):
    uri = client.api_schema["sandbox"]["users"].replace("{sandboxUserId}", "")
    body = {
        "data": {
            "type": "sandboxUser",
            "attributes": attributes
        }
    }
    response = client.post(uri, body, {}, None)
    return __create_user_named_tuple__(response["data"])


def delete(client, id):
    uri = client.api_schema["sandbox"]["users"] \
        .replace("{sandboxUserId}", id)
    response = client.delete(uri, {}, None)
    return __create_user_named_tuple__(response["data"])


def find(client, id):
    uri = client.api_schema["sandbox"]["users"] \
        .replace("{sandboxUserId}", id)
    response = client.get(uri, {}, None)
    return __create_user_named_tuple__(response["data"])


def __create_user_named_tuple__(user):
    return namedtuple("SandboxUser", user.keys())(**user)
