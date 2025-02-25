
# aioengine/exceptions.py

from typing import Optional
from rich.console import Console
from rich.text import Text


class EngineError(Exception):
    """
    Custom exception to handle errors with messages and suggested solutions.
    Supports colorized output based on error severity levels.

    Attributes:
        message (str): The error message.
        solution (Optional[str]): Suggested solution for the error.
        level (str): The severity level of the error ("Critical", "Warning", "Info").
    """

    def __init__(self, message: str, solution: Optional[str] = None, level: str = "Info") -> None:
        """
        Initializes the SearchEngineError exception.

        Args:
            message (str): The error message.
            solution (Optional[str], optional): Suggested solution to resolve the error. Defaults to None.
            level (str, optional): The severity level of the error. Defaults to "Info".
        """
        super().__init__(message)
        self._solution: Optional[str] = solution
        self._level: str = level
        self._console: Console = Console()

    def _get_color_for_level(self) -> str:
        """
        Returns the color associated with the error level.

        Returns:
            str: The color style to use based on error severity.
        """
        if self._level == "Critical":
            return "bold red3"
        elif self._level == "Warning":
            return "bold orange1"
        elif self._level == "Info":
            return "bold bright_blue"
        return "white"

    def __str__(self) -> str:
        """
        Formats the error message with color and solution.

        Returns:
            str: The formatted error message with the suggested solution, if provided.
        """
        color: str = self._get_color_for_level()
        error_message: Text = Text(self.args[0], style=color)
        if self._solution:
            error_message.append(f" | Suggested Solution: {self._solution}", style="italic white")
        return str(error_message)

    def display_error(self) -> None:
        """
        Displays the error message with the suggested solution using rich console.

        Uses the rich.console.Console to print the error with the appropriate style.
        """
        self._console.print(self.args[0], style=self._get_color_for_level())
        if self._solution:
            self._console.print(f"Suggested Solution: {self._solution}", style="italic white")
