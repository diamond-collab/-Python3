import enum
import random
from abc import ABC, abstractmethod
from dataclasses import dataclass


class MessageType(enum.Enum):
    TELEGRAM = enum.auto()
    MATTERMOST = enum.auto()
    SLACK = enum.auto()


@dataclass
class JsonMessage:
    message_type: MessageType
    payload: str


@dataclass
class ParsedMessage:
    """There is no need to describe anything here."""

    @staticmethod
    def parse_msg(text: str) -> str:
        return text


class BaseParser(ABC):
    @abstractmethod
    def parse(self, message: JsonMessage) -> str:
        pass


class TelegramParser(BaseParser):
    def parse(self, message: JsonMessage) -> str:
        return message.payload


class MattermostParser(BaseParser):
    def parse(self, message: JsonMessage) -> str:
        return message.payload


class SlackParser(BaseParser):
    def parse(self, message: JsonMessage) -> str:
        return message.payload


class FactoryMSG:
    @staticmethod
    def get_parser(message_type: MessageType) -> BaseParser:
        if message_type == MessageType.TELEGRAM:
            return TelegramParser()
        elif message_type == MessageType.MATTERMOST:
            return MattermostParser()
        elif message_type == MessageType.SLACK:
            return SlackParser()

        raise ValueError(f"Unknown message type: {message_type}")


# Demo data
json_msg_tg = JsonMessage(
    message_type=MessageType.TELEGRAM,
    payload='telegram message'
)

json_msg_mattermost = JsonMessage(
    message_type=MessageType.MATTERMOST,
    payload='mattermost message'
)

json_msg_slack = JsonMessage(
    message_type=MessageType.SLACK,
    payload='slack message'
)

messages_type: list[JsonMessage] = [
    json_msg_tg,
    json_msg_mattermost,
    json_msg_slack,
]

# Parser selection demo
random_msg: JsonMessage = random.choice(messages_type)

parser: BaseParser = FactoryMSG.get_parser(message_type=random_msg.message_type)
text = parser.parse(message=random_msg)

print(ParsedMessage.parse_msg(text=text))
