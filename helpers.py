import uuid


def generate_email():
    return f'sprint5_{uuid.uuid4().hex[:12]}@example.com'
