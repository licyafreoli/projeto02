from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        to = "contato@melhoramigo.com"
        subject = "Mensagem do site Petshop Melhor Amigo"
        body = f"Nome: {name}\nEmail: {email}\nTelefone: {phone}\n\nMensagem:\n{message}"
        headers = f"From: {email}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = to

        try:
            with smtplib.SMTP('smtp.example.com') as server:  # Use the appropriate SMTP server and port
                server.login("your_email@example.com", "your_password")  # Replace with your email login credentials
                server.sendmail(email, to, msg.as_string())
            return "Mensagem enviada com sucesso!"
        except Exception as e:
            return f"Falha ao enviar mensagem: {str(e)}"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
