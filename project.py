import time
import os
import pandas as pd
import matplotlib.pyplot as plt
import nltk

def bot(txt, t=0.03):
    for c in txt:
        print(c, end='', flush=True)
        time.sleep(t)
    print()

L = {
    "English": {
        "name": "Enter your name: ",
        "count": "How many student records do you want to enter?",
        "study": "Study hours: ",
        "sleep": "Sleep hours: ",
        "screen": "Screen time: ",
        "ex": "Exercise hours: ",
        "marks": "Marks obtained: ",
        "anal": "Analyzing data...",
        "res": "AI Analysis Results:",
        "s1": "Higher study hours generally improve marks.",
        "s2": "Adequate sleep has a positive impact on performance.",
        "s3": "Excessive screen time negatively affects marks.",
        "s4": "Physical activity supports better academic results.",
        "clean": "Temporary user data cleaned successfully.",
        "bye": "Thank you for using the AI system."
    },
    "French": {
        "name": "Entrez votre nom : ",
        "count": "Combien d'enregistrements voulez-vous saisir ?",
        "study": "Heures d'étude : ",
        "sleep": "Heures de sommeil : ",
        "screen": "Temps d'écran : ",
        "ex": "Heures d'exercice : ",
        "marks": "Notes obtenues : ",
        "anal": "Analyse des données...",
        "res": "Résultats de l'analyse IA :",
        "s1": "Plus d'heures d'étude améliorent généralement les notes.",
        "s2": "Un sommeil suffisant a un impact positif sur les performances.",
        "s3": "Un temps d'écran excessif nuit aux résultats.",
        "s4": "L'activité physique favorise de meilleurs résultats scolaires.",
        "clean": "Les données temporaires ont été supprimées.",
        "bye": "Merci d'utiliser le système IA."
    },
    "Spanish": {
        "name": "Ingrese su nombre: ",
        "count": "¿Cuántos registros desea ingresar?",
        "study": "Horas de estudio: ",
        "sleep": "Horas de sueño: ",
        "screen": "Tiempo de pantalla: ",
        "ex": "Horas de ejercicio: ",
        "marks": "Calificaciones obtenidas: ",
        "anal": "Analizando datos...",
        "res": "Resultados del análisis de IA:",
        "s1": "Más horas de estudio generalmente mejoran las calificaciones.",
        "s2": "Dormir adecuadamente mejora el rendimiento.",
        "s3": "Demasiado tiempo de pantalla afecta negativamente.",
        "s4": "La actividad física apoya mejores resultados académicos.",
        "clean": "Los datos temporales fueron eliminados.",
        "bye": "Gracias por usar el sistema de IA."
    },
    "German": {
        "name": "Geben Sie Ihren Namen ein: ",
        "count": "Wie viele Datensätze möchten Sie eingeben?",
        "study": "Lernstunden: ",
        "sleep": "Schlafstunden: ",
        "screen": "Bildschirmzeit: ",
        "ex": "Trainingsstunden: ",
        "marks": "Erhaltene Noten: ",
        "anal": "Daten werden analysiert...",
        "res": "KI-Analyseergebnisse:",
        "s1": "Mehr Lernstunden verbessern in der Regel die Noten.",
        "s2": "Ausreichender Schlaf wirkt sich positiv aus.",
        "s3": "Zu viel Bildschirmzeit wirkt sich negativ aus.",
        "s4": "Körperliche Aktivität unterstützt bessere Leistungen.",
        "clean": "Temporäre Daten wurden gelöscht.",
        "bye": "Danke für die Nutzung des KI-Systems."
    },
    "Russian": {
        "name": "Введите ваше имя: ",
        "count": "Сколько записей студентов вы хотите ввести?",
        "study": "Часы учёбы: ",
        "sleep": "Часы сна: ",
        "screen": "Время за экраном: ",
        "ex": "Часы упражнений: ",
        "marks": "Полученные оценки: ",
        "anal": "Анализ данных...",
        "res": "Результаты анализа ИИ:",
        "s1": "Большее количество часов учёбы обычно улучшает оценки.",
        "s2": "Достаточный сон положительно влияет на результаты.",
        "s3": "Чрезмерное время за экраном отрицательно влияет на оценки.",
        "s4": "Физическая активность способствует лучшим академическим результатам.",
        "clean": "Временные данные пользователя удалены.",
        "bye": "Спасибо за использование системы ИИ."
    }
}

print("Languages:")
for i, k in enumerate(L.keys(), 1):
    print(i, k)

ch = int(input("Select language number: "))
lang = list(L.values())[ch - 1]

name = input(lang["name"])
bot(f"{name}, AI system activated.")

n = int(input(lang["count"]))

rows = []
for i in range(n):
    bot(f"{i+1}")
    s = float(input(lang["study"]))
    sl = float(input(lang["sleep"]))
    sc = float(input(lang["screen"]))
    e = float(input(lang["ex"]))
    m = float(input(lang["marks"]))
    rows.append([s, sl, sc, e, m])

df = pd.DataFrame(rows, columns=["Study", "Sleep", "Screen", "Exercise", "Marks"])
df.to_csv("student_habits.csv", index=False)

bot(lang["anal"])

avg = df.groupby("Study")["Marks"].mean()
plt.bar(avg.index, avg.values)
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.title("Average Marks vs Study Hours")
plt.show()

plt.plot(df["Sleep"], df["Marks"], marker="o")
plt.xlabel("Sleep Hours")
plt.ylabel("Marks")
plt.title("Sleep Hours vs Marks")
plt.show()

mean = df.mean()
plt.pie(
    [mean["Study"], mean["Sleep"], mean["Screen"], mean["Exercise"]],
    labels=["Study", "Sleep", "Screen", "Exercise"],
    autopct="%1.1f%%"
)
plt.title("Average Daily Activity Distribution")
plt.show()

low = sum(df["Marks"] < 60)
mid = sum((df["Marks"] >= 60) & (df["Marks"] < 80))
high = sum(df["Marks"] >= 80)

plt.pie([low, mid, high], labels=["Low", "Medium", "High"], autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()

bot(lang["res"])
c = df.corr()["Marks"]
if c["Study"] > 0: bot(lang["s1"])
if c["Sleep"] > 0: bot(lang["s2"])
if c["Screen"] < 0: bot(lang["s3"])
if c["Exercise"] > 0: bot(lang["s4"])

os.remove("student_habits.csv")
bot(lang["clean"])
bot(lang["bye"])
