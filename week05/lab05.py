"""
Lab 05 - Functions and Error Handling
IS4010 - AI-Enhanced Application Development
"""

users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False},
]


def calculate_average_age(users: list[dict]) -> float:
    """
    Calculate the average age of users with valid integer ages.

    Parameters
    ----------
    users : list of dict
        A list of user dictionaries.

    Returns
    -------
    float
        The average age of users with valid integer ages.
        Returns 0.0 if no valid ages are found.
    """
    try:
        if not users:
            return 0.0

        total_age = 0
        count = 0

        for user in users:
            age = user.get("age")
            if isinstance(age, int):
                total_age += age
                count += 1

        return total_age / count

    except ZeroDivisionError:
        print("error: cannot calculate average age of an empty list.")
        return 0.0

    except TypeError:
        print("error: invalid data type encountered while calculating average age.")
        return 0.0


def get_active_user_emails(users: list[dict]) -> list:
    """
    Retrieve emails of active users.

    Parameters
    ----------
    users : list of dict
        A list of user dictionaries.

    Returns
    -------
    list
        A list of emails for users where 'is_active' is True
        and an 'email' field exists. Returns an empty list if none found.
    """
    try:
        if not users:
            return []

        active_emails = []

        for user in users:
            if user.get("is_active") and user.get("email"):
                active_emails.append(user["email"])

        return active_emails

    except KeyError:
        print("error: missing expected key in user dictionary.")
        return []

    except TypeError:
        print("error: invalid data encountered while retrieving emails.")
        return []


if __name__ == "__main__":
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")
