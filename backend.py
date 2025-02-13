from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_hair():
    img = request.files['image']
    # Send to Nyckel API:cite[8]
    response = requests.post(
        'https://nyckel.com/v1/functions/hair-types-identifier/invoke',
        headers={'Authorization': 'Bearer YOUR_TOKEN'},
        json={"data": img.url}
    )
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
    // Uncomment and modify this part to send to your Flask backend
/*
fetch('/analyze', {
    method: 'POST',
    headers: {'Content-Type': 'image/jpeg'},
    body: blob
})
.then(response => response.json())
.then(data => {
    // Show results: bald percentage, stage, etc.
    console.log("Analysis results:", data);
});
*/