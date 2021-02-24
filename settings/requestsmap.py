"""
Settings file for queries to social networks API
"""

INSTAGRAM_MOBILE_DATA = {
    # 'https://i.instagram.com/api/v1/'

    "main_url": "http://127.0.0.1:8000/api/v1/",

    "authorization": {
        "uri": "authorization/",
        "data": "",
        "params": ""
    },

    "login": {
        "uri": "accounts/login/",
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