from app import db


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)

    # one to many

    tasks = db.relationship("Task", back_populates="goal")

    def to_dict(self):
        result_dict = dict(
            # evaluates as False if null, True otherwise
            title=self.title,
            id=self.id,
        )
        return result_dict

    @classmethod
    def from_dict(cls, goal_dict):
        return cls(title=goal_dict["title"])
