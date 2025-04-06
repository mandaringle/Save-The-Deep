# Stage 1: Build front-end assets (if needed)
FROM node:22 AS frontend-builder
WORKDIR /app/frontend
COPY package.json package-lock.json ./
RUN npm install
COPY tailwindcss ./tailwind.config.js
# If you have other front-end build steps (e.g., building React/Vue), add them here
RUN npx tailwindcss -i ./tailwind.css -o ./static/output.css --minify

# Stage 2: Build Python backend
FROM python:3.13-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy backend source code
COPY app.py .
COPY templates ./templates
COPY static ./static
COPY --from=frontend-builder /app/frontend/static ./static

EXPOSE 5000

CMD ["python", "app.py"]