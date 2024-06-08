## third-party library
from openai import AsyncOpenAI

class GPTConnector:

    async_client = AsyncOpenAI(api_key="DummyKey")

##-------------------start-of-set_api_key()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def set_api_key(api_key:str) -> None:

        """

        Sets the API key for the OpenAI clients.

        Parameters:
        api_key (string) : The API key to set.

        """

        GPTConnector.async_client = AsyncOpenAI(api_key=api_key)

    @staticmethod
    async def make_request(model:str, prompt:str) -> str:

        """

        Makes a request to the OpenAI API.

        Parameters:
        model (string) : The model to use for the request.
        prompt (string) : The prompt to use for the request.

        Returns:
        string : The response from the API.

        """

        response = await GPTConnector.async_client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content if response.choices[0].message.content else "No response"