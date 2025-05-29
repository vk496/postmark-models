from datetime import datetime
from typing import Literal

from pydantic import (
    Base64Bytes,
    BaseModel,
    EmailStr,
    Field,
    computed_field,
    field_validator,
)

# NOTE: When Using EmailStr, we get a "The email address is too long before the @-sign" issue. Who is wrong? Well... TODO


class Headers(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class FullBase(BaseModel):
    email: str = Field(alias="Email")  # TODO: EmailStr
    name: str = Field(alias="Name")
    mailbox_hash: str | None = Field(None, alias="MailboxHash")


class Attachment(BaseModel):
    name: str = Field(alias="Name")
    content: Base64Bytes = Field(alias="Content")
    content_type: str = Field(alias="ContentType")
    content_length: int = Field(alias="ContentLength", gt=0)
    content_id: str | None = Field(None, alias="ContentID")


class Message(
    BaseModel,
    serialize_by_alias=True,
):
    from_name: str = Field(alias="FromName")
    from_full: FullBase = Field(alias="FromFull")

    to_full: list[FullBase] = Field(alias="ToFull")

    cc_full: list[FullBase] = Field(alias="CcFull")

    bcc_full: list[FullBase] = Field(alias="BccFull")

    original_recipient: str = Field(alias="OriginalRecipient")
    reply_to: str = Field(alias="ReplyTo")  # TODO: EmailStr
    subject: str = Field(alias="Subject")
    message_id: str = Field(alias="MessageID")
    date: datetime = Field(alias="Date")
    mailbox_hash: str = Field(alias="MailboxHash")
    text_body: str = Field(alias="TextBody")
    html_body: str = Field(alias="HtmlBody")
    stripped_text_reply: str = Field(alias="StrippedTextReply")
    tag: str = Field(alias="Tag")
    headers: list[Headers] = Field(alias="Headers")
    attachments: list[Attachment] = Field(alias="Attachments")

    @computed_field
    @property
    def is_spam(self) -> bool | None:
        for header in self.headers:
            if header.name == "X-Spam-Status":
                return header.value == "Yes"

        return None  # No spam status available

    @field_validator("date", mode="before")
    @classmethod
    def parse_multiple_formats(cls, value):
        if isinstance(value, datetime):
            return value  # If already a datetime object, return it

        formats = ["%a, %d %b %Y %H:%M:%S %z"]  # rfc2822
        for fmt in formats:
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue

        return value  # Pass to Pydantic to try other types like ISO

    def model_dump_json(self, *args, **kwargs) -> str:
        return super().model_dump_json(*args, exclude_unset=True, **kwargs)


class MessageInbound(Message):
    message_stream: Literal["inbound"] = Field(alias="MessageStream")

    from_: EmailStr | None = Field(None, alias="From")
    to_: str | None = Field(None, alias="To")  # TODO: EmailStr
    cc_: str | None = Field(None, alias="Cc")
    bcc_: str | None = Field(None, alias="Bcc")
