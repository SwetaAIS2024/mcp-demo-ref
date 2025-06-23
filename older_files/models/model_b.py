import json

def predict_fraud(processed_data):
    if processed_data["amount"] > 100 and processed_data["location"] != "California":
        return True
    return False

if __name__ == "__main__":
    with open("./data/mcp_message.json", "r") as f:
        mcp_message = json.load(f)

    print("MCP message received from Model A:")
    print(json.dumps(mcp_message, indent=2))

    processed_data = mcp_message["output"]
    is_fraud = predict_fraud(processed_data)

    result = {
        "context_id": mcp_message["context_id"],
        "model_name": "fraud_prediction_model",
        "output": {
            "is_fraud": is_fraud
        },
        "metadata": {
            "model_version": "v1.0",
            "prediction_threshold": 100.0
        }
    }

    print("\nPrediction Result:")
    print(json.dumps(result, indent=2))