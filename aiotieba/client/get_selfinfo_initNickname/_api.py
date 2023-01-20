import aiohttp
import yarl

from .._core import APP_BASE_HOST, TbCore
from .._exception import TiebaServerError
from .._helper import APP_SECURE_SCHEME, pack_form_request, parse_json, send_request
from ._classdef import UserInfo_selfinit


async def request(connector: aiohttp.TCPConnector, core: TbCore) -> bytes:

    data = [
        ('BDUSS', core._BDUSS),
        ('_client_version', core.main_version),
    ]

    request = pack_form_request(
        core,
        yarl.URL.build(scheme=APP_SECURE_SCHEME, host=APP_BASE_HOST, path="/c/s/initNickname"),
        data,
    )

    body = await send_request(request, connector, read_bufsize=1024)

    return body


def parse_body(body: bytes) -> UserInfo_selfinit:
    res_json = parse_json(body)
    if code := int(res_json['error_code']):
        raise TiebaServerError(code, res_json['error_msg'])

    user_dict = res_json['user_info']
    user = UserInfo_selfinit()._init(user_dict)

    return user
