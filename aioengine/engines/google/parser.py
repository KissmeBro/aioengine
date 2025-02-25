from typing import List, Dict
from pydantic import BaseModel
from ...exceptions import EngineError

class SearchResult(BaseModel):
    """
    Represents a single search result from the Google Custom Search API.

    Attributes:
        title (str): The title of the search result.
        link (str): The link to the search result.
        snippet (str): A brief snippet from the result page.
        formatted_date (str): The publication date or 'Unknown' if not found.
    """
    title: str
    link: str
    snippet: str
    formatted_date: str = "Unknown"


class GoogleSearchResults(BaseModel):
    """
    Represents the raw response from the Google Custom Search API.

    Attributes:
        items (List[SearchResult]): A list of search results.
        searchInformation (dict): Information about the search, such as total results.
    """
    items: List[SearchResult]
    searchInformation: dict

    def get_total_results(self) -> int:
        """
        Returns the total number of search results found.

        Returns:
            int: The total number of results.
        """
        return self.searchInformation.get("totalResults", 0)


class GoogleSearchParser:
    """
    A class to parse and transform raw Google Custom Search API results into
    a more user-friendly format.

    Attributes:
        results (Dict): The raw JSON response from the Google Custom Search API.

    Methods:
        parse_results() -> List[Dict]:
            Parses the raw search results and returns a list of dictionaries
            with formatted result data.
    """

    def __init__(self, results: Dict) -> None:
        """
        Initializes the parser with raw Google Custom Search results.

        Args:
            results (Dict): The raw JSON response from the API.
        """
        self.results = results

    def parse_results(self) -> List[SearchResult]:
        """
        Parses the raw search results into a more user-friendly format.

        Returns:
            List[SearchResult]: A list of SearchResult objects containing the parsed search result data.
        """
        try:
            google_results = GoogleSearchResults.parse_obj(self.results)
            return google_results.items
        except Exception as e:
            # Raise custom EngineError with detailed message and suggested solution
            raise EngineError(
                f"Failed to parse search results: {str(e)}", 
                solution="Ensure the raw data is in the correct format.",
                level="Critical"
            )

    def get_total_results(self) -> int:
        """
        Returns the total number of search results found.

        Returns:
            int: The total number of results.
        """
        try:
            google_results = GoogleSearchResults.parse_obj(self.results)
            return google_results.get_total_results()
        except Exception as e:
            # Raise custom EngineError with detailed message and suggested solution
            raise EngineError(
                f"Failed to extract total results: {str(e)}", 
                solution="Check if 'searchInformation' contains 'totalResults'.",
                level="Critical"
            )