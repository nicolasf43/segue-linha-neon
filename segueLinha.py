def control(left_sensor, right_sensor, speed):
    
    freio = 0
    error = right_sensor - left_sensor
    velocidade = 3500
    
    if (right_sensor == 0) or (left_sensor == 0):
            freio = 1000
            velocidade = 1500

    return {
        'engineTorque': velocidade,
        'brakingTorque': freio,
        'steeringAngle': 0.5*error,
        'log': [
            { 'name': 'Speed', 'value': speed, 'min': 0, 'max': 200 },
            { 'name': 'Left_sensor', 'value': left_sensor, 'min': 0, 'max': 1 },
            { 'name': 'Right_sensor', 'value': right_sensor, 'min': 0, 'max': 1 }
        ]
    }
