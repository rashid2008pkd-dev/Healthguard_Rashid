def analyze_symptoms(age, symptoms):

    symptoms = symptoms.lower()

    emergency_keywords = [
        "chest pain",
        "difficulty breathing",
        "severe bleeding",
        "unconscious",
        "stroke"
    ]

    for keyword in emergency_keywords:
        if keyword in symptoms:
            return {
                "status": "Emergency",
                "message": "Seek emergency medical help immediately. Do not wait for an AI assessment."
            }

    if "fever" in symptoms and "headache" in symptoms:
        return {
            "status": "Attention",
            "message": "Fever and headache can have several causes. Rest, drink fluids and consult a healthcare professional, especially if symptoms worsen."
        }

    if "cough" in symptoms:
        return {
            "status": "Attention",
            "message": "Cough can have several causes. Stay hydrated and consult a healthcare professional if it persists or worsens."
        }

    return {
        "status": "General",
        "message": "Your symptoms have been recorded. Please consult a healthcare professional for proper assessment."
    }