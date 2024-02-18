import pyautogui

n = int(input("Enter the number of rows for the pyramid: "))

if n == 1:
    print('#')
else:
    pyautogui.write('#', interval=0.25)
    for i in range(1, n + 1):  # Adjust the range for the outer loop
        for j in range(i):     # Use i as the end value to print the correct number of hashes
            pyautogui.write('#', interval=0.25)
        pyautogui.press('enter')  # Move to the next line after completing each row
##
        ####
        #####
        