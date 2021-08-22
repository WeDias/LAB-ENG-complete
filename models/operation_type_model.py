from models import base


class OperationTypeModel(base.Model):

    __tablename__ = 'operation_type'
    opt_id = base.Column(base.Integer, primary_key=True, autoincrement=True)
    opt_name = base.Column(base.String(80), nullable=False, unique=True)

    def __init__(self, opt_name: str) -> None:
        self.opt_name = opt_name

    def __repr__(self) -> str:
        return f'<OperationTypeModel {self.opt_name}>'
