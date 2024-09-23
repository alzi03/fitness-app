import asyncio
from datetime import date, timedelta, datetime
import json
import os


from sqlalchemy import select, delete, insert
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Exercise, Day, Split, ExerciseSet, DayExercise, SplitDay, WorkoutLog


# Exercise Functions

async def create_exercise(session: AsyncSession, name: str):
    new_exercise = Exercise(name=name)
    session.add(new_exercise)
    await session.commit()
    return new_exercise

async def read_exercises(session: AsyncSession):
    return await session.execute(select(Exercise)).scalars().all()

async def update_exercise(session: AsyncSession, exercise_id: int, name: str):
    exercise_to_update = await session.execute(select(Exercise).where(Exercise.id == exercise_id)).scalar()
    if exercise_to_update:
        exercise_to_update.name = name
        await session.commit()
        return exercise_to_update
    else:
        return None

async def delete_exercise(session: AsyncSession, exercise_id: int):
    exercise_to_delete = await session.execute(select(Exercise).where(Exercise.id == exercise_id)).scalar()
    if exercise_to_delete:
        await session.delete(exercise_to_delete)
        await session.commit()
        return True
    else:
        return False
    

# Day Functions

async def create_day(session: AsyncSession, name: str):
    new_day = Day(name=name)
    session.add(new_day)
    await session.commit()
    return new_day

async def read_days(session: AsyncSession):
    return await session.execute(select(Day)).scalars().all()

async def update_day(session: AsyncSession, day_id: int, name: str):
    day_to_update = await session.execute(select(Day).where(Day.id == day_id)).scalar()
    if day_to_update:
        day_to_update.name = name
        await session.commit()
        return day_to_update
    else:
        return None

async def delete_day(session: AsyncSession, day_id: int):
    day_to_delete = await session.execute(select(Day).where(Day.id == day_id)).scalar()
    if day_to_delete:
        await session.delete(day_to_delete)
        await session.commit()
        return True
    else:
        return False


# Split Functions

async def create_split(session: AsyncSession, name: str):
    new_split = Split(name=name)
    session.add(new_split)
    await session.commit()
    return new_split

async def read_splits(session: AsyncSession):
    return await session.execute(select(Split)).scalars().all()

async def update_split(session: AsyncSession, split_id: int, name: str):
    split_to_update = await session.execute(select(Split).where(Split.id == split_id)).scalar()
    if split_to_update:
        split_to_update.name = name
        await session.commit()
        return split_to_update
    else:
        return None

async def delete_split(session: AsyncSession, split_id: int):
    split_to_delete = await session.execute(select(Split).where(Split.id == split_id)).scalar()
    if split_to_delete:
        await session.delete(split_to_delete)
        await session.commit()
        return True
    else:
        return False


# Exercise-Sets Relationship Functions

async def create_exercise_set(session: AsyncSession, exercise_id: int, set_number: int, reps: int):
    new_exercise_set = ExerciseSet(exercise_id=exercise_id, set_number=set_number, reps=reps)
    session.add(new_exercise_set)
    await session.commit()
    return new_exercise_set

async def read_exercise_sets(session: AsyncSession, exercise_id: int):
    return await session.execute(select(ExerciseSet).where(ExerciseSet.exercise_id == exercise_id)).scalars().all()

async def update_exercise_set(session: AsyncSession, exercise_id: int, set_number: int):
    exercise_set = await session.execute(select(ExerciseSet).where(ExerciseSet.exercise_id == exercise_id and ExerciseSet.set_number == set_number)).scalar()
    if exercise_set:
        
        await session.commit()
        return exercise_set
    else:
        return None

async def delete_exercise_set(session: AsyncSession, exercise_id: int, set_number: int):
    exercise_set = await session.execute(select(ExerciseSet).where(ExerciseSet.exercise_id == exercise_id and ExerciseSet.set_number == set_number)).scalar()
    if exercise_set:
        await session.delete(exercise_set)
        await session.commit()
        return True
    else:
        return False


# Day-Exercise Relationship Functions
async def create_day_exercise(session: AsyncSession, day_id: int, exercise_id: int):
    new_day_exercise = DayExercise(day_id=day_id, exercise_id=exercise_id)
    session.add(new_day_exercise)
    await session.commit()
    return new_day_exercise

async def read_day_exercises(session: AsyncSession, day_id: int):
    return await session.execute(select(DayExercise).where(DayExercise.day_id == day_id)).scalars().all()

async def update_day_exercise(session: AsyncSession, day_id: int, exercise_id: int):
    day_exercise = await session.execute(select(DayExercise).where(DayExercise.day_id == day_id and DayExercise.exercise_id == exercise_id)).scalar()
    if day_exercise:
        # Update the day_exercise object here
        await session.commit()
        return day_exercise
    else:
        return None

async def delete_day_exercise(session: AsyncSession, day_id: int, exercise_id: int):
    day_exercise = await session.execute(select(DayExercise).where(DayExercise.day_id == day_id and DayExercise.exercise_id == exercise_id)).scalar()
    if day_exercise:
        await session.delete(day_exercise)
        await session.commit()
        return True
    else:
        return False
    
# Split-Day Relationship Functions
async def create_split_day(session: AsyncSession, split_id: int, day_id: int):
    new_split_day = SplitDay(split_id=split_id, day_id=day_id)
    session.add(new_split_day)
    await session.commit()
    return new_split_day

async def read_split_days(session: AsyncSession, split_id: int):
    return await session.execute(select(SplitDay).where(SplitDay.split_id == split_id)).scalars().all()

async def update_split_day(session: AsyncSession, split_id: int, day_id: int):
    split_day = await session.execute(select(SplitDay).where(SplitDay.split_id == split_id and SplitDay.day_id == day_id)).scalar()
    if split_day:
        # Update the split_day object here
        await session.commit()
        return split_day
    else:
        return None

async def delete_split_day(session: AsyncSession, split_id: int, day_id: int):
    split_day = await session.execute(select(SplitDay).where(SplitDay.split_id == split_id and SplitDay.day_id == day_id)).scalar()
    if split_day:
        await session.delete(split_day)
        await session.commit()
        return True
    else:
        return False
    
# Workout Log
async def create_workout_log(session: AsyncSession, day_id: int, date: date, notes: str):
    new_workout_log = WorkoutLog(day_id=day_id, date=date, notes=notes)
    session.add(new_workout_log)
    await session.commit()
    return new_workout_log

async def read_workout_logs(session: AsyncSession, day_id: int):
    return await session.execute(select(WorkoutLog).where(WorkoutLog.day_id == day_id)).scalars().all()