from peewee import CharField, Model, SqliteDatabase, IntegrityError, IntegerField, AutoField,TextField, BooleanField
from peewee_migrate import Router

database = SqliteDatabase("database.sqlite3")

router = Router(database)
router.run()

class BaseModel(Model):
    class Meta:
        database = database


class Setting(BaseModel):
    id = AutoField(primary_key=True)
    start_msg = TextField(default=None, null=True)
    start_from_user_id = IntegerField(default=None, null=True)
    start_kb = TextField(default=None, null=True)
    send_start = BooleanField(default=True, null=False)
    start_delete = TextField(default="0", null=True)

    mail_after = TextField(default=None, null=True)

    capcha_text = TextField(default="Are you human", null=True)
    capcha_btn_apply = TextField(default="Yes", null=True)
    capcha_btn_decline = TextField(default="No", null=True)
    capcha_time = IntegerField(default=30, null=True)


    # link = TextField(default="", null=True)
    def __repr__(self) -> str:
        return f"<Setting {self.id} {self.link}>"

    class Meta:
        table_name = "settings"

    # @classmethod
    # def get_many(cls, names, step=0):
    #     lst = cls.select(cls.value)
    #     lst = [cls.get_or_none(name=name,step=step) for name in names]
    #     return [item.value if item else None for item in lst]

    @classmethod
    def set_many(cls, kwargs, step=0):
        for name, value in kwargs.items():
            cls.update({cls.value:value}).where((cls.name == name) & (cls.step == step)).execute()

