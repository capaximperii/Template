
from Models.DbRef import db, ma, BaseModel
from Models.UsersModel import UsersSchema
from marshmallow import EXCLUDE

import enum
from marshmallow_enum import EnumField

class SubmitType(enum.Enum):
    hddsn = 'hddsn'
    hddtrial = 'hddtrial'
    csv = 'csv'

class MatchKeyPMode(enum.Enum):
    Auto = 'Auto'
    Custom = 'Custom'

class JobsModel(BaseModel):
    __tablename__ = 'Jobs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)                    # Id
    job_title = db.Column(db.String(32), nullable=False)                                # Title
    submit_type = db.Column(db.Enum(SubmitType), default=SubmitType.hddsn)              # Submit Type
    treatment_name = db.Column(db.String(32), nullable=False)                           # Treatment Name
    # Treatment list?
    control_name = db.Column(db.String(32), nullable=False)                             # Control Name
    # Control list?
    use_control_list = db.Column(db.Boolean, default=False)                             # Uses control list
    status = db.Column(db.String(32), nullable=False)                                   # Status
    analytics_level = db.Column(db.Integer, default=0)                                  # Analytics Level
    product = db.Column(db.String(32), nullable=False)                                  # Product
    target_data = db.Column(db.String(32), nullable=False)                              # Target Data
    # Match Key
    # Compare Key
    match_key_p_mode = db.Column(db.Enum(MatchKeyPMode), default=MatchKeyPMode.Auto)    # Submit Type
    # Match Key P
    # Compare Key P
    duration = db.Column(db.Integer, default=0)                                         # Time to process
    detail = db.Column(db.String(128), default='Job is queued.')
    user_email = db.Column(db.String(128), db.ForeignKey('Users.email'))
    Users = db.relationship('UsersModel', lazy='joined')

class JobsSchema(ma.ModelSchema):
    submit_type = EnumField(SubmitType, by_value=True)
    match_key_p_mode = EnumField(MatchKeyPMode, by_value=True)
    class Meta:
        unknown = EXCLUDE
        model = JobsModel
        sqla_session = db.session
        include_fk = True
        strict = True
        exclude = ('user_email',)
    # Deliberate match user table name
    Users = ma.Nested(UsersSchema, many=False, dump_only=True, exclude=('created', 'updated'))

class JobsPaginatedSchema(ma.ModelSchema):
    page = ma.Integer()
    pages = ma.Integer()
    per_page = ma.Integer()
    total = ma.Integer()
    items = ma.List(ma.Nested(JobsSchema))
    class Meta:
        unknown = EXCLUDE
        sqla_session = db.session
        include_fk = True
        strict = True
