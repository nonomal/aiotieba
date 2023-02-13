import sys
import time

import yarl

from .._core import HttpCore, TbCore, WsCore
from .._helper import log_exception, pack_proto_request, send_request
from ..const import APP_BASE_HOST, APP_INSECURE_SCHEME
from ..exception import TiebaServerError
from ._classdef import UserInfo_TUid
from .protobuf import GetUserByTiebaUidReqIdl_pb2, GetUserByTiebaUidResIdl_pb2

CMD = 309702


def pack_proto(core: TbCore, tieba_uid: int) -> bytes:
    req_proto = GetUserByTiebaUidReqIdl_pb2.GetUserByTiebaUidReqIdl()
    req_proto.data.common._client_version = core.main_version
    req_proto.data.tieba_uid = str(tieba_uid)

    return req_proto.SerializeToString()


def parse_body(body: bytes) -> UserInfo_TUid:
    res_proto = GetUserByTiebaUidResIdl_pb2.GetUserByTiebaUidResIdl()
    res_proto.ParseFromString(body)

    if code := res_proto.error.errorno:
        raise TiebaServerError(code, res_proto.error.errmsg)

    user_proto = res_proto.data.user
    user = UserInfo_TUid()._init(user_proto)

    return user


async def request_http(http_core: HttpCore, tieba_uid: int) -> UserInfo_TUid:
    start = time.perf_counter()
    request = pack_proto_request(
        http_core,
        yarl.URL.build(
            scheme=APP_INSECURE_SCHEME,
            host=APP_BASE_HOST,
            path="/c/u/user/getUserByTiebaUid",
            query_string=f"cmd={CMD}",
        ),
        pack_proto(http_core.core, tieba_uid),
    )

    try:
        body = await send_request(request, http_core.connector, read_bufsize=1024)
        user = parse_body(body)

    except Exception as err:
        log_exception(sys._getframe(1), err, f"tieba_uid={tieba_uid}")
        user = UserInfo_TUid()._init_null()

    end = time.perf_counter()
    print(f"http: {end-start}")

    return user


async def request_ws(ws_core: WsCore, tieba_uid: int) -> UserInfo_TUid:
    start = time.perf_counter()
    req_proto = pack_proto(ws_core.core, tieba_uid)

    try:
        response = await ws_core.send(req_proto, CMD)
        user = parse_body(await response.read())

    except Exception as err:
        log_exception(sys._getframe(1), err, f"tieba_uid={tieba_uid}")
        user = UserInfo_TUid()._init_null()

    end = time.perf_counter()
    print(f"ws: {end-start}")
    return user
