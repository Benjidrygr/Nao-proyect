from naoqi import ALProxy

def main():
    proxy = ALProxy("ALMotion", "localhost", 9559)
    proxy.wakeUp()
    proxy.rest()
    proxy.moveInit()
    proxy.move(0.1, 0.0, 0.0)
    proxy.move(0.0, 0.1, 0.0)
    proxy.move(0.0, 0.0, 0.1)
    proxy.move(0.0, 0.0, 0.0)
    proxy.rest()
    proxy.sleep()

if __name__ == "__main__":
    main()