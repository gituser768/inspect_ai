import argparse
import asyncio
from typing import Literal

from jsonrpcserver import async_dispatch
from pydantic import BaseModel

from inspect_multi_tool import SERVER_PORT
from inspect_multi_tool._util._common_types import JSONRPCResponseJSON
from inspect_multi_tool._util._json_rpc_helpers import json_rpc_http_call
from inspect_multi_tool._util._load_tools import load_tools

_SERVER_URL = f"http://localhost:{SERVER_PORT}/"


class JSONRPCRequest(BaseModel):
    jsonrpc: Literal["2.0"]
    method: str
    id: int | float | str
    params: list[object] | dict[str, object] | None = None


def main() -> None:
    asyncio.run(async_main())


# Example/testing requests
# {"jsonrpc": "2.0", "method": "editor", "id": 666, "params": {"command": "view", "path": "/tmp"}}
# {"jsonrpc": "2.0", "method": "bash", "id": 666, "params": {"command": "ls ~/Downloads"}}
async def async_main() -> None:
    in_process_tools = load_tools("inspect_multi_tool._in_process_tools")

    args: argparse.Namespace = parser.parse_args()

    validated_request = JSONRPCRequest.model_validate_json(args.request)
    tool_name = validated_request.method
    assert isinstance(tool_name, str)

    print(
        await (
            _dispatch_local_method
            if tool_name in in_process_tools
            else _dispatch_remote_method
        )(args.request)
    )


parser = argparse.ArgumentParser(prog="multi_tool_client")
parser.add_argument(
    "request", type=str, help="A JSON string representing the JSON RPC 2.0 request"
)


async def _dispatch_local_method(request_json_str: str) -> JSONRPCResponseJSON:
    return JSONRPCResponseJSON(await async_dispatch(request_json_str))


async def _dispatch_remote_method(request_json_str: str) -> JSONRPCResponseJSON:
    return await json_rpc_http_call(_SERVER_URL, request_json_str)


if __name__ == "__main__":
    main()
