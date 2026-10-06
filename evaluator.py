import requests
import json

# Local AI decision-engine framework
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def evaluate_deal(asset_name, listing_price, estimated_retail):
    prompt = (
        f"You are an arbitrage evaluator. An asset '{asset_name}' is listed for ${listing_price}. "
        f"Estimated retail is ${estimated_retail}. Is this a high-conviction buy? "
        f"Provide a short verdict and calculated profit margin percentage."
    )
    
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    
    print(f"Running financial logic on: {asset_name}...")
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        result = response.json()['response']
        print(f"\n[JARVIS VERDICT]:\n{result}")
    except Exception:
        print("\n[JARVIS OFFLINE]: Local AI server not detected on localhost:11434.")

if __name__ == "__main__":
    evaluate_deal("Commercial 2-Door Stainless Steel Fridge", 800, 3200)
