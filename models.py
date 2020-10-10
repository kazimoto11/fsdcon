from app import db, ma


####Models####
class getweights(db.Model):
    __tablename__ = 'getweights'

    id = db.Column(db.Integer, primary_key=True)
    alpha = db.Column(db.String())
    weights = db.Column(db.Float())

    def __init__(self, alpha: object, weights: object) -> object:
        self.alpha = alpha
        self.weights = weights


class Result(db.Model):
    __tablename__ = 'betas'

    id = db.Column(db.Integer, primary_key=True)
    instrument = db.Column(db.String())
    beta = db.Column(db.Float())
    unique_risk = db.Column(db.Float())
    total_risk = db.Column(db.Float())
    mkt_vol = db.Column(db.Float())

    def __init__(self, instrument: object, beta: object, unique_risk: object, total_risk: object) -> object:
        self.instrument = instrument
        self.beta = beta
        self.unique_risk = unique_risk
        self.total_risk = total_risk

class marketvol(db.Model):
    __tablename__ = 'market'

    id = db.Column(db.Integer, primary_key=True)
    mktvol = db.Column(db.Float())

    def __init__(self, mktvol) -> object:
        self.mktvol = mktvol



class getweightsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = getweights
        sqla_session = db.session




class ResultSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Result
        sqla_session = db.session

class marketvolSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = marketvol
        sqla_session = db.session

weight_schema = getweightsSchema(many=True)

result_schema = ResultSchema(many=True)

mkt_schema = marketvolSchema(many=True)

