from models import base


class OperationType(base.Model):

    __table_name__ = 'operation_type'
    opt_id = base.Column(base.Integer, primary_key=True, autoincrement=True)
    opt_name = base.Column(base.String(80), nullable=False, unique=True)

    def __init__(self, opt_name: str) -> None:
        self.opt_name = opt_name

    def __repr__(self) -> str:
        return f'<OperationType {self.opt_name}>'
