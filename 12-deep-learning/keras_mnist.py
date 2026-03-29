# Deep Learning with TensorFlow / Keras
# Course 4 §Deep Learning section
# pip install tensorflow

import numpy as np

# ═══════════════════════════════════════
#  KERAS MNIST CLASSIFIER
# ═══════════════════════════════════════
# MNIST: 70,000 grayscale images of handwritten digits (28×28 px)

try:
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras import layers

    print(f"TensorFlow version: {tf.__version__}")
except ImportError:
    print("TensorFlow not installed. Run: pip install tensorflow")
    raise SystemExit

# ─── Load and preprocess data ─────────────────────────────────────────────────
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print(f"Train: {x_train.shape}, Test: {x_test.shape}")

# Normalize pixel values [0, 255] → [0.0, 1.0]
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Flatten 28×28 images to 784-element vectors
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# ─── Build model ──────────────────────────────────────────────────────────────
model = keras.Sequential(
    [
        layers.Dense(128, activation="relu", input_shape=(784,)),
        layers.Dropout(0.2),
        layers.Dense(64, activation="relu"),
        layers.Dropout(0.2),
        layers.Dense(10, activation="softmax"),  # 10 digit classes
    ],
    name="mnist_classifier",
)

model.summary()

# ─── Compile ──────────────────────────────────────────────────────────────────
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

# ─── Train ────────────────────────────────────────────────────────────────────
callbacks = [
    keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
    keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=2),
]

history = model.fit(
    x_train,
    y_train,
    epochs=20,
    batch_size=128,
    validation_split=0.1,
    callbacks=callbacks,
    verbose=1,
)

# ─── Evaluate ─────────────────────────────────────────────────────────────────
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\nTest accuracy: {test_acc:.4f}")
print(f"Test loss:     {test_loss:.4f}")

# ─── Predictions ──────────────────────────────────────────────────────────────
y_pred_probs = model.predict(x_test[:5])
y_pred_classes = np.argmax(y_pred_probs, axis=1)
print(f"\nFirst 5 predictions: {y_pred_classes}")
print(f"Actual labels:        {y_test[:5]}")

# ─── Save and reload ──────────────────────────────────────────────────────────
model.save("mnist_model.keras")
print("\nModel saved to mnist_model.keras")

loaded_model = keras.models.load_model("mnist_model.keras")
_, loaded_acc = loaded_model.evaluate(x_test, y_test, verbose=0)
print(f"Reloaded model accuracy: {loaded_acc:.4f}")

# ═══════════════════════════════════════
#  CNN VERSION (better for images)
# ═══════════════════════════════════════
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# CNN needs shape (batch, height, width, channels)
x_train = x_train[..., np.newaxis]  # (60000, 28, 28, 1)
x_test = x_test[..., np.newaxis]

cnn = keras.Sequential(
    [
        layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(10, activation="softmax"),
    ],
    name="mnist_cnn",
)

cnn.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

cnn.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.1, verbose=1)

_, cnn_acc = cnn.evaluate(x_test, y_test, verbose=0)
print(f"\nCNN Test accuracy: {cnn_acc:.4f}")

# LAB EXERCISES
# 1. Try the Fashion-MNIST dataset (keras.datasets.fashion_mnist). Does the
#    same model architecture work as well?
# 2. Add BatchNormalization layers. Does it help?
# 3. Plot training vs validation accuracy curves using matplotlib.
