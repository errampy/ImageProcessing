import cv2
img = cv2.imread('lena.jpg',-1)# image pash and flag like 1,0,-1
#print(img)

cv2.imshow('Name of the image what to display',img)# show the image
k = cv2.waitKey(5000)# 5 secound

if k == 27:
    print('you press Esc button')
    cv2.destroyAllWindows()# to destroy all windows
elif k == ord('s'):
    print('you press s key')
    cv2.imwrite('lena_copy1.png',img)
    cv2.destroyAllWindows()