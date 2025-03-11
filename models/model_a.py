import json

def preprocess_data(input_data):
    processed_data = {
        "amount": input_data["amount"],
        "currency": input_data["currency"].upper(),
        "location": input_data["location"].strip().title(),
        "timestamp": input_data["timestamp"]
    }
    return processed_data

def create_mcp_message(processed_data):
    mcp_message = {
        "context_id": "txn_12345",
        "model_name": "preprocessing_model",
        "output": processed_data,
        "metadata": {
            "data_version": "v1.0",
            "preprocessing_steps": ["uppercase_currency", "clean_location"]
        }
    }
    return mcp_message

if __name__ == "__main__":
    input_data = {
        "amount": 150.0,
        "currency": "usd",
        "location": "new york",
        "timestamp": "2023-10-01T12:34:56Z"
    }

    processed_data = preprocess_data(input_data)
    mcp_message = create_mcp_message(processed_data)

    with open("./data/mcp_message.json", "w") as f:
        json.dump(mcp_message, f, indent=2)

    print("MCP message sent to Model B:")
    print(json.dumps(mcp_message, indent=2))