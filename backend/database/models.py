from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# Tables with Their Relationships
class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    sets = relationship("ExerciseSet", backref="exercise")

class ExerciseSet(Base):
    __tablename__ = "exercise_sets"
    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    set_number = Column(Integer)
    reps = Column(Integer)

class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    exercises = relationship("DayExercise", backref="day")
    workout_logs = relationship("WorkoutLog", backref="day")

class DayExercise(Base):
    __tablename__ = "day_exercises"
    id = Column(Integer, primary_key=True)
    day_id = Column(Integer, ForeignKey("days.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))

class Split(Base):
    __tablename__ = "splits"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    days = relationship("SplitDay", backref="split")

class SplitDay(Base):
    __tablename__ = "split_days"
    id = Column(Integer, primary_key=True)
    split_id = Column(Integer, ForeignKey("splits.id"))
    day_id = Column(Integer, ForeignKey("days.id"))
    
# Time Data
class WorkoutLog(Base):
    __tablename__ = "workout_logs"
    id = Column(Integer, primary_key=True)
    day_id = Column(Date)
    notes = Column(String)
    
    day = relationship("Day", backref="workouts_logs")