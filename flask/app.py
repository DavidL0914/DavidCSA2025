from flask import Flask, render_template, request, jsonify
import numpy as np
import wikipedia
import emoji

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    mean = None
    std_dev = None
    enhanced_text = None
    
    if request.method == "POST":
        option = request.form.get("option")
        
        if option == "search_wikipedia":
            query = request.form.get("query")
            try:
                summary = wikipedia.summary(query)
            except wikipedia.exceptions.DisambiguationError as e:
                summary = "Disambiguation error: " + str(e)
            except wikipedia.exceptions.PageError:
                summary = "Page not found."
        
        elif option == "calculate_statistics":
            data = request.form.get("data")
            try:
                numbers = list(map(float, data.split(',')))
                mean = np.mean(numbers)
                std_dev = np.std(numbers)
            except ValueError:
                mean = "Invalid data."
                std_dev = None
        
        elif option == "add_emoji":
            text = request.form.get("text")
            emoji_name = request.form.get("emoji_name")
            
            # Add emojis to the text
            try:
                emoji_dict = emoji.emojize(f":{emoji_name}:")
                enhanced_text = text + ' ' + emoji_dict
            except KeyError:
                enhanced_text = "No matching emoji found."
    
    return render_template("index.html", summary=summary, mean=mean, std_dev=std_dev, enhanced_text=enhanced_text)

@app.route("/suggest_emojis")
def suggest_emojis():
    emoji_name = request.args.get("emoji_name", "").lower()
    suggestions = []

    # Iterate over the emoji data and look for partial matches
    for name, data in emoji.EMOJI_DATA.items():
        if emoji_name in name.lower():
            suggestions.append((name, data['en']))

    return jsonify({"suggestions": suggestions})

if __name__ == "__main__":
    app.run(debug=True)
