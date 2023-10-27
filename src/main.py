"""main
"""
# from multiprocessing import Process
# from loguru import logger

import uvicorn

# os.system("export #=$PYTHONPATH:" + os.getcwd() + "/src")
# print(os.getcwd())

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="0.0.0.0", port=8081, reload=True)
    # uvicorn_process = Process(
    #     target=uvicorn.run,
    #     kwargs={
    #         "app": "api.main:app",
    #         "host": "127.0.0.1",
    #         "port": 5000,
    #         "log_level": "info",
    #     },
    # )
    # logger.info("Starting Uvicorn")
    # uvicorn_process.start()
    # uvicorn_process.join()
