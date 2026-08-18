import os
from flask import Flask, jsonify  

app = Flask(__name__)

# Fetch the connection string from your Linux environment
DATABASE_URL = os.environ.get("DATABASE_URL")

@app.route('/select', methods=['GET'])
def run_select_query():  
    # Check if the environment variable actually exists before connecting
    if not DATABASE_URL:
        return jsonify({"status": "error", "message": "DATABASE_URL environment variable is missing"}), 500

    try:
        import psycopg
        # Connect using the exact variable name defined above
        with psycopg.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                result = cur.fetchone()
                print("respond was successful")

                # Return a valid web response back to the client
                return jsonify({
                    "status": "success",
                    "message": "Response was successful",
                    "db_returned": result[0]  # Extracts the clean number '1' out of the tuple
                }), 200

    except Exception as e:
        # Catch network or database credential errors safely
        return jsonify({"status": "error", "message": f"Database connection failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
