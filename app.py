from fastapi import FastAPI, Request
import json
import uvicorn

app = FastAPI()

@app.post("/send-sms")
async def receive_sms(request: Request):
    body = await request.json()

    # print("\n=== Full JSON Body Received ===")
    # print(json.dumps(body, indent=4))
    # print("================================\n")

    data = json.dumps(body, indent=4)

    responseData = (data)

    print("\n=== Full JSON Body Received ===")
    print(responseData)
    print("================================\n")

    return {
        "message": "Full JSON received successfully",
        "data_received": body
    }


# ⭐ This makes the file runnable with: python SMS_Text.py
if __name__ == "__main__":
    uvicorn.run("SMS_Text:app", host="0.0.0.0", port=8080, reload=True)
