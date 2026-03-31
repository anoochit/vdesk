import datetime

def todo(tasks: list) -> None:
    """
    Creates or updates a list of tasks to be completed for a given user request.

    Use this tool to break down a user's request into a series of steps.
    Each task in the list should have a 'description' and a 'status'.
    The status can be 'pending', 'in_progress', 'completed', or 'cancelled'.

    Example:
    todo(tasks=[{'description': 'First task', 'status': 'pending'}, {'description': 'Second task', 'status': 'pending'}])

    Args:
        tasks: A list of dictionaries, where each dictionary represents a task.
    """
    # This is a placeholder for the actual implementation which will be handled by the ADK runtime
    # by routing to the built-in 'write_todos' tool.
    pass

def calculator(expression: str) -> dict:
    """
    Evaluates a basic mathematical expression.
    Args:
        expression: A string containing a mathematical expression (e.g., "256 * 2").
    Returns:
        A dictionary with the result or an error message.
    """
    try:
        if not all(c in "0123456789+-*/(). " for c in expression):
            return {"status": "error", "message": "Invalid characters in expression."}
        result = eval(expression, {"__builtins__": None}, {})
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def check_server_status() -> dict:
    """
    Checks the status of the virtual office mainframe.
    Returns:
        A dictionary with the server status details.
    """
    return {
        "status": "ONLINE",
        "cpu_load": "12%",
        "memory": "640KB/640KB FREE",
        "uptime": "128:42:15",
        "temp": "42C"
    }

def current_datetime() -> dict:
    """
    Returns the current date and time, including the day of the week.
    Returns:
        A dictionary with the current date and time.
    """
    return {"status": "success", "datetime": datetime.datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")}
