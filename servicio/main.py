from fastapi import FastAPI, UploadFile, File, Form
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI()

#model = tf.keras.models.load_model("../models/DataAugmentation_FL_alpha_2.keras")
model = tf.saved_model.load("../models/resnet/v1")
infer = model.signatures["serving_default"]

print("------------------------------")
print(type(model))
print("------------------------------")
print(model.signatures)
print("------------------------------")
print(infer.structured_input_signature)
print("------------------------------")

classes = [
    "akiec",
    "bcc",
    "bkl",
    "df",
    "nv",
    "mel",
    "vasc"
]

@app.post("/predict")
async def predict(
    image: UploadFile = File(...),
    age: int = Form(...),
    sex: str = Form(...),
    localization: str = Form(...)
):

    contents = await image.read()

    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img = img.resize((224, 224))

    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = infer(
        tf.constant(img_array)
    )
    
    scores = prediction["output_0"].numpy()

    print(scores)

    predicted_class = classes[np.argmax(scores)]
    confidence = float(np.max(scores))

    return {
        "scores": scores.tolist(),
        "prediction": predicted_class,
        "confidence": confidence
    }