from typing import List
from .network import Network
from .parser import GoogleSearchParser, SearchResult
from ...exceptions import EngineError

class GoogleEngine:
    """
    Represents the Google Custom Search Engine.

    Attributes:
        api_key (str): The API key for Google Custom Search API.
        cse_id (str): The Custom Search Engine ID.
        requestor (GoogleSearchRequest): Instance to handle the request to Google API.

    Methods:
        __aenter__(): Initializes the engine and prepares for search operations.
        __aexit__(): Cleans up after the search operation is done.
        search(query: str, **kwargs) -> List[SearchResult]: Executes the search query and returns structured results.
    """

    def __init__(self, api_key: str, cse_id: str) -> None:
        """
        Initializes the GoogleEngine object.

        Args:
            api_key (str): The API key for Google Custom Search API.
            cse_id (str): The Custom Search Engine ID.
        """
        self.api_key = api_key
        self.cse_id = cse_id
        self.requestor = Network(api_key, cse_id)

    async def __aenter__(self) -> "GoogleEngine":
        """
        Asynchronous entry point for async with context management.
        """
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Asynchronous exit point for async with context management.
        Handles any exceptions and cleanup.
        """
        pass

    async def search(self, query: str, **kwargs) -> List[SearchResult]:
        """
        Performs a search query using the Google Custom Search API.

        Args:
            query (str): The search query string.
            **kwargs: Additional parameters (num, start, etc.).

        Returns:
            List[SearchResult]: Parsed search result data.

        Raises:
            EngineError: If an error occurs while making the request.
        """
        try:
            # Send additional parameters (num, start, etc.) to the requestor
            raw_data = await self.requestor.send_request(query, **kwargs)

            # Parse the raw response using GoogleSearchParser
            parser = GoogleSearchParser(raw_data)
            parsed_results = parser.parse_results()

            return parsed_results

        except EngineError as e:
            # Here we raise a custom EngineError with specific details
            error_message = f"Search failed: {str(e)}"
            suggested_solution = "Check your API key or ensure the query format is correct."
            # Raise the EngineError with the provided message and solution
            raise EngineError(error_message, solution=suggested_solution, level="Critical")
        except Exception as e:
            # General fallback for any unexpected errors
            error_message = f"An unexpected error occurred: {str(e)}"
            suggested_solution = "Ensure the parameters are valid and try again."
            raise EngineError(error_message, solution=suggested_solution, level="Critical")