"""
Settings file for queries to social networks API
"""

INSTAGRAM_MOBILE_DATA = {
    # "main_url": "https://i.instagram.com/api/v1/",

    "main_url": "http://127.0.0.1:8000/api/v1/",

    "login": {
        "uri": "accounts/login/",
    },

    "read_msisdn_header": {
        "uri": "accounts/read_msisdn_header/"
    },

    "msisdn_header_bootstrap": {
        "uri": "accounts/msisdn_header_bootstrap/"
    },

    "token": {
        "uri": "zr/token/result/"
    },

    "contact_point_prefill": {
        "uri": "accounts/contact_point_prefill/"
    },

    "launcher_sync": {
        "uri": "launcher/sync/"
    },

    "qe_sync": {
        "uri": "qe/sync/"
    },

    "log_attribution": {
        "uri": "attribution/log_attribution/"
    },

    "get_prefill_candidates": {
        "uri": "accounts/get_prefill_candidates/"
    },

    "like": {
        "uri": "api/successlike/",
        "data": "",
        "params": ""
    },

    "flipping_type": {
        "uri": "api/flippingtape/",
        "data": "",
        "params": ""
    },

    "subscribe": {
        "uri": "api/subscribe/",
        "data": "",
        "params": ""
    }
}

INSTAGRAM_WEB_DATA = {
    "main_url": "http://127.0.0.1:8000/",

    "authorization": {
        "uri": "api/authorization/",
        "data": "",
        "params": ""
    },

    "login": {
        "uri": "api/accounts/login/ajax/",
        "data": "",
        "params": ""
    },

    "like": {
        "uri": "api/successlike/",
        "data": "",
        "params": ""
    },

    "flipping_type": {
        "uri": "api/flippingtape/",
        "data": "",
        "params": ""
    },

    "subscribe": {
        "uri": "api/subscribe/",
        "data": "",
        "params": ""
    }
}