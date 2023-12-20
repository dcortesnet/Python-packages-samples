import psutil

if __name__ == '__main__':
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    virtual_memory = int(psutil.virtual_memory().used / (1024 ** 2))
    available_memory = int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    
    print(f'''State: 
CPU {cpu_percent}% 
Used {virtual_memory} Mb of memory
Is left over {available_memory}% free''')
