"""Output parser."""
from llama_index.types import BaseOutputParser

from llama_index.core.query_pipeline.query_component import QueryComponent, validate_and_convert_stringable, InputKeys, OutputKeys
from typing import Dict, Any


# TODO: can this just be the base class

class QueryOutputParser(BaseOutputParser, QueryComponent):
    """Query output parser."""

    def __init__(self) -> None:
        """Init params."""

    def _validate_component_inputs(self, input: Dict[str, Any]) -> Dict[str, Any]:
        """Validate component inputs during run_component."""
        return input

    def _run_component(self, **kwargs: Any) -> Any:
        """Run component."""
        # TODO: support only complete for now
        # non-trivial to figure how to support chat/complete/etc.
        output = self.parse(kwargs["input"])
        return {"output": output}

    def input_keys(self) -> InputKeys:
        """Input keys."""
        # TODO: support only complete for now
        return InputKeys.from_keys({"input"})

    def output_keys(self) -> OutputKeys:
        """Output keys."""
        return OutputKeys.from_keys({"output"})