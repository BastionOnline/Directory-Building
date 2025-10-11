##########################################################################################################################
#Code to Exit Program

def exit(Exitcmd):
    ClosePhrase = ["stop", "exit", "close", "end"]

    def CloseProgram(Exitcmd):

        for x in ClosePhrase:
        # This loop returns a VALUE not an index, so compare directly
            if Exitcmd.lower() == x:
                # print(x.capitalize() + "ing program")
                ## exit() raise the SystemExit exception so can code this in that block
                exit()
                #sys.exit()
                #Sys.exit, EXITS IMMEDIATELY!
                    #still showed returning to code block, so will just use reg exit
            # else:
                #else statements do NOT need to be present all the time
        return Exitcmd



        # for x in ClosePhrase:

        #     if Exitcmd == ClosePhrase[x]:
        #         print(ClosePhrase[x] + "ing program")
        #         exit()
        #     else:
        #         return Exitcmd


    #     if Exitcmd == "exit":
    #         print("Exiting program")
    #         exit()
    # #        return None
    #     else:
    #         return Exitcmd

        # c = 0
        
        # while c < len(ClosePhrase):
        #     if Exitcmd.lower() == ClosePhrase[c]:
        #         print(ClosePhrase[c] + "ing program.")
        #         return None
        #     elif c == 0:
        #         c +=1
        #     else:
        #         return Exitcmd

