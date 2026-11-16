import ollama
import datetime

MODELS = ["gemma4", "llama3.2", "altri modelli da mettere"]

class Message:
    content: str
    timestamp: datetime.datetime

    def __init__(self, content: str, timestamp: datetime.datetime | None = None) -> None:
        self.content = content
        self.timestamp = timestamp or datetime.datetime.now()


    def __json__(self) -> dict:
        return self.__dict__

class LLM:
    model: str
    system_prompt: str | None

    def __init__(self, model: str = "gemma4", system_prompt: str | None = None) -> None:
        self.model = model
        self.system_prompt = system_prompt

        try:
            ollama.show(model=self.model)
            print(f"Model {self.model} Loaded Successfully!")
        except ollama.ResponseError as error:
            print(f"Model Not Available: {error}")
            return


    #Long ass instruction
    async def get_answer(self, question: Message) -> Message:
        response = await ollama.AsyncClient().chat(model=self.model, messages=([{"role": "system","content": self.system_prompt}] if self.system_prompt else []) + [{"role": "user","content": question.content}])
        return Message(response["message"]["content"])



