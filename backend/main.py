from fastapi import FastAPI
from analytics import calculate_metrics
from pdf_service import generate_pdf
from database import engine
import pandas as pd
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/analyze")
def analyze(matches: list):
    metrics = calculate_metrics(matches)

    prompt = f"""
    You are an elite Valorant analyst.
    Metrics:
    K/D: {metrics['kd']}
    Win Rate: {metrics['win_rate']}
    Early Death %: {metrics['early_death_percent']}
    Fatigue Slope: {metrics['fatigue_slope']}
    Tilt Index: {metrics['tilt_index']}
    Give tactical coaching advice.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response.choices[0].message.content

    generate_pdf(summary)

    return {"metrics": metrics, "summary": summary}
