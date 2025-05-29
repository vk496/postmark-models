import pytest

from postmark_models.message import MessageInbound
from tests.conftest import find_examp


@pytest.mark.parametrize("filename, content", argvalues=find_examp("examples"))
def test_examples(filename: str, content: str):
    assert MessageInbound.model_validate_json(content)
