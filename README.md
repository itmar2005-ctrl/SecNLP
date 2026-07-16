# SecNLP Platform

Plataforma de detección y prevención del ciberacoso mediante inteligencia artificial y procesamiento de lenguaje natural (NLP).

## 🌐 Páginas

| Ruta | Descripción |
|------|-------------|
| `/` | Portal principal con información, prevención y recursos |
| `/classifier` | Clasificador de amenazas con 5 categorías (Benigno, Acoso, Amenaza, Odio, Phishing) |
| `/guia-seguridad` | Guía de seguridad digital (2FA, contraseñas, privacidad) |
| `/guia-padres` | Guía para padres con videos educativos y consejos por edad |
| `/reportar` | Guía paso a paso para reportar en Instagram, Facebook, Twitter/X, WhatsApp, TikTok, YouTube |

## 🚀 Inicio rápido

```powershell
cd secnlp-platform
C:\Path\To\Python313\python.exe run.py
```

Abrir `http://localhost:8000`

## 🛠️ Stack

- **Backend:** FastAPI + Transformers (unitary/toxic-bert)
- **Frontend:** HTML, CSS, JavaScript vanilla
- **Monitoreo:** Prometheus
- **Despliegue:** Docker, Render

## 📁 Estructura

```
secnlp-platform/
├── backend/              # API FastAPI
│   ├── main.py          # Punto de entrada
│   ├── pipeline.py      # Pipeline de moderación
│   ├── config.py        # Configuración
│   ├── routers/         # Endpoints
│   └── requirements.txt
├── frontend/            # Páginas web
│   ├── index.html       # Portal principal
│   ├── classifier.html  # Clasificador
│   └── ...
├── docker/              # Docker + Prometheus
├── tests/               # Pruebas
└── run.py               # Script de inicio
```

## 📊 Modelo

Usa `unitary/toxic-bert` para clasificación de texto en 6 etiquetas de toxicidad. El frontend mapea la salida a 5 categorías de amenaza cibernética con análisis de palabras clave.

## 📝 Licencia

Proyecto educativo de ciberseguridad.
