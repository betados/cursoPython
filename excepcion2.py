while True:
    try:
        1/0
    except Exception:
        print("las liao")
    # finally:
    print("finally")
print("fuera del bucle")
