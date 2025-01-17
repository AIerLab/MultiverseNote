from abc import ABC, abstractmethod

from app.model.dataModel import MessageModel, SessionModel
from app.model.agentModel import AgentModel

class BaseBot(ABC):

    @abstractmethod
    def ask(self,
            message: MessageModel,
            agent: AgentModel,
            session: SessionModel) -> MessageModel:
        """
        Process input message and session context to return bot output.

        Args:
            message (MessageModel): The message to be processed by the bot.
            session (SessionModel): The session context in which the message is being processed, if applicable.

        Returns:
            str: The output generated by the bot in response to the message.
        """
        pass
