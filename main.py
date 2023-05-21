import uvicorn

from eco_challenge import application

app = application.create_app()


def main():
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8000,
        reload=True,
    )


if __name__ == '__main__':
    main()
