# Resilient Workflow Decision System

This project implements a configurable decision workflow system that processes requests using rule-based evaluation.

## Features

- Workflow engine
- Rule engine
- Configurable YAML workflows
- REST API
- Audit logging
- Retry handling
- Idempotency
- State tracking

## Installation

pip install -r requirements.txt

## Run

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs
