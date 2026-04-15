from flask import Flask, render_template, jsonify
import random
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# ---------------- EMAIL CONFIG ----------------
SENDER_EMAIL = "sangamithrap4@gmail.com"
APP_PASSWORD = "rfkwynlijshqgaex"  # 🔴 Gmail App Password
RECEIVER_EMAILS = ["sangamithrap4@gmail.com", "friend1@gmail.com"]  # Multiple receivers

# ---------------- EMAIL FUNCTION ----------------
def send_email_alert(gas_value):
    try:
        message = MIMEText(
            f"🚨 ALERT!\n\nIndustrial Gas Leak Detected.\nGas Value: {gas_value}"
        )
        message["Subject"] = "⚠️ Industrial Gas Leak Alert"
        message["From"] = SENDER_EMAIL
        message["To"] = ", ".join(RECEIVER_EMAILS)

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(message)
        server.quit()
        print("✅ Email alert sent successfully to:", message["To"])

    except Exception as e:
        print("❌ Email failed:", e)

# ---------------- HOME ROUTE ----------------
@app.route("/")
def home():
    return render_template("index.html")  # Dashboard

# ---------------- DATA ROUTE ----------------
@app.route("/data")
def data():
    gas_value = random.randint(100, 1000)  # Simulated sensor

    if gas_value > 600:
        status = "LEAK"
        send_email_alert(gas_value)
    else:
        status = "SAFE"

    return jsonify({
        "gas_value": gas_value,
        "status": status
    })

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)

