import cv2
import mediapipe as mp

# Inicialização do MediaPipe
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Inicia a captura da câmera (0 é a webcam padrão)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Não foi possível capturar imagem da câmera.")
        break

    # Converte a imagem para RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Processa a imagem e detecta os pontos do corpo
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Pega posições dos ombros e pulsos
        left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]

        # Verifica se os pulsos estão acima dos ombros
        if (left_wrist.y < left_shoulder.y) and (right_wrist.y < right_shoulder.y):
           cv2.putText(image, "Pessoa isolada detectada durante apagao!", (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 3)


    # Mostra a imagem com os pontos e alertas
    cv2.imshow('Detector de Gestos de Ajuda', image)

    # Sai se apertar ESC (tecla 27)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
