try:
    f = open("test.txt", "w+")
    # perform file operations
finally:
    f.close()
