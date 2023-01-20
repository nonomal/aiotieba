from typing import Tuple

import aiohttp
import yarl

from .._core import APP_BASE_HOST, TbCore
from .._exception import TiebaServerError
from .._helper import APP_SECURE_SCHEME, pack_form_request, parse_json, send_request
from ._classdef import UserInfo_login


async def request(connector: aiohttp.TCPConnector, core: TbCore) -> bytes:

    data = [
        ('_client_version', core.main_version),
        ('bdusstoken', core._BDUSS),
    ]

    request = pack_form_request(
        core,
        yarl.URL.build(scheme=APP_SECURE_SCHEME, host=APP_BASE_HOST, path="/c/s/login"),
        data,
    )

    body = await send_request(request, connector, read_bufsize=1024)

    return body


def parse_body(body: bytes) -> Tuple[UserInfo_login, str]:
    res_json = parse_json(body)
    if code := int(res_json['error_code']):
        raise TiebaServerError(code, res_json['error_msg'])

    user_dict = res_json['user']
    user = UserInfo_login()._init(user_dict)
    tbs = res_json['anti']['tbs']

    return user, tbs
