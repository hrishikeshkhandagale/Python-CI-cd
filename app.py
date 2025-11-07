from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cab Booking</title>
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #4facfe, #00f2fe);
                color: #333;
                text-align: center;
                padding: 50px;
            }
            .container {
                background-color: white;
                max-width: 400px;
                margin: auto;
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }
            h1 {
                color: #0077ff;
                margin-bottom: 20px;
            }
            input, select, button {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border-radius: 10px;
                border: 1px solid #ccc;
                font-size: 16px;
            }
            button {
                background-color: #0077ff;
                color: white;
                border: none;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover {
                background-color: #005fd4;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚖 Cab Booking</h1>
            <form>
                <input type="text" placeholder="Enter Pickup Location" required><br>
                <input type="text" placeholder="Enter Drop Location" required><br>
                <select>
                    <option value="">Select Cab Type</option>
                    <option value="mini">Mini</option>
                    <option value="sedan">Sedan</option>
                    <option value="suv">SUV</option>
                </select><br>
                <button type="submit">Book Now</button>
            </form>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/status')
def status():
    return "✅ Flask Cab Booking API is Running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
