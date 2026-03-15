import os

from celery import Celery

celery_app = Celery("tasks", broker=os.getenv("REDIS_URL", "redis://localhost:6379"))


@celery_app.task
def example_task(data):
    """Placeholder task. Replace with your own background jobs."""
    return {"received": data}
