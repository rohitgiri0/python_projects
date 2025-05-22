from plyer import notification
import chime
import time

def main():
    while True:
        notification.notify(
            title='Hey there!',
            message='Drink some water 💧',
            app_icon='glass.ico', 
            timeout=5             
        )
        time.sleep(60*60) 
        chime.success()
if __name__ == "__main__":
    main()
