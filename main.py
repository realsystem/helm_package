from backend import create_backend

if __name__ == "__main__":
    app = create_backend()
    app.run(host="0.0.0.0", port=80)
