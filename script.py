from flask import Flask, render_template, request

app = Flask(__name__)

# Données pour le portfolio (simples pour l'exemple)
projects = [
    {"title": "Site E-commerce", "description": "Développement d'un site complet en Django."},
    {"title": "API REST", "description": "Création d'une API RESTful pour un système de gestion d'inventaire."},
    {"title": "Analyse des données", "description": "Analyse de données financières avec Python."}
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    # Traitement du message (ex : envoyer un e-mail, stocker dans une base de données)
    return render_template("contact_confirmation.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
