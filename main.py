from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "OAuth2 Test: Visit <a href='/callback?code=demo_code'>Click Here</a> to test."

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "❌ No authorization code found!", 400

    print(f"✅ Captured OAuth2 Code: {code}")
    return f"✅ OAuth2 Code Captured: {code}"

if __name__ == "__main__":
    import os

    # Ensure Flask app runs on 0.0.0.0 to allow external connections
    host = "0.0.0.0"
    # Get the Pterodactyl-assigned port or use 5000 as default
    port = int(os.getenv("PORT", 5000))

    # Run Flask app with added configurations for production use
    app.run(host="57.129.29.116", port=port, debug=False)
