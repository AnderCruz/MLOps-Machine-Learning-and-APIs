# MLOps: Machine Learning and APIs

This project demonstrates how to **serve machine learning models via APIs** using **Flask**. It is part of an introduction to **MLOps** practices, covering model deployment, dependency management, and API development.

Developed by **Nowa Analytics**, a consultancy specialized in advanced data analytics, AI, and MLOps solutions.



## 📌 Project Overview

The project showcases:

* ✅ What **MLOps** is and why it matters
* ✅ How to build APIs with **Flask**
* ✅ How to serve **machine learning models** via APIs
* ✅ How to serialize and load models with **Pickle**
* ✅ How to manage dependencies and ensure reproducibility



## ⚙️ Features

This API provides two main functionalities:

1. **Sentiment Analysis**

   * Endpoint: `/sentimento/<frase>`
   * Translates a sentence from Portuguese to English using `GoogleTranslator`
   * Analyzes sentiment polarity using `TextBlob`

   Example request:

   ```http
   GET /sentimento/este produto é ótimo
   ```

   Example response:

   ```json
   {
     "polaridade": 0.8
   }
   ```

2. **House Price Prediction**

   * Endpoint: `/cotacao/`
   * Accepts a JSON input with house attributes (`tamanho`, `ano`, `garagem`)
   * Returns predicted price using a pre-trained **Linear Regression** model

   Example request:

   ```http
   POST /cotacao/
   Content-Type: application/json

   {
     "tamanho": 120,
     "ano": 2015,
     "garagem": 2
   }
   ```

   Example response:

   ```json
   {
     "preco": 350000.0
   }
   ```



## 📁 Project Structure

```
📦 mlops-flask-api
│
├── modelo.sav           # Serialized trained model
├── main_model.py        # Flask API code
├── requirements.txt     # Project dependencies
└── README.md            # This file
```

---

## 📊 Technologies

* **Python 3.9+**
* **Flask** → API development
* **Flask-BasicAuth** → Basic authentication
* **Scikit-learn** → Machine learning (Linear Regression model)
* **Pickle** → Model serialization
* **TextBlob** → Sentiment analysis
* **Deep Translator** → Language translation



## 🔐 Authentication

This API is protected with **Basic Authentication**.

* **Username:** `anderjcruz`
* **Password:** `Nmaster`

(You can update these credentials in `main_model.py`).



## ✅ Results

* Successfully deployed a **Machine Learning model** as an API
* Demonstrated **sentiment analysis service** with translation
* Implemented a **house price prediction service**
* Applied **MLOps best practices**: model serialization, dependency control, and service deployment



## 🏢 About Nowa Analytics

**Nowa Analytics** is a consultancy specialized in **data analytics, machine learning, and MLOps**. We help organizations transform their models into **production-ready solutions** with APIs, automation, and cloud deployment.

📍 São Paulo, Madrid, and London
🌐 [nowaanalytics.com](http://nowaanalytics.com) *(replace with real link if available)*



## 📬 Contact

For more information or consulting services:

* 📧 [contact@nowaanalytics.com](mailto:contact@nowaanalytics.com)
* 💼 LinkedIn: [Nowa Analytics](https://linkedin.com/company/nowaanalytics)


