import os
import time
import psutil
import asyncio
async def start():
    os.system('start /B python process_id2.py')
    await asyncio.sleep(20)
    f=open("file2.txt",'r')
    x=int(f.read().strip())
    f.close()
    await asyncio.sleep(15)
    print(f'Started process_id2.py : {x}') 
    print("terminating process_id2.py")
    try:
        child_process = psutil.Process(x)
        child_process.terminate()
        print("Process terminated")
        os.system('start /B python process_id.py')
    except psutil.NoSuchProcess:
        print(f"No such process: {x}")
    except psutil.AccessDenied:
        print(f"Access denied when trying to kill process: {x}")
    except psutil.Error as e:
        print(f"An error occurred: {x}")
asyncio.run(start())