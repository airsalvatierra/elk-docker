from elasticapm.contrib.starlette import ElasticAPM, make_apm_client

apm = make_apm_client({
      'SERVICE_NAME': 'my_python_service',
      'SECRET_TOKEN': 'supersecrettoken',
      'SERVER_URL': 'http://fleet-server:8200',
      'ENVIRONMENT': 'development'
  })

app = FastAPI()
app.add_middleware(ElasticAPM, client=apm)

apm.capture_message(f"Custom Message: {message}")

@app.get("/error")
async def throw_error():
    try:
        1 / 0
    except Exception as e:
        apm.capture_exception()
    return {"message": "Failed Successfully :)"}
