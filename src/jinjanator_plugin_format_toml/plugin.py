import tomllib

from collections.abc import Iterable, Mapping
from typing import Any

from jinjanator_plugins import (
    Formats,
    plugin_formats_hook,
)


class TOMLFormat:
    name = "toml"
    suffixes: Iterable[str] | None = ".toml"
    option_names: Iterable[str] | None = None

    def __init__(self, options: Iterable[str] | None) -> None:
        pass

    def parse(
        self,
        data_string: str,
    ) -> Mapping[str, Any]:
        return tomllib.loads(data_string)


@plugin_formats_hook
def plugin_formats() -> Formats:
    return {TOMLFormat.name: TOMLFormat}
