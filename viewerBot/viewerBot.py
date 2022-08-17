import random
import time
import webbrowser
import time
import os


class VB():
    """Open and close a specified internet url repetitively to generate views!!!!
        (But, they will probably be seen has fake by the use plateform.)


    """

    def __init__(self):
        """
        Constructeur de la classe VB
        """

        # Paramètres

    def cube(self,k):

        a, b = -10, 10
        x, y, z = (int(random.randrange(a, b)), int(random.randrange(a, b)), 0)
        try:
            if (k > 0):
                result = k + self.cube(k - 1)
                print('allo')

            else:
                result = 0
            return result
        except ValueError:
            pass


    def tri_recursion(self,u,v,t):
        """

        """

        try:
            if(int(v)>0):
                result = v+self.tri_recursion(u,v-1,t)
                #print(result)
                webbrowser.open(u, new=2)
                print('')
                print(f'Recursion left: {v}')
                print('')
                #webbrowser.open('https://youtu.be/h8kJ4HoxcWw', new=2)
                time.sleep(t)
                os.system("taskkill /im chrome.exe /f")


            else:
                result = 0
            return result

        except ValueError:
            pass






    def recursiveValue(self):

        rep = 0
        while not rep:
            try:
                rep = int(input('Enter a recursive value between 1 and 10, inclusively. Default value is 1:') or 1)
                if rep not in (range(11)[1:]):
                    raise ValueError
            except ValueError:
                rep = 0
                print('')
                print('Please enter a valid number.')
                time.sleep(1)
                print("")

        print("")
        print("Recursion will be:", rep)

        if rep == 1:
            print('Nice!')
        elif rep == 2:
            print('Cool!')
        elif rep >= 3:
            print('Awesome!')

        print("")


        return rep


    def recursiveUrl(self):
        """"""
        rurl = ""
        while not rurl:
            try:
                rurl = str(input('Enter a url (ex. https://google.com):') or 'https://www.google.com')
                #https://youtu.be/h8kJ4HoxcWw
                if 'https://' not in rurl[:8]:

                    raise ValueError

            except ValueError:
                rurl = ""
                print("")
                print('Entry is not valid. Must begin with https://')
                time.sleep(2)
                print("")

        print("")
        print("Default url is:",rurl)
        print("")

        return rurl

    def viewerBot(self):
        """"""

        activate = input("Press 1 to process, 0 to exit.")
        #print('1')
        while True:

            #
            if activate == "1":
                #print('2')

                print('')
                self.tri_recursion( self.recursiveUrl(), self.recursiveValue(), self.timeDelay())
                print('')
                activate = input("Press 1 to process, 0 to exit.")
                #activate = ""
                #activate = None

                continue

            elif activate == "1":

                activate = None
                continue
                #break

            elif activate == "0":
                print('')
                print('VIEWERBOT OVER')
                input('Enter to exit.')
                print('')
                #print('2')
                break

            else:
                print("\nInvalid input")
                #print("")
                print('')
                activate = input("Press 1 to process, 0 to exit.")
                #print('3')





    def timeDelay(self):
        """"""

        td = 0
        while not td:
            try:
                td = int(input('Enter a time delay between 10 and 60 seconds inclusively. Default will be 10 seconds:') or 10)
                if td not in (range(61)[10:]):
                    raise ValueError
            except ValueError:
                td = 0
                print('')
                print('Please enter a valid number.')
                time.sleep(1)
                print("")

        print("")
        print("Default time delay is:", td, "seconds")

        if td == 2:
            print('Thats a quicky!')
        elif td >= 3:
            print('Take your time!')
        elif td >= 10:
            print('Long run!')
        print("")
        #print(type(td))

        return td

    def survey(self):
        """"""

        ans = 0
        while not ans:
            try:
                ans = int(input('Out of these options\(1, 2, 3), which is your favourite?'))
                if ans not in (range(100)[1:]):
                    raise ValueError
            except ValueError:
                ans = 0
                print("That's not an option!")

        if ans == 1:
            print('Nice!')
        elif ans == 2:
            print('Cool!')
        elif ans >= 3:
            print('Awesome!')
        return None

if __name__ == '__main__':
    # Point d'entrée du programme
    print("\nViewerBot 1.04\n")

    vw = VB()

    #vw.recursiveUrl()
    #vw.recursiveValue()
    #print(type(vw.timeDelay()))
    #print("\n\nRecursive Viewer")
    #print("")
    vw.viewerBot()




