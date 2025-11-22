# memory/session_service.py
class SessionService:
    def __init__(self):
        self.sessions = {}

    def create(self, session_id, data):
        self.sessions[session_id] = data

    def get(self, session_id):
        return self.sessions.get(session_id, {})
