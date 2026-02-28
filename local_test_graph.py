from backend.graph import app

result = app.invoke({
    "query": "Explain AI"
})

print(result)