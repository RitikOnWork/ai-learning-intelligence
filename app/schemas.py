from pydantic import BaseModel

class StudentInput(BaseModel):
    student_id: str
    course_id: str
    chapter_order: int
    time_spent: float
    score: float
