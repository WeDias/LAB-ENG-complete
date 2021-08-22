from datetime import datetime
from models import base


class LogModel(base.Model):

    __tablename__ = 'log'
    log_id = base.Column(base.Integer, primary_key=True, autoincrement=True)
    log_date = base.Column(base.DateTime, nullable=False)
    log_args_op = base.Column(base.String(80), nullable=False)
    log_opt_id = base.Column(base.Integer, base.ForeignKey('operation_type.opt_id'), nullable=False)

    def __init__(self, log_date: datetime, log_args_op: str, log_opt_id: int) -> None:
        self.log_date = log_date
        self.log_args_op = log_args_op
        self.log_opt_id = log_opt_id

    def __repr__(self) -> str:
        return f'<LogModel {self.log_id}>'
