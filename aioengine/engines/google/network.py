import asyncio
from typing import Dict, Any
import aiohttp
from ...exceptions import EngineError

class Network:
    """
    Handles sending requests to the Google Custom Search API.

    Attributes:
        api_key (str): The API key for Google Custom Search API.
        cse_id (str): The Custom Search Engine ID.
        base_url (str): The base URL for the Google Custom Search API.

    Methods:
        _get_headers() -> Dict[str, str]:
            Returns the headers for the request.
        _get_params(query: str) -> Dict[str, str]:
            Returns the parameters for the request.
        send_request(query: str) -> Dict[str, Any]:
            Sends the GET request to the Google API and returns the response as JSON.
    """

    def __init__(self, api_key: str, cse_id: str) -> None:
        """
        Initializes the GoogleSearchRequest object with API key and CSE ID.

        Args:
            api_key (str): The API key for Google Custom Search API.
            cse_id (str): The Custom Search Engine ID.
        """
        self.api_key = api_key
        self.cse_id = cse_id
        self.base_url = "https://www.googleapis.com/customsearch/v1"

    def _get_headers(self) -> Dict[str, str]:
        """
        Returns the headers for the request.

        Returns:
            Dict[str, str]: A dictionary containing the headers for the request.
        """
        return {
            "User-Agent": "aioengine/1.0",
        }

    def _get_params(self, query: str, num: int = 10, start: int = 1, **extra_params) -> Dict[str, str]:
        """
        Returns the parameters for the request.

        Args:
            query (str): The query string to be searched.
            num (int, optional): The number of results to retrieve (default is 10).
            start (int, optional): The index of the first result to retrieve (default is 1).
            **extra_params: Additional query parameters.

        Returns:
            Dict[str, str]: A dictionary containing the query parameters.
        """
        params = {
            "q": query,
            "key": self.api_key,
            "cx": self.cse_id,
            "num": str(num),
            "start": str(start),
        }

        # Add extra parameters if provided
        params.update(extra_params)

        return params

    async def send_request(self, query: str, num: int = 10, start: int = 1, **extra_params) -> Dict[str, Any]:
        """
        Sends a GET request to the Google Custom Search API and returns the response.

        Args:
            query (str): The query to search for.
            num (int): The number of results to retrieve.
            start (int): The index of the first result to retrieve.
            **extra_params: Additional query parameters.

        Returns:
            Dict[str, Any]: The JSON response from the API containing search results.

        Raises:
            EngineError: If an error occurs while sending the request.
        """
        async with aiohttp.ClientSession() as session:
            try:
                # Constructing the parameters with extra ones
                params = self._get_params(query, num, start, **extra_params)

                # Sending the GET request
                async with session.get(self.base_url, headers=self._get_headers(), params=params) as response:
                    response.raise_for_status()  # Raise an error for bad status codes
                    data = await response.json()  # Parse the response as JSON

                    # Check if 'items' is in the response, otherwise handle no results
                    if 'items' not in data:
                        raise EngineError(
                            message="No results found in the response.",
                            solution="Please check the query or the API configuration.",
                            level="Warning"
                        )

                    return data

            except aiohttp.ClientError as e:
                raise EngineError(
                    message=f"Request failed: {str(e)}",
                    solution="Check network connection or try again later.",
                    level="Critical"
                )
            except asyncio.TimeoutError:
                raise EngineError(
                    message="The request timed out.",
                    solution="Please check your internet connection and try again.",
                    level="Warning"
                )
            except Exception as e:
                raise EngineError(
                    message=f"An unexpected error occurred: {str(e)}",
                    solution="If the issue persists, please check the API key or contact support.",
                    level="Critical"
                )