from collections import namedtuple
from ibanity import Ibanity
import requests
from ibanity.Flatten import flatten_json


def create(authorization_code, code_verifier, redirect_uri, client_id, authorization):
    uri = Ibanity.client.api_schema_ponto["oauth2"]["token"] \

    body = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code_verifier": code_verifier
        }
    response = Ibanity.client.post(uri, body, {}, authorization)
    return flatten_json(response)


def create_from_refresh_token(refresh_token, client_id, authorization):
    uri = Ibanity.client.api_schema_ponto["oauth2"]["token"] \

    body = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        }
    response = Ibanity.client.post(uri, body, {}, authorization)
    return flatten_json(response)
