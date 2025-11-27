from pydantic import BaseModel
from enum import Enum

class JobStatus(str, Enum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"

class Job(BaseModel):
    id: str
    topic: str
    status: JobStatus
    
# Defines a job with an ID, topic, 
# and controlled status using Pydantic and Enum.