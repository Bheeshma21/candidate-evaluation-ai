from datetime import datetime

from schemas.workflow_state import AuditEntry


class AuditLogger:

    @staticmethod
    def log(
        state,
        step: str,
        message: str
    ):

        state.audit_log.append(
            AuditEntry(
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                step=step,
                message=message
            )
        )

        return state