# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class ExpenseCourt(gl.Contract):

    claimant: str
    respondent: str
    amount: str
    reason: str
    status: str

    def __init__(self):
        self.claimant = ""
        self.respondent = ""
        self.amount = ""
        self.reason = ""
        self.status = "No dispute"

    @gl.public.write
    def submit_dispute(
        self,
        claimant: str,
        respondent: str,
        amount: str,
        reason: str
    ) -> None:

        self.claimant = claimant
        self.respondent = respondent
        self.amount = amount
        self.reason = reason
        self.status = "Open"

    @gl.public.view
    def get_case(self) -> str:
        return (
            "Claimant: " + self.claimant +
            ", Respondent: " + self.respondent +
            ", Amount: " + self.amount +
            ", Reason: " + self.reason +
            ", Status: " + self.status
        )