QUESTIONS = [
    '\nDo you have cough?',
    '\nDo you have a sore throat?',
    '\nDo you have a fever?',
    '\nAre you noticing any unexplained excessive sweating?',
    '\nDo you have an itchy throat?',
    '\nDo you have a runny nose?',
    '\nDo you have a stuffy nose?',
    '\nDo you have a headache?',
    '\nDo you feel tired without actually exhausting yourself?'
]

THRESHOLD = {
    'Mild' : 30,
    'Severe' : 50,
    'Extreme': 75
}


def expertSystem(questions, threshold):
    score = 0

    for question in questions:
        print(question)
        ans = input('Answer y/n ')

        if(ans.lower() == 'y'):
            level = input('On a scale of 0 to 10, how severe is it? ')
            score += int(level)

    print()

    if score >= threshold['Extreme']:
        print('You are showing symptoms of having EXTREME COVID-19')
    elif score >= threshold['Severe']:
        print('Based on your answers You are showing Symptoms of SEVERE COVID-19')
    elif score >= threshold['Mild']:
        print('Based on your answers You are showing Symptoms of VERY MILD COVID-19')
    else:
        print('You are Showing NO Symptoms of COVID-19')


expertSystem(QUESTIONS, THRESHOLD)